# Chuẩn bị trước khi sử dụng

## Thiết bị cần có

- Robot ESP32 Camera đã lắp ráp hoàn chỉnh.
- Cáp USB có khả năng truyền dữ liệu.
- Máy tính Windows 10 hoặc Windows 11.
- Arduino IDE để nạp chương trình cho ESP32.
- Trình duyệt Chrome hoặc Edge để mở giao diện điều khiển.
- Python và các thư viện AI nếu muốn chạy chương trình YOLO.

## Các tệp mã nguồn cần giữ nguyên

Mỗi chương trình ESP32 phải nằm trong một thư mục project riêng và có ít nhất các tệp sau:

```text
main/
├── main.ino
├── app_httpd.cpp
└── board_config.h
```

Tên thư mục phải trùng với tên tệp `.ino`. Với tệp `main.ino`, thư mục phải có tên là `main`.

Không tách `main.ino`, `app_httpd.cpp` và `board_config.h` sang các thư mục khác nhau. Không chép nội dung của hai chương trình ESP32 vào cùng một tệp `main.ino`.

## Chuẩn bị an toàn trước lần chạy đầu tiên

1. Đặt robot ở khu vực bằng phẳng và đủ rộng.
2. Kê robot để hai bánh chủ động không chạm sàn khi thử chiều quay lần đầu.
3. Để tay gần công tắc nguồn để có thể tắt robot ngay khi cần.
4. Không chạm vào bánh xe khi động cơ đang hoạt động.
5. Không cắm hoặc tháo dây cảm biến khi robot đang được cấp nguồn.

> **Cảnh báo phần cứng:** Cảnh báo ECHO 5 V áp dụng khi chạy chương trình kiểm tra đầy đủ cảm biến. Sản phẩm đã lắp sẵn phải giữ nguyên mạch chia áp hoặc mạch chuyển mức. Không nối trực tiếp tín hiệu ECHO 5 V vào ESP32-S3.

## Trình tự thực hiện

Việc cài Arduino IDE, driver, board và thư viện chỉ cần làm một lần trên mỗi máy tính. Việc kết nối Wi-Fi robot và mở giao diện điều khiển được thực hiện lại mỗi lần sử dụng.

Trước khi nạp chương trình khác, hãy lưu lại bộ firmware gốc do ROBOVIS cung cấp. Không thể khôi phục mã nguồn ban đầu chỉ bằng cách đọc ngược chương trình đã nạp trong ESP32.
