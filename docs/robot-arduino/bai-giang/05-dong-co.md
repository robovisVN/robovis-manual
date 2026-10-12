# Bài 5: Điều khiển động cơ DC với L298N

**Mục tiêu:** kiểm tra từng bên động cơ, đổi chiều quay và điều chỉnh mức điều khiển. Lượt đầu kê bánh khỏi sàn; bạn chưa cần để xe tự chạy trên mặt đất.

## Vì sao cần L298N?

Nano gửi tín hiệu điều khiển nhưng không cấp đủ dòng cho motor bánh xe. **L298N là driver**, tức mạch đứng giữa Nano và động cơ: lấy điện từ nguồn motor, cấp cho động cơ và đổi chiều dòng qua động cơ.

Một module L298N có hai nhóm đầu ra. Trong bài, nhóm A nối phía trái, nhóm B nối phía phải theo bộ mã xe; kiểm tra chiều lắp thực tế trước khi gọi một chuyển động là “tiến”.

## Trước khi làm

Đã biết nạp sketch và dùng HIGH/LOW ở [bài LED](03-led.md). Chuẩn bị Nano, driver đúng loại, động cơ và nguồn motor phù hợp bộ xe. Tắt mọi nguồn khi thay dây, kê xe chắc để bánh có thể quay mà không chạm sàn.

Sơ đồ bàn giao có một chú thích L9110s, trong khi mã dùng giao diện L298N. Nếu mạch thực tế không có IN1–IN4 và ENA/ENB như bảng, dừng để đối chiếu [sơ đồ và ghi chú sản phẩm](../08-su-dung-robot.md).

## Bước 1. Đọc tên chân trước khi nối

| Chân L298N | Chân Nano | Hiểu đơn giản |
| --- | --- | --- |
| IN1 / IN2 | D0 / D1 | Hai tín hiệu chọn chiều cho nhóm A |
| ENA | D5 | Cho nhóm A chạy và điều chỉnh mức điều khiển |
| IN3 / IN4 | D4 / D7 | Hai tín hiệu chọn chiều cho nhóm B |
| ENB | D6 | Cho nhóm B chạy và điều chỉnh mức điều khiển |
| OUT1 / OUT2 | Hai dây motor nhóm A | Đầu ra cấp điện cho motor |
| OUT3 / OUT4 | Hai dây motor nhóm B | Đầu ra cấp điện cho motor |
| GND | GND nguồn motor và GND Nano | Đường chung cho tín hiệu |

**IN** nhận lệnh từ Nano; **OUT** đi tới motor. Không nối hai dây motor vào chân IN. Các số D0/D1 là tên chân in trên Nano, không phải chân thứ nhất/thứ hai đếm từ mép bo.

Nguồn motor đi vào đầu nguồn công suất của module, theo điện áp được phép của motor/module. Chân ghi “12V” trên một số module là nhãn đầu nguồn motor, không phải hướng dẫn luôn phải dùng đúng 12 V. Không nối nguồn pin motor vào 5V Nano.

## Bước 2. Kiểm tra jumper và trạng thái nạp

**Jumper** là nắp nối nhỏ chụp lên hai chân. Nếu ENA/ENB đang được jumper nối lên HIGH, tháo jumper đó để Nano gửi PWM vào ENA/ENB. Jumper **5V_EN** liên quan nguồn logic, là jumper khác; giữ/tháo theo hướng dẫn đúng module, không tự thay chỉ vì vừa tháo ENA/ENB.

Nano dùng D0/D1 cho giao tiếp USB, còn xe dùng chúng điều khiển motor. Khi nạp, ngắt nguồn motor và ngắt dây D0/D1 tới IN1/IN2 nếu kết nối gây lỗi. Sau nạp, tắt nguồn trước khi nối lại. **Không thêm Serial.begin() vào các sketch motor trong bài này.**

**Kết quả cần thấy:** đúng IN/OUT, GND chung, nguồn phù hợp, ENA/ENB nhận tín hiệu từ Nano và bánh được kê khỏi sàn.

## Bước 3. Thử chỉ nhóm A trong một giây

Tạo `NanoMotorA` và thay toàn bộ sketch bằng:

```cpp
const int ENA = 5;
const int IN1 = 0;
const int IN2 = 1;
const int ENB = 6;
const int IN3 = 4;
const int IN4 = 7;

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  delay(1000);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 120);
  delay(1000);
  analogWrite(ENA, 0);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
}

void loop() {
}
```

Upload khi nguồn motor đã ngắt. Nối lại dây khi tắt nguồn, kiểm tra bánh kê chắc rồi cấp nguồn đúng sơ đồ. Chương trình chỉ thử một lượt khi Nano khởi động; nếu Nano đã chạy hết lượt trước lúc bật nguồn motor, bánh có thể không quay. Với dây đã nối và bánh kê, khởi động lại Nano theo cách cấp nguồn bình thường của xe để chạy lại lượt thử; không reset giữa lúc đang sửa dây.

**Kết quả cần thấy:** chờ một giây, nhóm A quay một giây rồi dừng; nhóm B không quay. `loop()` rỗng giúp tránh tự lặp lượt thử liên tục.

Đọc ba lệnh quan trọng:

