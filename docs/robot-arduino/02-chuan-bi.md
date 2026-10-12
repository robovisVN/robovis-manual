# Bài 2: Chuẩn bị trước khi học lập trình Arduino Nano

## 1. Giới thiệu

Trước khi bắt đầu lập trình xe robot Arduino Nano, chúng ta cần chuẩn bị các thiết bị, phần mềm và kiểm tra một số kết nối cơ bản.

Việc chuẩn bị đúng ngay từ đầu sẽ giúp quá trình thực hành thuận lợi hơn, đồng thời hạn chế những lỗi thường gặp như máy tính không nhận Arduino, nạp chương trình thất bại hoặc đấu nối sai nguồn điện.

Trong bài học này, chúng ta sẽ thực hiện:

- Kiểm tra các linh kiện và thiết bị của xe robot.
- Chuẩn bị máy tính và cáp kết nối Arduino.
- Làm quen với các chân kết nối trên Arduino Nano.
- Kiểm tra nguồn điện và dây kết nối.
- Chuẩn bị môi trường lưu trữ chương trình.

Sau khi hoàn thành, bạn sẽ sẵn sàng cài đặt Arduino IDE và thực hiện chương trình đầu tiên.

## 2. Chuẩn bị thiết bị

### 2.1. Máy tính

Để lập trình Arduino Nano, chúng ta cần một máy tính sử dụng hệ điều hành Windows, Ubuntu hoặc macOS.

Máy tính được sử dụng để:

- Cài đặt phần mềm Arduino IDE.
- Viết và chỉnh sửa chương trình.
- Biên dịch chương trình.
- Nạp chương trình vào Arduino Nano.
- Theo dõi dữ liệu từ Arduino trong quá trình thực hành.

Trong chuỗi bài học, chúng ta sẽ sử dụng **Arduino IDE** làm môi trường lập trình chính.

### 2.2. Board Arduino Nano

Arduino Nano là thiết bị quan trọng nhất cần chuẩn bị.

Board sử dụng trong bộ xe là **Arduino Nano classic với vi điều khiển ATmega328P**.

Trên board Arduino Nano, bạn có thể nhận diện một số thành phần:

- Cổng USB dùng để kết nối với máy tính.
- Vi điều khiển ATmega328P.
- Các chân Digital và Analog.
- Đèn LED nguồn.
- Đèn LED tích hợp dùng để kiểm tra chương trình.
- Nút Reset để khởi động lại chương trình.

Trong những bài học đầu tiên, chúng ta có thể sử dụng Arduino Nano độc lập mà chưa cần kết nối với các cảm biến hoặc động cơ.

### 2.3. Cáp USB

Cáp USB được sử dụng để kết nối Arduino Nano với máy tính.

Thông qua cáp USB, chúng ta có thể:

- Cấp nguồn cho Arduino trong quá trình lập trình.
- Nạp chương trình từ máy tính vào Arduino.
- Truyền và nhận dữ liệu thông qua giao tiếp Serial.

**Lưu ý:** Cần sử dụng cáp USB có khả năng truyền dữ liệu. Một số loại cáp chỉ hỗ trợ sạc và không thể sử dụng để nạp chương trình.

Arduino Nano classic thường sử dụng cổng Mini USB, tuy nhiên cần kiểm tra cổng thực tế trên board để lựa chọn đúng loại cáp.

### 2.4. Bộ xe robot Arduino

Đối với những bài học thực hành điều khiển robot, chúng ta sẽ sử dụng bộ xe đã được lắp ráp với các linh kiện sau:

