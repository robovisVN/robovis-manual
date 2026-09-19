# Các lỗi thường gặp

## Tổng hợp nhanh

| Hiện tượng | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| Không thấy Wi-Fi của robot | Đang tìm sai tên hoặc robot chưa khởi động | Với YOLO tìm `ESP32-Car-01`; với code test cảm biến tìm `ESP32-Car` |
| Windows báo không có Internet | Wi-Fi robot chỉ là mạng nội bộ | Chọn giữ kết nối; đây không phải lỗi |
| Không mở được trang điều khiển | Sai Wi-Fi hoặc sai cổng web | YOLO dùng `http://192.168.4.1:82`; code test cảm biến dùng `http://192.168.4.1` |
| Trang web mở nhưng không có hình | Luồng camera chưa chạy hoặc camera lỗi | Mở trực tiếp `http://192.168.4.1:81/stream`, giảm độ phân giải, khởi động lại robot |
| Camera có hình nhưng robot không chạy | WebSocket mất kết nối | Tải lại trang và kiểm tra trạng thái WS |
| Python báo lỗi WebSocket | Sai Wi-Fi hoặc đã xóa cổng 82 | Kết nối `ESP32-Car-01` và dùng `ws://192.168.4.1:82/ws` |
| Python báo model load failed | Sai đường dẫn model hoặc thiếu tệp `.pt` | Kiểm tra thư mục `models` và chọn đúng model |
| `ModuleNotFoundError` | Chưa cài thư viện hoặc chưa kích hoạt `.venv` | Kích hoạt môi trường rồi cài lại thư viện |
| YOLO rất chậm | Model hoặc input quá lớn | Dùng `yolov8n.pt`, Input size 320, QVGA |
| HC-SR04 hiện No echo | Không có phản hồi siêu âm | Kiểm tra hướng cảm biến, vật cản và dây nối |
| Encoder không tăng | Bánh chưa làm đĩa encoder đi qua cảm biến hoặc dây lỗi | Dừng robot, kiểm tra khe cảm biến và kết nối |

## Kiểm tra từng tầng

Khi có lỗi, kiểm tra theo thứ tự sau:

1. **Nguồn:** ESP32, camera và mạch động cơ đã có nguồn ổn định.
2. **Wi-Fi:** dùng với YOLO phải là `ESP32-Car-01`; code test cảm biến là `ESP32-Car`.
3. **Trang web:** dùng với YOLO là `http://192.168.4.1:82`; code test là `http://192.168.4.1`.
4. **Camera:** mở được `http://192.168.4.1:81/stream`.
5. **WebSocket:** YOLO dùng `ws://192.168.4.1:82/ws`; code test dùng `ws://192.168.4.1/ws`.
6. **Python:** môi trường đã kích hoạt, model và thư viện đầy đủ.

Không nên nạp lại firmware ngay khi chỉ gặp lỗi Python hoặc lỗi model. Nếu trang web của ESP32 vẫn hoạt động, firmware thường không phải nguyên nhân.

## Thông tin cần gửi khi yêu cầu hỗ trợ

- Ảnh đầy đủ thông báo lỗi.
- Ảnh Device Manager có cổng COM nếu lỗi nạp code.
- Ảnh hoặc video giao diện web và hiện tượng của robot.
- Nội dung Serial Monitor ở `115200 baud` từ lúc khởi động.
- Tên file code và model đang dùng.
- Các bước đã thực hiện ngay trước khi lỗi xuất hiện.
