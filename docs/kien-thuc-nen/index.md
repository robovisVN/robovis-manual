# Bắt đầu từ đây

Bạn không cần học hết mọi thứ trước khi làm robot. Chọn lối vào gần với kinh nghiệm và mục tiêu của mình, thực hành từng bước rồi chuyển sang tài liệu sản phẩm khi đã sẵn sàng.

- [A. Tôi mới bắt đầu học điện tử và lập trình](#lo-trinh-a).
- [B. Tôi đã biết Arduino/ESP32, muốn học robot ROS 2](#lo-trinh-b).
- [C. Tôi đã có robot Robovis, muốn sử dụng ngay](#lo-trinh-c).

## A. Tôi mới bắt đầu học điện tử và lập trình { #lo-trinh-a }

**Dành cho ai:** chưa quen đấu mạch hoặc chưa tự viết được một chương trình nhỏ. Chưa cần học Ubuntu hay ROS 2 ở giai đoạn này.

**Cần chuẩn bị:** máy tính, Arduino IDE, một bo **Arduino Nano classic ATmega328P, logic 5 V**, cáp USB dữ liệu. Bài GPIO cần nút nhấn; bài ADC/PWM cần biến trở 10 kΩ, LED và điện trở 1 kΩ. Các bài điện đầu tiên có thể làm trên giấy. Nếu chỉ có ESP32, vẫn học được phần lập trình qua Serial theo từng bài; không sao chép cách đấu 5 V của Nano sang ESP32.

### Thứ tự nên học

1. **Điện cơ bản:** [Điện áp, dòng điện và công suất](dien-dien-tu/01-dien-ap-dong-dien-cong-suat.md) → [GND và nối chung mass](dien-dien-tu/02-gnd-va-noi-chung-mass.md) → [Tín hiệu 3,3 V và 5 V](dien-dien-tu/03-tin-hieu-3v3-va-5v.md).
2. **Chuẩn bị công cụ:** theo [cài IDE và nạp Blink cho Nano](../robot-arduino/03-cai-arduino-ide.md). Nếu dùng ESP32, theo [cài IDE và gói ESP32](../robot-esp32/03-cai-arduino-ide.md). Quy trình nằm trong tài liệu sản phẩm và được dùng lại tại đây.
3. **Lập trình cơ bản:** [Biến và kiểu dữ liệu](lap-trinh/01-bien-kieu-du-lieu-toan-tu.md) → [Điều kiện](lap-trinh/02-cau-lenh-dieu-kien.md) → [Vòng lặp](lap-trinh/03-vong-lap.md) → [Hàm](lap-trinh/04-ham-va-chia-chuong-trinh.md) → [Thời gian với millis()](lap-trinh/05-delay-va-millis.md).
4. **Vi điều khiển và ngoại vi:** [GPIO và điện trở kéo](vi-dieu-khien/01-gpio-va-dien-tro-keo.md) → [Digital, ADC và PWM](vi-dieu-khien/02-digital-adc-pwm.md).
5. **Áp dụng vào robot:** chọn [Arduino](../robot-arduino/index.md) hoặc [ESP32](../robot-esp32/index.md). Làm theo sơ đồ và chân nối của đúng sản phẩm, bắt đầu từ LED rồi đến cảm biến và động cơ.

**Kết quả đạt được:** phân biệt nguồn với tín hiệu, biết giới hạn điện áp trước khi nối dây, viết chương trình có điều kiện và hàm, đọc nút nhấn và điều chỉnh LED trên mạch thực hành.

**Có thể bỏ qua:** phần cài IDE nếu đã Verify/Upload được; từng bài lập trình nếu bạn giải thích và tự sửa được ví dụ. Trước khi chuyển sang robot, vẫn đối chiếu điện áp và sơ đồ sản phẩm.

**Tự kiểm tra:** bạn giải thích được vì sao ESP32 không nhận trực tiếp tín hiệu 5 V, vì sao nút INPUT_PULLUP nhấn lại đọc LOW, và vì sao PWM không phải nguồn analog ổn định.

## B. Tôi đã biết Arduino/ESP32, muốn học robot ROS 2 { #lo-trinh-b }

**Dành cho ai:** đã quen nạp chương trình, cảm biến và điều khiển cơ bản, muốn hiểu phần mềm robot chạy trên máy tính.

**Cần chuẩn bị:** máy tính chạy Ubuntu 22.04, trực tiếp hoặc trong máy ảo theo tài liệu hiện có. Lộ trình dùng **ROS 2 Humble**, phù hợp Robot ESP32 LiDAR trong bộ tài liệu này. Bài ROS 2 mở đầu không cần robot; phần LiDAR cần robot và workspace (thư mục phần mềm dự án) do Robovis bàn giao.

### Thứ tự nên học

1. [Ubuntu và công cụ](../ubuntu-co-ban/index.md): đọc bài 1–6 để mở Terminal, tìm tệp và nạp môi trường; bài 7 cần robot, có thể để đến bước thực hành. Dùng bài 8 để tự kiểm tra thao tác.
2. [Lộ trình robot và ROS 2](robot-ros2/index.md): làm bài truyền dữ liệu giữa hai chương trình mẫu trên máy tính, rồi đọc bài node/topic hiện có theo chỉ dẫn.
3. [Hệ tọa độ và TF từ đầu](robot-ros2/he-toa-do-va-tf.md): hiểu trục tọa độ và quan hệ map, odom, base_link; tiếp tục bài RViz của sản phẩm.
4. [Robot ESP32 LiDAR](../robot-esp32-lidar/index.md): chuẩn bị môi trường/workspace → kết nối Wi-Fi → khởi động và kiểm tra dữ liệu → chạy thử → SLAM và điều hướng theo lộ trình sản phẩm.

**Kết quả đạt được:** phân biệt chương trình trên ESP32 với node ROS 2 trên PC, xem được dữ liệu topic, hiểu vì sao RViz cần TF và biết bắt đầu kiểm tra robot từ đâu.

**Có thể bỏ qua:** bài điện và lập trình cơ bản nếu đã nắm; bài Ubuntu 1–5 nếu đã tự dùng Terminal, cd, ls và đường dẫn. Vẫn kiểm tra phiên bản ROS 2 và môi trường ở bài 6; không dùng phần mềm robot với phiên bản khác chỉ vì đã quen Linux.

**Tự kiểm tra:** bạn chạy được ví dụ ROS 2, phân biệt topic với frame và biết đọc header.frame_id trước khi đổi Fixed Frame trong RViz.

## C. Tôi đã có robot Robovis, muốn sử dụng ngay { #lo-trinh-c }

**Dành cho ai:** muốn cài đặt, kết nối và vận hành robot theo cấu hình bàn giao, chưa cần tự viết chương trình.

**Cần chuẩn bị:** đúng robot, nguồn và phụ kiện theo hướng dẫn của sản phẩm; máy tính theo yêu cầu từng bộ. Nếu định nạp lại firmware (chương trình chạy trên bo điều khiển), cần giữ mã nguồn bàn giao trước khi thay chương trình.

### Chọn đúng sản phẩm

- [Robot Arduino](../robot-arduino/index.md): bắt đầu phần chuẩn bị, cài IDE, thư viện rồi thực hành theo sơ đồ bộ xe.
- [Robot ESP32](../robot-esp32/index.md): kiểm tra đúng bo CH340 Type-C, cài gói ESP32 và đọc hướng dẫn tương ứng.
- [Robot ESP32 Camera](../robot-esp32-camera/index.md): nhận diện hai chương trình ESP32, chuẩn bị môi trường rồi chọn nhánh điều khiển web hoặc YOLO.
- [Robot ESP32 LiDAR](../robot-esp32-lidar/index.md): chuẩn bị Ubuntu/ROS 2, kết nối mạng, kiểm tra dữ liệu trước khi chạy thử và tạo bản đồ.

**Kết quả đạt được:** đi đúng quy trình vận hành của robot đang có, biết nơi tìm sơ đồ, cấu hình và xử lý lỗi.

**Có thể bỏ qua:** các bài lý thuyết chưa liên quan đến thao tác hiện tại. Khi gặp thuật ngữ chưa hiểu, quay lại bài nền phù hợp; không cần hoàn thành toàn bộ lộ trình A hoặc B trước.

## Tìm nhanh kiến thức còn thiếu

| Bạn đang vướng ở đâu? | Bài nên đọc |
| --- | --- |
| Chọn nguồn hoặc đọc nhãn V/A/W | [Điện áp, dòng điện và công suất](dien-dien-tu/01-dien-ap-dong-dien-cong-suat.md) |
| Có nguồn nhưng tín hiệu không ổn định | [GND và nối chung mass](dien-dien-tu/02-gnd-va-noi-chung-mass.md) |
| Nối cảm biến 5 V với ESP32 | [Tín hiệu 3,3 V và 5 V](dien-dien-tu/03-tin-hieu-3v3-va-5v.md) |
| Đọc code chưa hiểu if, for, hàm | [Biến và kiểu dữ liệu](lap-trinh/01-bien-kieu-du-lieu-toan-tu.md), rồi học theo nút bài tiếp |
| Chưa hiểu nút nhấn, ADC hoặc PWM | [GPIO](vi-dieu-khien/01-gpio-va-dien-tro-keo.md) → [Digital, ADC và PWM](vi-dieu-khien/02-digital-adc-pwm.md) |
| Chưa biết nhập lệnh ở đâu | [Terminal Ubuntu](../ubuntu-co-ban/04-terminal.md) |
| Không hiểu node, topic hoặc TF | [Robot và ROS 2 cơ bản](robot-ros2/index.md) |

**Kiến thức nền** giải thích kiến thức dùng chung và bài thực hành nhỏ. **Tài liệu theo sản phẩm** chứa sơ đồ, cấu hình và thao tác trên từng robot. Các bài khám phá, so sánh và kinh nghiệm thuộc **Góc kỹ thuật**; bạn không cần đọc chúng để bắt đầu lộ trình này.
