# Phân biệt hai chương trình ESP32

Bộ tài liệu này sử dụng hai chương trình ESP32 khác nhau. Mỗi lần nạp chỉ có một chương trình hoạt động. Nạp chương trình mới sẽ thay thế chương trình đang có trong ESP32.

## Chương trình Camera và motor dùng với Python YOLO

Đây là chương trình tương ứng trực tiếp với ứng dụng `ESP32 Camera YOLO Viewer` trên Windows.

Chức năng:

- Phát Wi-Fi `ESP32-Car-01`.
- Truyền hình ảnh camera qua cổng `81`.
- Nhận lệnh điều khiển motor qua WebSocket cổng `82`.
- Điều khiển tiến, lùi, quay trái và quay phải.
- Nhận tốc độ dạng `SPD:<linear>,<rotate>` từ ứng dụng Python.
- Kích hoạt chân `STBY` của mạch động cơ tại GPIO19.

Thông số kết nối:

```text
Wi-Fi:          ESP32-Car-01
Mật khẩu:       abcd1234
Trang web:      http://192.168.4.1:82
Camera:         http://192.168.4.1:81/stream
WebSocket:      ws://192.168.4.1:82/ws
```

## Chương trình kiểm tra đầy đủ cảm biến và camera

Đây là chương trình đã gửi trước đó để kiểm tra toàn bộ phần cứng trên một giao diện web.

Chức năng:

- Phát Wi-Fi `ESP32-Car`.
- Hiển thị camera.
- Điều khiển tám hướng.
- Hiển thị khoảng cách HC-SR04.
- Hiển thị tổng xung và xung mới của encoder trái, phải.
- Hiển thị trạng thái năm mắt dò line.
- Điều chỉnh tốc độ trực tiếp trên giao diện web.

Thông số kết nối:

```text
Wi-Fi:          ESP32-Car
Mật khẩu:       12345678
Trang web:      http://192.168.4.1
Camera:         http://192.168.4.1:81/stream
WebSocket:      ws://192.168.4.1/ws
```

## Chọn đúng chương trình

| Mục đích | Chương trình cần nạp |
| --- | --- |
| Chạy ứng dụng Python và nhận diện YOLO | Camera và motor dùng với Python YOLO |
| Điều khiển cơ bản bằng giao diện web cổng 82 | Camera và motor dùng với Python YOLO |
| Kiểm tra camera, HC-SR04, encoder và dò line | Kiểm tra đầy đủ cảm biến và camera |
| Kiểm tra điều khiển tám hướng trên trình duyệt | Kiểm tra đầy đủ cảm biến và camera |

> **Không trộn hai cấu hình:** Hai chương trình sử dụng cổng mạng, tên Wi-Fi và chân GPIO khác nhau. Đặc biệt, GPIO19 là `STBY` trong chương trình dùng với YOLO nhưng là một đầu vào dò line trong chương trình kiểm tra đầy đủ. Chỉ sử dụng nguyên bộ mã nguồn và cấu hình phần cứng tương ứng.