| STT | Linh kiện | Số lượng | Chức năng |
|---|---|---|---|
| 1 | Arduino Nano | 1 | Bộ điều khiển trung tâm |
| 2 | Board mở rộng Nano | 1 | Kết nối các linh kiện |
| 3 | Động cơ giảm tốc DC màu vàng | 2 | Tạo chuyển động |
| 4 | Module L298N | 1 | Điều khiển động cơ |
| 5 | Module encoder ngoài | 2 | Đo chuyển động bánh xe |
| 6 | Cảm biến HC-SR04 | 1 | Đo khoảng cách |
| 7 | Servo SG90 | 1 | Xoay cảm biến siêu âm |
| 8 | Cảm biến dò line TCRT5000 5 mắt | 1 | Phát hiện đường line |
| 9 | Bluetooth HM-10 | 1 | Giao tiếp với điện thoại |
| 10 | Bộ pin và công tắc | 1 bộ | Cấp nguồn cho xe |
| 11 | Khung xe và bánh xe | 1 bộ | Lắp đặt các linh kiện |

Nếu đã có bộ xe được lắp ráp hoàn chỉnh, bạn chưa cần tháo rời hoặc thay đổi các kết nối.

Chúng ta sẽ lần lượt sử dụng từng linh kiện trong những bài học tương ứng.

### 2.5. Dây kết nối và dụng cụ hỗ trợ

Ngoài các linh kiện chính, nên chuẩn bị thêm một số dụng cụ:

- Dây jumper để kết nối Arduino với cảm biến.
- Tua vít nhỏ để tháo lắp linh kiện khi cần.
- Breadboard để thử nghiệm mạch điện.
- Đồng hồ đo điện để kiểm tra điện áp nguồn nếu có.
- Giá kê hoặc vật đỡ để nâng bánh xe khỏi mặt đất khi thử động cơ.

Đối với bài học nạp chương trình đầu tiên, chúng ta chỉ cần **máy tính, Arduino Nano và cáp USB**.

## 3. Kiểm tra xe trước khi thực hành

### 3.1. Kiểm tra các linh kiện

Trước khi cấp nguồn, hãy quan sát tổng thể xe và kiểm tra:

- Arduino Nano đã được cắm đúng vị trí trên board mở rộng.
- Các đầu dây kết nối không bị lỏng hoặc tuột.
- Hai động cơ được cố định chắc chắn.
- Bánh xe có thể quay mà không bị kẹt.
- Cảm biến siêu âm và servo được lắp đúng vị trí.
- Cảm biến dò line được đặt ở phía dưới xe.
- Hai module encoder được đặt đúng vị trí so với đĩa encoder.
- Bộ pin và công tắc nguồn không bị hư hỏng.

Nếu xe đã được đấu nối sẵn, nên chụp lại hình ảnh các đầu dây trước khi thực hiện bất kỳ thay đổi nào.

### 3.2. Kiểm tra nguồn điện

Xe robot sử dụng nguồn điện để cấp cho bộ điều khiển và các thiết bị ngoại vi.

Trước khi bật nguồn, cần kiểm tra:

- Cực dương và cực âm của bộ pin.
- Điện áp nguồn phù hợp với driver và các linh kiện.
- Các dây nguồn không bị chạm chập.
- Công tắc nguồn hoạt động bình thường.

**Lưu ý:** Không nối trực tiếp điện áp của bộ pin vào chân 5V Arduino nếu chưa xác định được điện áp và sơ đồ cấp nguồn.

Khi thực hành với Arduino Nano qua cáp USB, nên tắt nguồn pin của xe. Nếu sử dụng board mở rộng có mạch cấp nguồn riêng, cần kiểm tra sơ đồ trước khi cấp đồng thời nguồn USB và nguồn ngoài.

### 3.3. Kiểm tra kết nối động cơ

Xe sử dụng hai động cơ DC được điều khiển thông qua module L298N.

Trong quá trình thử nghiệm, động cơ có thể quay ngay khi Arduino bắt đầu thực hiện chương trình.

Vì vậy, trước khi nạp hoặc chạy chương trình điều khiển động cơ, cần:

- Đặt xe trên mặt phẳng ổn định.
- Kê bánh xe lên khỏi mặt đất trong lần thử đầu tiên.
- Kiểm tra các dây kết nối giữa Arduino và L298N.
- Đảm bảo có thể ngắt nguồn động cơ khi cần thiết.

