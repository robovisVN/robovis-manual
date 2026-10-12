# Chạy thử Robot Arduino Nano và xử lý lỗi

**Mục tiêu:** kiểm tra từng phần trước khi cho robot chuyển động.

## Đối chiếu robot thực tế

D2/D4 trong bài mạch rời không phải chân trống của robot; servo robot dùng A5. Đối chiếu [bảng chân và mã gốc](08-su-dung-robot.md) trước khi nạp:

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
3. Cài Servo/Dabble theo [bài thư viện](06-cai-thu-vien.md); Verify rồi Upload tệp chức năng cần chạy.
4. Kiểm tra riêng cảm biến. Nếu dùng sketch Serial chẩn đoán, tháo driver khỏi D0/D1; không bật Serial trong mã robot đang dùng hai chân này cho động cơ.
5. Kê bánh khỏi sàn, cấp nguồn theo sơ đồ, thử mỗi động cơ thời gian ngắn ở tốc độ thấp.
6. Kiểm tra lệnh dừng và chiều quay rồi mới thử trên sàn trống.

Bộ mã và sơ đồ nằm trong [thư mục bàn giao Arduino](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-). Gói ZIP website chứa tài liệu; tải chương trình robot từ liên kết gốc.

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
| Thiếu Dabble.h | Cài Dabble của STEMpedia cho Nano, không dùng DabbleESP32 |
| Servo kẹt | Kiểm tra ốc gá không chạm vỏ servo, dây và giới hạn góc |
| Quay tránh vật cản không dừng | Tắt nguồn động cơ, kiểm tra encoder D2/D3; vòng chờ xung trong mã chưa có timeout |

Thử Blink với Nano riêng trước khi kết luận hỏng bootloader.

## Nhờ hỗ trợ

Gửi tên chip/bo, hệ điều hành, phiên bản IDE, board/Processor, thư viện, ảnh đấu dây rõ nhãn chân và toàn bộ lỗi dạng văn bản. Nêu mã cuối cùng chạy tốt và thay đổi vừa thực hiện.

**Hoàn thành:** tự nạp Blink, thêm thư viện, đọc nút và phân biệt lỗi biên dịch/nạp/đấu nối.

[Bài trước](04-lap-trinh.md) · [Lộ trình](index.md) · [Tải tài liệu](../tai-xuong/robot-arduino.md)
