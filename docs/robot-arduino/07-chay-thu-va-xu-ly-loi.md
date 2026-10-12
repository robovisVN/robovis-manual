# Chạy thử Robot Arduino và xử lý lỗi

**Mục tiêu:** xác định lỗi ở cài đặt, nạp, đọc dữ liệu hay chuyển động, rồi kiểm tra đúng phần. Không sửa mọi đoạn mã và mọi đầu dây cùng lúc.

## Bạn đang gặp lỗi ở đâu?

| Bạn thấy gì? | Mở mục |
| --- | --- |
| Máy không nhận Nano/không có COM | Kiểm tra kết nối USB |
| Verify báo lỗi | Kiểm tra mã và thư viện |
| Verify được nhưng Upload lỗi | Kiểm tra cấu hình nạp |
| Upload xong nhưng kết quả sai | Kiểm tra đúng sketch, dây và từng bộ phận |
| Xe tự chạy hoặc không dừng | Ngắt nguồn motor trước khi tiếp tục kiểm tra |

**Verify** chạy trên máy tính; **Upload** gửi mã tới Nano; **chạy chương trình** là việc diễn ra sau đó trên bo. Ba giai đoạn cần kiểm tra khác nhau.

## Nếu không có cổng COM

1. Rút Nano, xem Device Manager rồi cắm lại.
2. Xem Ports (COM & LPT) có thêm cổng nào không.
3. Nếu không, thử cáp dữ liệu/cổng USB khác; đèn nguồn sáng chưa chứng minh có dữ liệu.
4. Nếu Windows báo thiếu driver, xác định chip USB trên bo; dùng driver phù hợp, như CH340 khi đúng chip.

**Kết quả cần thấy:** một COM xuất hiện/biến mất theo Nano. Chọn chính cổng đó trong IDE. Xem [bài cài đặt](05-cai-arduino-ide.md) khi chưa rõ thao tác.

## Nếu Verify báo lỗi

Giữ mã mẫu chưa sửa và đọc lỗi đầu tiên trong Output:

| Ví dụ lỗi | Bắt đầu kiểm tra |
| --- | --- |
| expected ';' hoặc '}' | Dấu chấm phẩy/ngoặc ở dòng báo lỗi và phía trước |
| Servo.h / Dabble.h: No such file or directory | Đúng [thư viện](06-cai-thu-vien.md) đã cài chưa |
| redefinition of setup / loop | Có chép thêm setup/loop thay vì thay phần cũ không |
| Tên hàm/biến không được nhận | Viết hoa/thường, khai báo và tệp đang mở |

**Kết quả cần thấy:** Verify hoàn tất trước khi Upload. Chưa đấu lại cảm biến để chữa một lỗi cú pháp trên máy tính.

## Nếu Upload báo not in sync hoặc stk500_recv

Kiểm tra lần lượt:

1. Board là **Arduino Nano**, Port đúng cổng.
2. Processor là **ATmega328P** theo bộ bàn giao; thử Old Bootloader khi bo thực tế dùng bootloader cũ.
3. Nguồn motor ngắt, driver IN1/IN2 không ảnh hưởng D0/D1. Thử Nano riêng để tách lỗi kết nối robot.
4. Đóng ứng dụng khác đang dùng COM; rút/cắm và chọn lại Port nếu cần.

**Kết quả cần thấy:** nạp được Blink trên Nano riêng. Chưa kết luận phải nạp lại bootloader hoặc bo đã hỏng chỉ từ một thông báo này.

## Nếu Upload được nhưng không có log

Chạy [sketch thông báo nhỏ](bai-giang/02-lap-trinh.md), mở Monitor đúng COM và chọn 9600. Thông báo xuất hiện thì đường giao tiếp đã chạy.

Sketch motor của bộ xe không dùng Serial để in log trên D0/D1. Monitor trống khi đang chạy nó không tự có nghĩa lỗi. Khi muốn chẩn đoán cảm biến, dùng sketch riêng và ngắt driver khỏi D0/D1 theo bài, rồi khôi phục mã robot sau đó.

## Nếu linh kiện không phản ứng

| Hiện tượng | Thử riêng theo bài nào? | Kết quả cần thấy |
| --- | --- | --- |
| Servo không quay/kẹt | [Servo](bai-giang/04-servo.md) | Góc nhỏ đổi được, không va gá/ốc |
| Motor không quay/đảo chiều sai | [L298N](bai-giang/05-dong-co.md) | Mỗi bên chạy một lượt rồi dừng |
| Khoảng cách không đổi | [HC-SR04](bai-giang/06-hc-sr04.md) | Vật gần/xa làm số đo đổi |
| Không nhận line | [Dò line](bai-giang/07-do-line.md) | Mỗi mắt đổi giá trị trên line/nền |
| Encoder không đếm | [Encoder](bai-giang/08-encoder.md) | Quay một bánh chỉ số bên đó tăng |
| App kết nối nhưng không chạy đúng | [Bluetooth đọc lệnh](bai-giang/09-bluetooth.md) | Từng nút tạo đúng thông báo |

Khi servo/motor làm Nano khởi động lại, ngắt tải và kiểm tra nguồn, dòng tải, dây/GND. Không tăng PWM/góc để che lỗi nguồn hoặc cơ cấu kẹt. Servo gá siêu âm cần kiểm tra ốc theo [ảnh nhận hàng](03-lap-rap.md).

## Chạy thử xe sau khi từng phần đạt

1. Giữ một bản mã đã chạy đúng, ghi board/Processor và thư viện.
2. Nạp đúng sketch chức năng từ [bộ bàn giao](08-su-dung-robot.md).
3. Tắt nguồn, nối về đúng sơ đồ, kê bánh rồi mới cấp nguồn.
4. Với điều khiển tay, thử tiến, dừng, lùi, dừng, quay từng chiều và dừng; mỗi lần ngắn.
5. Xác nhận nút dừng/thả nút hoạt động khi kết nối tốt, và công tắc có thể ngắt nguồn motor.
6. Chỉ hạ xe xuống sàn trống khi chiều quay và dừng đã đúng.

Các mã tự động có thể chạy ngay khi cấp nguồn; không nạp một chương trình rồi bật xe trên mép bàn. Mã tránh vật cản chờ đủ xung lúc quay, encoder lỗi có thể làm quay kéo dài: tắt nguồn và sửa encoder trước khi thử lại.

## Khi cần nhờ hỗ trợ

Gửi tên bo, ảnh rõ nhãn chân, sketch đang dùng, board/Processor/COM và toàn bộ lỗi dạng văn bản. Nêu cụ thể **“Verify được, Upload lỗi”** hoặc **“Upload được, motor trái không quay”**, cùng bước cuối đã chạy đúng. Thông tin đó giúp khoanh vùng tốt hơn câu “xe không chạy”.

[Lộ trình](index.md) · [Cài đặt](05-cai-arduino-ide.md) · [Sử dụng bộ mã](08-su-dung-robot.md)
