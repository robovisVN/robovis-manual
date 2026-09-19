# Cài các thư viện cần thiết

## Mở Library Manager

Trong Arduino IDE, chọn **Tools → Manage Libraries**. Gõ lần lượt từng tên thư viện vào ô tìm kiếm và nhấn **Install**.

| Tên tìm kiếm | Tác giả cần chọn | Mục đích |
| --- | --- | --- |
| `AsyncTCP` | ESP32Async | Giao tiếp TCP bất đồng bộ trên ESP32 |
| `ESPAsyncTCP` | ESP32Async | Thư viện tương thích được một số mã ví dụ sử dụng |
| `ESPAsyncWebServer` | ESP32Async | Tạo trang web và WebSocket điều khiển |
| `ESP32Servo` | Kevin Harrington | Dùng cho các chương trình có servo trong bộ bài thực hành |

> **Lưu ý:** `AsyncTCP` và `ESPAsyncTCP` là hai tên khác nhau. Hãy kiểm tra đúng tên và đúng tác giả. Với chương trình ESP32-S3 Camera hiện tại, hai thư viện quan trọng trực tiếp là `AsyncTCP` và `ESPAsyncWebServer`.

## Kiểm tra cài đặt

Sau khi cài xong:

1. Đóng cửa sổ Library Manager.
2. Mở project `main.ino`.
3. Chọn **Sketch → Verify Compile** hoặc nhấn nút dấu kiểm để biên dịch thử.

Nếu xuất hiện lỗi dạng:

```text
fatal error: ESPAsyncWebServer.h: No such file or directory
```

thư viện chưa được cài đúng. Mở lại Library Manager và kiểm tra `ESPAsyncWebServer by ESP32Async`.

Nếu Arduino IDE đề nghị cài thêm dependency khi cài `ESPAsyncWebServer`, chọn cài tất cả dependency được đề nghị.

