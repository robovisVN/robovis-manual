# Bài giảng xe ESP32 CH340 Type-C

Lộ trình từ lập trình cơ bản đến điều khiển xe có phản hồi, theo [bộ tài liệu Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt). Các bài dùng cấu hình chân sản phẩm, không chia lộ trình theo số bánh.

Mỗi bài thực hành theo trình tự: **mục tiêu → nguyên lý → bảng chân/đấu nối → mã chạy thử → giải thích → kiểm tra kết quả → lỗi thường gặp → bài tập**. Cuối bài có liên kết bài trước/bài tiếp để học liên tục.

## Lộ trình bài giảng

| Bài học | Kiến thức đạt được |
| --- | --- |
| 1. [Giới thiệu xe ESP32 CH340 Type-C](01-gioi-thieu.md) | Nhận diện bo, cảm biến và driver |
| 2. [Hướng dẫn lập trình xe](bai-giang/02-lap-trinh.md) | Sketch, Verify, Upload, Serial |
| 3. [Điều khiển LED](bai-giang/03-led.md) | Đầu ra HIGH/LOW và thời gian |
| 4. [Điều khiển servo SG90](bai-giang/04-servo.md) | Nguồn, tín hiệu và góc |
| 5. [Động cơ DC với L298N](bai-giang/05-dong-co.md) | PWM, chiều quay, tiến/lùi/rẽ/dừng |
| 6. [Đọc HC-SR04](bai-giang/06-hc-sr04.md) | Khoảng cách và timeout |
| 7. [Cảm biến dò line TCRT5000](bai-giang/07-do-line.md) | Năm kênh và vị trí line |
| 8. [Đọc encoder](bai-giang/08-encoder.md) | Ngắt, số xung, RPM và vận tốc |
| 9. [Điều khiển xe qua Wi-Fi](bai-giang/09-wifi.md) | Nhận lệnh từ điện thoại/trình duyệt |
| 10. [Điều khiển xe với PID](bai-giang/10-pid.md) | Sai số, phản hồi và hiệu chỉnh |

Học cảm biến riêng trước khi ghép vào điều khiển motor. PID tốc độ dùng encoder; PID bám line còn cần vị trí line và một vòng điều khiển khác. Hệ số, chu vi bánh và PPR trong mã học là giá trị thử cần đo/hiệu chỉnh.

## Cài công cụ và chuẩn bị

- [Chuẩn bị](02-chuan-bi.md)
- [Cài IDE/CH340/core](03-cai-arduino-ide.md)
- [Nạp đủ project main và xem Serial](04-nap-code-va-serial.md)
- [Cài thư viện](05-cai-thu-vien.md)
- [Nút nhấn và PWM](06-lap-trinh-co-ban.md)

Ví dụ LED/Serial dùng bo riêng hoặc ngắt các kết nối robot được ghi trong bài. Không coi chân robot là chân trống để gắn thêm linh kiện. Ngắt nguồn khi đổi dây, kê bánh khi thử motor. Mã học là sketch độc lập; Upload thay chương trình robot, nên giữ bộ mã gốc để nạp lại.

## Muốn dùng ngay robot đã bàn giao?

Đọc [hướng dẫn sử dụng robot chung](08-su-dung-robot.md) để lắp ráp, nạp chương trình và dùng chức năng có sẵn. Chuỗi bài giảng phía trên giúp bạn hiểu và tự viết từng phần.

[Xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) · [Tải bộ tài liệu](../tai-xuong/robot-esp32.md)

[Bắt đầu bài 1](01-gioi-thieu.md){ .md-button .md-button--primary }
