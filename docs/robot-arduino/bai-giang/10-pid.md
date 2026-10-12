# Bài 10: Làm quen với điều khiển tốc độ bằng PID

**Mục tiêu:** hiểu vì sao cần đo tốc độ, tính một sai số và quan sát cách bộ điều khiển sửa mức PWM. Bắt đầu bằng tính trên giấy và mô phỏng trên Nano; chưa bật motor ngay với một đoạn mã dài.

## Bạn đã sẵn sàng học bài này chưa?

Trước khi làm, cần:

- Thử được hai bên motor và dừng đúng ở [bài 5](05-dong-co.md).
- Đọc được xung của cả hai encoder và đo số xung một vòng ở [bài 8](08-encoder.md).
- Hiểu biến, if và cách xem log ở [bài 2](02-lap-trinh.md).

Nếu encoder chưa đọc ổn định, quay lại kiểm tra nó trước. Bạn vẫn dùng được mã robot bàn giao và Bluetooth mà chưa cần tự chỉnh PID.

## Bước 1. Hiểu vấn đề của PWM đặt trước

Giả sử đặt cùng PWM 120 cho hai bên. Xe có thể lệch vì hai motor, ma sát, tải hoặc pin không hoàn toàn giống nhau. Nano chỉ ra lệnh “mức 120” chưa biết bánh thực tế quay nhanh bao nhiêu.

Encoder giúp Nano **đo kết quả**. Chương trình so kết quả với mong muốn rồi sửa PWM. Cách làm này gọi là **điều khiển có phản hồi**.

```mermaid
flowchart LR
    A[Tốc độ mong muốn] --> B[So với tốc độ đo]
    B --> C[Tính mức sửa PWM]
    C --> D[Driver và motor]
    D --> E[Encoder đo bánh]
    E --> B
```

Phản hồi giống việc bạn nhìn xe bị lệch rồi chỉnh tay lái; ở đây việc đo và chỉnh được chương trình làm lặp lại.

## Bước 2. Tính sai số bằng ví dụ cụ thể

**Tốc độ đặt** là tốc độ muốn đạt. **Tốc độ đo** là số tính từ encoder. **Sai số** là phần chênh lệch:

```text
sai số = tốc độ đặt − tốc độ đo
```

Giả sử muốn 0,15 m/s:

| Tốc độ đo | Sai số | Ý nghĩa |
| --- | --- | --- |
| 0,10 m/s | 0,15 − 0,10 = +0,05 | Bánh chậm hơn mong muốn |
| 0,15 m/s | 0 | Bằng mong muốn |
| 0,20 m/s | −0,05 | Bánh nhanh hơn mong muốn |

Bạn phải đo với cùng đơn vị. Không lấy tốc độ đặt m/s trừ trực tiếp số xung hoặc RPM.

## Bước 3. Học phần P trước

**P** sửa PWM theo sai số hiện tại. Chọn hệ số thử `Kp = 100`; sai số +0,05 tạo mức sửa +5, sai số −0,05 tạo mức sửa −5.

Nếu PWM ban đầu là 120, các mức đề xuất trong hai trường hợp là 125 và 115. Hệ số 100 chỉ để dễ tính, không phải giá trị đã hiệu chỉnh cho xe của bạn.

| Ký hiệu | Hiểu đơn giản |
| --- | --- |
| Kp | Mỗi đơn vị sai số sẽ làm thay PWM bao nhiêu |
| PWM ban đầu | Mức cơ sở trước khi cộng phần sửa |
| Giới hạn PWM | Khoảng được phép gửi cho driver |

Kp quá lớn có thể làm sửa quá mạnh rồi dao động. Chưa thêm I/D khi chưa hiểu chiều sửa của P.

## Bước 4. Quan sát P bằng sketch mô phỏng

**Ngắt motor và ngắt driver khỏi D0/D1** để dùng Serial. Sketch này chỉ tính và in kết quả, **không dùng analogWrite và không làm bánh quay**.

Tạo `NanoPThuNghiem`, chép:

```cpp
float tocDoDat = 0.15;
float tocDoDo = 0.10;
float Kp = 100;
int pwmBanDau = 120;

void setup() {
  Serial.begin(9600);
}

void loop() {
  float saiSo = tocDoDat - tocDoDo;
  float mucSua = Kp * saiSo;
  int pwmMoi = pwmBanDau + mucSua;

  if (pwmMoi > 200) {
    pwmMoi = 200;
  }
  if (pwmMoi < 0) {
    pwmMoi = 0;
  }

  Serial.print("Sai so: ");
  Serial.print(saiSo);
  Serial.print(" | PWM de xuat: ");
  Serial.println(pwmMoi);
  delay(1000);
}
```

Upload và mở Monitor 9600.

**Kết quả cần thấy:** sai số khoảng 0,05 và PWM đề xuất khoảng 125. Giá trị tốc độ đo trong mã là số bạn nhập để mô phỏng, **chưa đến từ encoder**.

Lần lượt đổi `tocDoDo` thành 0,15 rồi 0,20 và nạp lại. So với bảng ở bước 2: PWM phải giảm khi tốc độ đo lớn hơn tốc độ đặt.

## Bước 5. I và D bổ sung việc gì?

Sau khi hiểu P, mới xem hai phần còn lại:

| Phần | Khi nào hữu ích? | Điều cần chú ý |
| --- | --- | --- |
| I, tích phân | Sai số nhỏ nhưng kéo dài qua nhiều lần đo | Cộng dồn theo thời gian; quá lớn có thể tích lũy quá mức |
| D, đạo hàm | Sai số đang đổi nhanh và cần giảm phản ứng mạnh | Dễ bị nhiễu số đo làm tác động sai |

Ví dụ I: sai số +0,05 kéo dài mỗi khoảng 0,2 giây. Mỗi lần cộng `0,05 × 0,2 = 0,01` vào tổng. Sau năm lần, tổng là 0,05; nhân Ki mới đổi tổng đó thành phần sửa PWM.

Ví dụ D: sai số đổi từ 0,05 về 0,02 trong 0,2 giây, tốc độ thay đổi sai số là `(0,02 − 0,05) / 0,2 = −0,15`. Nhân Kd sẽ tạo phần sửa bổ sung. Chưa cần tự bật Kd nếu số encoder còn nhảy mạnh.

**PID** cộng cả ba phần P/I/D. **PI** dùng P/I và đặt Kd bằng 0. Tên thuật toán không bảo đảm chạy đúng; số đo, thời gian đo, giới hạn đầu ra và hệ số đều phải phù hợp.

## Bước 6. Ghép vào xe theo đúng thứ tự

1. Đo PPR trên bánh thật với cách đếm đã chọn, như bài encoder.
2. Đo chu vi bánh và đổi số xung trong khoảng đo thành m/s.
3. Thử motor với mức PWM nhỏ và xác nhận chiều tiến của từng bên.
4. Tạo một bộ điều khiển tốc độ cho mỗi bên, cập nhật theo khoảng thời gian đo thực tế.
5. Giới hạn PWM và thời gian thử, dừng khi mất xung kéo dài.
6. Bắt đầu với P hoặc PI; thay một hệ số mỗi lần và ghi kết quả trước/sau.

**Kết quả cần kiểm tra:** tốc độ đo thay đổi phù hợp khi mức đặt đổi, xe có thể dừng, và khi encoder không hoạt động chương trình không tiếp tục tăng PWM vô hạn. Chỉ nhìn bánh quay chưa đủ để kết luận điều khiển chính xác.

Để giữ bảng chân robot, khi ghép motor Nano phải bỏ log Hardware Serial trên D0/D1. Bạn có thể đo kiểm với sketch cảm biến riêng rồi quay lại sketch motor; không đơn giản thêm Serial vào mã đang điều khiển driver qua hai chân đó.

## Thực hành nâng cao: xem mã ghép hai bên motor

Chỉ mở phần dưới khi các bước đo và kiểm tra bên trên đã đạt. Ví dụ dùng PPR 20, chu vi 0,2042 m và hệ số thử; **thay bằng số đo của bạn trước khi áp dụng**. Nó chạy tiến tối đa 8 giây, dừng nếu một bên không có xung liên tục 2 giây, và giới hạn PWM 0–200. Kd ban đầu bằng 0.