Không đặt xe trực tiếp trên mặt bàn hoặc gần mép bàn khi chưa biết chương trình đang chạy.

## 4. Làm quen với các chân kết nối Arduino Nano

Arduino Nano cung cấp nhiều chân tín hiệu để kết nối với cảm biến và các thiết bị bên ngoài.

Các chân này được chia thành một số nhóm chính.

### 4.1. Chân Digital

Các chân Digital được ký hiệu từ **D0 đến D13**.

Chúng có thể được sử dụng để đọc hoặc xuất tín hiệu logic với hai trạng thái:

- HIGH: mức logic cao.
- LOW: mức logic thấp.

Ví dụ:

- Xuất tín hiệu điều khiển chiều quay động cơ.
- Đọc trạng thái cảm biến dò line.
- Đọc xung từ encoder.
- Điều khiển bật và tắt LED.

Một số chân Digital còn hỗ trợ chức năng PWM, thường được sử dụng để điều chỉnh tốc độ động cơ.

### 4.2. Chân Analog

Các chân Analog trên Arduino Nano được ký hiệu từ **A0 đến A7**.

Chúng được sử dụng để đọc tín hiệu điện áp thay đổi liên tục từ các cảm biến.

Đối với Arduino Nano ATmega328P, bộ chuyển đổi ADC có độ phân giải 10 bit, cho phép biểu diễn giá trị đo trong khoảng từ 0 đến 1023.

Ngoài chức năng đọc Analog, các chân A0 đến A5 còn có thể được sử dụng như chân Digital.

Trong bộ xe của chúng ta:

- A0 được sử dụng để điều khiển chân TRIG của HC-SR04.
- A1 được sử dụng để đọc chân ECHO của HC-SR04.
- A5 được sử dụng để điều khiển servo SG90.

Riêng A6 và A7 chỉ hỗ trợ đầu vào Analog trên Arduino Nano classic.

### 4.3. Chân nguồn

Một số chân nguồn thường gặp trên Arduino Nano:

| Chân | Chức năng |
|---|---|
| 5V | Đường nguồn 5V |
| 3V3 | Đường nguồn 3,3V |
| GND | Điểm nối đất chung |
| VIN | Đầu vào nguồn ngoài theo thông số board |

Khi kết nối cảm biến, chúng ta cần xác định đúng chân nguồn, chân GND và chân tín hiệu.

Ví dụ, một module cảm biến thường có ba chân:

- VCC: Cấp nguồn.
- GND: Nối đất.
- OUT hoặc Signal: Xuất tín hiệu về Arduino.

Không được nhầm lẫn giữa chân nguồn và chân tín hiệu vì có thể làm hỏng linh kiện.

## 5. Lưu ý khi kết nối và nạp chương trình

### 5.1. Chân D0 và D1

Trên Arduino Nano, hai chân D0 và D1 được sử dụng cho giao tiếp Serial phần cứng:

- D0: RX, nhận dữ liệu.
- D1: TX, truyền dữ liệu.

Hai chân này cũng được sử dụng trong quá trình nạp chương trình thông qua USB.

Trong bộ xe hiện tại, D0 và D1 được kết nối với các chân điều khiển của L298N.

Vì vậy, kết nối này có thể gây xung đột khi nạp chương trình hoặc sử dụng Serial Monitor.

Để hạn chế lỗi:

- Nên thực hành bài nạp chương trình đầu tiên với Arduino Nano độc lập.
- Khi nạp chương trình trên xe, cần kiểm tra kết nối D0 và D1.
- Nếu gặp lỗi, hãy tắt nguồn và tạm thời ngắt dây driver khỏi hai chân này trước khi nạp.
- Khôi phục kết nối đúng sơ đồ sau khi hoàn thành.

**Lưu ý:** Chỉ tắt nguồn động cơ không đồng nghĩa với việc hai chân D0 và D1 đã được ngắt khỏi driver.

