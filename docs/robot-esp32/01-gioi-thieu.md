# Bài 1: Giới thiệu xe Robot ESP32 30P CH340 Type-C

## 1. Giới thiệu

Trong các hệ thống robot, vi điều khiển đóng vai trò trung tâm, thực hiện việc thu thập dữ liệu từ cảm biến, xử lý thông tin và điều khiển các thiết bị như động cơ, servo hoặc module giao tiếp.

Ở bộ xe robot này, chúng ta sử dụng **ESP32 DevKit 30 chân (30P), cổng USB Type-C và chip giao tiếp CH340**.

ESP32 là dòng vi điều khiển có khả năng xử lý mạnh, tích hợp kết nối không dây và hỗ trợ nhiều giao tiếp ngoại vi. Nhờ đó, ESP32 được sử dụng rộng rãi trong các ứng dụng IoT, điều khiển thiết bị thông minh và robot.

Khác với Arduino Nano ATmega328P, ESP32 có thể kết nối Wi-Fi trực tiếp mà không cần bổ sung module Wi-Fi bên ngoài.

Trong bộ robot Robovis, ESP32 được sử dụng để:

- Điều khiển chuyển động của xe thông qua driver L298N.
- Đọc tín hiệu cảm biến dò line.
- Đọc xung Encoder từ bánh xe.
- Đo khoảng cách bằng cảm biến HC-SR04.
- Kết nối Wi-Fi để nhận lệnh điều khiển từ điện thoại hoặc máy tính.
- Thực hiện các thuật toán điều khiển và xử lý dữ liệu cảm biến.

Tài liệu và chương trình của sản phẩm được cung cấp tại [bộ tài liệu Robot ESP32 Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt).

## 2. Mục tiêu bài học

Sau khi hoàn thành bài học, bạn có thể:

- Hiểu ESP32 là gì và vai trò của ESP32 trong hệ thống robot.
- Nhận biết bo mạch ESP32 30P CH340 Type-C.
- Phân biệt vi điều khiển ESP32, module ESP32-WROOM-32, chip CH340 và cổng USB Type-C.
- Nhận diện các thành phần phần cứng của xe robot.
- Hiểu nguyên lý kết nối và điều khiển động cơ thông qua L298N.
- Hiểu cách ESP32 đọc dữ liệu từ các cảm biến.
- Nắm được nguyên lý giao tiếp Wi-Fi để điều khiển xe.
- Phân biệt những đặc điểm cơ bản giữa ESP32 và Arduino Nano.
- Nhận biết các lưu ý quan trọng về nguồn điện và mức logic GPIO.

---

## 3. Tìm hiểu về vi điều khiển ESP32

### 3.1. ESP32 là gì?

ESP32 là họ vi điều khiển do Espressif Systems phát triển, được thiết kế cho các ứng dụng nhúng, điều khiển và kết nối không dây.

Đối với dòng ESP32 classic được sử dụng trong bộ xe, vi điều khiển có những đặc điểm nổi bật:

- Bộ xử lý 32-bit.
- Hỗ trợ kết nối Wi-Fi.
- Hỗ trợ Bluetooth.
- Có nhiều chân GPIO để kết nối thiết bị ngoại vi.
- Hỗ trợ tín hiệu PWM để điều khiển động cơ.
- Có các bộ chuyển đổi tín hiệu Analog sang Digital (ADC).
- Hỗ trợ các giao tiếp như UART, I2C và SPI.
- Hỗ trợ ngắt để xử lý tín hiệu từ Encoder và cảm biến.

ESP32 có thể được lập trình bằng nhiều môi trường phát triển khác nhau. Trong bộ tài liệu này, chúng ta sử dụng **Arduino IDE** để viết và nạp chương trình.

### 3.2. Vai trò của ESP32 trong xe robot

ESP32 đóng vai trò bộ điều khiển trung tâm, thực hiện ba nhóm nhiệm vụ chính.

**Thu thập dữ liệu**

