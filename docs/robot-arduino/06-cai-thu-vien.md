# Thêm thư viện và thử servo

**Mục tiêu:** cài thư viện, hiểu `#include` và biên dịch ví dụ.

**Arduino AVR Boards** hỗ trợ Nano trong IDE. **Servo** cung cấp lệnh cho servo; cài thư viện không thay thế việc chọn board.

## Library Manager

Các tệp bàn giao cần thư viện như sau:

| Chương trình | Thư viện ngoài |
| --- | --- |
| `test_bluetooth.ino` | Dabble, Servo |
| `tranh_vat_can*.ino` | Servo |
| `do_line*.ino` | Không có thư viện ngoài trong các tệp đã đối chiếu; Arduino.h đi cùng core |

Với Bluetooth, tìm **Dabble by STEMpedia**, cài rồi Verify `test_bluetooth.ino`. Giữ `CUSTOM_SETTINGS` và `INCLUDE_GAMEPAD_MODULE` trước `#include <Dabble.h>` như mã gốc. Không thay bằng DabbleESP32. Xem [thư viện Dabble](https://github.com/STEMpedia/Dabble).

Mở **Library Manager** hoặc **Tools → Manage Libraries**. Tìm `Servo`, kiểm tra tác giả **Arduino**, nhấn **Install** và cài dependency được yêu cầu. Xem ví dụ ở **File → Examples → Servo**, biên dịch với Nano. Ghi lại phiên bản đã chạy tốt. Xem [hướng dẫn thư viện Arduino](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library/).

## Thư viện dạng ZIP

Vào **Sketch → Include Library → Add .ZIP Library**, chọn ZIP thư viện. ZIP phải là thư viện Arduino, không phải cả project hoặc gói tài liệu. Nếu giải nén thủ công, đặt thư mục thư viện trong `libraries` của **Sketchbook location** ở Preferences rồi mở lại IDE. Tránh giữ nhiều bản trùng tên. Xem [các cách cài thư viện](https://support.arduino.cc/hc/en-us/articles/5145457742236-Install-libraries-in-the-Arduino-IDE).

## Thử servo vị trí

Có thể chỉ Verify nếu chưa có servo. Dùng servo vị trí SG90 như bộ bàn giao; servo quay liên tục diễn giải lệnh khác. Thử Nano/servo riêng, ngắt mọi dây robot. Nếu thử servo trên xe, ngắt nguồn động cơ và kiểm tra gá/ốc không gây kẹt.

| Dây servo | Kết nối |
| --- | --- |
| Signal | A5 Nano, khớp SERVO_PIN trong bộ mã robot |
| VCC | Nguồn ngoài đúng thông số servo |
| GND | GND nguồn ngoài và GND Nano |

Nano cấp bằng USB. Không nối cực dương nguồn servo vào 5V Nano trong bài này. Nhận diện dây theo tài liệu linh kiện. Xem [kiến thức servo của Arduino](https://docs.arduino.cc/learn/electronics/servo-motors/).

Tạo sketch `NanoServo`:

```cpp
#include <Servo.h>

Servo servoThu;

void setup() {
  servoThu.attach(A5);
  servoThu.write(90);
  delay(1000);
}

void loop() {
  servoThu.write(75);
  delay(1000);
  servoThu.write(105);
  delay(1000);
}
```

`#include` đưa khai báo thư viện vào mã; `attach(A5)` chọn chân; `write()` đặt góc. Servo phải đổi vị trí trong khoảng nhỏ. Ngắt nguồn nếu kẹt, nóng hoặc va cơ cấu; không thử ngay 0°/180° vì giới hạn cơ khí tùy servo.

**Kiểm tra:** không còn lỗi thiếu `Servo.h`; nếu có servo, nó chuyển động và Nano không reset. Servo dùng timer trên Nano, có thể ảnh hưởng PWM D9/D10; kiểm tra trước khi kết hợp driver động cơ.

[Bài trước](05-cai-arduino-ide.md) · [Bài tiếp: Đấu nối](03-lap-rap.md)