### 5.2. Không thay đổi dây khi đang cấp nguồn

Trong quá trình thực hành, chúng ta sẽ thường xuyên kết nối và thay đổi các linh kiện.

Để đảm bảo an toàn:

1. Tắt nguồn xe.
2. Rút cáp USB nếu cần thay đổi kết nối.
3. Kiểm tra sơ đồ chân.
4. Thực hiện đấu nối.
5. Kiểm tra lại trước khi cấp nguồn.

Không nên cắm hoặc rút dây tín hiệu, dây nguồn khi mạch đang hoạt động.

### 5.3. Kiểm tra chương trình đang có trên Arduino

Arduino Nano có thể đã được nạp một chương trình trước đó.

Khi cấp nguồn, Arduino sẽ tự động chạy chương trình đang lưu trong bộ nhớ.

Điều này có nghĩa là động cơ hoặc servo có thể hoạt động ngay khi bật công tắc.

Vì vậy, khi chưa biết chương trình đang có trên xe, cần kê bánh xe lên khỏi mặt đất hoặc ngắt nguồn động cơ trước khi thử nghiệm.

## 6. Chuẩn bị thư mục lưu chương trình

Trong quá trình học, chúng ta sẽ viết nhiều chương trình khác nhau cho từng linh kiện.

Để dễ quản lý, nên tạo một thư mục riêng trên máy tính.

Ví dụ:

```text
HocRobotArduino/
├── 01_Blink/
│   └── 01_Blink.ino
│
├── 02_DongCo/
│   └── 02_DongCo.ino
│
├── 03_Servo/
│   └── 03_Servo.ino
│
├── 04_HCSR04/
│   └── 04_HCSR04.ino
│
├── 05_DoLine/
│   └── 05_DoLine.ino
│
├── 06_Encoder/
│   └── 06_Encoder.ino
│
└── 07_Bluetooth/
    └── 07_Bluetooth.ino
```

Mỗi chương trình Arduino thường được lưu dưới dạng tệp có phần mở rộng `.ino`.

Arduino IDE sẽ quản lý chương trình trong thư mục có cùng tên với tệp chính.

Việc lưu riêng từng bài giúp chúng ta dễ dàng kiểm tra, chỉnh sửa và sử dụng lại chương trình trong những bài học tiếp theo.

Nếu bộ xe đã có chương trình hoàn chỉnh, nên sao lưu mã nguồn gốc trước khi nạp các chương trình thực hành mới.

## 7. Kiểm tra trước khi bắt đầu

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã chuẩn bị máy tính để cài đặt Arduino IDE.
- [ ] Đã có Arduino Nano và cáp USB truyền dữ liệu.
- [ ] Đã nhận diện các linh kiện chính của xe.
- [ ] Đã kiểm tra sơ bộ nguồn điện và dây kết nối.
- [ ] Đã biết vị trí các chân Digital, Analog và chân nguồn.
- [ ] Đã hiểu lưu ý về hai chân D0 và D1.
- [ ] Đã tạo thư mục để lưu các chương trình thực hành.

## 8. Tổng kết

Qua bài học này, chúng ta đã chuẩn bị các thiết bị cần thiết và làm quen với những yêu cầu cơ bản trước khi lập trình Arduino Nano.

Những nội dung quan trọng bao gồm:

- Chuẩn bị Arduino Nano, máy tính và cáp USB.
- Kiểm tra các linh kiện và kết nối của xe robot.
- Phân biệt các nhóm chân Digital, Analog và chân nguồn.
- Nắm được các lưu ý khi cấp nguồn và nạp chương trình.
- Tổ chức thư mục để quản lý mã nguồn trong quá trình học.

Ở bài tiếp theo, chúng ta sẽ bắt đầu **cài đặt Arduino IDE, kết nối Arduino Nano với máy tính và nạp chương trình Blink đầu tiên** để kiểm tra hoạt động của board.