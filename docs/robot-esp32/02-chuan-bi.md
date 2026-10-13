# Bài 2: Chuẩn bị trước khi học lập trình ESP32

## 1. Giới thiệu

Trước khi bắt đầu lập trình xe robot ESP32, chúng ta cần chuẩn bị các thiết bị, phần mềm và kiểm tra một số kết nối phần cứng cơ bản.

Việc chuẩn bị đúng ngay từ đầu sẽ giúp quá trình thực hành thuận lợi hơn, đồng thời hạn chế những lỗi thường gặp như máy tính không nhận ESP32, nạp chương trình thất bại, sử dụng sai chân GPIO hoặc cấp nguồn không phù hợp.

Trong bài học này, chúng ta sẽ thực hiện:

- Kiểm tra các linh kiện và thiết bị của xe robot.
- Chuẩn bị máy tính và cáp USB Type-C.
- Làm quen với bo ESP32 và board mở rộng.
- Tìm hiểu các nhóm chân GPIO và chân nguồn.
- Kiểm tra nguồn điện và dây kết nối.
- Chuẩn bị thư mục lưu trữ chương trình.

Sau khi hoàn thành, bạn sẽ sẵn sàng cài đặt Arduino IDE, kết nối ESP32 với máy tính và thực hiện chương trình đầu tiên.

---

## 2. Chuẩn bị thiết bị

### 2.1. Máy tính

Để lập trình ESP32, chúng ta cần một máy tính sử dụng hệ điều hành Windows, Ubuntu hoặc macOS.

Máy tính được sử dụng để:

- Cài đặt phần mềm Arduino IDE.
- Cài đặt driver USB–UART CH340 khi cần.
- Cài đặt gói hỗ trợ bo mạch ESP32.
- Viết và chỉnh sửa chương trình.
- Biên dịch chương trình.
- Nạp chương trình vào ESP32.
- Theo dõi dữ liệu từ ESP32 thông qua Serial Monitor.

Trong chuỗi bài học, chúng ta sẽ sử dụng **Arduino IDE** làm môi trường lập trình chính.

Máy tính cần có kết nối Internet trong quá trình cài đặt phần mềm, gói hỗ trợ ESP32 và các thư viện cần thiết.

### 2.2. Bo mạch ESP32 30P CH340 Type-C

ESP32 là thiết bị quan trọng nhất cần chuẩn bị.

Bo mạch sử dụng trong bộ xe là **ESP32 classic 30 chân, sử dụng cổng USB Type-C và chip USB–UART CH340**.

<AsyncImage query="ESP32 WROOM 32 30 pin CH340 USB Type C development board top view" aspectRatio="5:3"/>

Trên bo ESP32, bạn có thể nhận diện một số thành phần:

- Module ESP32-WROOM-32.
- Cổng USB Type-C.
- Chip giao tiếp CH340.
- Các chân GPIO.
- Chân nguồn 3V3, VIN/5V và GND tùy thiết kế bo.
- Đèn LED báo nguồn.
- Nút EN/RESET để khởi động lại ESP32.
- Nút BOOT hỗ trợ chế độ nạp chương trình.

ESP32 là vi điều khiển thực hiện chương trình, trong khi CH340 giúp máy tính giao tiếp với ESP32 thông qua USB.

Cổng USB Type-C được sử dụng để kết nối máy tính, cấp nguồn USB và nạp chương trình.

Trong những bài học đầu tiên, chúng ta có thể sử dụng ESP32 độc lập hoặc gắn trên board mở rộng mà chưa cần kết nối các cảm biến và động cơ.

**Lưu ý:** Các bài học áp dụng cho ESP32 classic trong bộ xe Robovis. Nếu bo của bạn sử dụng ESP32-S3 hoặc ESP32-C3, cần lựa chọn sơ đồ chân và cấu hình lập trình tương ứng.

### 2.3. Board mở rộng ESP32

Bộ xe sử dụng **board mở rộng ESP32 30P** để kết nối các thiết bị ngoại vi.

<AsyncImage query="ESP32 30 pin expansion board GPIO sensor shield ESP32 DevKit 30P" aspectRatio="5:3"/>

