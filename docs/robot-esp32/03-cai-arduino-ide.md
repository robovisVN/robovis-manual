# Cài Arduino IDE, driver CH340 và gói ESP32

**Mục tiêu:** IDE có gói ESP32 và nhìn thấy cổng của bo.

Bài này đối chiếu với [HD nạp code ESP32 của Robovis](https://docs.google.com/document/d/1kt_3J2K9uy3t73HraCWzz_dliXwaGpwbH0eBLzfxwZQ/edit): dùng **CH340**, chọn **ESP32 Dev Module**, tải toàn bộ thư mục `main`. Không dùng driver CP2102 cho bo CH340.

## 1. Arduino IDE 2

Tải IDE phù hợp hệ điều hành tại [Arduino Software](https://www.arduino.cc/en/software), cài và mở ứng dụng. Trên Windows dùng trình cài; macOS/Linux làm theo [hướng dẫn Arduino](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/).

## 2. Kiểm tra CH340 trên Windows

1. Cắm bo bằng cáp Type-C có truyền dữ liệu.
2. Mở **Device Manager → Ports (COM & LPT)**, tìm cổng xuất hiện khi cắm bo, thường có tên USB-SERIAL CH340.
3. Nếu chưa có cổng hoặc thiết bị báo lỗi driver, tải [CH341SER của WCH](https://www.wch.cn/downloads/ch341ser_exe.html), cài rồi cắm lại.
4. Ghi số COM; số này có thể đổi sau khi chuyển cổng USB.

Nếu COM đã hoạt động, không cần cài lại driver. Driver CH340 và gói ESP32 là hai phần riêng. Trên macOS/Linux, kiểm tra cổng thiết bị và quyền truy cập theo hệ điều hành, không chạy bộ cài `.exe` của Windows.

Trong bộ bàn giao có [CH341SER.ZIP](https://drive.google.com/file/d/11mAAeBN780_u6sukouse0D0uVT7j5VUu/view). Theo tài liệu gốc, tải ZIP, giải nén và chạy `SETUP.EXE` để cài driver Windows, rồi kiểm tra COM lại.

## 3. Thêm hỗ trợ ESP32

Mở **File → Preferences** (macOS: mục Settings/Preferences của ứng dụng). Thêm URL sau vào **Additional Boards Manager URLs**; giữ lại các URL đang dùng:

```text
https://espressif.github.io/arduino-esp32/package_esp32_index.json
```

Mở **Boards Manager**, tìm **esp32 by Espressif Systems**, cài bản ổn định phù hợp bộ mã. Các bài PWM tại đây dùng **core 3.x**; nếu mã robot yêu cầu 2.x, giữ môi trường theo README và không trộn API. Ghi lại phiên bản đã cài. Thực hiện theo [hướng dẫn cài của Espressif](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html).

## 4. Chọn board theo module

Đối với **robot trong bộ bàn giao này**, chọn **Tools → Board → ESP32 Dev Module**. Bảng dưới chỉ giúp phân biệt khi bạn dùng một bo khác; không đổi robot hiện tại sang S3/C3 chỉ vì có cổng Type-C.

| Module đã xác nhận | Lựa chọn khởi đầu trong Tools → Board |
| --- | --- |
| ESP32-WROOM-32 trên bo phát triển thông thường | ESP32 Dev Module |
| ESP32-S3 | Board S3 đúng nhà sản xuất; nếu phù hợp, ESP32S3 Dev Module |
| ESP32-C3 | Board C3 đúng nhà sản xuất; nếu phù hợp, ESP32C3 Dev Module |

Tên CH340 không phải tên board trong IDE. Nếu nhà cung cấp có cấu hình riêng, ưu tiên hướng dẫn của đúng bo đó. Không bật PSRAM khi bo không có; chưa thay Flash Size/Partition Scheme nếu không biết thông số.

Chọn **Tools → Port** theo cổng xác nhận ở bước 2. Nếu IDE hiển thị Unknown, vẫn có thể chọn board và port thủ công sau khi đã nhận diện module.

**Kiểm tra:** thấy phiên bản core ESP32, tên board phù hợp module và đúng cổng. Sang bài nạp mã để kiểm tra kết nối thực tế.

## Khi tải core báo DEADLINE_EXCEEDED

Tài liệu gốc hướng dẫn tăng thời gian chờ tải xuống:

1. Đóng Arduino IDE và sao lưu `C:\Users\<username>\.arduinoIDE\arduino-cli.yaml`.
2. Mở file, thêm hoặc sửa mục `network` như bên dưới; không tạo hai mục `network` nếu đã có.
3. Lưu, mở lại IDE và thử Boards Manager lần nữa. Kiểm tra kết nối Internet nếu vẫn lỗi.

```yaml
network:
  connection_timeout: 600s
```

Giữ các cấu hình khác, dùng khoảng trắng khi thụt dòng. Đây là bước xử lý lỗi tải gói, không thay thế driver CH340 hoặc lựa chọn COM.

[Bài trước](02-chuan-bi.md) · [Bài tiếp: Nạp mã và Serial](04-nap-code-va-serial.md)
