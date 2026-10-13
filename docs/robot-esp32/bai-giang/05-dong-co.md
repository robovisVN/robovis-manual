# Bài 5: Điều khiển động cơ DC bằng L298N và ESP32

## 1. Giới thiệu

Trong các bài học trước, chúng ta đã tìm hiểu cách lập trình ESP32, điều khiển LED và động cơ servo.

Ở bài học này, chúng ta sẽ tìm hiểu cách sử dụng **ESP32 kết hợp với module L298N để điều khiển hai động cơ DC của xe robot**.

Động cơ DC là bộ phận tạo chuyển động cho robot. Tuy nhiên, các chân GPIO của ESP32 chỉ cung cấp tín hiệu điều khiển với mức logic 3,3 V và không thể cấp trực tiếp dòng điện lớn cho động cơ.

Vì vậy, chúng ta cần sử dụng một mạch điều khiển công suất, gọi là **driver động cơ**.

Trong bộ xe robot ESP32, module L298N được sử dụng để điều khiển chiều quay và tốc độ của hai động cơ DC.

Trong bài học này, chúng ta sẽ thực hiện:

- Tìm hiểu nguyên lý hoạt động của động cơ DC.
- Tìm hiểu chức năng của module L298N.
- Làm quen với nguyên lý cầu H.
- Tìm hiểu các chân điều khiển IN1, IN2, IN3, IN4, ENA và ENB.
- Kết nối L298N với ESP32 thông qua board mở rộng.
- Điều khiển động cơ quay thuận và quay ngược.
- Sử dụng PWM để thay đổi tốc độ động cơ.
- Lập trình xe tiến, lùi, rẽ trái, rẽ phải và dừng.
- Kiểm tra các lỗi thường gặp khi điều khiển động cơ.

Sau khi hoàn thành, bạn sẽ hiểu cách ESP32 điều khiển chuyển động của robot thông qua driver L298N.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Hiểu nguyên lý hoạt động cơ bản của động cơ DC.
- Giải thích vì sao ESP32 cần driver để điều khiển động cơ.
- Hiểu nguyên lý cầu H và cách đảo chiều động cơ.
- Phân biệt các chân điều khiển và chân nguồn của L298N.
- Sử dụng GPIO để điều khiển chiều quay động cơ.
- Sử dụng PWM để điều chỉnh mức công suất cấp cho động cơ.
- Viết các hàm điều khiển robot tiến, lùi, rẽ và dừng.
- Biết cách kiểm tra nguồn điện, dây kết nối và lỗi điều khiển động cơ.

---

## 3. Nguyên lý hoạt động của động cơ DC

### 3.1. Động cơ DC là gì?

Động cơ DC (*Direct Current Motor*) là loại động cơ hoạt động bằng nguồn điện một chiều.

Khi được cấp điện, động cơ tạo ra chuyển động quay.

<AsyncImage query="yellow TT DC geared motor robot car single motor white shaft" aspectRatio="5:3"/>

Trong xe robot, động cơ DC thường được kết hợp với hộp giảm tốc để:

- Giảm tốc độ quay của trục động cơ.
- Tăng mô-men xoắn tại bánh xe.
- Giúp robot di chuyển với tốc độ phù hợp.

Bộ xe sử dụng hai động cơ DC để điều khiển hai bánh chủ động.

### 3.2. Nguyên lý đảo chiều động cơ

Động cơ DC thông thường có hai đầu cấp điện.

Khi đặt điện áp theo một chiều, động cơ quay theo một hướng.

Khi đảo cực điện áp cấp vào hai đầu động cơ, chiều quay sẽ đảo ngược.

Ví dụ:

| Cực A | Cực B | Trạng thái |
|---|---|---|
| Dương | Âm | Quay theo chiều thứ nhất |
| Âm | Dương | Quay theo chiều ngược lại |
| Không cấp điện | Không cấp điện | Không tạo mô-men dẫn động |

Chiều quay thực tế còn phụ thuộc cách đấu dây và cách lắp động cơ trên robot.

Để ESP32 có thể đảo chiều điện áp cấp cho động cơ, chúng ta sử dụng mạch cầu H.

### 3.3. Vì sao không điều khiển động cơ trực tiếp từ ESP32?

Các chân GPIO của ESP32 được thiết kế để xử lý tín hiệu điều khiển, không phải cấp công suất cho động cơ.

Động cơ DC có thể yêu cầu dòng điện lớn, đặc biệt khi khởi động hoặc bị kẹt.

Nếu nối động cơ trực tiếp vào GPIO, có thể gây:

- Quá tải chân GPIO.
- Sụt điện áp.
- ESP32 hoạt động không ổn định.
- Hư hỏng vi điều khiển.