ESP32 nhận tín hiệu từ các cảm biến:

- HC-SR04 cung cấp thông tin khoảng cách.
- TCRT5000 cung cấp trạng thái của các mắt dò line.
- Encoder cung cấp xung theo chuyển động của bánh xe.

**Xử lý dữ liệu**

Chương trình trên ESP32 xử lý các tín hiệu nhận được để xác định trạng thái và đưa ra quyết định điều khiển.

Ví dụ:

- Phát hiện vật cản ở phía trước.
- Xác định vạch nằm bên trái hay bên phải xe.
- Tính tốc độ quay của bánh xe.
- Xác định lệnh tiến, lùi hoặc rẽ từ người điều khiển.

**Điều khiển thiết bị**

Sau khi xử lý dữ liệu, ESP32 tạo tín hiệu điều khiển gửi đến các thiết bị ngoại vi.

Ví dụ:

- Gửi tín hiệu PWM đến L298N để điều chỉnh tốc độ động cơ.
- Thay đổi trạng thái các chân điều khiển để đảo chiều động cơ.
- Gửi tín hiệu điều khiển servo.
- Trả dữ liệu trạng thái về giao diện điều khiển qua Wi-Fi.

### 3.3. Nguyên lý hoạt động tổng quát

```text
      Cảm biến HC-SR04
              |
      Cảm biến dò line
              |
           Encoder
              |
              v
        +-----------+
        |   ESP32   |
        +-----------+
              |
       Xử lý chương trình
              |
      +-------+--------+
      |                |
      v                v
    L298N            Wi-Fi
      |                |
      v                v
  Động cơ DC      Điện thoại /
                  Trình duyệt
```

Trong quá trình hoạt động, ESP32 liên tục thực hiện chương trình đã được nạp, đọc dữ liệu đầu vào và cập nhật tín hiệu điều khiển đầu ra.

---

## 4. Tìm hiểu bo mạch ESP32 30P CH340 Type-C

### 4.1. Cấu tạo bo mạch

Bo mạch ESP32 30P CH340 Type-C là một bo phát triển giúp người dùng dễ dàng cấp nguồn, lập trình và kết nối ESP32 với các thiết bị ngoại vi.

<AsyncImageGroup query={["ESP32 DevKit 30 pin USB Type C CH340 development board top view","ESP32 WROOM 32 30 pin CH340 type C development board pinout"]} aspectRatio="5:4" layout="carousel"/>

Các thành phần chính bao gồm:

| Thành phần | Chức năng |
|---|---|
| Module ESP32-WROOM-32 | Chứa vi điều khiển ESP32 và các thành phần liên quan |
| Chip CH340 | Chuyển đổi giao tiếp USB sang UART |
| Cổng USB Type-C | Kết nối với máy tính và cấp nguồn USB |
| Chân GPIO | Kết nối cảm biến, driver và các thiết bị ngoại vi |
| Chân 3V3 | Đường nguồn 3,3 V của bo |
| Chân GND | Điểm tham chiếu điện áp chung |
| Nút EN/RESET | Khởi động lại ESP32 |
| Nút BOOT | Hỗ trợ đưa ESP32 vào chế độ nạp khi cần |
| Mạch ổn áp | Tạo nguồn hoạt động phù hợp cho ESP32 |

Vị trí và cách ghi nhãn các thành phần có thể khác nhau giữa những phiên bản bo ESP32 30 chân.

### 4.2. Phân biệt ESP32 và ESP32-WROOM-32

Hai tên gọi này thường xuất hiện cùng nhau nhưng không hoàn toàn giống nhau.

**ESP32** là tên dòng vi điều khiển.

**ESP32-WROOM-32** là tên một module tích hợp chip ESP32 cùng những thành phần cần thiết để sử dụng trong thiết kế phần cứng, chẳng hạn bộ nhớ Flash và mạch RF.

Module ESP32-WROOM-32 thường được nhận biết bằng phần vỏ kim loại trên bo mạch.