Board mở rộng giúp việc kết nối phần cứng thuận tiện hơn, không cần sử dụng breadboard.

Thông thường, board mở rộng có các nhóm chân phục vụ:

- Kết nối tín hiệu GPIO.
- Kết nối GND.
- Cấp nguồn cho các module ngoại vi.
- Kết nối cảm biến và các thiết bị điều khiển.

Tùy thiết kế, một số board mở rộng có thể bố trí các chân theo nhóm ba chân:

| Ký hiệu | Chức năng |
|---|---|
| S | Signal – Chân tín hiệu |
| V | Voltage – Chân nguồn |
| G | Ground – Chân GND |

Cách bố trí và điện áp tại chân V phụ thuộc vào từng loại board mở rộng.

**Lưu ý:** Không mặc định chân V trên board mở rộng luôn là 3,3 V hoặc 5 V. Cần kiểm tra ký hiệu, jumper chọn nguồn và sơ đồ của board thực tế trước khi kết nối linh kiện.

Board mở rộng không làm thay đổi mức logic GPIO 3,3 V của ESP32.

### 2.4. Cáp USB Type-C

Cáp USB được sử dụng để kết nối ESP32 với máy tính.

Thông qua cáp USB, chúng ta có thể:

- Cấp nguồn cho bo ESP32 trong quá trình lập trình.
- Nạp chương trình từ máy tính vào ESP32.
- Truyền và nhận dữ liệu thông qua giao tiếp Serial.

**Lưu ý:** Cần sử dụng cáp USB Type-C có khả năng truyền dữ liệu. Một số loại cáp chỉ hỗ trợ sạc và không thể sử dụng để nạp chương trình.

Khi kết nối ESP32 với máy tính, đèn nguồn trên bo có thể sáng. Tuy nhiên, điều này chưa đảm bảo máy tính đã nhận được cổng giao tiếp.

Chúng ta sẽ kiểm tra cổng COM và driver CH340 trong bài cài đặt Arduino IDE.

### 2.5. Bộ xe robot ESP32

Đối với các bài thực hành điều khiển robot, chúng ta sẽ sử dụng bộ xe đã được lắp ráp với các linh kiện sau:

| STT | Linh kiện | Số lượng | Chức năng |
|---|---|---|---|
| 1 | ESP32 30P CH340 Type-C | 1 | Bộ điều khiển trung tâm |
| 2 | Board mở rộng ESP32 30P | 1 | Kết nối các linh kiện |
| 3 | Động cơ giảm tốc DC | 2 | Tạo chuyển động cho xe |
| 4 | Module L298N | 1 | Điều khiển động cơ |
| 5 | Cảm biến Encoder | 2 | Đo chuyển động bánh xe |
| 6 | Cảm biến HC-SR04 | 1 | Đo khoảng cách |
| 7 | Cảm biến dò line TCRT5000 5 mắt | 1 | Phát hiện đường line |
| 8 | Bộ pin và công tắc | 1 bộ | Cấp nguồn cho xe |
| 9 | Khung xe và bánh xe | 1 bộ | Lắp đặt các linh kiện |

Tùy cấu hình sản phẩm, robot có thể được trang bị thêm servo hoặc cơ cấu gắp.

Trong một phiên bản mã bàn giao, GPIO18 được sử dụng để điều khiển servo gắp. Chỉ đấu nối thiết bị này khi robot thực tế có cơ cấu tương ứng.

Nếu đã có bộ xe được lắp ráp hoàn chỉnh, bạn chưa cần tháo rời hoặc thay đổi các kết nối.

Chúng ta sẽ lần lượt sử dụng từng linh kiện trong những bài học tương ứng.