Vì vậy, ESP32 chỉ gửi tín hiệu điều khiển đến L298N.

Nguồn điện riêng của động cơ sẽ cung cấp năng lượng cho quá trình quay.

---

## 4. Tìm hiểu module L298N

### 4.1. Module L298N là gì?

L298N là driver điều khiển động cơ sử dụng hai mạch cầu H.

Module có thể điều khiển độc lập hai động cơ DC hoặc hai nhóm tải phù hợp với khả năng của driver.

<AsyncImage query="L298N dual H bridge motor driver module red board ENA IN1 IN2 IN3 IN4 ENB OUT1 OUT2 OUT3 OUT4" aspectRatio="5:3"/>

Trong bộ xe robot, L298N được sử dụng để:

- Điều khiển động cơ bên trái.
- Điều khiển động cơ bên phải.
- Thay đổi chiều quay từng động cơ.
- Điều chỉnh tốc độ thông qua PWM.
- Dừng một hoặc cả hai động cơ.

### 4.2. Các chân kết nối của L298N

Module L298N thường có các nhóm chân sau:

| Chân | Chức năng |
|---|---|
| IN1 | Điều khiển chiều quay động cơ A |
| IN2 | Điều khiển chiều quay động cơ A |
| ENA | Cho phép hoạt động và điều khiển PWM động cơ A |
| IN3 | Điều khiển chiều quay động cơ B |
| IN4 | Điều khiển chiều quay động cơ B |
| ENB | Cho phép hoạt động và điều khiển PWM động cơ B |
| OUT1, OUT2 | Kết nối hai đầu động cơ A |
| OUT3, OUT4 | Kết nối hai đầu động cơ B |
| GND | Cực âm nguồn và điểm tham chiếu tín hiệu |
| Chân nguồn động cơ | Cấp nguồn công suất cho động cơ |
| Chân 5V | Đường nguồn logic, chức năng phụ thuộc cấu hình module |

Trên một số module L298N, chân nguồn động cơ có thể được in nhãn `12V` hoặc `+12V`.

Đây là tên thường thấy trên module, không có nghĩa mọi động cơ đều phải sử dụng nguồn 12 V.

Điện áp cấp cần phù hợp với động cơ và thông số của module.

### 4.3. Nguyên lý cầu H

Cầu H là mạch điện cho phép thay đổi chiều dòng điện đi qua động cơ.

Đối với một kênh L298N, hai chân IN được sử dụng để lựa chọn chiều quay.

Ví dụ:

| EN | IN1 | IN2 | Trạng thái |
|---|---|---|---|
| HIGH | HIGH | LOW | Quay chiều thứ nhất |
| HIGH | LOW | HIGH | Quay chiều ngược lại |
| HIGH | LOW | LOW | Dừng theo quán tính |
| HIGH | HIGH | HIGH | Phanh điện |
| LOW | Bất kỳ | Bất kỳ | Ngắt đầu ra, động cơ quay theo quán tính |

Trong đó:

- HIGH: Mức logic cao.
- LOW: Mức logic thấp.
- EN: Chân cho phép hoạt động của kênh động cơ.

Khi EN ở mức LOW, đầu ra cầu H bị vô hiệu hóa. Động cơ không còn được chủ động cấp điện để quay nhưng vẫn có thể tiếp tục chuyển động do quán tính.

Khi cả hai đầu động cơ được đưa về cùng một mức thông qua cầu H đang hoạt động, động cơ có thể chịu tác dụng phanh điện.

### 4.4. Chân ENA và ENB

Hai chân ENA và ENB quyết định trạng thái hoạt động của từng kênh động cơ.

- ENA điều khiển kênh động cơ A.
- ENB điều khiển kênh động cơ B.

Khi EN được giữ HIGH, kênh tương ứng hoạt động theo trạng thái các chân IN.

Khi EN được đưa LOW, kênh tương ứng bị ngắt.

Ngoài hai trạng thái HIGH và LOW, chúng ta có thể đưa tín hiệu PWM vào ENA và ENB để điều chỉnh mức công suất trung bình cấp cho động cơ.

**Lưu ý:** Một số module L298N có jumper nối ENA và ENB lên mức HIGH. Muốn điều khiển PWM từ ESP32, cần tháo các jumper ENA/ENB này.

---

## 5. Điều chỉnh tốc độ động cơ bằng PWM

### 5.1. PWM là gì?

PWM (*Pulse Width Modulation*) là phương pháp điều khiển bằng cách thay đổi tỷ lệ thời gian tín hiệu ở mức HIGH trong một chu kỳ.

