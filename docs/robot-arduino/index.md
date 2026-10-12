# Học và sử dụng Robot Arduino Nano

Bạn có thể bắt đầu dù chưa biết lập trình hoặc chưa từng đấu dây điện tử. Bộ bài này giúp bạn làm quen với từng bộ phận, chạy một ví dụ nhỏ, kiểm tra kết quả rồi mới ghép thành chức năng của xe.

Các bài áp dụng cho **Arduino Nano classic dùng ATmega328P** và bộ robot trong [thư mục bàn giao Robovis](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-). Mỗi bài dùng chung sơ đồ chân của bộ robot, không tách hướng dẫn theo số bánh.

## Bạn muốn bắt đầu từ đâu?

| Tình huống của bạn | Bắt đầu ở đây |
| --- | --- |
| Mới nhận xe, muốn biết xe có những gì | [Bài 1: Giới thiệu xe](01-gioi-thieu.md) |
| Chưa có Arduino IDE trên máy tính | [Chuẩn bị](02-chuan-bi.md), rồi [cài IDE và nạp thử](05-cai-arduino-ide.md) |
| Đã nạp được chương trình, muốn học tự viết mã | [Bài 2: Lập trình đầu tiên](bai-giang/02-lap-trinh.md) |
| Muốn dùng ngay Bluetooth, dò line hoặc tránh vật cản | [Sử dụng chương trình bàn giao](08-su-dung-robot.md) |
| Đang gặp lỗi | [Kiểm tra theo từng hiện tượng](07-chay-thu-va-xu-ly-loi.md) |

## Máy tính và robot làm gì?

**Máy tính** dùng Arduino IDE để viết và nạp chương trình. **Nano trên robot** thực hiện chương trình đó: đọc cảm biến và gửi lệnh cho mạch điều khiển động cơ. Khi đã nạp xong, Nano vẫn chạy khi có nguồn, kể cả khi không nối máy tính.

Bạn chưa cần học ROS 2 hoặc Ubuntu để làm các bài này. Nếu dùng Windows, bắt đầu bằng Arduino IDE và cáp USB.

## Học theo thứ tự nào?

| Bài | Bạn sẽ làm được gì trước khi học tiếp? |
| --- | --- |
| [1. Giới thiệu xe Arduino Nano](01-gioi-thieu.md) | Chỉ được Nano, driver, cảm biến và nguồn trên xe |
| [2. Lập trình xe từ đầu](bai-giang/02-lap-trinh.md) | Nạp mã và nhìn thấy một dòng thông báo từ Nano |
| [3. Điều khiển LED](bai-giang/03-led.md) | Làm đèn trên Nano bật, tắt và đổi nhịp |
| [4. Servo SG90](bai-giang/04-servo.md) | Đưa servo về giữa, rồi quay trong khoảng nhỏ |
| [5. Động cơ DC và L298N](bai-giang/05-dong-co.md) | Thử từng bên động cơ, đảo chiều và dừng |
| [6. Cảm biến HC-SR04](bai-giang/06-hc-sr04.md) | Đọc được khoảng cách và nhận biết lúc không có số đo |
| [7. Cảm biến dò line](bai-giang/07-do-line.md) | Thấy từng mắt cảm biến đổi tín hiệu trên nền và line |
| [8. Encoder](bai-giang/08-encoder.md) | Quay bánh bằng tay và quan sát số xung tăng |
| [9. Bluetooth HM-10](bai-giang/09-bluetooth.md) | Nhấn nút trên điện thoại và thấy Nano nhận đúng lệnh |
| [10. Làm quen với PID](bai-giang/10-pid.md) | Hiểu cách đo tốc độ rồi sửa mức điều khiển động cơ |

Hai bài cuối cần kiến thức từ các bài trước. Bạn không cần hiểu PID để nạp chương trình có sẵn hoặc điều khiển xe bằng điện thoại.

## Cách làm một bài thực hành

1. Đọc mục **Trước khi làm** và chuẩn bị đúng trạng thái đấu dây.
2. Chạy mã của bước đầu tiên; chưa ghép nhiều ví dụ với nhau.
3. So sánh đèn, chuyển động hoặc dòng thông báo với mục **Kết quả cần thấy**.
4. Nếu khác, xử lý ngay tại bước đó rồi mới học tiếp.
5. Lưu bản đã chạy đúng, sau đó chỉ thay một giá trị để quan sát sự khác nhau.

**Nạp mã mới sẽ thay chương trình cũ trên Nano.** Tạo một thư mục riêng cho mỗi bài và giữ bộ mã bàn giao để khôi phục xe sau khi học.

Một số bài đọc dữ liệu dùng D0/D1 để nối máy tính, trong khi robot dùng hai chân này điều khiển driver. [Bài chuẩn bị](02-chuan-bi.md) giải thích cách ngắt dây đúng; không chỉ tắt nguồn motor rồi bỏ qua các dây tín hiệu.

## Các hướng dẫn có thể mở lại khi cần

- [Cài Arduino IDE, chọn Nano và cổng COM](05-cai-arduino-ide.md).
- [Thêm thư viện Servo/Dabble](06-cai-thu-vien.md).
- [Lắp cảm biến theo ảnh khi nhận hàng](03-lap-rap.md).
- [Thực hành nút nhấn và cách dùng millis](04-lap-trinh.md).
- [Sơ đồ chân, bộ mã và cách sử dụng robot](08-su-dung-robot.md).

[Bắt đầu bài 1](01-gioi-thieu.md){ .md-button .md-button--primary }
[Tải tài liệu đọc trên máy](../tai-xuong/robot-arduino.md){ .md-button }
