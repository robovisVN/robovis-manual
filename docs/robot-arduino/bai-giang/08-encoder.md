# Bài 8: Đọc encoder và hiểu tốc độ bánh xe

**Mục tiêu:** quay bánh bằng tay và quan sát số xung tăng. Khi bước này chạy đúng, bạn mới dùng encoder để tính tốc độ hoặc cho xe quay một góc định trước.

## Encoder nhìn thấy chuyển động thế nào?

Trên xe có đĩa với nhiều khe và module đọc quang. Khi bánh/trục quay, khe và phần chắn lần lượt đi qua đầu đọc. Đầu ra đổi mức nhiều lần, giống một chuỗi bật/tắt.

Mỗi lần tín hiệu chuyển theo cách đã chọn được gọi là một **xung đếm**. Nano cộng các xung để biết bánh đã quay bao nhiêu. Module một đầu ra chỉ cho biết số chuyển động; nó không tự nói bánh đang tiến hay lùi.

## Trước khi làm

Ngắt nguồn motor để bánh không tự quay. Đĩa encoder phải ở đúng khe của đầu đọc và quay được tự do. Ngắt IN1/IN2 khỏi D0/D1 để dùng Serial qua USB; giữ dây encoder ở D2/D3.

| Encoder | Nối Nano | Chú ý |
| --- | --- | --- |
| D0/DO của module trái | D2 | D0 ở đây là nhãn **đầu ra module**, không phải chân D0 Nano |
| D0/DO của module phải | D3 | D3 Nano đọc phía phải |
| VCC | Nguồn phù hợp module | Không cấp theo màu dây khi chưa kiểm tra |
| GND | GND Nano | Nối chung mốc tín hiệu |

## Bước 1. Kiểm tra tín hiệu đơn giản

Tạo `NanoEncoderTinHieu`, chép:

```cpp
void setup() {
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  Serial.println(digitalRead(2));
  delay(50);
}
```

`INPUT_PULLUP` dùng đầu vào với điện trở kéo lên bên trong, giúp đầu vào không bị để trôi ở cấu hình này. Mở Monitor 9600, quay bánh trái **rất chậm** bằng tay.

**Kết quả cần thấy:** khi đĩa đi qua các vùng khe/chắn, số đọc chuyển giữa 0 và 1. Bạn có thể dừng ở hai vị trí để quan sát. Quay nhanh sẽ bỏ lỡ các thay đổi vì mã chỉ đọc mỗi 50 ms; đây chưa phải chương trình đếm xung.

Nếu không đổi mức, kiểm tra đĩa, khe đọc, VCC/GND và D2 trước khi thử chương trình dài hơn.

## Bước 2. Vì sao phải dùng ngắt?

Nếu chỉ đọc mỗi 50 ms, nhiều xung có thể đi qua giữa hai lần đọc. **Ngắt** là cách để Nano thực hiện một việc nhỏ ngay khi chân tín hiệu đổi mức, dù chương trình chính đang làm việc khác.

Ta chọn **RISING**, nghĩa là lần tín hiệu từ LOW/0 lên HIGH/1. Mỗi lần đó, một hàm chỉ cộng bộ đếm thêm 1. Không đặt lệnh in, chờ hoặc phép tính dài trong hàm ngắt.

## Bước 3. Đếm xung tích lũy của hai bánh

Tạo `NanoEncoderDem`, thay toàn bộ mã bằng:

```cpp
volatile unsigned long xungTrai = 0;
volatile unsigned long xungPhai = 0;

void demTrai() {
  xungTrai = xungTrai + 1;
}

void demPhai() {
  xungPhai = xungPhai + 1;
}

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), demTrai, RISING);
  attachInterrupt(digitalPinToInterrupt(3), demPhai, RISING);
}

void loop() {
  noInterrupts();
  unsigned long trai = xungTrai;
  unsigned long phai = xungPhai;
  interrupts();

  Serial.print("Trai: ");
  Serial.print(trai);
  Serial.print(" | Phai: ");
  Serial.println(phai);
  delay(500);
}
```

Upload, mở Monitor **9600** và thử:

| Thao tác | Kết quả cần thấy |
| --- | --- |
| Để hai bánh đứng yên | Hai số giữ gần như không đổi |
| Quay chỉ bánh trái | Số Trai tăng, Phai giữ nguyên |
| Quay chỉ bánh phải | Số Phai tăng |
| Quay bánh theo chiều ngược | Số vẫn tăng; một kênh chưa phân biệt chiều |