Thay vì thay đổi liên tục điện áp đầu ra GPIO, ESP32 tạo ra các xung HIGH và LOW với tần số xác định.

Tỷ lệ thời gian HIGH được gọi là *Duty Cycle*.

Ví dụ:

- Duty Cycle 0%: Tín hiệu luôn LOW.
- Duty Cycle 25%: Tín hiệu HIGH trong 25% chu kỳ.
- Duty Cycle 50%: Tín hiệu HIGH trong 50% chu kỳ.
- Duty Cycle 100%: Tín hiệu luôn HIGH.

Khi đưa PWM vào ENA hoặc ENB, L298N sẽ đóng/ngắt đầu ra theo tín hiệu này, làm thay đổi điện áp trung bình đặt lên động cơ.

### 5.2. Giá trị PWM trên ESP32

Trong bài học này, chúng ta sử dụng PWM với độ phân giải 8 bit.

Giá trị điều khiển nằm trong khoảng từ 0 đến 255.

| Giá trị PWM | Duty Cycle gần đúng | Ý nghĩa |
|---|---|---|
| 0 | 0% | Ngắt kênh động cơ |
| 64 | 25% | Mức điều khiển thấp |
| 128 | 50% | Mức điều khiển trung bình |
| 192 | 75% | Mức điều khiển cao |
| 255 | 100% | Kênh được cho phép liên tục |

Ví dụ:

```cpp
analogWrite(13, 120);
```

Lệnh trên tạo tín hiệu PWM trên GPIO13 với giá trị 120, theo cách sử dụng `analogWrite()` của Arduino-ESP32.

Trong các phiên bản Arduino-ESP32 core 3.x, `analogWrite()` có thể được sử dụng để tạo PWM theo cách tương tự Arduino.

**Lưu ý:** Giá trị PWM không phải tốc độ quay thực tế của động cơ.

Ví dụ, PWM bằng 128 không có nghĩa động cơ sẽ quay đúng một nửa tốc độ tối đa.

Tốc độ còn phụ thuộc:

- Điện áp nguồn.
- Tải trọng của robot.
- Ma sát bánh xe.
- Đặc tính từng động cơ.
- Sụt áp trên driver L298N.
- Trạng thái bộ pin.

Hai động cơ nhận cùng một giá trị PWM cũng không đảm bảo quay với tốc độ bằng nhau.

---

## 6. Chuẩn bị thiết bị và kết nối

### 6.1. Thiết bị cần thiết

| STT | Thiết bị | Số lượng |
|---|---|---|
| 1 | ESP32 30P CH340 Type-C | 1 |
| 2 | Board mở rộng ESP32 30P | 1 |
| 3 | Module L298N | 1 |
| 4 | Động cơ giảm tốc DC | 2 |
| 5 | Bộ pin và công tắc nguồn | 1 bộ |
| 6 | Dây kết nối | Theo nhu cầu |
| 7 | Máy tính đã cài Arduino IDE | 1 |
| 8 | Cáp USB Type-C có truyền dữ liệu | 1 |

Nếu đã có bộ xe robot hoàn chỉnh, chúng ta có thể sử dụng các kết nối sẵn có mà không cần lắp lại toàn bộ mạch.

### 6.2. Sơ đồ chân điều khiển

Trong cấu hình chương trình robot ESP32 đang sử dụng, các chân kết nối giữa ESP32 và L298N như sau:

| L298N | ESP32 GPIO | Chức năng |
|---|---|---|
| ENA | GPIO13 | PWM động cơ bên trái |
| IN1 | GPIO12 | Điều khiển chiều động cơ trái |
| IN2 | GPIO14 | Điều khiển chiều động cơ trái |
| ENB | GPIO15 | PWM động cơ bên phải |
| IN3 | GPIO4 | Điều khiển chiều động cơ phải |
| IN4 | GPIO2 | Điều khiển chiều động cơ phải |

Các chân GPIO trên được sử dụng trong chương trình thực hành của bài này.

**Lưu ý:** Số GPIO là số hiệu chân tín hiệu của ESP32, không phải vị trí chân tính từ đầu hàng chân cắm.

Tham khảo [sơ đồ chân robot ESP32](../08-su-dung-robot.md) để đối chiếu với phần cứng thực tế.

### 6.3. Kết nối động cơ với L298N

Hai động cơ DC được kết nối với các đầu ra công suất của L298N.

| Đầu ra L298N | Thiết bị |
|---|---|
| OUT1, OUT2 | Động cơ bên trái |
| OUT3, OUT4 | Động cơ bên phải |

Nếu động cơ quay ngược chiều mong muốn, cần kiểm tra cách đấu dây và chiều lắp đặt.

Không thay đổi dây khi hệ thống đang được cấp nguồn.