| Lệnh | Tác dụng |
| --- | --- |
| IN1 HIGH, IN2 LOW | Chọn một chiều cho nhóm A |
| analogWrite(ENA, 120) | Đặt mức PWM 120 trên chân D5 |
| analogWrite(ENA, 0) | Ngắt điều khiển ENA để motor dừng theo quán tính |

## Bước 4. Đảo chiều và thử bên còn lại

Để đảo nhóm A, đổi cặp `IN1 HIGH / IN2 LOW` thành `IN1 LOW / IN2 HIGH`. Nạp lại và chạy một lượt khi bánh vẫn kê.

**Kết quả cần thấy:** nhóm A quay theo chiều ngược lần trước. Nếu không đổi chiều, kiểm tra đúng hai dòng và dây IN1/IN2; chưa sửa đồng thời mức PWM.

Sau đó lưu thành `NanoMotorB`. Giữ nguyên các khai báo chân, sáu lệnh pinMode, phần đặt ENA/ENB về 0 và khoảng chờ đầu. Thay đoạn từ `digitalWrite(IN1, HIGH);` đến trước dấu `}` cuối setup bằng:

```cpp
digitalWrite(IN3, HIGH);
digitalWrite(IN4, LOW);
analogWrite(ENB, 120);
delay(1000);
analogWrite(ENB, 0);
digitalWrite(IN3, LOW);
digitalWrite(IN4, LOW);
```

**Kết quả cần thấy:** nhóm B quay một giây rồi dừng, nhóm A giữ tắt. Đây là phần thay trong setup, không chép thành một sketch chỉ có các dòng rời.

Chỉ khi từng bên chạy và dừng đúng mới thử cùng lúc. Làm từng bên giúp biết lỗi nằm ở nhóm nào.

## Bước 5. Hiểu PWM qua một thay đổi nhỏ

**PWM** bật/tắt đầu ra nhanh. Tỷ lệ thời gian bật lớn hơn thường làm motor quay mạnh hơn. `analogWrite()` trên các chân PWM Nano nhận giá trị 0–255; tên hàm không có nghĩa xuất một điện áp analog tùy ý.

| Giá trị thử | Điều bạn nên quan sát |
| --- | --- |
| 0 | Motor không được EN cho chạy; bánh có thể còn quán tính |
| 100 | Mức điều khiển thấp hơn, có thể chưa đủ thắng ma sát |
| 120 | Mức khởi đầu trong bài |
| 150 | Mức cao hơn; kiểm tra thay đổi bằng quan sát |

Thử 100 rồi 150 trong cùng lượt chạy một giây. Không gọi 120 là “một tốc độ cố định”: pin, tải, motor và ma sát đều ảnh hưởng. Đo tốc độ thật sẽ học ở bài encoder.

## Bước 6. Ghép thành tiến, lùi và rẽ

Khi dây/chiều của hai bên đã đúng:

| Muốn xe làm gì? | Nhóm trái | Nhóm phải |
| --- | --- | --- |
| Tiến | Quay để bánh đẩy xe về trước | Cùng hướng tiến của xe |
| Lùi | Đảo chiều | Đảo chiều |
| Rẽ trái theo cung | Dừng hoặc chậm hơn | Tiến |
| Rẽ phải theo cung | Tiến | Dừng hoặc chậm hơn |
| Quay tại chỗ | Hai bên ngược chiều nhau | Hai bên ngược chiều nhau |

“Cùng hướng tiến của xe” không nhất thiết nghĩa hai motor có cùng chiều quay khi nhìn từ hai phía. Nếu một bên ngược, tắt nguồn rồi kiểm tra dây/hướng motor trước khi ghép.

Giữa tiến và lùi, đặt cả ENA/ENB về 0 và chờ bánh dừng rồi mới đảo chiều. Xem [datasheet L298](https://www.st.com/resource/en/datasheet/l298.pdf) nếu cần phân biệt dừng thả và hãm điện.

## Nếu motor chưa chạy đúng

| Hiện tượng | Việc kiểm tra đầu tiên |
| --- | --- |
| Không quay cả hai bên | Nguồn tải, công tắc, GND chung; USB Nano không thay nguồn motor |
| Chỉ một bên không quay | Dây OUT, IN và EN của đúng nhóm đó |
| PWM đổi nhưng motor không khác | EN có đang bị jumper giữ HIGH không? |
| Không nạp được | D0/D1 có còn nối driver? Chọn đúng Nano/COM chưa? |
| Driver/motor nóng, cơ cấu kẹt | Tắt nguồn tải, kiểm tra kẹt và thông số nguồn; không tăng PWM |

## Khi nào hoàn thành?

Từng bên motor chạy một lượt rồi dừng, bạn đảo được chiều và biết dòng nào đổi mức điều khiển.

**Bài tập:** thử chỉ nhóm B, sau đó vẽ bảng các lệnh để hai bên cùng tiến một giây, dừng một giây, cùng lùi một giây rồi dừng hẳn. Chạy trên bánh kê trước khi đặt xuống sàn.

[Bài trước](04-servo.md) · [Lộ trình](../index.md) · [Bài tiếp: HC-SR04](06-hc-sr04.md)