Một mẫu log khi chỉ quay bánh trái:

```text
Trai: 0 | Phai: 0
Trai: 5 | Phai: 0
Trai: 12 | Phai: 0
```

Các con số minh họa; không cần tăng đúng 5 hoặc 12 như mẫu.

## Bước 4. Hiểu những dòng mới

| Dòng/khái niệm | Vì sao có trong mã? |
| --- | --- |
| unsigned long | Giữ số đếm không âm có thể lớn |
| volatile | Báo rằng biến có thể đổi bởi hàm ngắt, không chỉ trong loop |
| attachInterrupt(..., demTrai, RISING) | Gắn việc gọi demTrai với cạnh lên ở D2 |
| noInterrupts() rồi chép hai biến | Tạm ngừng ngắt rất ngắn để số không đổi giữa lúc Nano chép giá trị nhiều byte |
| interrupts() | Cho ngắt hoạt động lại ngay sau khi chép |
| In trai/phai thay vì đọc lại xungTrai | In bản đã chép nhất quán; không giữ ngắt tắt khi gửi log |

Chỉ cần vùng chép ngắn đó. Không thêm delay hoặc Serial vào giữa noInterrupts/interrupts. Đây là cách bảo vệ số đếm trên Nano, không phải một thủ thuật cần chép vào mọi chương trình.

## Bước 5. Đếm một vòng bánh để biết PPR

**PPR** trong các bài sau nghĩa là số xung đếm được trên **một vòng bánh** với cách đếm đang dùng.

1. Đánh dấu một điểm trên bánh, để dễ nhận ra một vòng đủ.
2. Ghi số Trai đang hiển thị, ví dụ 12.
3. Quay bánh trái đúng một vòng thật chậm và chờ log cập nhật.
4. Ghi số mới, ví dụ 32. Hiệu `32 − 12 = 20` là số xung vòng đó.
5. Lặp lại để xem kết quả có nhất quán không.

Không mặc định mọi xe có PPR 20. Đĩa, truyền động, cách đếm RISING/CHANGE và nhiễu đều có thể ảnh hưởng. Giữ **RISING** trong bài và đo trên bánh thật; chưa thay thông số xe chỉ từ số khe nhìn thấy.

## Bước 6. Tính tốc độ bằng một ví dụ

Nếu PPR đã đo là 20 và trong một giây có thêm 10 xung, bánh quay **10 / 20 = 0,5 vòng/giây**, tương đương **30 vòng/phút**. Vòng/phút thường viết **RPM**.

Nếu chu vi bánh đo được là 0,20 m, tốc độ trong ví dụ là `0,5 × 0,20 = 0,10 m/s`. Đây là ví dụ tính, không khẳng định bánh của bạn có chu vi đó.

Công thức để nhớ sau khi đã hiểu ví dụ:

```text
RPM = số xung tăng × 60 / (PPR × thời gian đo tính bằng giây)
vận tốc = số xung tăng × chu vi bánh / (PPR × thời gian đo)
```

Sketch trên in tổng tích lũy từ lúc khởi động. Muốn đo tốc độ, lấy **hiệu hai số ở đầu/cuối khoảng thời gian**, không dùng toàn bộ tổng như số xung trong một giây.

## Nếu kết quả bất thường

| Hiện tượng | Kiểm tra |
| --- | --- |
| Có 0/1 ở bước đầu nhưng không đếm | Đúng chân D2/D3, đúng sketch và RISING |
| Quay trái nhưng số Phai tăng | Đầu dây hai encoder bị đổi |
| Đứng yên mà số tăng | Đĩa/rung/nguồn/dây/đầu vào; kiểm tra tín hiệu trước khi thêm lọc |
| Đếm một vòng mỗi lần rất khác | Quay đủ vòng, dây/nguồn, nhiễu hoặc tiếp xúc |

## Khi nào hoàn thành?

Bạn kiểm tra được riêng hai encoder, đo được số xung một vòng và hiểu tổng xung khác số xung trong một khoảng đo.

**Bài tập:** ghi số đầu/cuối khi quay đúng hai vòng bánh. So số xung với hai lần PPR đo trước; giải thích vì sao số vẫn tăng khi quay ngược.

[Bài trước](07-do-line.md) · [Lộ trình](../index.md) · [Bài tiếp: Bluetooth HM-10](09-bluetooth.md)