### 6.4. Kết nối nguồn điện

Nguồn động cơ được cấp vào các chân nguồn công suất của L298N theo thông số của module.

Đồng thời, ESP32 và L298N cần có điểm GND chung để các tín hiệu điều khiển được nhận diện đúng trong cấu hình không cách ly.

Nguyên tắc kết nối:

- ESP32 xuất tín hiệu điều khiển đến L298N.
- Nguồn động cơ cấp năng lượng cho động cơ thông qua L298N.
- GND ESP32 và GND L298N được nối chung.
- Không cấp nguồn động cơ từ GPIO của ESP32.
- Không đưa điện áp bộ pin trực tiếp vào chân 3V3 hoặc 5V của ESP32 khi chưa xác định sơ đồ cấp nguồn.

### 6.5. Kiểm tra jumper trên L298N

Trước khi chạy chương trình PWM, cần kiểm tra jumper ENA và ENB.

Nếu jumper ENA/ENB đang nối cố định chân EN lên HIGH, cần tháo jumper tương ứng để ESP32 có thể điều khiển PWM.

Một số module còn có jumper `5V_EN`.

Jumper này liên quan đến mạch nguồn logic của module, không phải jumper điều khiển tốc độ động cơ.

Không tự ý tháo hoặc cắm jumper `5V_EN` khi chưa kiểm tra sơ đồ và điện áp nguồn thực tế.

**Lưu ý an toàn:** Trước khi nạp và chạy chương trình điều khiển động cơ, cần kê bánh xe khỏi mặt đất. Chương trình có thể làm động cơ quay ngay sau khi ESP32 khởi động.

---

## 7. Điều khiển một động cơ DC

Trước khi điều khiển cả xe, chúng ta cần hiểu cách điều khiển một động cơ.

### 7.1. Điều khiển động cơ quay thuận

Ví dụ với động cơ bên trái:

```cpp
digitalWrite(12, HIGH);
digitalWrite(14, LOW);
analogWrite(13, 150);
```

Trong đó:

- GPIO12 được đưa HIGH.
- GPIO14 được đưa LOW.
- GPIO13 tạo tín hiệu PWM với giá trị 150.

Động cơ sẽ quay theo một chiều xác định bởi cách đấu dây.

### 7.2. Điều khiển động cơ quay ngược

Để đảo chiều quay, chúng ta đổi trạng thái hai chân điều khiển:

```cpp
digitalWrite(12, LOW);
digitalWrite(14, HIGH);
analogWrite(13, 150);
```

Động cơ sẽ quay theo chiều ngược lại.

### 7.3. Dừng động cơ

Để ngắt kênh điều khiển động cơ:

```cpp
analogWrite(13, 0);
```

Khi PWM bằng 0, chân EN không còn cho phép kênh động cơ hoạt động.

Động cơ sẽ giảm tốc và dừng do ma sát và các lực cản.

Tuy nhiên, động cơ không nhất thiết dừng ngay lập tức vì còn quán tính.

---

## 8. Thực hành điều khiển hai động cơ

### 8.1. Mục tiêu thực hành

Chúng ta sẽ viết chương trình để robot thực hiện lần lượt:

1. Đứng yên.
2. Tiến.
3. Dừng.
4. Lùi.
5. Dừng.
6. Rẽ trái.
7. Dừng.
8. Rẽ phải.
9. Dừng hoàn toàn.

Chương trình chỉ thực hiện một chuỗi thử nghiệm sau mỗi lần khởi động, không tự động lặp lại liên tục.

### 8.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn **File → New Sketch**.

Lưu chương trình với tên:

```text
ESP32L298N
```

Cấu trúc thư mục:

```text
ESP32L298N/
└── ESP32L298N.ino
```

### 8.3. Chương trình hoàn chỉnh

