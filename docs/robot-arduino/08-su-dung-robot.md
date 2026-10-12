# Sử dụng Robot Arduino Nano với chương trình bàn giao

**Mục tiêu:** chọn một chức năng, nạp đúng sketch và kiểm tra xe chạy theo chức năng đó. Bạn không phải viết xong toàn bộ các bài giảng mới dùng được robot.

Các bước dưới dùng chung cho bộ Nano. Chọn gói mã đi kèm xe bạn nhận; không chia hướng dẫn vận hành theo số bánh và không trộn tệp giữa các gói.

## Bạn muốn xe làm gì?

| Chức năng | Chương trình cần nạp | Cách bắt đầu |
| --- | --- | --- |
| Điều khiển bằng điện thoại | test_bluetooth.ino | Kết nối Dabble GamePad với HM-10 |
| Tự tránh vật cản | tranh_vat_can.ino hoặc tệp cùng chức năng trong gói | Kiểm tra HC-SR04, servo, encoder trước |
| Tự dò line | do_line.ino hoặc tệp cùng chức năng trong gói | Kiểm tra năm mắt, encoder và siêu âm trước |

**Mỗi chức năng là một sketch riêng.** Nạp sketch mới thay chức năng cũ; Nano không có menu web đổi chế độ như ESP32. Tải trong [bộ bàn giao Arduino](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-), chọn gói phù hợp [thứ nhất](https://drive.google.com/drive/folders/1JDA5cqlwjThLIAqfd9OYg1nh3cAbpIBu) hoặc [thứ hai](https://drive.google.com/drive/folders/1pZ4AKd9IdsDU_FH12oR0vp2u__hx4ApM) của xe.

## Trước khi nạp

- Đã [cài IDE và nạp Blink](05-cai-arduino-ide.md).
- Đã [lắp lại cảm biến](03-lap-rap.md), ghi/chụp các đầu dây.
- Motor đang ngắt nguồn, có cách kê bánh và ngắt nguồn khi thử.
- Có thư viện của chức năng: Servo cho tránh vật cản, Servo/Dabble cho Bluetooth; mã dò line đã đối chiếu dùng core Arduino.

## Bước 1. Giữ đúng sơ đồ chân

| Bộ phận / tín hiệu | Chân Nano |
| --- | --- |
| HC-SR04 Trig / Echo | A0 / A1 |
| Servo SG90 Signal | A5 |
| Line OUT1 → OUT5 | D8 / D9 / D10 / D11 / D12 |
| Encoder trái / phải | D2 / D3 |
| Driver IN1 / IN2 / IN3 / IN4 | D0 / D1 / D4 / D7 |
| Driver ENA / ENB | D5 / D6 |
| Nano nhận từ HM-10 TX / gửi tới HM-10 RX | A3 / A2 |

Đây là tên chân, không phải số thứ tự đếm. Đối chiếu [Sơ đồ chân.pptx](https://drive.google.com/file/d/1kHN7YzN9rrrt3P5gOQJKpwLSXNAbj3KS/view) và nhãn trên mạch thật.

Sơ đồ có chú thích **L9110s**, trong khi mã khai báo **L298N** với ENA/ENB/IN1–IN4. Nếu driver không có các chân tương ứng, không nối theo bảng bằng cách đoán; kiểm tra đúng module trước.

GND các thiết bị nối chung; nguồn VCC theo linh kiện/board. HM-10 RX có thể cần hạ mức tín hiệu từ Nano. Nếu chưa rõ nguồn/đường tín hiệu, xem bài của linh kiện trước khi bật xe.

## Bước 2. Đặt tệp vào đúng thư mục

Ví dụ dùng Bluetooth:

```text
test_bluetooth/
└── test_bluetooth.ino
```

Tên thư mục sketch trùng tên tệp .ino chính. Hướng dẫn nạp gốc gọi `main.ino`, nhưng tệp thực tế trong Drive mang tên chức năng; mở **tệp bạn đã tải**, không tạo thêm sketch rỗng main. Nếu tải một ZIP, giải nén trước rồi tìm .ino bên trong.

Giữ bản gốc, lưu bản chỉnh sửa riêng. Xem [HD nạp code gốc](https://docs.google.com/document/d/1zUuMvjFEuTOBrwMFcFzYiy-x51EDbZutoixD51jM_8Q/edit) khi cần đối chiếu.

## Bước 3. Mở, kiểm tra và Upload

1. Ngắt nguồn motor, ngắt D0/D1 tới driver khi kết nối ảnh hưởng nạp.
2. Trong IDE chọn **File → Open**, mở .ino của chức năng.
3. Chọn **Arduino Nano / ATmega328P / đúng COM**.
4. Cài [thư viện cần thiết](06-cai-thu-vien.md), nhấn Verify và đọc lỗi nếu có.
5. Verify thành công thì Upload và chờ hoàn tất.
6. Tắt nguồn trước khi nối lại dây đã rút, kê bánh để thử chương trình.

**Kết quả cần thấy:** Upload hoàn tất. Chưa đặt xe lên sàn trước khi biết sketch tự chạy lúc khởi động hay chờ lệnh điện thoại.

## Bước 4A. Thử Bluetooth bằng Dabble

Sau khi nạp test_bluetooth.ino, kết nối đúng HM-10 trong Dabble, mở GamePad ở chế độ nút digital. Nếu chưa rõ TX/RX hoặc kết nối app, làm [bài kiểm tra lệnh Bluetooth](bai-giang/09-bluetooth.md) trước.

Khi bánh kê, thử từng nút, thả nút sau mỗi lần:

| Thao tác | Kết quả cần thấy theo mã |
| --- | --- |
| Up / Down | Tiến / lùi |
| Left / Right | Quay trái / phải |
| Thả nút hướng | Gọi lệnh dừng |
| Cross / Triangle | Tăng / giảm góc servo |
| Square / Circle / Start | Đặt góc 180° / 10° / 90° |

Kiểm tra chiều quay và khoảng servo trước khi dùng góc lớn. Comment Cross/Triangle có chỗ ngược, bảng theo hàm kiểm tra nút thực tế. Tên/mật khẩu Bluetooth không được tài liệu quy định cố định.

**Hoàn thành lượt thử:** các hướng đúng, thả nút dừng khi kết nối tốt, servo không va gá. Mã chưa có thời hạn xác nhận lệnh mới; đóng app/mất Bluetooth không bảo đảm dừng. Giữ công tắc nguồn dễ thao tác khi thử trên sàn.

## Bước 4B. Thử tránh vật cản

Trước khi bật chương trình tự động, kiểm tra [khoảng cách](bai-giang/06-hc-sr04.md), [servo](bai-giang/04-servo.md) và [encoder](bai-giang/08-encoder.md) bằng các sketch riêng. Sau đó nạp lại sketch tránh vật cản.

Mã có ngưỡng phía trước 20 cm. Khi gặp vật gần, xe dừng/quét hai phía bằng servo rồi chọn hướng quay; số đo phía trước không có Echo trả 0 thì xe dừng ở nhánh kiểm tra đó. Góc trong mã là giữa 90°, trái 180°, phải 10°; chúng phải phù hợp giới hạn gá thật.

**Kết quả cần thấy trên sàn trống:** khi gặp tấm vật đủ lớn ở gần, xe thay đổi hành động thay vì tiếp tục tiến thẳng. Thử ngắn, ở khoảng trống và chủ động ngắt nguồn khi bất thường.

Các vòng quay chờ xung encoder; thiếu xung có thể khiến xe quay không kết thúc. Khi đó tắt nguồn và sửa encoder, không tăng hệ số quay để thử tiếp. Tên hàm “90°” là mục tiêu, góc thật còn phụ thuộc hiệu chỉnh.

## Bước 4C. Thử dò line

1. Kiểm tra từng mắt theo [bài dò line](bai-giang/07-do-line.md): mã gốc nhận LOW là line, thứ tự D8–D12 từ trái tới phải theo cấu hình.
2. Nạp sketch dò line, đặt xe trên nền sáng có line tương phản và đoạn thẳng rộng rãi.
3. Đặt mắt giữa gần line, chạy thử ngắn và quan sát xe có sửa hướng về line không.
4. Thử đường rẽ/vật cản chỉ sau khi đoạn thẳng và các cảm biến đã hoạt động.

**Kết quả cần thấy:** xe phản ứng theo line. Khi không đúng, dừng để kiểm tra đầu vào/chiều motor, chưa đổi nhiều hệ số cùng lúc. Sketch dò line còn có xử lý tránh vật cản/tìm lại line, nên encoder và siêu âm cũng cần đúng.

Mã gốc tắt Serial.begin; Monitor trống khi chạy xe không tự nghĩa lỗi. Nếu cần đọc tín hiệu, chuyển về sketch chẩn đoán riêng và ngắt driver khỏi D0/D1, rồi khôi phục chương trình robot sau đó.

## Khi nào hoàn thành?

Bạn nạp đúng chức năng, nối lại dây đúng và thử được hành vi cơ bản với cách dừng/ngắt nguồn rõ ràng. Học [chuỗi bài giảng](index.md) khi muốn hiểu và tự sửa từng phần. Nếu chưa đạt, xem [xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) theo giai đoạn đang gặp.
