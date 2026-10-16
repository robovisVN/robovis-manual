# Học lập trình và điều khiển Robot ESP32 30P CH340 Type-C

## 1. Giới thiệu

Chào mừng bạn đến với bộ tài liệu **Học lập trình và điều khiển Robot ESP32 30P CH340 Type-C**.

Bộ tài liệu được xây dựng dành cho người mới bắt đầu tìm hiểu về lập trình vi điều khiển, điện tử và robot, đồng thời phù hợp với những người đã có kiến thức Arduino và muốn chuyển sang sử dụng ESP32.

Thông qua các bài học, chúng ta sẽ từng bước tìm hiểu cấu tạo của xe robot, cách lập trình ESP32, điều khiển động cơ, đọc dữ liệu cảm biến và xây dựng các chức năng điều khiển có phản hồi.

Nội dung được tổ chức theo phương pháp **học lý thuyết kết hợp thực hành**. Mỗi bài tập trung vào một thành phần hoặc chức năng cụ thể, từ tìm hiểu nguyên lý, kết nối phần cứng đến viết chương trình, chạy thử và đánh giá kết quả.

Bộ tài liệu áp dụng cho **bo mạch ESP32 DevKit 30 chân (30P), sử dụng cổng USB Type-C và chip giao tiếp USB–UART CH340**, cùng các linh kiện được trang bị trên bộ xe robot.

Tài liệu và chương trình của sản phẩm được cung cấp tại:

[Bộ tài liệu Robot ESP32 Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt)

Các bài học sử dụng chung cấu hình chân của sản phẩm, không phân chia lộ trình theo số lượng bánh xe.

---

## 2. Bạn sẽ học được những gì?

Sau khi hoàn thành chương trình, bạn có thể:

- Nhận biết các thành phần phần cứng của xe robot ESP32.
- Hiểu sự khác biệt cơ bản giữa ESP32 và Arduino Nano.
- Cài đặt Arduino IDE và gói hỗ trợ ESP32.
- Kết nối ESP32 với máy tính thông qua USB Type-C.
- Viết, biên dịch và nạp chương trình vào ESP32.
- Sử dụng các chân GPIO, tín hiệu Digital và PWM.
- Điều khiển LED, servo SG90 và động cơ DC.
- Điều khiển tốc độ và chiều quay động cơ thông qua L298N.
- Đọc dữ liệu từ cảm biến siêu âm HC-SR04.
- Xác định vị trí vạch bằng cảm biến dò line TCRT5000.
- Đọc xung Encoder để tính tốc độ quay và vận tốc bánh xe.
- Sử dụng Wi-Fi của ESP32 để nhận lệnh điều khiển.
- Làm quen với thuật toán PID trong điều khiển tốc độ động cơ.
- Kết hợp các thành phần để xây dựng những chức năng robot hoàn chỉnh.

Mục tiêu của chương trình không chỉ là nạp và chạy được mã mẫu, mà còn giúp bạn hiểu cách ESP32 xử lý dữ liệu và điều khiển phần cứng, từ đó có thể tự phát triển hoặc mở rộng chức năng của robot.

---

## 3. Tìm hiểu về hệ thống Robot ESP32

### 3.1. ESP32 là gì?

ESP32 là dòng vi điều khiển được phát triển bởi Espressif Systems, tích hợp nhiều tính năng phục vụ các ứng dụng điều khiển và kết nối không dây.

So với những bo Arduino cơ bản như Arduino Nano ATmega328P, ESP32 có một số đặc điểm nổi bật:

- Bộ xử lý có hiệu năng cao hơn.
- Nhiều chân GPIO có thể cấu hình cho các chức năng khác nhau.
- Hỗ trợ giao tiếp Wi-Fi và Bluetooth trên những dòng ESP32 phù hợp.
- Hỗ trợ PWM để điều khiển động cơ và thiết bị ngoại vi.
- Hỗ trợ ngắt để đọc tín hiệu từ cảm biến và Encoder.
- Có thể sử dụng Arduino IDE để lập trình.

Trong bộ robot này, ESP32 đóng vai trò bộ điều khiển trung tâm, tiếp nhận dữ liệu cảm biến, xử lý chương trình và phát lệnh điều khiển đến các thiết bị.