```cpp
// ================= MOTOR PINS =================

// Motor trai
const int ENA = 13;
const int IN1 = 12;
const int IN2 = 14;

// Motor phai
const int ENB = 15;
const int IN3 = 4;
const int IN4 = 2;

// ================= PARAMETERS =================

const int MOTOR_SPEED = 120;

unsigned long batDau = 0;

// ================= MOTOR CONTROL =================

void motor(int en, int a, int b, int pwm) {

  pwm = constrain(pwm, -255, 255);

  if (pwm > 0) {
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
  }
  else if (pwm < 0) {
    digitalWrite(a, LOW);
    digitalWrite(b, HIGH);
  }
  else {
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
  }

  analogWrite(en, abs(pwm));
}

// ================= ROBOT CONTROL =================

void drive(int left, int right) {
  motor(ENA, IN1, IN2, left);
  motor(ENB, IN3, IN4, right);
}

// ================= SETUP =================

void setup() {

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  drive(0, 0);

  batDau = millis();
}

// ================= LOOP =================

void loop() {

  unsigned long t = millis() - batDau;

  if (t < 1000) {
    drive(0, 0);
  }
  else if (t < 1800) {
    drive(MOTOR_SPEED, MOTOR_SPEED);  // Tien
  }
  else if (t < 2300) {
    drive(0, 0);
  }
  else if (t < 3100) {
    drive(-MOTOR_SPEED, -MOTOR_SPEED); // Lui
  }
  else if (t < 3600) {
    drive(0, 0);
  }
  else if (t < 4100) {
    drive(0, MOTOR_SPEED);            // Re trai
  }
  else if (t < 4600) {
    drive(0, 0);
  }
  else if (t < 5100) {
    drive(MOTOR_SPEED, 0);            // Re phai
  }
  else {
    drive(0, 0);                      // Dung
  }
}
```

Chương trình sử dụng `analogWrite()` theo Arduino-ESP32 core 3.x và không cần cài thêm thư viện điều khiển động cơ.

**Lưu ý:** Các giá trị PWM dương và âm trong chương trình được quy ước tương ứng với chiều tiến và lùi. Nếu phần cứng được đấu theo chiều ngược, cần hiệu chỉnh quy ước chiều quay cho đúng trước khi thử xe trên mặt đất.

---

## 9. Giải thích chương trình

### 9.1. Khai báo các chân động cơ

```cpp
const int ENA = 13;
const int IN1 = 12;
const int IN2 = 14;

const int ENB = 15;
const int IN3 = 4;
const int IN4 = 2;
```

Các hằng số trên xác định chân ESP32 được sử dụng để điều khiển L298N.

Việc khai báo bằng tên giúp chương trình dễ đọc và thuận tiện khi cần đối chiếu sơ đồ kết nối.

### 9.2. Khai báo tốc độ động cơ

```cpp
const int MOTOR_SPEED = 120;
```

Hằng số `MOTOR_SPEED` được sử dụng làm mức PWM cho các thao tác thử nghiệm.

Giá trị 120 nằm trong khoảng 0–255.

Đây chỉ là mức điều khiển ban đầu.

Nếu động cơ không quay ở PWM 120, có thể cần điều chỉnh lên mức phù hợp với nguồn và tải thực tế.

### 9.3. Hàm điều khiển một động cơ

```cpp
void motor(int en, int a, int b, int pwm)
```

Hàm `motor()` nhận bốn tham số:

| Tham số | Chức năng |
|---|---|
| `en` | Chân PWM |
| `a` | Chân điều khiển chiều thứ nhất |
| `b` | Chân điều khiển chiều thứ hai |
| `pwm` | Giá trị điều khiển có dấu |

Trong chương trình, giá trị `pwm` được quy ước:

- PWM dương: Quay theo chiều tiến.
- PWM âm: Quay theo chiều lùi.
- PWM bằng 0: Ngắt kênh động cơ.

Ví dụ:

```cpp
motor(ENA, IN1, IN2, 150);
```

Điều khiển động cơ trái quay theo chiều tiến với mức PWM 150.

```cpp
motor(ENA, IN1, IN2, -150);
```

Điều khiển động cơ trái quay theo chiều ngược lại.

```cpp
motor(ENA, IN1, IN2, 0);
```

Ngắt kênh điều khiển động cơ trái.

### 9.4. Giới hạn giá trị PWM

```cpp
pwm = constrain(pwm, -255, 255);
```

Hàm `constrain()` giới hạn giá trị PWM trong khoảng từ -255 đến 255.

Ví dụ:

| Giá trị đầu vào | Giá trị sau giới hạn |
|---|---|
| 100 | 100 |
| -150 | -150 |
| 300 | 255 |
| -300 | -255 |

Điều này giúp tránh truyền giá trị điều khiển vượt phạm vi dự kiến.

### 9.5. Hàm điều khiển hai động cơ

```cpp
void drive(int left, int right) {
  motor(ENA, IN1, IN2, left);
  motor(ENB, IN3, IN4, right);
}
```

Hàm `drive()` cho phép điều khiển đồng thời hai động cơ.

Trong đó:

- `left`: Giá trị PWM động cơ trái.
- `right`: Giá trị PWM động cơ phải.

Ví dụ:

```cpp
drive(120, 120);
```

Hai động cơ quay theo chiều tiến.

```cpp
drive(-120, -120);
```

Hai động cơ quay theo chiều lùi.

```cpp
drive(0, 0);
```

Dừng cấp lực dẫn động cho cả hai động cơ.

