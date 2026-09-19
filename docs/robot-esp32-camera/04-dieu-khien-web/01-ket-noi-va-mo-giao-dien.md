# Kết nối Wi-Fi và mở giao diện

Phần này không cần cài Python. Có thể dùng máy tính hoặc điện thoại có trình duyệt web.

## 1. Bật robot

1. Đặt robot tại khu vực thử an toàn.
2. Bật nguồn robot.
3. Chờ khoảng 5 đến 10 giây để ESP32 khởi động camera và phát Wi-Fi.

## 2. Xác định chương trình đang chạy

| Chương trình | Wi-Fi | Mật khẩu | Trang điều khiển |
| --- | --- | --- | --- |
| Camera và motor dùng với Python YOLO | `ESP32-Car-01` | `abcd1234` | `http://192.168.4.1:82` |
| Kiểm tra đầy đủ camera và cảm biến | `ESP32-Car` | `12345678` | `http://192.168.4.1` |

## 3. Kết nối Wi-Fi của robot

1. Mở danh sách Wi-Fi trên máy tính hoặc điện thoại.
2. Chọn đúng Wi-Fi theo bảng phía trên.
3. Nhập đúng mật khẩu của chương trình đang chạy.

4. Nếu thiết bị báo **No Internet**, **Không có Internet** hoặc hỏi có muốn giữ kết nối hay không, hãy chọn tiếp tục giữ kết nối.

Thông báo không có Internet là bình thường. Wi-Fi này được dùng để kết nối trực tiếp với robot, không phải để truy cập Internet.

## 4. Mở giao diện điều khiển

Mở Chrome hoặc Edge và nhập đúng địa chỉ vào thanh địa chỉ:

```text
Chương trình dùng với YOLO:       http://192.168.4.1:82
Chương trình kiểm tra cảm biến:   http://192.168.4.1
```

Không nhập địa chỉ này vào ô tìm kiếm Google.

Sau khi trang mở, hình ảnh camera sẽ được tải từ:

```text
http://192.168.4.1:81/stream
```

## Kiểm tra trước khi cho robot chạy

- Hình ảnh camera xuất hiện trên trang.
- Các nút điều khiển gửi được lệnh đến robot.
- Khu vực phía trước robot không có người hoặc vật dễ va chạm.
- Tốc độ đang ở mức thấp.

Nếu trang không mở, kiểm tra thiết bị vẫn đang kết nối đúng `ESP32-Car-01` hoặc `ESP32-Car`. Một số máy tính có thể tự chuyển về Wi-Fi có Internet; cần tắt tính năng tự động chuyển mạng hoặc kết nối lại Wi-Fi robot.