### 3.2. ESP32 30P CH340 Type-C

Bo mạch sử dụng trong tài liệu có những đặc điểm nhận dạng chính:

| Thành phần | Mô tả |
|---|---|
| Vi điều khiển | ESP32 |
| Số chân trên bo | 30 chân |
| Cổng USB | USB Type-C |
| Chip USB–UART | CH340 |
| Kết nối không dây | Wi-Fi và Bluetooth theo khả năng của chip ESP32 |
| Môi trường lập trình | Arduino IDE |
| Mức logic GPIO | 3,3 V |

**Lưu ý:** ESP32 sử dụng mức logic GPIO 3,3 V. Không được đưa trực tiếp tín hiệu 5 V vào chân GPIO nếu không có mạch chuyển mức phù hợp.

Cổng USB Type-C được sử dụng để cấp nguồn và kết nối ESP32 với máy tính trong quá trình lập trình.

Chip CH340 thực hiện chức năng chuyển đổi giao tiếp USB sang UART để máy tính có thể truyền chương trình và trao đổi dữ liệu với ESP32.

### 3.3. Các thành phần chính của xe robot

| Thành phần | Chức năng |
|---|---|
| ESP32 30P CH340 Type-C | Bộ điều khiển trung tâm |
| Driver L298N | Điều khiển chiều quay và tốc độ động cơ |
| Động cơ DC | Tạo chuyển động cho xe |
| Servo SG90 | Điều chỉnh góc quay của cơ cấu hoặc cảm biến |
| Cảm biến HC-SR04 | Đo khoảng cách đến vật cản |
| Cảm biến dò line TCRT5000 | Phát hiện vị trí vạch di chuyển |
| Encoder | Đếm xung chuyển động của bánh xe |
| Wi-Fi | Giao tiếp và nhận lệnh điều khiển không dây |
| Bộ nguồn | Cung cấp năng lượng cho hệ thống |

Từng thành phần sẽ được giới thiệu và thực hành riêng trong các bài học trước khi kết hợp thành hệ thống điều khiển robot.

### 3.4. Nguyên lý hoạt động tổng quát

Trong hệ thống robot, ESP32 thực hiện ba nhóm nhiệm vụ chính:

**Thu thập dữ liệu**

ESP32 đọc tín hiệu từ cảm biến khoảng cách, cảm biến dò line và Encoder.

**Xử lý và ra quyết định**

Chương trình phân tích dữ liệu, xác định trạng thái robot và tính toán lệnh điều khiển.

**Điều khiển thiết bị**

ESP32 gửi tín hiệu đến L298N, servo hoặc các thiết bị ngoại vi để thực hiện chuyển động mong muốn.

Quá trình hoạt động có thể mô tả như sau:

```text
Cảm biến HC-SR04 ────┐
                     |
Cảm biến dò line ────┼──> ESP32 ───> L298N ───> Động cơ DC
                     |       |
Encoder ─────────────┘       +─────> Servo SG90
                             |
Điện thoại / Trình duyệt     |
          |                  |
          +──── Wi-Fi ───────+
```

Ví dụ, trong chức năng điều khiển tốc độ có phản hồi:

1. ESP32 gửi tín hiệu PWM đến L298N để điều khiển động cơ.
2. Encoder tạo xung khi bánh xe quay.
3. ESP32 đọc số xung và tính tốc độ thực tế.
4. Chương trình so sánh tốc độ thực tế với tốc độ mong muốn.
5. Bộ điều khiển điều chỉnh PWM để giảm sai số tốc độ.

Đây là nguyên lý cơ bản của điều khiển vòng kín, sẽ được tìm hiểu trong bài PID.

---

## 4. Lộ trình học lập trình Robot ESP32

Chương trình gồm 10 bài học, được sắp xếp từ kiến thức lập trình cơ bản đến điều khiển robot có phản hồi.

### Giai đoạn 1: Làm quen với ESP32 và lập trình cơ bản

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 1: Giới thiệu xe ESP32](01-gioi-thieu.md) | Tìm hiểu cấu tạo xe và các linh kiện | Nhận biết ESP32, driver, cảm biến và nguồn |
| [Bài 2: Lập trình ESP32 từ đầu](bai-giang/02-lap-trinh.md) | Cấu trúc sketch, Verify, Upload và Serial | Viết, nạp chương trình và quan sát dữ liệu |
| [Bài 3: Điều khiển LED](bai-giang/03-led.md) | Điều khiển GPIO và thời gian | Bật, tắt và thay đổi nhịp LED |