### 9.6. Các lệnh điều khiển chuyển động

| Lệnh | Chuyển động dự kiến |
|---|---|
| `drive(120, 120)` | Tiến |
| `drive(-120, -120)` | Lùi |
| `drive(0, 120)` | Rẽ trái theo cung |
| `drive(120, 0)` | Rẽ phải theo cung |
| `drive(-120, 120)` | Xoay trái tại chỗ |
| `drive(120, -120)` | Xoay phải tại chỗ |
| `drive(0, 0)` | Dừng cấp lực dẫn động |

Các chuyển động trên giả định hai động cơ đã được cấu hình đúng chiều tiến của robot.

Khi rẽ theo cung, một bánh được dừng trong khi bánh còn lại tiếp tục quay.

Khi xoay tại chỗ, hai bánh quay ngược chiều nhau.

### 9.7. Sử dụng millis() để quản lý thời gian

Trong chương trình, chúng ta sử dụng:

```cpp
batDau = millis();
```

Để ghi lại thời điểm bắt đầu.

Trong `loop()`:

```cpp
unsigned long t = millis() - batDau;
```

Biến `t` biểu diễn khoảng thời gian đã trôi qua kể từ khi bắt đầu thử nghiệm.

Chương trình dựa vào giá trị `t` để lựa chọn chuyển động tương ứng.

Ưu điểm của cách này là không cần sử dụng nhiều lệnh `delay()` để tạo chuỗi chuyển động.

Tuy nhiên, `millis()` chỉ giúp quản lý thời gian. Nó không tự đảm bảo động cơ đã dừng hẳn trước khi chuyển sang chiều quay ngược lại.

### 9.8. Vì sao cần có khoảng dừng trước khi đảo chiều?

Khi động cơ đang quay tiến, việc lập tức điều khiển quay lùi có thể tạo ra dòng điện và lực cơ học lớn.

Vì vậy, chương trình thử nghiệm có các khoảng dừng giữa những chuyển động.

Ví dụ:

```cpp
else if (t < 1800) {
  drive(120, 120);
}
else if (t < 2300) {
  drive(0, 0);
}
else if (t < 3100) {
  drive(-120, -120);
}
```

Trong ví dụ trên:

- Robot tiến đến mốc 1800 ms.
- Ngắt lực dẫn động trong 500 ms.
- Sau đó bắt đầu lùi.

Khoảng dừng giúp giảm nguy cơ đảo chiều quá đột ngột, nhưng không bảo đảm động cơ đã dừng hoàn toàn trong mọi điều kiện.

Đối với robot có tải lớn hoặc tốc độ cao, cần có cơ chế giảm tốc và xác nhận trạng thái phù hợp trước khi đảo chiều.

---

## 10. Biên dịch và chạy thử

### 10.1. Kiểm tra trước khi cấp nguồn

Trước khi nạp và chạy chương trình:

1. Kê hai bánh chủ động khỏi mặt đất.
2. Kiểm tra dây động cơ.
3. Kiểm tra kết nối ESP32 với L298N.
4. Kiểm tra nguồn động cơ.
5. Kiểm tra jumper ENA và ENB.
6. Đảm bảo có thể ngắt nguồn động cơ khi cần.

Không đặt robot trên sàn ngay trong lần thử đầu tiên.

### 10.2. Biên dịch chương trình

Trong Arduino IDE:

1. Chọn **ESP32 Dev Module**.
2. Chọn đúng cổng COM.
3. Nhấn **Verify**.
4. Kiểm tra thông báo biên dịch.

Nếu chương trình không có lỗi, chuyển sang bước nạp.

### 10.3. Nạp chương trình

Nhấn **Upload**.

Chờ Arduino IDE hoàn tất quá trình nạp.

Sau khi nạp thành công, ESP32 sẽ chạy chương trình mới.

Cần lưu ý rằng chương trình mới sẽ thay thế chương trình robot đang lưu trên ESP32.

### 10.4. Quan sát kết quả

Nếu hệ thống hoạt động đúng, chuỗi chuyển động dự kiến như sau:

| Thời gian tính từ khi bắt đầu | Hoạt động |
|---|---|
| 0–1,0 giây | Dừng |
| 1,0–1,8 giây | Tiến |
| 1,8–2,3 giây | Dừng |
| 2,3–3,1 giây | Lùi |
| 3,1–3,6 giây | Dừng |
| 3,6–4,1 giây | Rẽ trái |
| 4,1–4,6 giây | Dừng |
| 4,6–5,1 giây | Rẽ phải |
| Sau 5,1 giây | Dừng |

Chương trình chỉ thực hiện một chuỗi thử nghiệm.

