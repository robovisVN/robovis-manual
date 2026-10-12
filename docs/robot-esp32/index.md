# Bắt đầu với Robot ESP32 CH340 Type-C

Lộ trình cho người mới: nhận diện bo, cài Arduino IDE/CH340, thêm thư viện, nạp project main rồi điều khiển qua Wi-Fi và dò line theo [bộ bàn giao ESP32 Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt). Hướng dẫn sản phẩm dùng chung, không tách bài theo số bánh.

**CH340** là chip USB–Serial, **Type-C** là cổng USB. Tài liệu bàn giao chọn **ESP32 Dev Module**. Bảng chân robot theo sơ đồ và mã gốc nằm trong bài 8; các ví dụ LED/nút/PWM dùng bo ESP32 classic riêng, ngắt dây robot trước khi thử.

| Thứ tự | Bài học | Kết quả |
| --- | --- | --- |
| 1 | [ESP32 là gì?](01-gioi-thieu.md) | Phân biệt ESP32, CH340 và Type-C |
| 2 | [Chuẩn bị bo và linh kiện](02-chuan-bi.md) | Xác định module và nguồn |
| 3 | [Cài IDE, CH340 và gói ESP32](03-cai-arduino-ide.md) | Có đúng board và COM |
| 4 | [Nạp mã và dùng Serial](04-nap-code-va-serial.md) | Nhận thông báo từ bo |
| 5 | [Thêm thư viện](05-cai-thu-vien.md) | Hiểu thư viện tích hợp và thư viện ngoài |
| 6 | [LED, nút nhấn và PWM](06-lap-trinh-co-ban.md) | Đọc đầu vào, điều khiển đầu ra |
| 7 | [Chạy thử robot và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) | Kiểm tra từng phần trước chuyển động |
| 8 | [Sử dụng robot theo bộ bàn giao](08-su-dung-robot.md) | Lắp ráp, bảng chân, nạp main, Manual và Line follow |

Nếu robot đã lắp sẵn, đọc bài cài IDE, nạp project main và thư viện, rồi sang **bài 8**. Không bắt buộc làm mạch LED/nút trước khi dùng giao diện web.

Không cần học Ubuntu hoặc ROS để làm các bài này. Nếu robot của bạn có camera hoặc LiDAR, học phần nền tảng rồi chuyển sang [ESP32 Camera](../robot-esp32-camera/01-bat-dau/01-tong-quan.md) hoặc [ESP32 LiDAR](../robot-esp32-lidar/index.md).

[Bắt đầu bài 1](01-gioi-thieu.md){ .md-button .md-button--primary }
[Tải tài liệu](../tai-xuong/robot-esp32.md){ .md-button }
