# Học và sử dụng Robot Arduino Nano

## 1. Giới thiệu

Chào mừng bạn đến với bộ tài liệu **Học và sử dụng Robot Arduino Nano**.

Bộ tài liệu được xây dựng dành cho người mới bắt đầu tìm hiểu về lập trình Arduino, điện tử và robot. Bạn không cần có kiến thức lập trình hoặc kinh nghiệm sử dụng vi điều khiển trước khi bắt đầu.

Thông qua các bài học, chúng ta sẽ từng bước tìm hiểu cấu tạo của xe robot, cách lập trình Arduino Nano, điều khiển động cơ và sử dụng các cảm biến để xây dựng những chức năng điều khiển cơ bản.

Nội dung được tổ chức theo hướng **học lý thuyết kết hợp thực hành**. Mỗi bài học tập trung vào một thành phần hoặc chức năng cụ thể, giúp người học hiểu nguyên lý hoạt động, thực hiện chương trình mẫu và kiểm tra kết quả trước khi chuyển sang nội dung tiếp theo.

Bộ tài liệu áp dụng cho **Arduino Nano classic sử dụng vi điều khiển ATmega328P** và bộ xe robot được cung cấp trong [thư mục bàn giao Robovis](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-).

## 2. Bạn sẽ học được những gì?

Sau khi hoàn thành chương trình, bạn có thể:

- Nhận biết các thành phần phần cứng của xe robot Arduino Nano.
- Cài đặt Arduino IDE và nạp chương trình vào bo mạch.
- Hiểu cấu trúc cơ bản của chương trình Arduino.
- Sử dụng các chân Digital, Analog và PWM.
- Điều khiển đèn LED, động cơ servo và động cơ DC.
- Đọc dữ liệu từ cảm biến khoảng cách HC-SR04.
- Nhận biết vạch di chuyển bằng cảm biến dò line TCRT5000.
- Đọc xung Encoder để xác định chuyển động của bánh xe.
- Kết nối Bluetooth HM-10 và nhận lệnh điều khiển từ điện thoại.
- Làm quen với thuật toán PID để điều chỉnh tốc độ động cơ.
- Kết hợp các thành phần để phát triển những chức năng điều khiển xe robot.

Mục tiêu không chỉ là chạy được chương trình mẫu mà còn giúp bạn hiểu cách chương trình tương tác với phần cứng và biết cách thay đổi, kiểm tra hoặc mở rộng chức năng của robot.

---

## 3. Tìm hiểu về hệ thống Robot Arduino Nano

### 3.1. Arduino Nano đóng vai trò gì?

Arduino Nano là bộ điều khiển trung tâm của xe robot.

Chương trình được nạp vào Arduino sẽ quyết định cách robot hoạt động, bao gồm việc đọc tín hiệu từ cảm biến, xử lý dữ liệu và gửi tín hiệu điều khiển đến các thiết bị ngoại vi.

Ví dụ, khi thực hiện chức năng tránh vật cản:

1. Arduino phát tín hiệu kích hoạt cảm biến HC-SR04.
2. Cảm biến trả về tín hiệu để Arduino tính khoảng cách.
3. Chương trình kiểm tra khoảng cách đo được.
4. Arduino điều khiển động cơ thông qua L298N.
5. Robot thay đổi chuyển động theo điều kiện đã lập trình.

### 3.2. Các thành phần chính của xe robot

| Thành phần | Chức năng |
|---|---|
| Arduino Nano | Điều khiển trung tâm, xử lý chương trình |
| Driver L298N | Điều khiển tốc độ và chiều quay động cơ DC |
| Động cơ DC | Tạo chuyển động cho bánh xe |
| Servo SG90 | Điều chỉnh góc quay của cơ cấu hoặc cảm biến |
| Cảm biến HC-SR04 | Đo khoảng cách đến vật cản |
| Cảm biến dò line TCRT5000 | Nhận biết vạch di chuyển |
| Encoder | Đếm xung chuyển động của bánh xe |
| Bluetooth HM-10 | Giao tiếp không dây với điện thoại |
| Nguồn điện | Cung cấp năng lượng cho hệ thống |

Các bài học sử dụng chung cấu hình chân của bộ robot. Việc học không được phân chia theo số lượng bánh xe mà tập trung vào nguyên lý và chức năng của từng thành phần.

### 3.3. Máy tính và Arduino Nano hoạt động như thế nào?

Máy tính được sử dụng để viết, biên dịch và nạp chương trình bằng Arduino IDE.

Arduino Nano tiếp nhận chương trình và thực thi các lệnh điều khiển trên robot.

Quá trình cơ bản:

```text
Máy tính
   |
   | Viết chương trình bằng Arduino IDE
   |
   v
Biên dịch chương trình
   |
   | Nạp qua USB
   |
   v
Arduino Nano
   |
   +----> Đọc cảm biến
   |
   +----> Xử lý dữ liệu
   |
   +----> Điều khiển động cơ
   |
   +----> Giao tiếp Bluetooth
```

Sau khi chương trình được nạp thành công, Arduino Nano có thể hoạt động độc lập khi được cấp nguồn phù hợp, không cần kết nối liên tục với máy tính.

Đối với bộ tài liệu này, bạn chỉ cần máy tính Windows, Arduino IDE và cáp USB để bắt đầu. Chưa cần cài đặt ROS 2 hoặc Ubuntu.

---

## 4. Lộ trình học lập trình Robot Arduino Nano

Chương trình được chia thành 10 bài học, từ kiến thức cơ bản đến các chức năng điều khiển robot.

### Giai đoạn 1: Làm quen với Arduino và lập trình cơ bản

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 1: Giới thiệu xe Arduino Nano](01-gioi-thieu.md) | Tìm hiểu cấu tạo và các thành phần của xe | Nhận biết Arduino, driver, động cơ, cảm biến và nguồn |
| [Bài 2: Lập trình Arduino từ đầu](bai-giang/02-lap-trinh.md) | Cấu trúc chương trình, biến, hàm và Serial | Viết, nạp chương trình và quan sát dữ liệu từ Nano |
| [Bài 3: Điều khiển LED](bai-giang/03-led.md) | Điều khiển tín hiệu Digital | Bật, tắt và thay đổi thời gian nhấp nháy LED |

Sau giai đoạn này, bạn sẽ hiểu cách viết một chương trình Arduino cơ bản, biên dịch và nạp chương trình vào bo mạch.

### Giai đoạn 2: Điều khiển cơ cấu chấp hành

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 4: Điều khiển Servo SG90](bai-giang/04-servo.md) | Nguyên lý và cách điều khiển góc servo | Đưa servo về vị trí giữa và thay đổi góc quay |
| [Bài 5: Điều khiển động cơ DC bằng L298N](bai-giang/05-dong-co.md) | Điều khiển chiều quay và tốc độ động cơ | Cho từng bên động cơ quay thuận, quay ngược và dừng |

Sau giai đoạn này, bạn sẽ biết cách tạo chuyển động cho các cơ cấu trên xe robot.

### Giai đoạn 3: Đọc và xử lý dữ liệu cảm biến

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 6: Cảm biến HC-SR04](bai-giang/06-hc-sr04.md) | Nguyên lý đo khoảng cách bằng sóng siêu âm | Đọc và hiển thị khoảng cách đến vật cản |
| [Bài 7: Cảm biến dò line TCRT5000](bai-giang/07-do-line.md) | Đọc tín hiệu từ cảm biến dò line 5 mắt | Phân biệt tín hiệu của từng mắt cảm biến trên nền và vạch |
| [Bài 8: Đọc tín hiệu Encoder](bai-giang/08-encoder.md) | Đọc xung bằng ngắt ngoài và xác định tốc độ | Đếm xung khi bánh xe quay và tính tốc độ quay |

Sau giai đoạn này, bạn sẽ biết cách thu thập dữ liệu từ cảm biến để phục vụ các thuật toán điều khiển.

### Giai đoạn 4: Giao tiếp và điều khiển nâng cao

| Bài học | Nội dung | Kết quả thực hành |
|---|---|---|
| [Bài 9: Bluetooth HM-10 và Dabble](bai-giang/09-bluetooth.md) | Giao tiếp Bluetooth và nhận lệnh GamePad | Nhấn nút trên điện thoại và kiểm tra lệnh Arduino nhận được |
| [Bài 10: Làm quen với PID](bai-giang/10-pid.md) | Nguyên lý phản hồi và điều chỉnh tốc độ động cơ | Hiểu cách sử dụng Encoder và PID để điều chỉnh tốc độ |

Hai bài cuối sử dụng kiến thức từ những bài trước, đặc biệt là điều khiển động cơ và đọc tín hiệu Encoder.

Bạn không cần học PID trước khi thử chương trình Bluetooth hoặc sử dụng những chương trình robot có sẵn.

---

## 5. Hướng dẫn chuẩn bị trước khi thực hành

### 5.1. Cài đặt phần mềm

Trước khi bắt đầu các bài thực hành, cần chuẩn bị môi trường lập trình trên máy tính.

Thực hiện theo thứ tự:

1. [Chuẩn bị Arduino Nano và kết nối phần cứng](02-chuan-bi.md).
2. [Cài đặt Arduino IDE và nạp chương trình thử nghiệm](05-cai-arduino-ide.md).
3. [Cài đặt các thư viện cần thiết](06-cai-thu-vien.md) khi bài học yêu cầu.

Sau khi hoàn thành, bạn cần nạp được chương trình vào Arduino Nano và kiểm tra được kết quả thực thi.

### 5.2. Chuẩn bị phần cứng

Trước mỗi bài học, cần kiểm tra:

- Arduino Nano được kết nối đúng.
- Các chân tín hiệu phù hợp với sơ đồ của bộ robot.
- Nguồn cấp phù hợp với thiết bị đang sử dụng.
- Dây nguồn và dây GND được kết nối đúng.
- Các bộ phận chuyển động được đặt ở trạng thái an toàn.

Khi thử động cơ, nên kê xe để bánh không tiếp xúc với mặt đất trong lần chạy đầu tiên.

**Lưu ý về chân D0 và D1:** Trong bộ xe, hai chân này được sử dụng cho tín hiệu điều khiển L298N, đồng thời là chân Serial phần cứng của Arduino Nano.

Khi thực hành với Serial Monitor hoặc nạp chương trình, cần thực hiện đúng hướng dẫn ngắt dây tại [bài chuẩn bị](02-chuan-bi.md). Chỉ ngắt nguồn motor có thể chưa đủ để loại bỏ xung đột tín hiệu.

---

## 6. Phương pháp học và thực hành

Để đạt hiệu quả, mỗi bài học nên được thực hiện theo quy trình sau.

### Bước 1: Tìm hiểu nguyên lý

Đọc phần giới thiệu và nguyên lý hoạt động của linh kiện.

Cần hiểu linh kiện có chức năng gì, Arduino giao tiếp với linh kiện như thế nào và dữ liệu được sử dụng để làm gì.

### Bước 2: Kiểm tra kết nối phần cứng

Đối chiếu sơ đồ chân của bài học với bộ robot.

Không tự ý thay đổi chân kết nối khi chưa hiểu chức năng của từng chân hoặc chưa cập nhật lại chương trình tương ứng.

### Bước 3: Chạy chương trình mẫu

Sử dụng chương trình được cung cấp trong bài học.

Thực hiện:

1. Mở Arduino IDE.
2. Chọn đúng Board và Port.
3. Sao chép chương trình mẫu.
4. Nhấn Verify.
5. Nhấn Upload nếu bài học yêu cầu nạp.
6. Quan sát kết quả.

### Bước 4: Kiểm tra kết quả thực hành

So sánh hoạt động thực tế với kết quả mong đợi.

Ví dụ:

- LED có nhấp nháy đúng thời gian không?
- Servo có quay đến vị trí yêu cầu không?
- Động cơ có quay đúng chiều không?
- Cảm biến có thay đổi dữ liệu khi môi trường thay đổi không?
- Encoder có tăng số xung khi bánh xe quay không?
- Arduino có nhận đúng lệnh từ điện thoại không?

Nếu kết quả không đúng, cần kiểm tra và xử lý trước khi chuyển sang bài tiếp theo.

### Bước 5: Thay đổi chương trình

Sau khi chương trình mẫu hoạt động đúng, hãy thử thay đổi một tham số.

Ví dụ:

- Thay đổi thời gian nhấp nháy LED.
- Thay đổi góc servo.
- Thay đổi giá trị PWM động cơ.
- Thay đổi khoảng cách phát hiện vật cản.
- Thay đổi tốc độ mục tiêu của động cơ.

Việc chỉ thay đổi một tham số tại một thời điểm giúp dễ quan sát ảnh hưởng của tham số đó đến hoạt động của hệ thống.

---

## 7. Sử dụng chương trình có sẵn của xe robot

Ngoài các bài học cơ bản, bộ robot còn có những chương trình được bàn giao để thực hiện các chức năng hoàn chỉnh.

Tùy phiên bản chương trình, các chức năng có thể bao gồm:

- Điều khiển xe bằng điện thoại qua Bluetooth.
- Di chuyển theo vạch.
- Phát hiện và tránh vật cản.
- Đọc dữ liệu Encoder.
- Điều khiển servo và động cơ.

Bạn có thể sử dụng các chương trình này sau khi hoàn thành bước chuẩn bị Arduino IDE và kiểm tra kết nối.

Xem [hướng dẫn sử dụng chương trình robot](08-su-dung-robot.md).

### 7.1. Lưu ý khi nạp chương trình

Arduino Nano thực thi chương trình đã được nạp vào bộ nhớ.

Khi nạp một chương trình mới, chương trình trước đó trên Nano sẽ được thay thế.

Ví dụ:

