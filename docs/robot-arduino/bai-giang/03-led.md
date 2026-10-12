# Bài 3: Điều khiển LED trên Arduino Nano

**Mục tiêu:** làm đèn trên Nano bật/tắt và thay đổi nhịp nháy. Bạn sẽ thấy tác động của từng lệnh mà chưa cần đấu motor hoặc cảm biến.

## Trước khi làm

Bạn đã tạo và nạp được sketch ở [bài 2](02-lap-trinh.md). Dùng Nano riêng, cáp USB và IDE. Bài này dùng LED có sẵn trên Nano nên chưa cần mua LED, điện trở hoặc breadboard.

## Bước 1. Tìm đúng LED

Trên Nano thường có đèn nguồn, đèn RX/TX và đèn **L**. Đèn nguồn sáng cho biết bo có điện. Đèn L mới là đèn bạn điều khiển trong bài này.

Tên `LED_BUILTIN` trong chương trình có nghĩa là chân của LED tích hợp theo board đã chọn. Với Nano classic, LED này gắn với D13. Dùng tên có sẵn giúp bạn chưa cần ghi nhớ con số đó.

**Kết quả cần thấy:** bạn xác định được LED L, không dùng trạng thái đèn nguồn để kết luận mã bật/tắt đúng.

## Bước 2. Bật đèn liên tục

Tạo sketch `NanoLED`. Thay toàn bộ mã bằng:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void loop() {
}
```

Nhấn Verify rồi Upload.

| Lệnh | Hiểu đơn giản |
| --- | --- |
| pinMode(LED_BUILTIN, OUTPUT) | Cho chân đèn làm đầu ra để Nano điều khiển |
| digitalWrite(LED_BUILTIN, HIGH) | Đưa đầu ra lên mức HIGH, làm đèn L sáng trên Nano |
| loop rỗng | Không làm thêm gì, đèn giữ trạng thái đã đặt |

**Kết quả cần thấy:** đèn L sáng liên tục. Đổi HIGH thành LOW, nạp lại: đèn L tắt. Đèn nguồn vẫn sáng là bình thường.

HIGH/LOW là hai mức tín hiệu. Với chân logic Nano classic, HIGH gần mức 5 V, LOW gần 0 V. Bạn không dùng chân này để cấp điện cho motor; bài motor sẽ dùng driver riêng.

## Bước 3. Cho đèn nhấp nháy

Thay toàn bộ sketch bằng:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Upload và quan sát một chu kỳ:

| Thời điểm | Lệnh đang thực hiện | Đèn |
| --- | --- | --- |
| Đầu loop | Xuất HIGH | Bật |
| Một giây tiếp theo | delay(1000) | Vẫn bật |
| Sau đó | Xuất LOW | Tắt |
| Một giây tiếp theo | delay(1000) | Vẫn tắt |
| Hết loop | Quay lại lệnh HIGH | Bắt đầu chu kỳ mới |

**Kết quả cần thấy:** sáng một giây, tắt một giây. Một chu kỳ hoàn chỉnh dài hai giây vì có hai khoảng chờ.

## Bước 4. Thay đổi nhịp có chủ đích

Chỉ đổi khoảng chờ sau HIGH từ 1000 thành 200; giữ khoảng chờ sau LOW là 1000. Upload lại.

**Kết quả cần thấy:** đèn sáng ngắn, tắt lâu. Nếu đổi cả hai thành 200, đèn sẽ sáng/tắt đều và nhanh hơn. Làm từng thay đổi để biết dòng nào ảnh hưởng phần nào.

Mã Blink có sẵn trong **File → Examples → 01.Basics → Blink** cũng theo nguyên lý này. Xem [bài Blink của Arduino](https://docs.arduino.cc/built-in-examples/basics/Blink/) khi cần mở lại ví dụ chuẩn.

## Nếu muốn thử LED ngoài

Bạn có thể đọc phần [đấu LED/nút trên mạch riêng](../03-lap-rap.md). LED ngoài cần điện trở nối tiếp và đúng cực; LED tích hợp đã có mạch trên bo. Chưa cần làm phần này để hoàn thành bài.

## Khi chưa thấy đúng kết quả

| Hiện tượng | Kiểm tra theo thứ tự |
| --- | --- |
| Đèn bạn xem không đổi | Có đang nhìn LED L hay đèn nguồn? |
| Đèn vẫn nháy theo mã cũ | Verify rồi Upload, kiểm tra đúng Nano/COM |
| Không có LED L hoạt động | Mở Blink chuẩn và kiểm tra Nano riêng, cáp, thông báo Upload |
| LED ngoài không sáng | Đúng cực, có điện trở, chung GND và đúng chân trong mã |

## Khi nào hoàn thành?

Bạn bật/tắt được LED và giải thích được vì sao đổi từng delay làm thời gian sáng/tắt thay đổi.

**Bài tập:** tạo hai nháy ngắn, rồi tắt hai giây. Viết thứ tự các lệnh trên giấy trước khi sửa sketch.

[Bài trước](02-lap-trinh.md) · [Lộ trình](../index.md) · [Bài tiếp: Servo SG90](04-servo.md)