Sau giai đoạn này, bạn sẽ biết cách sử dụng Arduino IDE để lập trình ESP32, điều khiển GPIO và kiểm tra hoạt động của chương trình.

### Giai đoạn 2: Điều khiển cơ cấu chấp hành

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 4: Điều khiển Servo SG90](bai-giang/04-servo.md) | Tín hiệu điều khiển, nguồn và góc quay | Đưa servo về vị trí giữa và thay đổi góc |
| [Bài 5: Điều khiển động cơ DC bằng L298N](bai-giang/05-dong-co.md) | Điều khiển chiều quay và PWM | Điều khiển xe tiến, lùi, rẽ và dừng |

Sau giai đoạn này, bạn sẽ hiểu cách ESP32 tạo tín hiệu điều khiển và sử dụng L298N để điều khiển chuyển động của xe.

### Giai đoạn 3: Đọc và xử lý dữ liệu cảm biến

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 6: Cảm biến HC-SR04](bai-giang/06-hc-sr04.md) | Nguyên lý đo khoảng cách và xử lý timeout | Đọc và hiển thị khoảng cách |
| [Bài 7: Cảm biến dò line TCRT5000](bai-giang/07-do-line.md) | Đọc năm kênh cảm biến và xác định vị trí line | Nhận biết vạch di chuyển |
| [Bài 8: Đọc tín hiệu Encoder](bai-giang/08-encoder.md) | Ngắt, đếm xung, RPM và vận tốc | Tính tốc độ bánh xe từ Encoder |

Sau giai đoạn này, bạn sẽ biết cách đọc và xử lý tín hiệu từ các cảm biến để phục vụ những thuật toán điều khiển robot.

### Giai đoạn 4: Giao tiếp và điều khiển nâng cao

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 9: Điều khiển xe qua Wi-Fi](bai-giang/09-wifi.md) | Giao tiếp Wi-Fi và nhận lệnh điều khiển | Điều khiển xe từ điện thoại hoặc trình duyệt |
| [Bài 10: Điều khiển tốc độ bằng PID](bai-giang/10-pid.md) | Sai số, phản hồi và hiệu chỉnh tốc độ | Điều chỉnh PWM dựa trên tốc độ đo từ Encoder |

Hai bài cuối sử dụng kiến thức từ những bài trước, đặc biệt là điều khiển động cơ và đọc tín hiệu Encoder.

**Phân biệt hai ứng dụng PID:**

- PID tốc độ sử dụng sai số giữa tốc độ đặt và tốc độ đo từ Encoder.
- PID bám line sử dụng sai số vị trí của vạch so với vị trí mong muốn.

Đây là hai bài toán điều khiển khác nhau, dù có thể sử dụng cùng nguyên lý PID.

---

## 5. Chuẩn bị môi trường lập trình ESP32

Trước khi bắt đầu thực hành, chúng ta cần cài đặt môi trường lập trình và kiểm tra kết nối giữa ESP32 với máy tính.

### 5.1. Phần mềm cần chuẩn bị

| Thành phần | Mục đích |
|---|---|
| Arduino IDE | Viết và nạp chương trình |
| ESP32 Board Package | Hỗ trợ biên dịch và nạp chương trình cho ESP32 |
| Driver CH340 | Giúp máy tính nhận diện giao tiếp USB–UART nếu chưa có driver |
| Thư viện Arduino | Cung cấp các chức năng điều khiển theo từng bài |

Thực hiện theo các hướng dẫn:

1. [Chuẩn bị thiết bị và kết nối phần cứng](02-chuan-bi.md).
2. [Cài đặt Arduino IDE, driver CH340 và ESP32 core](03-cai-arduino-ide.md).
3. [Nạp chương trình và sử dụng Serial Monitor](04-nap-code-va-serial.md).
4. [Cài đặt thư viện cần thiết](05-cai-thu-vien.md).

### 5.2. Kiểm tra kết nối ESP32

Sau khi cài đặt, bạn cần:

- Kết nối ESP32 với máy tính bằng cáp USB Type-C hỗ trợ truyền dữ liệu.
- Xác định cổng COM trên Windows.
- Chọn đúng loại bo mạch ESP32 trong Arduino IDE.
- Biên dịch và nạp thành công một chương trình kiểm tra.
- Quan sát dữ liệu từ ESP32 thông qua Serial Monitor.

**Lưu ý:** Tên bo mạch cần chọn trong Arduino IDE phụ thuộc vào phiên bản ESP32 và cấu hình thực tế của bo 30P. Không chọn board chỉ dựa vào việc bo sử dụng cổng Type-C hoặc chip CH340.

---

## 6. Lưu ý về cấu hình chân GPIO

ESP32 có nhiều chân GPIO, nhưng không phải tất cả đều có chức năng giống nhau.

Một số chân có thể:

- Sử dụng làm đầu vào hoặc đầu ra Digital.
- Hỗ trợ PWM.
- Hỗ trợ ADC.
- Được sử dụng trong quá trình khởi động.
- Có giới hạn về chức năng đầu vào hoặc đầu ra.

Đặc biệt, trên ESP32 classic:

- GPIO34–GPIO39 chỉ hỗ trợ đầu vào.
- Một số chân có chức năng strapping, ảnh hưởng đến cấu hình khởi động.
- Các chân GPIO sử dụng mức logic 3,3 V.
- Không nên sử dụng những chân đã được kết nối với linh kiện của robot cho chức năng khác nếu chưa kiểm tra sơ đồ.

Trong bộ xe, các chân GPIO đã được phân bổ cho động cơ, cảm biến và thiết bị ngoại vi.

Vì vậy, các bài học sẽ sử dụng **cấu hình chân thống nhất của sản phẩm** để tránh xung đột khi kết hợp chương trình.

Khi thực hành các ví dụ LED hoặc Serial độc lập, cần kiểm tra và ngắt những kết nối phần cứng có thể ảnh hưởng đến quá trình thử nghiệm.

---

## 7. Phương pháp học và thực hành

Mỗi bài học được xây dựng theo cấu trúc thống nhất để người học có thể thực hiện từng bước.

### Bước 1: Xác định mục tiêu

Đọc mục tiêu bài học để biết chức năng cần thực hiện và kết quả mong đợi.

Ví dụ, trong bài điều khiển động cơ DC, mục tiêu là điều khiển được chiều quay và tốc độ của động cơ thông qua L298N.

### Bước 2: Tìm hiểu nguyên lý

Tìm hiểu cách linh kiện hoạt động và phương pháp ESP32 giao tiếp với linh kiện đó.

Ví dụ:

- LED sử dụng tín hiệu Digital.
- Động cơ DC sử dụng driver và tín hiệu PWM.
- HC-SR04 sử dụng xung Trigger và Echo.
- Encoder tạo xung theo chuyển động của bánh xe.

### Bước 3: Kiểm tra sơ đồ chân

Đối chiếu bảng chân trong bài học với cấu hình thực tế của robot.

Cần chú ý:

- Chân tín hiệu.
- Chân nguồn.
- Chân GND.
- Mức điện áp tín hiệu.
- Các chân có thể ảnh hưởng đến quá trình khởi động ESP32.

Không thay đổi dây kết nối khi hệ thống đang được cấp nguồn.

### Bước 4: Chạy chương trình mẫu

Thực hiện:

1. Mở Arduino IDE.
2. Chọn đúng Board và Port.
3. Sao chép chương trình mẫu.
4. Nhấn Verify.
5. Nhấn Upload.
6. Quan sát kết quả hoạt động.

Các chương trình trong bài học được xây dựng để kiểm tra từng chức năng riêng lẻ.

Không nên ghép nhiều chương trình mẫu khi chưa kiểm tra được hoạt động độc lập của từng phần.

### Bước 5: Kiểm tra kết quả

So sánh kết quả thực tế với nội dung mong đợi trong bài.

Ví dụ:

- LED có nhấp nháy đúng không?
- Servo có quay đến góc yêu cầu không?
- Động cơ có quay đúng chiều không?
- HC-SR04 có trả về khoảng cách hợp lý không?
- Cảm biến dò line có thay đổi tín hiệu khi gặp vạch không?
- Encoder có tăng số xung khi bánh xe quay không?
- ESP32 có nhận được lệnh điều khiển qua Wi-Fi không?

