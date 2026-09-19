# Xử lý lỗi khi nạp chương trình

## Không thấy cổng COM

Nguyên nhân thường gặp:

- Chưa cài driver CH340.
- Cáp USB chỉ có dây nguồn và không truyền dữ liệu.
- Cổng USB hoặc cáp bị lỏng.
- Windows chưa cập nhật danh sách thiết bị.

Cách xử lý:

1. Đổi cáp USB.
2. Đổi cổng USB trên máy tính.
3. Cài lại driver `CH341SER`.
4. Rút ESP32, mở Device Manager rồi cắm lại để xác định cổng mới xuất hiện.

## Failed to connect hoặc Connecting kéo dài

1. Kiểm tra đã chọn đúng cổng COM.
2. Đóng Serial Monitor và các phần mềm khác đang dùng cổng COM.
3. Upload lại và giữ nút **BOOT** khi Console hiện `Connecting...`.
4. Nhả BOOT khi thấy `Writing at...`.

## Lỗi thiếu thư viện

Ví dụ:

```text
ESPAsyncWebServer.h: No such file or directory
```

Mở Library Manager và cài đúng `ESPAsyncWebServer by ESP32Async` cùng `AsyncTCP by ESP32Async`.

## Lỗi thiếu board config hoặc hàm camera

Ví dụ:

```text
board_config.h: No such file or directory
```

hoặc lỗi liên quan đến `startCameraServer()`.

Kiểm tra `main.ino`, `board_config.h` và `app_httpd.cpp` có nằm trong cùng thư mục `main` hay không. Không chỉ tải riêng tệp `.ino`.

## Nạp thành công nhưng không thấy Wi-Fi của chương trình

1. Chờ ít nhất 10 giây sau khi ESP32 khởi động.
2. Tắt rồi bật lại nguồn robot.
3. Mở **Tools → Serial Monitor** và chọn `115200 baud`.
4. Xác định tên Wi-Fi đúng theo chương trình vừa nạp:

```text
Chương trình dùng với YOLO:       ESP32-Car-01
Chương trình kiểm tra cảm biến:   ESP32-Car
```

5. Nhấn nút reset trên ESP32 và kiểm tra Serial Monitor. Cả hai chương trình đều phải in địa chỉ AP `192.168.4.1`. Chương trình kiểm tra đầy đủ còn in các địa chỉ UI, Stream và WebSocket.

Nếu xuất hiện `Camera init failed`, không tiếp tục nạp ngẫu nhiên nhiều cấu hình khác. Kiểm tra đúng `board_config.h` của sản phẩm hoặc liên hệ ROBOVIS.