Bo phát triển ESP32 là bảng mạch lớn hơn, trên đó gắn module ESP32-WROOM-32, chip USB–UART, mạch nguồn, các nút điều khiển và hàng chân kết nối.

### 4.3. Chip CH340 có chức năng gì?

CH340 là chip chuyển đổi giao tiếp USB sang UART.

Máy tính sử dụng giao tiếp USB, trong khi ESP32 có thể sử dụng UART để nhận dữ liệu và thực hiện quá trình nạp chương trình.

CH340 đóng vai trò trung gian giữa hai giao tiếp này.

Quá trình nạp chương trình có thể mô tả:

```text
Arduino IDE
    |
    | USB
    v
Cổng USB Type-C
    |
    v
Chip CH340
    |
    | UART
    v
ESP32
    |
    v
Bộ nhớ Flash
    |
    v
Thực thi chương trình
```

Khi kết nối ESP32 với máy tính, Windows có thể nhận diện chip CH340 dưới dạng một cổng COM.

Ví dụ:

```text
USB-SERIAL CH340 (COM5)
```

Số cổng COM có thể khác nhau trên từng máy tính.

**Lưu ý:** CH340 không phải là vi điều khiển thực thi chương trình robot. Chương trình được xử lý bởi ESP32.

### 4.4. Cổng USB Type-C có chức năng gì?

Cổng USB Type-C trên bo được sử dụng để:

- Cấp nguồn cho bo mạch trong quá trình lập trình.
- Kết nối bo mạch với máy tính.
- Truyền chương trình từ Arduino IDE đến ESP32 thông qua chip USB–UART.
- Trao đổi dữ liệu Serial phục vụ kiểm tra và gỡ lỗi.

USB Type-C chỉ mô tả kiểu đầu nối USB, không quyết định loại vi điều khiển.

Hai bo mạch cùng sử dụng USB Type-C có thể dùng những chip hoàn toàn khác nhau.

Khi kết nối máy tính, cần sử dụng cáp USB Type-C **có hỗ trợ truyền dữ liệu**, không chỉ có chức năng sạc.

---

## 5. Tìm hiểu các chân GPIO của ESP32

### 5.1. GPIO là gì?

GPIO là viết tắt của *General Purpose Input/Output*, nghĩa là chân vào/ra đa mục đích.

Các chân GPIO cho phép ESP32 giao tiếp với thiết bị ngoại vi thông qua tín hiệu điện.

Một chân GPIO có thể được cấu hình làm đầu vào hoặc đầu ra tùy theo khả năng của chân đó.

Ví dụ:

- Đọc trạng thái cảm biến dò line.
- Nhận tín hiệu xung Encoder.
- Tạo tín hiệu Trigger cho HC-SR04.
- Điều khiển chiều quay động cơ.
- Tạo PWM để điều chỉnh tốc độ động cơ.

### 5.2. Tín hiệu Digital

Tín hiệu Digital có hai trạng thái logic cơ bản:

- `HIGH`: Mức logic cao.
- `LOW`: Mức logic thấp.

Đối với ESP32, mức logic GPIO danh định là 3,3 V.

Ví dụ:

```cpp
digitalWrite(23, HIGH);
```

Lệnh này yêu cầu GPIO23 xuất mức logic cao khi chân đã được cấu hình làm đầu ra.

Tương tự:

```cpp
digitalWrite(23, LOW);
```

Lệnh này yêu cầu GPIO23 xuất mức logic thấp.

Các lệnh trên chỉ minh họa cú pháp. Trong robot, cần sử dụng đúng GPIO được quy định trong sơ đồ chân sản phẩm.

### 5.3. Tín hiệu PWM

PWM (*Pulse Width Modulation*) là phương pháp điều khiển công suất trung bình bằng cách thay đổi tỷ lệ thời gian tín hiệu ở mức cao trong một chu kỳ.

Trong xe robot, PWM được sử dụng để điều chỉnh tốc độ động cơ thông qua driver L298N.