Nếu nhấn EN/RESET, ESP32 sẽ khởi động lại và thực hiện chuỗi từ đầu.

### 10.5. Kiểm tra chiều quay

Khi thử nghiệm, cần quan sát:

- Hai bánh có quay đúng chiều tiến không?
- Hai bánh có quay đúng chiều lùi không?
- Robot có rẽ đúng hướng không?
- Một bên động cơ có quay yếu hơn bên còn lại không?
- Động cơ có phát ra tiếng bất thường không?

Nếu một động cơ quay ngược chiều mong muốn, cần tắt nguồn và kiểm tra lại cách đấu dây hoặc quy ước điều khiển chiều quay.

Không nên đưa robot xuống sàn khi chưa xác nhận đúng chiều quay của cả hai động cơ.

---

## 11. Các lỗi thường gặp

### 11.1. Động cơ không quay

**Nguyên nhân có thể:**

- Chưa cấp nguồn cho L298N.
- Nguồn động cơ không đủ điện áp hoặc dòng điện.
- Chưa nối GND chung.
- Chân ENA hoặc ENB không nhận được tín hiệu điều khiển.
- Dây động cơ bị lỏng.
- Kết nối GPIO không đúng.

**Cách xử lý:**

1. Kiểm tra nguồn động cơ.
2. Kiểm tra GND chung.
3. Kiểm tra jumper ENA và ENB.
4. Kiểm tra dây nối OUT1–OUT4.
5. Đối chiếu chân GPIO với chương trình.

### 11.2. Động cơ chỉ quay một chiều

**Nguyên nhân có thể:**

- Một trong hai chân IN bị mất tín hiệu.
- Dây kết nối bị lỏng.
- Chân GPIO trong chương trình không đúng.
- Một đầu ra của driver bị lỗi.

**Cách xử lý:**

1. Kiểm tra IN1, IN2 hoặc IN3, IN4.
2. Kiểm tra mức logic điều khiển.
3. Thử riêng từng chiều quay.
4. Kiểm tra dây và đầu ra driver.

### 11.3. Động cơ quay nhưng không thay đổi tốc độ

**Nguyên nhân có thể:**

- Jumper ENA/ENB vẫn đang giữ mức HIGH.
- PWM chưa được đưa đúng chân.
- Giá trị PWM thay đổi quá nhỏ để quan sát.
- Động cơ đang ở vùng tốc độ thấp hoặc gần bão hòa.

**Cách xử lý:**

1. Kiểm tra jumper ENA/ENB.
2. Kiểm tra GPIO13 và GPIO15.
3. Thử các mức PWM khác nhau.
4. Kiểm tra nguồn điện và tải động cơ.

### 11.4. Chỉ một bánh xe quay

**Nguyên nhân có thể:**

- Một động cơ không được cấp nguồn.
- Một kênh L298N không hoạt động.
- Dây kết nối động cơ bị lỗi.
- Chân điều khiển hoặc chân EN không đúng.
- Động cơ bị kẹt cơ khí.

**Cách xử lý:**

1. Kiểm tra từng động cơ.
2. Kiểm tra đầu ra OUT1–OUT4.
3. Kiểm tra ENA và ENB.
4. Kiểm tra các chân điều khiển IN.
5. Kiểm tra khả năng quay tự do của bánh xe.

### 11.5. Hai bánh quay không đều

Ngay cả khi hai động cơ nhận cùng một giá trị PWM, tốc độ thực tế vẫn có thể khác nhau.

Nguyên nhân có thể:

- Sai khác giữa hai động cơ.
- Ma sát cơ khí khác nhau.
- Đường kính bánh xe không hoàn toàn bằng nhau.
- Tải trọng phân bố không đều.
- Sụt áp và tổn hao trên driver.

Để điều khiển chính xác hơn, chúng ta cần sử dụng Encoder để đo tốc độ thực tế của từng bánh.

Trong những bài học tiếp theo, chúng ta sẽ tìm hiểu cách đọc Encoder và ứng dụng phản hồi để điều khiển chuyển động.

### 11.6. ESP32 bị Reset khi động cơ chạy

**Nguyên nhân có thể:**

- Nguồn cấp bị sụt áp khi động cơ khởi động.
- Nguồn không đủ dòng.
- Nhiễu điện từ từ động cơ.
- Cách cấp nguồn và nối GND chưa phù hợp.

**Cách xử lý:**

- Kiểm tra điện áp nguồn khi động cơ khởi động.
- Sử dụng nguồn có khả năng cấp dòng phù hợp.
- Kiểm tra dây nguồn và các đầu nối.
- Kiểm tra cách bố trí nguồn ESP32 và nguồn động cơ.
- Hạn chế đường dây nguồn và tín hiệu bị lỏng hoặc tiếp xúc kém.

