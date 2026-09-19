# Chuẩn bị thư mục mã nguồn

Mỗi chức năng của robot có thể được cung cấp trong một thư mục mã nguồn riêng. Chỉ nạp một chương trình phù hợp với bài thực hành đang sử dụng.

## Tải và giải nén mã nguồn

1. Mở liên kết Google Drive do ROBOVIS cung cấp.
2. Tải toàn bộ thư mục chương trình về máy tính.
3. Giải nén tệp tải xuống.
4. Mở thư mục và kiểm tra các tệp bên trong.

Cấu trúc của chương trình Camera Car phải tương tự:

```text
main/
├── main.ino
├── app_httpd.cpp
└── board_config.h
```

Nếu Drive tải các tệp riêng lẻ, hãy tự tạo một thư mục tên `main` rồi đặt toàn bộ các tệp vào thư mục này.

## Mở project

1. Trong Arduino IDE, chọn **File → Open**.
2. Mở thư mục `main`.
3. Chọn tệp `main.ino`.
4. Kiểm tra các tab `main`, `app_httpd.cpp` và `board_config.h` xuất hiện trong Arduino IDE.

## Xác định đúng chương trình trước khi nạp

| Dấu hiệu trong mã nguồn | Chương trình |
| --- | --- |
| `ssid = "ESP32-Car-01"` và `AsyncWebServer server(82)` | Camera và motor dùng với Python YOLO |
| `ssid = "ESP32-Car"` và `AsyncWebServer server(80)` | Kiểm tra đầy đủ camera và cảm biến |

Không ghép các phần của hai chương trình với nhau. Mỗi chương trình có cấu hình cổng mạng và GPIO riêng.

## Không chỉnh sửa khi chưa cần thiết

Nếu chỉ muốn sử dụng chức năng có sẵn, không sửa chân GPIO, cấu hình camera hoặc thông số Wi-Fi trong mã nguồn.

Các giá trị của chương trình dùng với Python YOLO là:

```cpp
const char* ssid = "ESP32-Car-01";
const char* password = "abcd1234";
AsyncWebServer server(82);
```

Chương trình kiểm tra đầy đủ dùng Wi-Fi `ESP32-Car`, mật khẩu `12345678` và WebSocket cổng `80`.

Chỉ thay đổi tên hoặc mật khẩu Wi-Fi khi thực sự cần. Nếu thay đổi, phải dùng đúng thông tin mới trong các bước kết nối sau này và cập nhật địa chỉ được ghi cố định trong trang HTML nếu có.

> **Quan trọng:** Trước khi nạp chương trình khác, sao lưu bộ mã nguồn gốc. Nạp code mới sẽ ghi đè firmware đang có trên ESP32.