Ví dụ:

- Duty cycle thấp: động cơ thường nhận mức điều khiển nhỏ hơn.
- Duty cycle cao: động cơ thường nhận mức điều khiển lớn hơn.

Tốc độ thực tế còn phụ thuộc vào nguồn điện, tải, đặc tính động cơ và tổn hao trên driver.

### 5.4. Một số lưu ý về GPIO

Không phải mọi chân GPIO của ESP32 đều có chức năng giống nhau.

Đối với ESP32 classic:

- GPIO34–GPIO39 chỉ hỗ trợ đầu vào.
- Một số chân ảnh hưởng đến chế độ khởi động của ESP32.
- Một số chân được sử dụng cho giao tiếp UART.
- Những chân kết nối với bộ nhớ Flash trên module không được sử dụng tùy tiện.
- Các chân GPIO hoạt động với mức logic 3,3 V.

**Đặc biệt quan trọng:** GPIO ESP32 không được xem là chân chịu được tín hiệu 5 V. Cần sử dụng mạch chuyển mức hoặc chia áp phù hợp khi kết nối với thiết bị xuất tín hiệu 5 V.

Ví dụ, chân Echo của nhiều module HC-SR04 thông dụng có thể xuất xung mức 5 V. Không nên nối trực tiếp tín hiệu này vào GPIO ESP32 nếu chưa có giải pháp hạ mức điện áp.

---

## 6. Giới thiệu các thành phần của xe robot

### 6.1. Driver điều khiển động cơ L298N

L298N là mạch driver được sử dụng để điều khiển động cơ DC.

ESP32 không thể cấp trực tiếp dòng điện lớn để vận hành động cơ. Vì vậy, cần sử dụng driver làm tầng công suất trung gian.

<AsyncImage query="L298N dual H bridge motor driver module red board heatsink" aspectRatio="5:3"/>

Driver L298N cho phép:

- Điều khiển hai kênh động cơ DC.
- Thay đổi chiều quay.
- Điều chỉnh mức điều khiển bằng PWM.
- Dừng động cơ.

Trong bộ xe, ESP32 gửi các tín hiệu điều khiển đến L298N. Driver sử dụng nguồn động cơ để cấp công suất cho các động cơ.

Nguyên lý:

```text
ESP32
  |
  | Tín hiệu điều khiển
  v
L298N
  |
  | Công suất động cơ
  v
Động cơ DC
  |
  v
Bánh xe chuyển động
```

L298N sẽ được tìm hiểu chi tiết trong [Bài 5: Điều khiển động cơ DC](bai-giang/05-dong-co.md).

### 6.2. Cảm biến khoảng cách HC-SR04

HC-SR04 là cảm biến sử dụng sóng siêu âm để đo khoảng cách đến vật thể.

<AsyncImage query="HC-SR04 ultrasonic distance sensor module front view" aspectRatio="5:3"/>

Cảm biến có bốn chân thông dụng:

| Chân | Chức năng |
|---|---|
| VCC | Cấp nguồn |
| TRIG | Nhận xung kích hoạt phép đo |
| ECHO | Xuất xung phản hồi |
| GND | Mass |

Nguyên lý hoạt động:

1. ESP32 gửi xung kích hoạt đến chân TRIG.
2. Cảm biến phát sóng siêu âm.
3. Sóng gặp vật cản và phản xạ trở lại.
4. Cảm biến tạo xung tại chân ECHO.
5. ESP32 đo thời gian xung để tính khoảng cách.

Cảm biến thường được sử dụng trong chức năng phát hiện và tránh vật cản.

Xem [Bài 6: Cảm biến HC-SR04](bai-giang/06-hc-sr04.md).

### 6.3. Cảm biến dò line TCRT5000

Bộ robot sử dụng cảm biến dò line gồm năm kênh.

<AsyncImage query="five channel TCRT5000 infrared line tracking sensor array module" aspectRatio="5:3"/>