---

## 12. Bài tập thực hành

### Bài tập 1: Thay đổi giá trị PWM

Thử lần lượt các giá trị:

```cpp
const int MOTOR_SPEED = 100;
```

```cpp
const int MOTOR_SPEED = 120;
```

```cpp
const int MOTOR_SPEED = 150;
```

Quan sát sự thay đổi tốc độ quay khi hai bánh được kê khỏi mặt đất.

Ghi lại mức PWM thấp nhất mà mỗi động cơ bắt đầu quay ổn định.

Giải thích vì sao hai động cơ có thể bắt đầu quay ở các mức PWM khác nhau.

### Bài tập 2: Viết hàm điều khiển chuyển động

Dựa trên hàm `drive()`, viết thêm các hàm:

```cpp
void forward() {
  drive(120, 120);
}

void backward() {
  drive(-120, -120);
}

void stopMotor() {
  drive(0, 0);
}
```

Sau đó sử dụng các hàm này để điều khiển robot.

### Bài tập 3: Điều khiển robot xoay tại chỗ

Viết chương trình để robot thực hiện:

1. Dừng một giây.
2. Xoay trái tại chỗ trong thời gian ngắn.
3. Dừng.
4. Xoay phải tại chỗ trong thời gian ngắn.
5. Dừng hoàn toàn.

Gợi ý:

```cpp
drive(-120, 120);  // Xoay trai
```

```cpp
drive(120, -120);  // Xoay phai
```

Cần bố trí khoảng dừng phù hợp trước khi đảo chiều động cơ.

### Bài tập 4: Điều chỉnh tốc độ hai bánh

Thử chương trình:

```cpp
drive(100, 150);
```

Quan sát sự khác biệt giữa hai bánh.

Giải thích vì sao khi hai bánh quay với tốc độ khác nhau, robot có xu hướng đổi hướng di chuyển.

### Bài tập 5: Phân biệt dừng và phanh

Trả lời:

1. Khi ENA và ENB bằng LOW, động cơ có dừng ngay lập tức không?
2. Vì sao bánh xe vẫn có thể tiếp tục quay sau khi ngắt PWM?
3. Phanh điện khác gì so với ngắt đầu ra cầu H?
4. Vì sao không nên đảo chiều động cơ đột ngột khi đang quay nhanh?

---

## 13. Kiểm tra trước khi bắt đầu bài tiếp theo

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã hiểu nguyên lý hoạt động của động cơ DC.
- [ ] Đã biết vì sao ESP32 cần driver L298N.
- [ ] Đã hiểu nguyên lý cầu H.
- [ ] Đã phân biệt IN1, IN2, IN3, IN4, ENA và ENB.
- [ ] Đã biết cách điều khiển chiều quay động cơ.
- [ ] Đã hiểu chức năng của PWM.
- [ ] Đã biết giá trị PWM 0–255 không phải tốc độ thực tế.
- [ ] Đã kiểm tra nguồn và jumper của L298N.
- [ ] Đã nạp thành công chương trình điều khiển động cơ.
- [ ] Đã điều khiển được robot tiến, lùi, rẽ và dừng.
- [ ] Đã hiểu vì sao cần dừng hoặc giảm tốc trước khi đảo chiều.

---

## 14. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu cách điều khiển động cơ DC bằng ESP32 và module L298N.

Những nội dung quan trọng bao gồm:

- Hiểu nguyên lý hoạt động của động cơ DC.
- Tìm hiểu cấu tạo và chức năng của driver L298N.
- Sử dụng cầu H để thay đổi chiều quay động cơ.
- Sử dụng PWM để điều chỉnh mức công suất điều khiển.
- Kết nối L298N với ESP32 theo sơ đồ chân của robot.
- Viết chương trình điều khiển hai động cơ.
- Thực hiện các chuyển động tiến, lùi, rẽ trái, rẽ phải và dừng.
- Tìm hiểu những nguyên nhân khiến động cơ không quay hoặc quay không đều.
- Nắm được các nguyên tắc an toàn khi thử nghiệm động cơ.

Đây là kiến thức nền tảng để xây dựng các chức năng chuyển động của xe robot.

Ở bài tiếp theo, chúng ta sẽ tìm hiểu **cảm biến siêu âm HC-SR04**, cách đo khoảng cách đến vật cản và sử dụng dữ liệu khoảng cách để hỗ trợ điều khiển robot.

---

[Bài trước: Điều khiển Servo](04-servo.md) · [Lộ trình bài học](../index.md) · [Bài tiếp: Cảm biến HC-SR04](06-hc-sr04.md)