Bạn có thể tham khảo [hướng dẫn lắp ráp robot Robovis](https://drive.google.com/file/d/1Tu1aiRez8NBzwQ63apHPXwV0UD9wpH0b/view) để kiểm tra vị trí và cách kết nối các thành phần.

### 2.6. Dây kết nối và dụng cụ hỗ trợ

Ngoài các linh kiện chính, nên chuẩn bị thêm:

- Dây jumper hoặc dây Dupont để kết nối board mở rộng với cảm biến.
- Tua vít nhỏ để tháo lắp linh kiện khi cần.
- Đồng hồ đo điện để kiểm tra điện áp nguồn nếu có.
- Giá kê hoặc vật đỡ để nâng bánh xe khỏi mặt đất khi thử động cơ.

Đối với các bài học điều khiển LED và đọc nút nhấn, cần chuẩn bị thêm:

- LED thông thường.
- Điện trở hạn dòng 330 Ω – 1 kΩ.
- Nút nhấn.

Các linh kiện này sẽ được kết nối trực tiếp thông qua board mở rộng ESP32.

Đối với bài học nạp chương trình đầu tiên, chúng ta chỉ cần **máy tính, ESP32 và cáp USB Type-C có truyền dữ liệu**.

---

## 3. Kiểm tra xe trước khi thực hành

### 3.1. Kiểm tra các linh kiện

Trước khi cấp nguồn, hãy quan sát tổng thể xe và kiểm tra:

- ESP32 đã được cắm đúng vị trí và đúng chiều trên board mở rộng.
- Các chân ESP32 không bị cong hoặc lệch khỏi hàng chân cắm.
- Các đầu dây kết nối không bị lỏng hoặc tuột.
- Hai động cơ được cố định chắc chắn.
- Bánh xe có thể quay mà không bị kẹt.
- Driver L298N được lắp và kết nối đúng vị trí.
- Cảm biến HC-SR04 được cố định chắc chắn.
- Cảm biến dò line được đặt ở phía dưới xe.
- Hai Encoder được lắp đúng vị trí.
- Bộ pin và công tắc nguồn không bị hư hỏng.

Nếu xe đã được đấu nối sẵn, nên chụp lại hình ảnh các đầu dây trước khi thực hiện bất kỳ thay đổi nào.

Không cần tháo toàn bộ hệ thống để bắt đầu học lập trình.

### 3.2. Kiểm tra nguồn điện

Xe robot sử dụng nguồn điện để cấp cho bộ điều khiển và các thiết bị ngoại vi.

Trước khi bật nguồn, cần kiểm tra:

- Cực dương và cực âm của bộ pin.
- Điện áp nguồn phù hợp với driver và các linh kiện.
- Các dây nguồn không bị chạm chập.
- Công tắc nguồn hoạt động bình thường.
- Các đầu nối nguồn trên board mở rộng được kết nối đúng.

**Lưu ý:** Không nối trực tiếp điện áp của bộ pin vào chân 3V3 hoặc VIN/5V của ESP32 khi chưa xác định được điện áp và sơ đồ cấp nguồn.

Khi thực hành ESP32 qua cáp USB, nên tắt nguồn pin của xe.

Nếu board mở rộng có mạch cấp nguồn riêng, cần kiểm tra sơ đồ trước khi cấp đồng thời nguồn USB và nguồn ngoài.

### 3.3. Kiểm tra kết nối động cơ

Xe sử dụng hai động cơ DC được điều khiển thông qua module L298N.

ESP32 gửi tín hiệu điều khiển đến L298N, còn driver sử dụng nguồn động cơ để tạo công suất cho các động cơ DC.

Trong quá trình thử nghiệm, động cơ có thể quay ngay khi ESP32 bắt đầu thực hiện chương trình đang lưu trong bộ nhớ.

Vì vậy, trước khi nạp hoặc chạy chương trình điều khiển động cơ, cần:

- Đặt xe trên mặt phẳng ổn định.
- Kê bánh xe lên khỏi mặt đất trong lần thử đầu tiên.
- Kiểm tra các dây kết nối giữa ESP32 và L298N.
- Đảm bảo có thể ngắt nguồn động cơ khi cần thiết.

Không đặt xe trực tiếp gần mép bàn khi chưa biết chương trình đang chạy.

---

## 4. Làm quen với các chân kết nối ESP32

ESP32 cung cấp nhiều chân tín hiệu để kết nối với cảm biến và các thiết bị bên ngoài.

Các chân này được chia thành một số nhóm chính.

### 4.1. Chân Digital GPIO

Các chân vào/ra đa mục đích trên ESP32 được gọi là GPIO.

Ví dụ:

- GPIO23.
- GPIO22.
- GPIO21.
- GPIO18.
- GPIO19.
- GPIO32.
- GPIO33.

GPIO có thể được sử dụng để đọc hoặc xuất tín hiệu logic với hai trạng thái:

- `HIGH`: Mức logic cao.
- `LOW`: Mức logic thấp.

Ví dụ:

- Xuất tín hiệu điều khiển chiều quay động cơ.
- Đọc trạng thái cảm biến dò line.
- Đọc xung từ Encoder.
- Điều khiển bật và tắt LED.

Trên ESP32, mức logic GPIO danh định là **3,3 V**.

Không đưa trực tiếp tín hiệu 5 V vào chân GPIO.

Một số chân GPIO còn hỗ trợ chức năng PWM, thường được sử dụng để điều chỉnh tốc độ động cơ.

**Lưu ý:** GPIO34–GPIO39 trên ESP32 classic chỉ hỗ trợ đầu vào, không thể sử dụng để xuất tín hiệu điều khiển thông thường.

### 4.2. Chân Analog

ESP32 có bộ chuyển đổi tín hiệu Analog sang Digital, gọi là ADC.

ADC cho phép vi điều khiển đọc điện áp thay đổi liên tục từ cảm biến và chuyển thành giá trị số.

Ví dụ:

- Đọc cảm biến ánh sáng có đầu ra Analog.
- Đọc cảm biến điện áp.
- Đọc tín hiệu Analog từ cảm biến khoảng cách phù hợp.

Trên ESP32 classic, ADC thường được chia thành hai nhóm:

- ADC1.
- ADC2.

Độ phân giải đọc ADC thường được cấu hình ở mức 12 bit, tương ứng giá trị số từ 0 đến 4095.

Giá trị thực tế còn phụ thuộc cấu hình độ phân giải, mức suy hao và giới hạn đo.

**Lưu ý:** Trên ESP32 classic, ADC2 có thể xung đột với Wi-Fi. Vì vậy, khi cần đọc Analog đồng thời với Wi-Fi, nên ưu tiên những chân ADC1 phù hợp.

### 4.3. Chân PWM

PWM là phương pháp tạo tín hiệu xung với tỷ lệ thời gian mức cao có thể thay đổi.

Trong robot, PWM thường được sử dụng để:

- Điều chỉnh tốc độ động cơ DC.
- Tạo tín hiệu điều khiển servo.
- Điều chỉnh độ sáng LED.

ESP32 sử dụng phần cứng PWM, chẳng hạn bộ điều khiển LEDC, để tạo tín hiệu với tần số và độ phân giải phù hợp.

Trong bài điều khiển động cơ, chúng ta sẽ tìm hiểu cách sử dụng PWM để thay đổi tốc độ quay của bánh xe.

### 4.4. Chân nguồn

Một số chân nguồn thường gặp trên ESP32 và board mở rộng:

| Chân | Chức năng |
|---|---|
| 3V3 | Đường nguồn 3,3 V |
| GND | Điểm tham chiếu điện áp chung |
| VIN hoặc 5V | Đường nguồn theo thiết kế bo |
| EN | Chân cho phép hoạt động/reset ESP32 |

Khi kết nối cảm biến, chúng ta cần xác định đúng chân nguồn, chân GND và chân tín hiệu.

Ví dụ, một module cảm biến thường có ba chân:

- VCC: Cấp nguồn.
- GND: Nối đất.
- OUT hoặc Signal: Xuất tín hiệu về ESP32.

Trên board mở rộng, các chân có thể được bố trí thành nhóm S–V–G để thuận tiện khi kết nối.

Tuy nhiên, cần kiểm tra điện áp tại chân V trước khi sử dụng.

Không được nhầm lẫn giữa chân nguồn và chân tín hiệu vì có thể làm hỏng linh kiện.

---

## 5. Lưu ý khi kết nối và nạp chương trình

### 5.1. Các chân UART0

Trên ESP32 classic, UART0 thường sử dụng:

- GPIO3: RX0, nhận dữ liệu.
- GPIO1: TX0, truyền dữ liệu.

Hai chân này thường được kết nối với chip CH340 để phục vụ quá trình nạp chương trình và giao tiếp Serial.

Nếu kết nối thêm thiết bị ngoại vi vào GPIO1 hoặc GPIO3, thiết bị đó có thể ảnh hưởng đến quá trình nạp chương trình hoặc sử dụng Serial Monitor.

Để hạn chế lỗi:

- Không tự ý đấu thêm thiết bị vào GPIO1 và GPIO3.
- Khi gặp lỗi nạp chương trình, kiểm tra các kết nối ngoại vi có thể gây xung đột.
- Chỉ thay đổi dây sau khi đã ngắt nguồn.
- Khôi phục đúng kết nối theo sơ đồ sản phẩm sau khi kiểm tra.

### 5.2. Các chân ảnh hưởng đến quá trình khởi động

Một số chân ESP32 classic có chức năng xác định chế độ khởi động, thường được gọi là chân strapping.

Ví dụ:

- GPIO0.
- GPIO2.
- GPIO5.
- GPIO12.
- GPIO15.

Trạng thái của các chân này tại thời điểm reset có thể ảnh hưởng đến quá trình khởi động hoặc nạp chương trình.

Trong bộ robot, một số chân thuộc nhóm này có thể được sử dụng để điều khiển L298N.

Vì vậy, không tự ý thay đổi kết nối hoặc gắn thêm linh kiện vào những chân này khi chưa kiểm tra sơ đồ.

Nếu ESP32 không khởi động hoặc không nạp được chương trình, cần kiểm tra cả trạng thái các chân strapping.

### 5.3. Không thay đổi dây khi đang cấp nguồn

Trong quá trình thực hành, chúng ta sẽ thường xuyên kết nối và thay đổi các linh kiện.

Để đảm bảo an toàn:

1. Tắt nguồn xe.
2. Rút cáp USB nếu cần thay đổi kết nối.
3. Kiểm tra sơ đồ chân.
4. Thực hiện đấu nối trên board mở rộng.
5. Kiểm tra lại trước khi cấp nguồn.

Không nên cắm hoặc rút dây nguồn, dây tín hiệu khi mạch đang hoạt động.

### 5.4. Kiểm tra chương trình đang có trên ESP32

ESP32 có thể đã được nạp chương trình điều khiển robot trước đó.

Khi cấp nguồn, ESP32 sẽ tự động chạy chương trình đang lưu trong bộ nhớ Flash.

Điều này có nghĩa là động cơ hoặc thiết bị ngoại vi có thể hoạt động ngay khi bật công tắc.

Vì vậy, khi chưa biết chương trình đang có trên xe, cần kê bánh xe lên khỏi mặt đất hoặc ngắt nguồn động cơ trước khi thử nghiệm.

### 5.5. Lưu ý khi sử dụng GPIO của robot

Các chân GPIO trên robot đã được phân bổ cho những thiết bị cụ thể.

Ví dụ, trong cấu hình chương trình sản phẩm:

- GPIO12, GPIO14 và GPIO13 được sử dụng cho một kênh động cơ.
- GPIO4, GPIO2 và GPIO15 được sử dụng cho kênh động cơ còn lại.
- GPIO21 và GPIO19 được sử dụng cho HC-SR04.
- GPIO26 và GPIO22 được sử dụng cho Encoder.
- GPIO32, GPIO33, GPIO34, GPIO27 và GPIO35 được sử dụng cho cảm biến dò line.

Đây là cấu hình cần đối chiếu với phiên bản mã nguồn và sơ đồ chân thực tế của robot.

Khi thực hành LED, nút nhấn hoặc thiết bị khác, không sử dụng các chân đã được kết nối với thiết bị robot nếu chưa ngắt kết nối tương ứng.

Trong một số phiên bản có servo gắp, GPIO18 đã được sử dụng cho servo. Không kết nối thêm nút nhấn vào GPIO18 khi servo còn đang đấu nối.

Xem [sơ đồ chân và hướng dẫn sử dụng robot](08-su-dung-robot.md).

---

## 6. Chuẩn bị thư mục lưu chương trình

Trong quá trình học, chúng ta sẽ viết nhiều chương trình khác nhau cho từng linh kiện.

Để dễ quản lý, nên tạo một thư mục riêng trên máy tính.

Ví dụ:

```text
HocRobotESP32/
├── 01_Serial/
│   └── 01_Serial.ino
│
├── 02_LED/
│   └── 02_LED.ino
│
├── 03_Servo/
│   └── 03_Servo.ino
│
├── 04_DongCo/
│   └── 04_DongCo.ino
│
├── 05_HCSR04/
│   └── 05_HCSR04.ino
│
├── 06_DoLine/
│   └── 06_DoLine.ino
│
├── 07_Encoder/
│   └── 07_Encoder.ino
│
├── 08_WiFi/
│   └── 08_WiFi.ino
│
└── 09_PID/
    └── 09_PID.ino
```

Mỗi chương trình Arduino thường được lưu dưới dạng tệp có phần mở rộng `.ino`.

Arduino IDE quản lý chương trình trong thư mục có cùng tên với tệp chính.

Việc lưu riêng từng bài giúp chúng ta dễ dàng kiểm tra, chỉnh sửa và sử dụng lại chương trình trong những bài học tiếp theo.

Nếu bộ xe đã có chương trình hoàn chỉnh, nên sao lưu mã nguồn gốc trước khi nạp các chương trình thực hành mới.

**Lưu ý:** Khi nạp một chương trình mới vào ESP32, chương trình ứng dụng trước đó sẽ được thay thế. Vì vậy, cần giữ bộ mã nguồn bàn giao để có thể nạp lại khi muốn sử dụng robot.

---

## 7. Kiểm tra trước khi bắt đầu

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã chuẩn bị máy tính để cài đặt Arduino IDE.
- [ ] Đã có ESP32 30P CH340 Type-C và board mở rộng.
- [ ] Đã có cáp USB Type-C hỗ trợ truyền dữ liệu.
- [ ] Đã nhận diện các linh kiện chính của xe.
- [ ] Đã kiểm tra sơ bộ nguồn điện và dây kết nối.
- [ ] Đã biết vị trí các chân GPIO và chân nguồn.
- [ ] Đã hiểu ESP32 sử dụng mức logic GPIO 3,3 V.
- [ ] Đã biết lưu ý về GPIO1, GPIO3 và các chân strapping.
- [ ] Đã tắt nguồn động cơ để chuẩn bị thực hành.
- [ ] Đã tạo thư mục để lưu các chương trình.

---

## 8. Tổng kết

Qua bài học này, chúng ta đã chuẩn bị các thiết bị cần thiết và làm quen với những yêu cầu cơ bản trước khi lập trình ESP32.

Những nội dung quan trọng bao gồm:

- Chuẩn bị ESP32 30P CH340 Type-C, board mở rộng, máy tính và cáp USB.
- Kiểm tra các linh kiện và kết nối của xe robot.
- Phân biệt các nhóm chân GPIO, Analog, PWM và chân nguồn.
- Nắm được các lưu ý về mức logic 3,3 V.
- Hiểu những chân GPIO có chức năng đặc biệt.
- Nắm được nguyên tắc cấp nguồn và nạp chương trình an toàn.
- Tổ chức thư mục để quản lý mã nguồn trong quá trình học.

Ở bài tiếp theo, chúng ta sẽ bắt đầu **cài đặt Arduino IDE, driver CH340 và gói hỗ trợ ESP32**, sau đó kết nối ESP32 với máy tính và nạp chương trình đầu tiên để kiểm tra hoạt động của bo mạch.

---

[Bài trước: Giới thiệu xe ESP32](01-gioi-thieu.md) · [Bài tiếp: Cài đặt Arduino IDE và driver CH340](03-cai-arduino-ide.md)