- Nạp chương trình Blink: Nano thực hiện chức năng nhấp nháy LED.
- Nạp chương trình đọc cảm biến: Nano thực hiện chương trình đọc cảm biến.
- Nạp lại chương trình điều khiển xe: Nano thực hiện chức năng tương ứng của chương trình đó.

Vì vậy, cần lưu giữ chương trình bàn giao trước khi thực hành.

### 7.2. Quản lý chương trình học

Nên tạo một thư mục riêng cho các bài thực hành, ví dụ:

```text
HocRobotArduinoNano/
|
|-- Bai02_LapTrinh/
|-- Bai03_LED/
|-- Bai04_Servo/
|-- Bai05_DongCo/
|-- Bai06_HCSR04/
|-- Bai07_DoLine/
|-- Bai08_Encoder/
|-- Bai09_Bluetooth/
|-- Bai10_PID/
```

Đồng thời, lưu riêng bộ chương trình gốc của xe robot để có thể nạp lại khi cần.

---

## 8. Bạn nên bắt đầu từ đâu?

Tùy theo kinh nghiệm và mục đích sử dụng, bạn có thể lựa chọn nội dung phù hợp.

| Nhu cầu | Nội dung nên bắt đầu |
|---|---|
| Chưa từng sử dụng robot Arduino | [Bài 1: Giới thiệu xe](01-gioi-thieu.md) |
| Chưa biết kết nối và cấp nguồn | [Chuẩn bị thiết bị](02-chuan-bi.md) |
| Chưa cài đặt Arduino IDE | [Cài Arduino IDE và nạp thử](05-cai-arduino-ide.md) |
| Muốn học lập trình từ đầu | [Bài 2: Lập trình Arduino](bai-giang/02-lap-trinh.md) |
| Muốn điều khiển động cơ | [Bài 5: Động cơ DC và L298N](bai-giang/05-dong-co.md) |
| Muốn đọc cảm biến | [Bài 6: HC-SR04](bai-giang/06-hc-sr04.md) |
| Muốn điều khiển xe bằng điện thoại | [Bài 9: Bluetooth HM-10](bai-giang/09-bluetooth.md) |
| Muốn sử dụng chương trình xe có sẵn | [Hướng dẫn sử dụng robot](08-su-dung-robot.md) |
| Gặp lỗi khi kết nối hoặc nạp chương trình | [Hướng dẫn xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) |

Đối với người mới bắt đầu, nên học theo thứ tự từ Bài 1 đến Bài 10 để có kiến thức nền tảng trước khi xây dựng các chức năng phức tạp hơn.

---

## 9. Tài liệu và hướng dẫn bổ sung

Trong quá trình học, bạn có thể tham khảo thêm các hướng dẫn sau:

- [Chuẩn bị thiết bị và kết nối phần cứng](02-chuan-bi.md).
- [Hướng dẫn lắp ráp robot](03-lap-rap.md).
- [Thực hành nút nhấn và sử dụng millis](04-lap-trinh.md).
- [Cài đặt Arduino IDE](05-cai-arduino-ide.md).
- [Cài đặt thư viện Servo và Dabble](06-cai-thu-vien.md).
- [Kiểm tra và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md).
- [Sơ đồ chân và sử dụng chương trình robot](08-su-dung-robot.md).
- [Thư mục bàn giao Robovis](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-).

---

## 10. Tổng kết

Bộ tài liệu **Học và sử dụng Robot Arduino Nano** cung cấp lộ trình học từ những kiến thức lập trình cơ bản đến các chức năng điều khiển robot.

Trong quá trình học, bạn sẽ từng bước:

1. Hiểu cấu tạo và nguyên lý hoạt động của xe robot.
2. Làm quen với Arduino IDE và ngôn ngữ lập trình Arduino.
3. Điều khiển các thiết bị như LED, servo và động cơ DC.
4. Đọc và xử lý tín hiệu từ cảm biến.
5. Sử dụng Bluetooth để nhận lệnh điều khiển.
6. Làm quen với điều khiển tốc độ động cơ bằng PID.
7. Kết hợp các thành phần để xây dựng những chức năng robot hoàn chỉnh.

Điều quan trọng là **hiểu nguyên lý, chạy đúng từng ví dụ và kiểm tra kết quả trước khi kết hợp các chức năng**.

Sau khi hoàn thành chương trình, bạn sẽ có nền tảng để tiếp tục nghiên cứu, phát triển và mở rộng các ứng dụng robot sử dụng Arduino.

---

[Bắt đầu Bài 1: Giới thiệu xe Arduino Nano](01-gioi-thieu.md)

[Tải tài liệu học Robot Arduino Nano](../tai-xuong/robot-arduino.md)