Cảm biến sử dụng nguyên lý phản xạ ánh sáng hồng ngoại để phân biệt các bề mặt có đặc tính phản xạ khác nhau.

Mỗi mắt cảm biến tạo ra một tín hiệu để ESP32 đọc và xử lý.

Từ trạng thái của năm mắt cảm biến, chương trình có thể xác định tương đối vị trí của vạch so với robot.

Ví dụ:

- Vạch nằm gần giữa robot.
- Vạch lệch sang trái.
- Vạch lệch sang phải.
- Không phát hiện được vạch.

Dựa trên dữ liệu này, ESP32 có thể điều chỉnh tốc độ hai bên động cơ để robot bám theo đường.

Xem [Bài 7: Cảm biến dò line TCRT5000](bai-giang/07-do-line.md).

### 6.4. Cảm biến Encoder

Encoder được sử dụng để tạo tín hiệu xung tương ứng với chuyển động quay của bánh xe hoặc trục động cơ.

<AsyncImage query="DC geared motor wheel encoder disk sensor robotics encoder module" aspectRatio="5:3"/>

ESP32 có thể đếm số xung Encoder trong một khoảng thời gian để tính tốc độ quay.

Ví dụ, nếu biết số xung tương ứng với một vòng quay, chương trình có thể tính:

- Số vòng quay của bánh xe.
- Tốc độ quay theo RPM.
- Vận tốc tuyến tính của bánh xe.
- Quãng đường ước tính từ chuyển động quay.

Dữ liệu Encoder đặc biệt quan trọng trong các hệ thống điều khiển tốc độ có phản hồi.

Xem [Bài 8: Đọc tín hiệu Encoder](bai-giang/08-encoder.md).

### 6.5. Nguồn điện của robot

Robot cần nguồn điện để cung cấp năng lượng cho các thành phần điện tử và động cơ.

Các nhóm tải có yêu cầu nguồn khác nhau:

- ESP32 cần nguồn phù hợp với mạch nguồn trên bo.
- Động cơ DC sử dụng nguồn động cơ thông qua L298N.
- Cảm biến cần được cấp điện áp đúng thông số.
- Servo cần nguồn có khả năng cung cấp dòng điện phù hợp khi chuyển động.

Cần phân biệt **điện áp cấp nguồn** và **mức điện áp tín hiệu GPIO**.

Ví dụ, bo ESP32 có thể nhận nguồn 5 V từ cổng USB, nhưng chân GPIO vẫn hoạt động với mức logic 3,3 V.

Khi sử dụng nhiều nguồn, cần xác định cách nối GND chung phù hợp để các tín hiệu điều khiển có cùng mức tham chiếu.

---

## 7. So sánh ESP32 và Arduino Nano

Arduino Nano và ESP32 đều có thể được sử dụng để xây dựng robot, nhưng có những khác biệt về phần cứng và khả năng xử lý.

| Đặc điểm | Arduino Nano classic | ESP32 classic |
|---|---|---|
| Vi điều khiển | ATmega328P | ESP32 |
| Kiến trúc | 8-bit | 32-bit |
| Mức logic GPIO | 5 V | 3,3 V |
| Wi-Fi tích hợp | Không | Có |
| Bluetooth tích hợp | Không | Có |
| PWM | Có | Có |
| ADC | Có | Có |
| Ngắt ngoài | Có | Có |
| Gói hỗ trợ Arduino IDE | Arduino AVR Boards | esp32 by Espressif Systems |
| Lựa chọn bo trong tài liệu | Arduino Nano | ESP32 Dev Module |

### 7.1. Ưu điểm của ESP32

ESP32 phù hợp với những ứng dụng cần:

- Xử lý dữ liệu từ nhiều cảm biến.
- Điều khiển nhiều chức năng đồng thời.
- Giao tiếp Wi-Fi.
- Xây dựng giao diện điều khiển qua mạng.
- Thực hiện thuật toán điều khiển có phản hồi.

### 7.2. Những điểm cần chú ý khi chuyển từ Nano sang ESP32