Nếu kết quả khác mong đợi, cần xử lý trước khi chuyển sang nội dung tiếp theo.

### Bước 6: Thay đổi chương trình

Sau khi chạy đúng chương trình mẫu, hãy thử thay đổi một tham số.

Ví dụ:

- Thời gian nhấp nháy LED.
- Góc quay servo.
- Mức PWM của động cơ.
- Ngưỡng phát hiện vật cản.
- Tốc độ đặt của bộ điều khiển PID.

Việc thay đổi từng tham số giúp dễ dàng quan sát ảnh hưởng của nó đến hoạt động của hệ thống.

---

## 8. Sử dụng chương trình có sẵn của robot

Ngoài các bài học, bộ robot còn được cung cấp chương trình điều khiển để sử dụng những chức năng đã tích hợp.

Bạn có thể tham khảo [hướng dẫn sử dụng robot](08-su-dung-robot.md) để tìm hiểu:

- Cách chuẩn bị và kiểm tra phần cứng.
- Cách nạp chương trình điều khiển.
- Cách sử dụng các chức năng có sẵn.
- Cách kiểm tra hoạt động của robot.
- Cách xử lý các lỗi thường gặp.

### 8.1. Phân biệt chương trình học và chương trình robot

**Chương trình học**

Được thiết kế để kiểm tra một chức năng cụ thể, ví dụ:

- Nhấp nháy LED.
- Điều khiển servo.
- Quay một động cơ.
- Đọc khoảng cách.
- Đếm xung Encoder.

**Chương trình robot hoàn chỉnh**

Kết hợp nhiều chức năng trong cùng một hệ thống, có thể bao gồm điều khiển động cơ, xử lý cảm biến, giao tiếp Wi-Fi và các thuật toán điều khiển.

Việc học các chức năng riêng lẻ trước sẽ giúp bạn dễ dàng hiểu cấu trúc của chương trình hoàn chỉnh.

### 8.2. Lưu ý khi nạp chương trình mới

Khi Upload một chương trình mới vào ESP32, chương trình ứng dụng trước đó trong vùng nạp tương ứng sẽ được thay thế.

Vì vậy, trước khi thực hành:

1. Lưu giữ bộ mã nguồn robot đã bàn giao.
2. Tạo thư mục riêng cho các chương trình học.
3. Không chỉnh sửa trực tiếp mã gốc nếu chưa có bản sao.
4. Sau khi học xong, nạp lại chương trình robot nếu muốn khôi phục chức năng ban đầu.

Đối với chương trình robot gồm nhiều tệp, cần mở đúng tệp chính và giữ nguyên cấu trúc thư mục của dự án.

---

## 9. Lưu ý an toàn khi thực hành

Khi làm việc với xe robot ESP32, cần tuân thủ một số nguyên tắc cơ bản.

### 9.1. An toàn nguồn điện

- Ngắt nguồn trước khi thay đổi dây kết nối.
- Kiểm tra cực dương và GND.
- Không cấp điện áp 5 V trực tiếp vào GPIO của ESP32.
- Kiểm tra nguồn cấp phù hợp với servo và động cơ.
- Tránh chập nguồn khi kết nối các module.

### 9.2. An toàn khi thử động cơ

- Kê xe để bánh không tiếp xúc với mặt đất khi thử lần đầu.
- Bắt đầu với mức PWM thấp.
- Kiểm tra chiều quay từng bên động cơ.
- Chuẩn bị phương án ngắt nguồn động cơ nhanh khi cần.
- Không đặt tay gần bánh xe hoặc cơ cấu đang chuyển động.

### 9.3. An toàn khi thử chương trình

- Kiểm tra chân GPIO trước khi Upload.
- Không sử dụng chân đã được đấu với linh kiện khác cho ví dụ mới khi chưa kiểm tra.
- Không tự ý tăng PWM hoặc tốc độ mục tiêu quá cao.
- Kiểm tra giá trị tham số trước khi chạy các thuật toán điều khiển.

Trong các bài PID, thông số điều khiển, chu vi bánh xe và số xung Encoder trên mỗi vòng quay cần được đo hoặc hiệu chỉnh theo phần cứng thực tế.

