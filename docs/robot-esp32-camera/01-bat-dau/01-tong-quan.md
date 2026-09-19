# Tổng quan Robot ESP32 Camera

Robot ESP32 Camera là nền tảng thực hành robot có camera Wi-Fi và động cơ. Tùy chương trình được nạp, người dùng có thể điều khiển robot bằng trình duyệt, chạy nhận diện vật thể bằng YOLO trên máy tính hoặc kiểm tra đầy đủ các cảm biến của robot.

## Các chức năng trong bộ mã nguồn

- Phát Wi-Fi riêng để máy tính hoặc điện thoại kết nối trực tiếp.
- Truyền hình ảnh camera theo dạng MJPEG.
- Điều khiển robot tiến, lùi, quay trái và quay phải.
- Điều chỉnh tốc độ tịnh tiến và tốc độ quay.
- Chạy YOLO trên máy tính để nhận diện người hoặc các vật thể trong hình ảnh camera.
- Với chương trình kiểm tra đầy đủ: điều khiển tám hướng và hiển thị HC-SR04, hai encoder cùng năm mắt dò line.

## Hai cách sử dụng

### Điều khiển bằng trình duyệt

Đây là cách đơn giản nhất và không cần cài Python. Địa chỉ cần mở phụ thuộc vào chương trình đang nạp:

```text
Camera và motor dùng với YOLO:  http://192.168.4.1:82
Kiểm tra đầy đủ cảm biến:       http://192.168.4.1
```

Chương trình dùng với YOLO có giao diện điều khiển bốn hướng. Chương trình kiểm tra đầy đủ có giao diện điều khiển tám hướng và hiển thị dữ liệu cảm biến.

### Điều khiển và nhận diện YOLO trên Windows

Cách này cần máy tính Windows đã cài Python và các thư viện cần thiết. Chương trình nhận hình ảnh từ robot, chạy YOLO trên máy tính rồi vẽ khung nhận diện lên hình ảnh.

> **Điểm cần hiểu đúng:** ESP32 thu hình ảnh và điều khiển động cơ. YOLO chạy trên PC hoặc Laptop, không chạy trực tiếp trên ESP32. Chỉ chương trình kiểm tra đầy đủ mới đọc HC-SR04, encoder và cảm biến dò line.

## Thông số kết nối mặc định

| Hạng mục | Camera và motor dùng với YOLO | Kiểm tra đầy đủ cảm biến |
| --- | --- | --- |
| Tên Wi-Fi | `ESP32-Car-01` | `ESP32-Car` |
| Mật khẩu | `abcd1234` | `12345678` |
| Trang điều khiển | `http://192.168.4.1:82` | `http://192.168.4.1` |
| Luồng camera | `http://192.168.4.1:81/stream` | `http://192.168.4.1:81/stream` |
| WebSocket | `ws://192.168.4.1:82/ws` | `ws://192.168.4.1/ws` |
| Serial Monitor | `115200` baud | `115200` baud |

## Lộ trình đọc tài liệu

Nếu ESP32 đã được nạp đúng chương trình, có thể chuyển thẳng đến nhóm **Điều khiển robot bằng trình duyệt**.

Nếu cần nạp lại chương trình, đọc lần lượt:

1. Chuẩn bị trước khi sử dụng.
2. Phân biệt hai chương trình ESP32.
3. Cài Arduino IDE, driver CH340, board ESP32 và thư viện.
4. Chuẩn bị đúng thư mục mã nguồn.
5. Chọn board và nạp chương trình.

Nếu muốn chạy nhận diện vật thể, phải nạp chương trình **Camera và motor dùng với Python YOLO**, kiểm tra trang `http://192.168.4.1:82`, sau đó mới đọc nhóm **Chạy nhận diện YOLO trên Windows**.


## Tải tài liệu

[Tải bộ tài liệu Robot ESP32 Camera dạng ZIP](../../tai-xuong/robot-esp32-camera.md).