Nếu đã học Arduino Nano, bạn có thể tiếp tục sử dụng nhiều kiến thức lập trình tương tự trên ESP32.

Ví dụ:

```cpp
pinMode(23, OUTPUT);
digitalWrite(23, HIGH);
```

Tuy nhiên, cần chú ý:

- Không giữ nguyên sơ đồ chân của Nano khi chuyển sang ESP32.
- Không đưa tín hiệu 5 V trực tiếp vào GPIO ESP32.
- Phải chọn đúng gói hỗ trợ và loại bo mạch trong Arduino IDE.
- Cách sử dụng PWM và một số thư viện có thể khác nhau.
- Cần kiểm tra các chân ảnh hưởng đến quá trình khởi động.

---

## 8. Kết nối và điều khiển robot qua Wi-Fi

### 8.1. Wi-Fi trên ESP32

Một trong những ưu điểm của ESP32 là khả năng kết nối Wi-Fi tích hợp.

ESP32 có thể hoạt động theo các chế độ kết nối khác nhau, trong đó có:

**Station (STA)**

ESP32 kết nối đến một mạng Wi-Fi có sẵn, chẳng hạn mạng từ router.

**Access Point (AP)**

ESP32 tạo một mạng Wi-Fi để điện thoại hoặc máy tính kết nối trực tiếp.

Trong bộ chương trình robot được bàn giao, ESP32 tạo mạng Wi-Fi có tên:

**ESP32-Car**

Điện thoại hoặc máy tính có thể kết nối đến mạng này để sử dụng giao diện điều khiển robot.

### 8.2. Nguyên lý điều khiển qua Wi-Fi

```text
Điện thoại / Máy tính
          |
          | Kết nối Wi-Fi
          v
      ESP32-Car
          |
          v
      Web Server
       trên ESP32
          |
          v
   Xử lý lệnh điều khiển
          |
          v
        L298N
          |
          v
       Động cơ
```

Quá trình điều khiển có thể được mô tả:

1. ESP32 khởi tạo mạng Wi-Fi.
2. Điện thoại kết nối đến mạng ESP32-Car.
3. Người dùng mở giao diện điều khiển trên trình duyệt.
4. Người dùng lựa chọn chế độ hoặc gửi lệnh.
5. ESP32 nhận và xử lý lệnh.
6. ESP32 điều khiển động cơ theo chương trình.

### 8.3. Các chế độ điều khiển

Chương trình robot được bàn giao có giao diện web với hai chế độ chính.

**Manual**

Chế độ điều khiển thủ công.

Người dùng gửi lệnh điều khiển từ giao diện web, chẳng hạn:

- Tiến.
- Lùi.
- Rẽ trái.
- Rẽ phải.
- Dừng.

ESP32 nhận lệnh và điều khiển L298N để tạo chuyển động tương ứng.

**Line follow**

Chế độ dò line.

ESP32 đọc dữ liệu từ cảm biến dò line và tự động điều chỉnh chuyển động của xe theo thuật toán đã lập trình.

Ở chế độ này, dữ liệu cảm biến được sử dụng trực tiếp để xác định hướng di chuyển.

Để tìm hiểu chi tiết cách kết nối và điều khiển xe, xem [Bài 9: Điều khiển robot qua Wi-Fi](bai-giang/09-wifi.md).

---

## 9. Lập trình ESP32 bằng Arduino IDE

### 9.1. Arduino IDE có lập trình được ESP32 không?

Có.

Arduino IDE có thể lập trình ESP32 sau khi cài đặt gói hỗ trợ bo mạch tương ứng.

Gói hỗ trợ được sử dụng là:

**esp32 by Espressif Systems**

Gói này cung cấp các thành phần cần thiết để biên dịch và nạp chương trình cho những bo ESP32 được hỗ trợ.

### 9.2. Lựa chọn bo mạch

Đối với bộ xe trong tài liệu bàn giao, cấu hình lựa chọn là:

**Tools → Board → esp32 → ESP32 Dev Module**

Tuy nhiên, cần kiểm tra đúng loại vi điều khiển trên bo.

Nếu sử dụng ESP32-S3, ESP32-C3 hoặc một dòng ESP32 khác, cần lựa chọn bo mạch và sơ đồ chân tương ứng.

### 9.3. Quy trình nạp chương trình

Quy trình lập trình cơ bản:

1. Kết nối ESP32 với máy tính bằng USB Type-C.
2. Mở Arduino IDE.
3. Chọn đúng bo mạch.
4. Chọn cổng COM tương ứng.
5. Mở chương trình cần nạp.
6. Nhấn Verify để biên dịch.
7. Nhấn Upload để nạp chương trình.
8. Quan sát kết quả hoạt động.

Nếu bo không tự động vào chế độ nạp, có thể cần thao tác với nút BOOT theo hướng dẫn của bo mạch.

Chi tiết được trình bày trong [hướng dẫn cài đặt Arduino IDE](03-cai-arduino-ide.md) và [hướng dẫn nạp chương trình](04-nap-code-va-serial.md).

---

## 10. Thực hành nhận diện phần cứng

### 10.1. Mục tiêu thực hành

Sau phần thực hành này, bạn cần nhận diện được các thành phần chính của robot và hiểu chức năng cơ bản của từng thành phần.

### 10.2. Thực hành 1: Nhận diện bo ESP32

Quan sát bo mạch và xác định:

1. Module ESP32-WROOM-32.
2. Chip CH340.
3. Cổng USB Type-C.
4. Nút EN/RESET.
5. Nút BOOT.
6. Các chân GPIO.
7. Chân 3V3.
8. Chân GND.

**Kết quả mong đợi:** Phân biệt được vi điều khiển ESP32, chip CH340 và cổng USB Type-C.

### 10.3. Thực hành 2: Nhận diện các linh kiện trên robot

Quan sát robot và xác định:

1. Driver L298N.
2. Các động cơ DC.
3. Cảm biến HC-SR04.
4. Cảm biến dò line năm kênh.
5. Encoder.
6. Bộ nguồn và dây cấp nguồn.

Với mỗi linh kiện, hãy giải thích chức năng của nó trong quá trình robot hoạt động.

### 10.4. Thực hành 3: Phân loại tín hiệu

Hãy xác định loại tín hiệu thường được sử dụng cho từng chức năng.

| Chức năng | Loại tín hiệu |
|---|---|
| Điều khiển chiều quay động cơ | Digital |
| Điều chỉnh tốc độ động cơ | PWM |
| Đọc cảm biến dò line Digital | Digital Input |
| Đọc xung Encoder | Digital Input / Interrupt |
| Kích hoạt HC-SR04 | Digital Output |
| Đo thời gian Echo | Digital Input |
| Nhận lệnh từ điện thoại | Wi-Fi |

### 10.5. Thực hành 4: Giải thích quá trình điều khiển robot

Hãy mô tả quá trình hoạt động khi người dùng nhấn nút tiến trên giao diện web.

Gợi ý:

```text
Người dùng nhấn Tiến
          |
          v
Giao diện web gửi lệnh
          |
          v
ESP32 nhận lệnh qua Wi-Fi
          |
          v
Chương trình xử lý lệnh
          |
          v
ESP32 gửi tín hiệu đến L298N
          |
          v
Động cơ quay
          |
          v
Robot di chuyển
```

---

## 11. Một số lưu ý khi sử dụng ESP32

### 11.1. Không nhầm mức nguồn và mức logic

ESP32 có thể được cấp nguồn thông qua USB 5 V, nhưng GPIO hoạt động ở mức logic 3,3 V.

Không được kết luận rằng chân GPIO chịu được 5 V chỉ vì bo có chân nguồn 5 V.

### 11.2. Không sử dụng tùy ý các chân GPIO

Một số GPIO có chức năng đặc biệt hoặc ảnh hưởng đến quá trình khởi động.

