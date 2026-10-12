# Bài 5: Điều khiển động cơ DC với L298N và Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Đảo chiều một nhóm động cơ bằng cầu H.
- Điều chỉnh mức PWM qua ENA/ENB.
- Viết lệnh tiến, lùi, rẽ và dừng với đúng chân robot.

**Trước khi bắt đầu:** Servo và nguồn tải — [mở bài trước](04-servo.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

L298N là driver cầu H kép: bo gửi tín hiệu logic, nguồn tải cung cấp dòng cho motor. IN1/IN2 điều khiển một cầu, IN3/IN4 điều khiển cầu còn lại; ENA/ENB cho phép hoạt động và nhận PWM.

| EN | IN thứ nhất | IN thứ hai | Trạng thái |
| --- | --- | --- | --- |
| HIGH/PWM | HIGH | LOW | Một chiều |
| HIGH/PWM | LOW | HIGH | Chiều ngược lại |
| LOW | Bất kỳ | Bất kỳ | Ngắt cầu, motor dừng theo quán tính |

| PWM 8 bit | Tỷ lệ bật gần đúng | Ý nghĩa |
| --- | --- | --- |
| 0 | 0% | Ngắt EN |
| 64 | 25% | Mức thấp, có thể chưa đủ thắng ma sát |
| 128 | 50% | Tỷ lệ bật một nửa, không bảo đảm nửa tốc độ |
| 255 | 100% | EN bật liên tục, vẫn chịu giới hạn nguồn/tải |

Chiều “tiến” phụ thuộc dây và cách lắp motor. PWM 0–255 là tỷ lệ bật, không phải tốc độ m/s; cùng PWM chưa bảo đảm hai bánh bằng tốc độ. Xem [datasheet L298 của ST](https://www.st.com/resource/en/datasheet/l298.pdf).

## 2. Chuẩn bị, bảng chân và đấu nối

| L298N | Arduino Nano | Chức năng |
| --- | --- | --- |
| ENA / ENB | 5 / 6 | PWM nhóm motor trái / phải theo mã |
| IN1 / IN2 | 0 / 1 | Chiều nhóm motor A |
| IN3 / IN4 | 4 / 7 | Chiều nhóm motor B |
| OUT1 / OUT2 | Hai dây motor A | Đầu ra công suất |
| OUT3 / OUT4 | Hai dây motor B | Đầu ra công suất |
| GND | GND bo và nguồn motor | Mốc tín hiệu chung |

Chân số trong bảng là tên D/GPIO, không phải thứ tự đếm chân. Đối chiếu [sơ đồ sản phẩm](../08-su-dung-robot.md) và chiều lắp động cơ.

Để dùng PWM ngoài, tháo jumper **ENA/ENB** nếu module đang nối cố định hai chân này lên HIGH. Jumper **5V_EN** là phần nguồn logic khác: kiểm tra hướng dẫn đúng module trước khi giữ/tháo, không nối hai nguồn 5 V đối đầu. Cấp nguồn motor theo thông số motor và board nguồn; nhãn “12V” trên một số module không bắt buộc cấp đúng 12 V. Không cấp motor từ chân GPIO/5V của bo.

Bộ Drive dùng D0/D1 cho motor: không thêm Serial.begin() vào sketch điều khiển này, ngắt IN1/IN2 khi nạp nếu ảnh hưởng USB rồi nối lại khi đã tắt nguồn. Sơ đồ gốc có chú thích L9110s nhưng mã dùng giao diện L298N; xác nhận module thật có ENA/ENB trước khi làm.

Kê bánh khỏi sàn, chuẩn bị công tắc nguồn motor. Ví dụ bên dưới chạy ngay sau khi khởi động bo.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
const int ENA = 5, ENB = 6;
const int IN1 = 0, IN2 = 1;
const int IN3 = 4, IN4 = 7;

void motor(int en, int a, int b, int pwm) {
  pwm = constrain(pwm, -255, 255);
  digitalWrite(a, pwm > 0 ? HIGH : LOW);
  digitalWrite(b, pwm < 0 ? HIGH : LOW);
  analogWrite(en, abs(pwm));
}

void drive(int left, int right) {
  motor(ENA, IN1, IN2, left);
  motor(ENB, IN3, IN4, right);
}

void setupMotors() {
  pinMode(ENA, OUTPUT); pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  drive(0, 0);
}

unsigned long batDau;

void setup() {
  setupMotors();
  batDau = millis();
}

void loop() {
  unsigned long t = millis() - batDau;
  if (t < 1000)      drive(0, 0);
  else if (t < 1800) drive(120, 120);   // tien
  else if (t < 2300) drive(0, 0);
  else if (t < 3100) drive(-120, -120); // lui
  else if (t < 3600) drive(0, 0);
  else if (t < 4100) drive(0, 120);     // re trai theo cung
  else if (t < 4600) drive(0, 0);
  else if (t < 5100) drive(120, 0);     // re phai theo cung
  else              drive(0, 0);      // dung, khong lap lai
}
```

## 4. Giải thích chương trình

motor() nhận PWM có dấu: dương tiến theo cấu hình, âm đảo chiều, 0 ngắt EN. drive() đặt hai nhóm motor. Chương trình thử một lượt rồi dừng, có khoảng nghỉ trước đổi hướng. Hàm motor() không có thời gian chờ đổi chiều riêng; khi tự viết chuỗi lệnh, gọi drive(0, 0) và chờ motor dừng trước khi đảo chiều.

`drive(0, 120)` dừng một bên để rẽ theo cung, không xoay tại chỗ. Xoay tại chỗ cần hai bên ngược chiều: `drive(-120, 120)`. Giá trị 120 chỉ là mức khởi đầu; motor có thể không vượt ma sát ở mức này.

## 5. Chạy thử và kết quả mong đợi

Kê bánh khỏi sàn trước khi bật nguồn tải. Sau một giây, xe thử tiến, lùi và rẽ theo bảng thời gian rồi dừng. Nếu một bên quay ngược, ngắt nguồn và kiểm tra dây/hàm chiều trước khi thử trên sàn. Reset chạy lại một lượt; không giữ nguồn nếu driver/motor nóng.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Motor không quay | Nguồn tải, GND, EN, jumper và dây OUT |
| PWM không đổi tốc độ | ENA/ENB có bị jumper giữ HIGH không |
| Chỉ một chiều | IN, dây và chân trong mã |
| Xe lệch | Pin, ma sát, PWM từng bên; học encoder/PID sau |

## 7. Bài tập thực hành

1. So sánh PWM 100, 120, 150 khi bánh kê khỏi sàn; ghi kết quả, không gọi đây là tốc độ cố định.
2. Viết forward(), backward(), stopMotor() dùng drive().
3. Thêm một bước xoay tại chỗ ngắn, có khoảng dừng trước/sau.
4. Giải thích vì sao dừng với EN=0 có thể vẫn còn quán tính.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](04-servo.md) · [Lộ trình](../index.md) · [Bài tiếp: HC-SR04](06-hc-sr04.md)