Các giá trị trong mã ví dụ chỉ là giá trị phục vụ học tập và thử nghiệm ban đầu.

---

## 10. Bạn nên bắt đầu từ đâu?

Tùy theo kinh nghiệm và mục đích sử dụng, bạn có thể lựa chọn nội dung phù hợp.

| Nhu cầu | Nội dung nên bắt đầu |
|---|---|
| Mới nhận xe ESP32 | [Bài 1: Giới thiệu xe](01-gioi-thieu.md) |
| Chưa biết cách cấp nguồn và kết nối | [Chuẩn bị thiết bị](02-chuan-bi.md) |
| Chưa cài Arduino IDE hoặc driver CH340 | [Cài đặt Arduino IDE](03-cai-arduino-ide.md) |
| Muốn học lập trình ESP32 từ đầu | [Bài 2: Lập trình ESP32](bai-giang/02-lap-trinh.md) |
| Muốn học GPIO và PWM | [Lập trình cơ bản](06-lap-trinh-co-ban.md) |
| Muốn điều khiển động cơ | [Bài 5: Động cơ DC và L298N](bai-giang/05-dong-co.md) |
| Muốn đọc cảm biến | [Bài 6: HC-SR04](bai-giang/06-hc-sr04.md) |
| Muốn điều khiển xe bằng điện thoại | [Bài 9: Điều khiển qua Wi-Fi](bai-giang/09-wifi.md) |
| Muốn điều khiển tốc độ có phản hồi | [Bài 10: PID](bai-giang/10-pid.md) |
| Muốn sử dụng chương trình xe có sẵn | [Hướng dẫn sử dụng robot](08-su-dung-robot.md) |
| Đang gặp lỗi | [Kiểm tra và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) |

Đối với người mới bắt đầu, nên học lần lượt từ Bài 1 đến Bài 10 để có kiến thức nền tảng trước khi phát triển các chức năng nâng cao.

---

## 11. Tài liệu và hướng dẫn bổ sung

Trong quá trình học, bạn có thể sử dụng các tài liệu sau:

- [Chuẩn bị thiết bị và kết nối phần cứng](02-chuan-bi.md).
- [Cài đặt Arduino IDE, CH340 và ESP32 core](03-cai-arduino-ide.md).
- [Nạp chương trình và sử dụng Serial Monitor](04-nap-code-va-serial.md).
- [Cài đặt thư viện](05-cai-thu-vien.md).
- [Lập trình nút nhấn và PWM](06-lap-trinh-co-ban.md).
- [Kiểm tra và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md).
- [Hướng dẫn sử dụng robot](08-su-dung-robot.md).
- [Bộ tài liệu bàn giao Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt).

---

## 12. Tổng kết

Bộ tài liệu **Học lập trình và điều khiển Robot ESP32 30P CH340 Type-C** cung cấp lộ trình học từ lập trình cơ bản đến điều khiển robot có phản hồi.

Trong quá trình học, bạn sẽ từng bước:

1. Hiểu cấu tạo và nguyên lý hoạt động của xe robot ESP32.
2. Cài đặt môi trường lập trình và nạp chương trình.
3. Sử dụng GPIO, Digital và PWM.
4. Điều khiển servo và động cơ DC.
5. Đọc dữ liệu từ các cảm biến.
6. Tính tốc độ bánh xe từ Encoder.
7. Sử dụng Wi-Fi để điều khiển robot.
8. Làm quen với thuật toán PID.
9. Kết hợp các thành phần để xây dựng những chức năng robot hoàn chỉnh.

Phương pháp học xuyên suốt là **tìm hiểu nguyên lý, kiểm tra từng chức năng độc lập, quan sát kết quả và chỉ kết hợp các chức năng sau khi đã chạy đúng**.

Sau khi hoàn thành chương trình, bạn sẽ có nền tảng để tiếp tục nghiên cứu và phát triển các ứng dụng robot sử dụng ESP32.

---

[Bắt đầu Bài 1: Giới thiệu xe ESP32](01-gioi-thieu.md)

[Hướng dẫn sử dụng robot](08-su-dung-robot.md) · [Xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) 

<!-- [Tải bộ tài liệu](../tai-xuong/robot-esp32.md) -->