Cần sử dụng đúng cấu hình chân trong tài liệu sản phẩm.

### 11.3. Không nhầm chip CH340 với ESP32

CH340 chỉ đảm nhiệm việc chuyển đổi USB–UART.

ESP32 mới là thành phần thực thi chương trình và điều khiển robot.

### 11.4. Không nhầm cổng Type-C với loại bo mạch

USB Type-C là kiểu đầu nối.

Khi lựa chọn Board trong Arduino IDE, cần dựa vào vi điều khiển và cấu hình phần cứng thực tế.

### 11.5. Đảm bảo an toàn khi thử động cơ

Khi chạy thử chương trình điều khiển động cơ:

- Kê xe để bánh không tiếp xúc với mặt đất.
- Kiểm tra nguồn cấp.
- Bắt đầu với tốc độ thấp.
- Kiểm tra chiều quay.
- Ngắt nguồn trước khi thay đổi dây kết nối.

---

## 12. Bài tập ôn tập

**Bài tập 1: Kiến thức ESP32**

Trả lời các câu hỏi:

1. ESP32 có vai trò gì trong hệ thống robot?
2. ESP32-WROOM-32 là gì?
3. Chip CH340 có chức năng gì?
4. USB Type-C có quyết định loại vi điều khiển không?
5. Vì sao ESP32 có thể điều khiển robot qua Wi-Fi mà không cần module Wi-Fi ngoài?

**Bài tập 2: Tìm hiểu phần cứng**

Hãy giải thích chức năng của:

1. Driver L298N.
2. Cảm biến HC-SR04.
3. Cảm biến dò line TCRT5000.
4. Encoder.
5. Bộ nguồn của robot.

**Bài tập 3: So sánh Arduino Nano và ESP32**

Hãy nêu ít nhất ba điểm khác biệt giữa Arduino Nano ATmega328P và ESP32 classic.

Giải thích vì sao không thể chuyển toàn bộ dây tín hiệu từ một robot Arduino Nano sang ESP32 mà không kiểm tra lại mức điện áp và sơ đồ chân.

**Bài tập 4: Điều khiển Wi-Fi**

Trả lời:

1. Chế độ Access Point là gì?
2. ESP32-Car có vai trò gì trong chương trình robot?
3. Chế độ Manual và Line follow khác nhau như thế nào?
4. Khi xe chạy theo line, dữ liệu cảm biến được sử dụng để làm gì?

---

## 13. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu:

- Khái niệm và vai trò của ESP32 trong hệ thống robot.
- Cấu tạo bo mạch ESP32 30P CH340 Type-C.
- Sự khác biệt giữa ESP32, ESP32-WROOM-32, CH340 và USB Type-C.
- Chức năng của GPIO, Digital, PWM và các giao tiếp ngoại vi.
- Vai trò của L298N, HC-SR04, TCRT5000 và Encoder.
- Những khác biệt cơ bản giữa Arduino Nano và ESP32.
- Nguyên lý kết nối và điều khiển robot qua Wi-Fi.
- Cách ESP32 nhận lệnh từ giao diện web.
- Các lưu ý về nguồn điện, mức logic và an toàn phần cứng.

Sau khi hoàn thành bài học, bạn cần đạt được ba kết quả:

1. **Nhận diện đúng các thành phần chính của xe robot ESP32.**
2. **Hiểu cách ESP32 đọc cảm biến và điều khiển động cơ.**
3. **Giải thích được quá trình nạp chương trình và điều khiển xe qua Wi-Fi.**

Đây là nền tảng để tiếp tục tìm hiểu cách viết chương trình, sử dụng GPIO và xây dựng các chức năng điều khiển robot trong những bài tiếp theo.

---

[Lộ trình học](index.md) · [Bài tiếp: Hướng dẫn lập trình ESP32](bai-giang/02-lap-trinh.md) · [Hướng dẫn sử dụng robot](08-su-dung-robot.md)