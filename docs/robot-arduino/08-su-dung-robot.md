# Sử dụng Robot Arduino Nano theo bộ tài liệu bàn giao

**Mục tiêu:** lắp cảm biến, nạp mã và chạy Bluetooth, tránh vật cản hoặc dò line. Hướng dẫn dùng chung cho Robot Arduino Nano, không tách bài theo số bánh.

Nguồn: [thư mục Arduino Robovis](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-), [HD nạp code](https://docs.google.com/document/d/1zUuMvjFEuTOBrwMFcFzYiy-x51EDbZutoixD51jM_8Q/edit), [HD khi nhận hàng](https://docs.google.com/document/d/1v15Tzh_bDJ4Tez326MCeS8L-1pQc-sz2sl5fraLJJmo/edit) và [Sơ đồ chân.pptx](https://drive.google.com/file/d/1kHN7YzN9rrrt3P5gOQJKpwLSXNAbj3KS/view). Bảng chân được đối chiếu thêm với các tệp `.ino` trong bộ bàn giao.

## 1. Lắp ráp và đối chiếu chân

Lắp cảm biến theo [ảnh khi nhận hàng](03-lap-rap.md), ngắt nguồn trước khi đổi dây. Đây là tên chân in trên Nano, không phải số thứ tự đếm chân.

| Tín hiệu | Chân Nano trong mã |
| --- | --- |
| HC-SR04 Trig / Echo | A0 / A1 |
| Servo SG90 Signal | A5 |
| Dò line OUT1 → OUT5 | D8, D9, D10, D11, D12 |
| Encoder trái / phải | D2 / D3 |
| Driver IN1 / IN2 / IN3 / IN4 | D0 / D1 / D4 / D7 |
| Driver ENA / ENB, PWM | D5 / D6 |
| RX của Nano / TX của Nano tới Bluetooth | A3 / A2, theo Dabble.begin(9600, A3, A2) |

HM10 TX nối về A3; HM10 RX nhận từ A2 qua chuyển mức nếu module yêu cầu. Dabble trên Nano dùng SoftwareSerial; không chuyển module sang D0/D1. Kiểm tra nguồn/logic đúng module trước khi nối.

!!! warning "Driver và D0/D1"
    Sơ đồ chú thích **L9110s**, nhưng mã khai báo **L298N** và sử dụng ENA/ENB/IN1–IN4. Kiểm tra tên, nhãn chân trên driver thật trước khi cấp nguồn; không dùng bảng này cho module chân khác. D0/D1 đang điều khiển driver: ngắt hai đường này khi nạp nếu gây lỗi, và không dùng Hardware Serial in log đồng thời trong chương trình robot.

Nguồn động cơ qua driver, không qua GPIO. Các mạch giao tiếp không cách ly nối chung GND; cấp nguồn dương theo đúng linh kiện/board mở rộng. Không suy ra mọi chân V đều có cùng điện áp.

## 2. Chọn mã và nạp

Mỗi chức năng là một sketch riêng. Nạp sketch mới thay chương trình cũ; mã Nano không có menu web chuyển chế độ như ESP32.

| Chức năng | Tên tệp trong bộ bàn giao | Thư viện |
| --- | --- | --- |
| Bluetooth | test_bluetooth.ino | Dabble, Servo |
| Tránh vật cản | tranh_vat_can.ino hoặc tranh_vat_can_4wd.ino | Servo |
| Dò line | do_line.ino hoặc do_line_4wd.ino | Core Arduino AVR |

Drive có các gói theo cấu hình xe. Chọn gói đi kèm robot bạn nhận, làm cùng quy trình dưới đây và không trộn tệp giữa các gói: [thư mục mã gói thứ nhất](https://drive.google.com/drive/folders/1JDA5cqlwjThLIAqfd9OYg1nh3cAbpIBu), [thư mục mã gói thứ hai](https://drive.google.com/drive/folders/1pZ4AKd9IdsDU_FH12oR0vp2u__hx4ApM).

1. Tải tệp chức năng cần chạy; đặt `.ino` trong thư mục trùng tên, ví dụ `test_bluetooth/test_bluetooth.ino`.
2. Ngắt nguồn động cơ, cắm Nano qua cáp dữ liệu. Ngắt tín hiệu driver D0/D1 nếu ảnh hưởng nạp; ghi lại để nối đúng sau đó.
3. **File → Open**, mở tệp vừa tải. Hướng dẫn gốc gọi `main.ino`, nhưng dùng tên thực tế trong gói, không tạo thêm sketch rỗng tên main.
4. Chọn **Arduino Nano**, **ATmega328P**, đúng **COM**. Cài thư viện theo [bài thư viện](06-cai-thu-vien.md).
5. Verify rồi Upload, chờ báo hoàn tất. Old Bootloader chỉ thử khi đã kiểm tra cáp/cổng và bo thực tế dùng bootloader cũ.
6. Ngắt nguồn trước khi nối lại dây, kê bánh khỏi sàn để kiểm tra trước khi thử trên sàn.

## 3. Điều khiển Bluetooth

Nạp `test_bluetooth.ino`, kiểm tra HM10 và kết nối điện thoại qua **Dabble → GamePad** theo [hướng dẫn STEMpedia](https://ai.thestempedia.com/docs/dabble-app/gamepad-module/). Baud module cần phù hợp `9600` trong mã. Chọn đúng module robot; tài liệu không quy định một tên Bluetooth hoặc mật khẩu cố định.

| Nút | Hành động trong mã |
| --- | --- |
| Up / Down | Tiến / lùi |
| Left / Right | Quay trái / phải |
| Không giữ hướng | Gọi stopMotor() |
| Cross / Triangle | Tăng / giảm góc servo |
| Square / Circle / Start | Đặt góc 180° / 10° / 90° |

Comment Triangle/Cross trong tệp gốc ngược với hàm kiểm tra nút; bảng trên theo lệnh thực sự chạy. Kiểm tra giới hạn cơ khí trước khi dùng Square/Circle. Thả nút và thử xe dừng khi kết nối hoạt động; mã chưa có thời hạn xác nhận lệnh mới, nên không coi mất Bluetooth là cách dừng bảo đảm.

## 4. Tránh vật cản

Nạp sketch tránh vật cản. HC-SR04 nhìn trước; servo quét hai phía khi vật ở gần. Mã dùng `OBSTACLE_THRESHOLD = 20` cm; phép đo phía trước không nhận Echo trả 0 thì xe dừng. Góc cấu hình giữa 90°, trái 180°, phải 10°; chỉ thử sau khi gá/ốc không gây kẹt.

Thử trên sàn trống với vật lớn phản xạ tốt và sẵn sàng ngắt nguồn động cơ. Hàm quay chờ encoder đủ xung: encoder không hoạt động có thể làm xe tiếp tục quay. Khi đó tắt nguồn, kiểm tra D2/D3 và đĩa encoder. Tên hàm quay 90° không bảo đảm góc thực tế nếu chưa hiệu chỉnh cơ khí.

## 5. Dò line

Nạp sketch dò line, đặt đường line tương phản trên nền sáng dưới cảm biến. Trong mã, D8 → D12 tương ứng từ trái ngoài tới phải ngoài; xác nhận hướng lắp module thật. `onLine()` nhận LOW là thấy line.

Kiểm tra từng kênh thay đổi khi đưa qua line/nền trước khi chạy. Nếu cần Serial chẩn đoán, dùng sketch riêng và tháo driver khỏi D0/D1. Mã gốc tắt `Serial.begin()`, nên Monitor trống không tự có nghĩa robot lỗi.

Thử đoạn thẳng rồi góc rẽ và vật cản. Sketch dò line còn có xử lý tránh vật cản/tìm lại line; kiểm tra siêu âm và encoder trước khi thử. Thay một tham số mỗi lần, giữ bản gốc và ghi kết quả.

**Hoàn thành:** nạp đúng chức năng, dây khớp mã và chủ động dừng/ngắt nguồn khi hành vi không đúng.

[Lộ trình Nano](index.md) · [Xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) · [Tải tài liệu](../tai-xuong/robot-arduino.md)
