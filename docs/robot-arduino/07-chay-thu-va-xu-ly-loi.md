# Chạy thử Robot Arduino Nano và xử lý lỗi

**Mục tiêu:** kiểm tra từng phần trước khi cho robot chuyển động.

## Đối chiếu robot thực tế

D2, D4, D9 trong bài học là chân ví dụ. Lập bảng từ sơ đồ thật trước khi nạp bộ mã robot:

| Bộ phận | Cần ghi lại |
| --- | --- |
| Driver | Tên module, chân IN/EN/PWM, mức logic |
| Động cơ | Điện áp, dòng tải, nguồn |
| Cảm biến | Nguồn, kiểu tín hiệu, chân Nano |
| Servo | Nguồn, chân tín hiệu, giới hạn cơ khí |

Không nối động cơ DC trực tiếp với GPIO. Với L298N hoặc driver khác, đối chiếu jumper và nguồn theo đúng module. Mạch giao tiếp không cách ly cần chung GND. Không suy ra chức năng chân từ màu dây.

## Chạy thử từng bước

1. Sao lưu mã chạy tốt, ghi board/Processor/cổng và phiên bản thư viện.
2. Ngắt nguồn động cơ, mở sketch chính trong thư mục bộ mã robot.
3. Cài dependency theo README; Verify rồi Upload.
4. Xem Serial để kiểm tra riêng từng cảm biến.
5. Kê bánh khỏi sàn, cấp nguồn theo sơ đồ, thử mỗi động cơ thời gian ngắn ở tốc độ thấp.
6. Kiểm tra lệnh dừng và chiều quay rồi mới thử trên sàn trống.

Nếu chưa có sơ đồ/bộ mã, hoàn thành bài linh kiện rời trước. Gói tải website chứa tài liệu; mã trong bài không tự điều khiển mọi cấu hình robot.

## Lỗi thường gặp

| Hiện tượng | Kiểm tra theo thứ tự |
| --- | --- |
| Không có COM | Cáp dữ liệu → USB → Device Manager → driver đúng chip |
| `stk500_recv()` / `not in sync` | Nano → cổng → ATmega328P/Old Bootloader → ngắt thiết bị D0/D1 |
| Cổng bận / access denied | Đóng ứng dụng dùng COM, kết nối và chọn Port lại |
| Thiếu tệp `.h` | Tên thư viện, dependency; đọc lỗi đầu tiên trong Output |
| Serial ký tự lạ | Baud trùng mã, đúng cổng |
| LED không sáng | Cực LED, điện trở, GND và chân trong mã |
| Nút luôn báo nhấn | Kiểm tra cặp chân nút và D2 có chạm GND không |
| Reset khi tải chạy | Ngắt tải, kiểm tra nguồn, dòng yêu cầu, GND và dây |

Thử Blink với Nano riêng trước khi kết luận hỏng bootloader.

## Nhờ hỗ trợ

Gửi tên chip/bo, hệ điều hành, phiên bản IDE, board/Processor, thư viện, ảnh đấu dây rõ nhãn chân và toàn bộ lỗi dạng văn bản. Nêu mã cuối cùng chạy tốt và thay đổi vừa thực hiện.

**Hoàn thành:** tự nạp Blink, thêm thư viện, đọc nút và phân biệt lỗi biên dịch/nạp/đấu nối.

[Bài trước](04-lap-trinh.md) · [Lộ trình](index.md) · [Tải tài liệu](../tai-xuong/robot-arduino.md)