??? info "Mã ghép đầy đủ — dành cho lúc đã hiểu từng khối"
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

    volatile unsigned long xungL = 0, xungR = 0;
    void demL() { xungL++; }
    void demR() { xungR++; }

    void layXung(unsigned long &l, unsigned long &r) {
      noInterrupts();
      l = xungL; r = xungR;
      xungL = 0; xungR = 0;
      interrupts();
    }

    const float PPR = 20.0f;       // hieu chuan voi RISING
    const float CHU_VI = 0.2042f;  // vi du ban kinh 0.0325 m
    const float V_DAT = 0.15f;     // m/s, gia tri thu
    const float KP = 120.0f, KI = 15.0f, KD = 0.0f;
    float iL = 0, iR = 0, eCuL = 0, eCuR = 0;
    unsigned long batDau, moc, matXungL = 0, matXungR = 0;
    bool ketThuc = false;

    int pid(float v, float dt, float &tichPhan, float &eCu) {
      float e = V_DAT - v;
      float ungVien = constrain(tichPhan + e * dt, -1.0f, 1.0f);
      float daoHam = (e - eCu) / dt;
      float u = 100.0f + KP * e + KI * ungVien + KD * daoHam;
      // Khong tich luy them theo huong day dau ra vuot gioi han.
      if (!((u > 200 && e > 0) || (u < 0 && e < 0))) tichPhan = ungVien;
      eCu = e;
      u = 100.0f + KP * e + KI * tichPhan + KD * daoHam;
      return (int)constrain(u, 0.0f, 200.0f);
    }

    void setup() {
      setupMotors();
      pinMode(2, INPUT_PULLUP);
      pinMode(3, INPUT_PULLUP);
      attachInterrupt(digitalPinToInterrupt(2), demL, RISING);
      attachInterrupt(digitalPinToInterrupt(3), demR, RISING);
      batDau = moc = millis();
    }

    void loop() {
      unsigned long now = millis();
      if (ketThuc || now - batDau >= 8000) {
        drive(0, 0);
        ketThuc = true;
        return;
      }
      unsigned long dtMs = now - moc;
      if (dtMs < 200) return;
      moc = now;
      unsigned long l, r;
      layXung(l, r);
      matXungL = l == 0 ? matXungL + dtMs : 0;
      matXungR = r == 0 ? matXungR + dtMs : 0;
      if (matXungL >= 2000 || matXungR >= 2000) {
        drive(0, 0);
        ketThuc = true;
        return;
      }
      float dt = dtMs / 1000.0f;
      float vL = l * CHU_VI / (PPR * dt);
      float vR = r * CHU_VI / (PPR * dt);
      drive(pid(vL, dt, iL, eCuL), pid(vR, dt, iR, eCuR));
    }
    ```

Trong mã ghép, đọc theo thứ tự: setupMotors → hàm đếm encoder → lấy số xung sau 200 ms → đổi thành tốc độ → pid → drive. `noInterrupts()` chỉ bảo vệ đoạn chép số xung. Phần giới hạn tích phân giúp tránh cộng dồn thêm khi PWM đã chạm giới hạn, thường gọi là chống windup.

Không thay các hệ số nguồn bằng một lần đo trên bánh kê rồi coi đã tối ưu cho chạy trên sàn; tải thực tế khác. Không ghép thêm tránh vật cản hoặc dò line ở lượt kiểm tra đầu.

## PID tốc độ khác PID dò line thế nào?

PID tốc độ so **tốc độ đặt và tốc độ đo encoder**. PID dò line so **vị trí đường line và vị trí mong muốn dưới cụm cảm biến**. Một thiết kế có thể dùng vị trí line để tạo tốc độ đặt khác nhau cho hai bên, rồi PID tốc độ thực hiện hai giá trị đó. Đó là bước ghép nâng cao, không phải chỉ đổi tên biến trong sketch mô phỏng.

## Khi nào hoàn thành phần cơ bản?

Bạn tính được sai số, dự đoán chiều sửa PWM và xác nhận bằng sketch mô phỏng. Có thể tiếp tục sử dụng robot dù chưa mở mã ghép nâng cao.

**Bài tập:** tính PWM đề xuất với tốc độ đặt 0,15, tốc độ đo 0,12, Kp 100 và mức cơ sở 120. Kết quả gần 123; giải thích vì sao tăng Kp làm phần sửa lớn hơn. Sau đó thử trên sketch, chưa bật motor.

[Bài trước](09-bluetooth.md) · [Lộ trình](../index.md) · [Sử dụng robot bàn giao](../08-su-dung-robot.md)
