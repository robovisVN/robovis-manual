# Bắt đầu với Robot ESP32 CH340 Type-C

Lộ trình cho người mới: nhận diện bo, cài Arduino IDE, kiểm tra USB, thêm thư viện, lập trình LED/nút nhấn và chuẩn bị chạy robot.

**CH340** là chip giao tiếp USB–Serial, **Type-C** là loại cổng USB. Hai thông tin này chưa xác định ESP32, ESP32-S3 hay ESP32-C3. Các ví dụ chân GPIO trong bộ bài dùng **ESP32 classic với module ESP32-WROOM-32**; hãy đọc tên module và pinout trước khi đấu mạch.

| Thứ tự | Bài học | Kết quả |
| --- | --- | --- |
| 1 | [ESP32 là gì?](01-gioi-thieu.md) | Phân biệt ESP32, CH340 và Type-C |
| 2 | [Chuẩn bị bo và linh kiện](02-chuan-bi.md) | Xác định module và nguồn |
| 3 | [Cài IDE, CH340 và gói ESP32](03-cai-arduino-ide.md) | Có đúng board và COM |
| 4 | [Nạp mã và dùng Serial](04-nap-code-va-serial.md) | Nhận thông báo từ bo |
| 5 | [Thêm thư viện](05-cai-thu-vien.md) | Hiểu thư viện tích hợp và thư viện ngoài |
| 6 | [LED, nút nhấn và PWM](06-lap-trinh-co-ban.md) | Đọc đầu vào, điều khiển đầu ra |
| 7 | [Chạy thử robot và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) | Kiểm tra từng phần trước chuyển động |

Không cần học Ubuntu hoặc ROS để làm các bài này. Nếu robot của bạn có camera hoặc LiDAR, học phần nền tảng rồi chuyển sang [ESP32 Camera](../robot-esp32-camera/01-bat-dau/01-tong-quan.md) hoặc [ESP32 LiDAR](../robot-esp32-lidar/index.md).

[Bắt đầu bài 1](01-gioi-thieu.md){ .md-button .md-button--primary }
[Tải tài liệu](../tai-xuong/robot-esp32.md){ .md-button }
