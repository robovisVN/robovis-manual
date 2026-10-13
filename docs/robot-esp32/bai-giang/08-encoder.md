# Bài 8: Đọc cảm biến Encoder và đo tốc độ bánh xe bằng ESP32

## 1. Giới thiệu

Trong các bài học trước, chúng ta đã tìm hiểu cách điều khiển động cơ DC bằng module L298N, đọc cảm biến siêu âm HC-SR04 và sử dụng cảm biến TCRT5000 để xác định vị trí vạch line.

Tuy nhiên, khi điều khiển động cơ bằng PWM, chúng ta mới chỉ điều chỉnh mức công suất cấp cho động cơ, chưa biết chính xác bánh xe đang quay với tốc độ bao nhiêu.

Ví dụ, khi cấp cùng một giá trị PWM cho hai động cơ, tốc độ thực tế của hai bánh có thể khác nhau do:

- Đặc tính của từng động cơ.
- Ma sát và tải trọng.
- Độ lệch cơ khí.
- Điện áp nguồn.
- Điều kiện tiếp xúc giữa bánh xe và mặt sàn.

Để đo tốc độ quay thực tế, chúng ta sử dụng **cảm biến Encoder**.

Encoder tạo ra các xung điện khi trục hoặc bánh xe quay. Bằng cách đếm số xung trong một khoảng thời gian xác định, ESP32 có thể tính được tốc độ quay của bánh xe.

Trong bài học này, chúng ta sẽ sử dụng **hai cảm biến Encoder, một cho bánh trái và một cho bánh phải**, kết nối với ESP32 thông qua GPIO26 và GPIO22.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Hiểu Encoder là gì và nguyên lý hoạt động của Encoder quang.
- Phân biệt Encoder một kênh và Encoder hai kênh.
- Hiểu ý nghĩa của xung Encoder.
- Kết nối Encoder với board mở rộng ESP32.
- Sử dụng ngắt ngoài để đếm xung.
- Hiểu vai trò của `volatile` và hàm xử lý ngắt.
- Đọc và đặt lại bộ đếm xung an toàn.
- Xác định số xung trên một vòng quay (PPR).
- Tính tốc độ quay theo đơn vị RPM.
- Tính tốc độ tuyến tính của bánh xe theo đơn vị m/s.
- Đo tốc độ bánh trái và bánh phải độc lập.
- Hiểu các yếu tố ảnh hưởng đến độ chính xác của phép đo.

---

## 3. Tìm hiểu cảm biến Encoder

### 3.1. Encoder là gì?

Encoder là cảm biến dùng để xác định chuyển động quay hoặc chuyển động tuyến tính thông qua các tín hiệu điện.

Trong robot sử dụng động cơ DC, Encoder thường được gắn vào trục động cơ hoặc bánh xe để theo dõi chuyển động quay.

Khi trục quay, Encoder tạo ra các xung Digital. ESP32 có thể đếm các xung này để xác định số vòng quay và tốc độ.

Ví dụ:

- Bánh xe quay chậm: Số xung trong một giây ít.
- Bánh xe quay nhanh: Số xung trong một giây nhiều.
- Bánh xe đứng yên: Không có xung mới, nếu cảm biến hoạt động bình thường.

Encoder được sử dụng trong nhiều ứng dụng như robot tự hành, robot dò line, điều khiển tốc độ động cơ, đo quãng đường và hệ thống điều khiển PID.

### 3.2. Nguyên lý hoạt động của Encoder quang

Encoder quang thường sử dụng một đĩa có các khe hoặc vùng chắn sáng.

Đĩa được gắn với trục quay. Một bộ phát và thu ánh sáng được đặt hai phía của đĩa.

Khi đĩa quay:

1. Khe trên đĩa đi qua cảm biến, ánh sáng có thể truyền tới bộ thu.
2. Phần chắn sáng đi qua, tín hiệu tại bộ thu thay đổi.
3. Mạch Encoder chuyển sự thay đổi này thành tín hiệu Digital.
4. ESP32 đếm các lần chuyển trạng thái để xác định chuyển động quay.

Sơ đồ nguyên lý:

```text
          Đĩa Encoder quay
                 ↻
           ┌──────────┐
           │ Khe chắn │
           │ ánh sáng │
           └──────────┘
                 │
      LED phát → │ → Bộ thu
                 │
                 ▼
          Tín hiệu Digital
                 │
                 ▼
                ESP32
```

Tín hiệu đầu ra thường có dạng xung vuông:

```text
HIGH  ────┐    ┌────┐    ┌────┐
          │    │    │    │    │
LOW       └────┘    └────┘    └───

        Thời gian →
```

Khi trục quay nhanh hơn, các xung xuất hiện với tần suất cao hơn.

### 3.3. Encoder một kênh và hai kênh

Có hai cấu hình thường gặp.

**Encoder một kênh**

Chỉ cung cấp một tín hiệu xung, thường ký hiệu D0, OUT hoặc A.

ESP32 có thể đếm xung để xác định:

- Số vòng quay tương đối.
- Tốc độ quay.

Tuy nhiên, chỉ từ một kênh xung, ESP32 không thể tự xác định chiều quay.

**Encoder hai kênh**

Có hai tín hiệu A và B lệch pha nhau.

Bằng cách so sánh thứ tự chuyển trạng thái giữa A và B, bộ điều khiển có thể xác định cả số xung và chiều quay.

Trong bộ robot thực hành, chúng ta sử dụng **một tín hiệu D0 cho mỗi bánh xe**, nên bài học chỉ tập trung đo số xung và độ lớn tốc độ.

### 3.4. Phân biệt tốc độ quay và tốc độ tuyến tính

Tốc độ quay cho biết bánh xe quay bao nhiêu vòng trong một đơn vị thời gian.

Đơn vị thường sử dụng là RPM (*Revolutions Per Minute*), nghĩa là vòng/phút.

Tốc độ tuyến tính cho biết quãng đường mà bánh xe lăn được trong một giây, giả sử bánh lăn không trượt.

Đơn vị thường sử dụng là m/s.

Hai đại lượng này có liên hệ với nhau thông qua chu vi bánh xe.

---

## 4. Xung Encoder và PPR

### 4.1. PPR là gì?

PPR là viết tắt của *Pulses Per Revolution*, nghĩa là số xung trên một vòng quay.

Ví dụ, nếu Encoder tạo ra 20 xung khi bánh xe quay đúng một vòng, chúng ta có:

```text
PPR = 20
```

Khi đếm được 40 xung, bánh xe đã quay tương đương khoảng 2 vòng.

Khi đếm được 100 xung, bánh xe đã quay tương đương khoảng 5 vòng.

Tuy nhiên, số xung trên một vòng phụ thuộc vào cấu tạo Encoder và phương pháp đếm.

### 4.2. Phân biệt RISING, FALLING và CHANGE

Một tín hiệu Digital có hai loại sườn:

- **RISING:** Chuyển từ LOW sang HIGH.
- **FALLING:** Chuyển từ HIGH sang LOW.

Trong Arduino, chúng ta có thể lựa chọn chế độ đếm:

| Chế độ | Ý nghĩa |
|---|---|
| RISING | Đếm khi tín hiệu chuyển LOW → HIGH |
| FALLING | Đếm khi tín hiệu chuyển HIGH → LOW |
| CHANGE | Đếm khi tín hiệu thay đổi ở cả hai sườn |

Ví dụ, nếu tín hiệu tạo ra 20 chu kỳ xung trên một vòng:

- Đếm RISING: Khoảng 20 lần.
- Đếm FALLING: Khoảng 20 lần.
- Đếm CHANGE: Khoảng 40 lần.

Do đó, **PPR phải tương ứng với đúng phương pháp đếm được sử dụng trong chương trình**.

Trong bài học này, chúng ta sử dụng chế độ `RISING`.

### 4.3. Phân biệt vòng quay trục động cơ và vòng quay bánh xe

Đây là điểm quan trọng đối với robot sử dụng động cơ có hộp giảm tốc.

Nếu Encoder được gắn ở trục động cơ trước hộp giảm tốc, số xung trên một vòng bánh xe sẽ lớn hơn số xung trên một vòng trục động cơ.

Ví dụ:

- Encoder tạo 20 xung trên một vòng trục động cơ.
- Hộp giảm tốc có tỷ số truyền 1:30.

Khi đó, số xung lý thuyết trên một vòng bánh xe là:

\[
PPR_{bánh}=20\times30=600
\]

Nếu Encoder được gắn trực tiếp trên trục bánh xe thì không cần nhân tỷ số truyền.

Vì vậy, khi đo tốc độ bánh xe, chúng ta phải sử dụng **PPR tương ứng với một vòng quay thực tế của bánh**, không mặc định PPR của trục động cơ.

---

## 5. Chuẩn bị thiết bị

### 5.1. Thiết bị cần thiết

| STT | Thiết bị | Số lượng |
|---|---|---|
| 1 | ESP32 30P CH340 Type-C | 1 |
| 2 | Board mở rộng ESP32 30P | 1 |
| 3 | Cảm biến Encoder | 2 |
| 4 | Đĩa Encoder hoặc cơ cấu Encoder gắn trên bánh | 2 |
| 5 | Bánh xe và động cơ DC | 2 bộ |
| 6 | Dây kết nối | Theo nhu cầu |
| 7 | Máy tính cài Arduino IDE | 1 |
| 8 | Cáp USB Type-C có truyền dữ liệu | 1 |

### 5.2. Chuẩn bị trước khi thực hành

Trước khi đo:

1. Đảm bảo Encoder đã được lắp đúng vị trí.
2. Kiểm tra đĩa Encoder không chạm vào đầu cảm biến.
3. Kiểm tra dây tín hiệu.
4. Kê bánh xe khỏi mặt sàn.
5. Ngắt nguồn động cơ.
6. Chuẩn bị quay bánh xe bằng tay để kiểm tra xung.

Trong bài học này, chúng ta chưa cần cấp nguồn để động cơ tự quay.

---

## 6. Kết nối Encoder với ESP32

### 6.1. Bảng chân kết nối

Trong cấu hình robot ESP32 đang sử dụng:

| Encoder | ESP32 | Chức năng |
|---|---|---|
| D0 Encoder trái | GPIO26 | Đọc xung bánh trái |
| D0 Encoder phải | GPIO22 | Đọc xung bánh phải |
| VCC | Nguồn phù hợp với module | Cấp nguồn Encoder |
| GND | GND | Mass chung |

Sơ đồ kết nối:

```text
ENCODER TRÁI                  ESP32

D0 ------------------------- GPIO26
VCC ------------------------ Nguồn phù hợp
GND ------------------------ GND


ENCODER PHẢI                  ESP32

D0 ------------------------- GPIO22
VCC ------------------------ Nguồn phù hợp
GND ------------------------ GND
```

### 6.2. Lưu ý về điện áp

ESP32 sử dụng mức logic 3,3 V.

Vì vậy, tín hiệu D0 của Encoder phải có mức điện áp phù hợp với GPIO ESP32.

Nếu module Encoder được cấp nguồn 3,3 V và hoạt động ổn định, tín hiệu D0 có thể kết nối trực tiếp sau khi xác nhận mức điện áp.

Nếu module được cấp nguồn 5 V, cần kiểm tra mức HIGH của D0. Không được đưa tín hiệu 5 V trực tiếp vào GPIO ESP32.

Tùy thiết kế đầu ra, module có thể cần mạch chuyển mức hoặc điện trở kéo lên phù hợp.

### 6.3. Lưu ý về INPUT_PULLUP

Trong chương trình, chúng ta sử dụng:

```cpp
pinMode(26, INPUT_PULLUP);
pinMode(22, INPUT_PULLUP);
```

Lệnh này kích hoạt điện trở kéo lên nội của ESP32.

Điện trở kéo lên giúp giữ tín hiệu ở mức HIGH khi đầu ra cảm biến không chủ động kéo tín hiệu xuống LOW.

Tuy nhiên, việc sử dụng `INPUT_PULLUP` phải phù hợp với loại đầu ra Encoder. Nếu module có đầu ra push-pull và đã có mức logic ổn định, có thể sử dụng `INPUT`.

Không sử dụng điện trở kéo lên 5 V cho tín hiệu nối trực tiếp với ESP32.

---

## 7. Tại sao cần sử dụng ngắt?

### 7.1. Đọc tín hiệu bằng vòng lặp

Một cách đơn giản để đọc Encoder là liên tục gọi:

```cpp
digitalRead(26);
```

Tuy nhiên, phương pháp này có hạn chế.

Nếu ESP32 đang thực hiện các công việc khác như:

- Đọc cảm biến siêu âm.
- Xử lý cảm biến dò line.
- Điều khiển động cơ.
- Giao tiếp Wi-Fi.
- Hiển thị dữ liệu Serial.

Chương trình có thể không đọc Encoder kịp thời.

Khi đó, một số xung có thể bị bỏ qua.

### 7.2. Ngắt ngoài là gì?

Ngắt ngoài (*External Interrupt*) cho phép ESP32 thực hiện một hàm xử lý khi tín hiệu tại GPIO xuất hiện sự kiện đã cấu hình.

Ví dụ:

```cpp
attachInterrupt(
  digitalPinToInterrupt(26),
  demXungTrai,
  RISING
);
```

Khi GPIO26 xuất hiện sườn RISING, ESP32 gọi hàm `demXungTrai()` để xử lý.

Nhờ đó, chương trình không cần liên tục kiểm tra trạng thái Encoder trong `loop()`.

### 7.3. Hàm xử lý ngắt ISR

ISR là viết tắt của *Interrupt Service Routine*.

Đây là hàm được gọi khi có sự kiện ngắt.

Ví dụ:

```cpp
volatile unsigned long xungTrai = 0;

void ARDUINO_ISR_ATTR demXungTrai() {
  xungTrai++;
}
```

Mỗi lần xuất hiện sự kiện ngắt, biến `xungTrai` tăng thêm 1.

Trên ESP32, ISR cần được viết ngắn gọn và hạn chế tối đa thời gian xử lý.

Không nên thực hiện các công việc như:

- In Serial.
- Sử dụng `delay()`.
- Tính toán phức tạp.
- Thực hiện các thao tác có thể chờ lâu.

Trong bài học này, ISR chỉ thực hiện việc tăng bộ đếm xung.

---

## 8. Biến volatile và đọc dữ liệu an toàn

### 8.1. Tại sao sử dụng volatile?

Bộ đếm xung được thay đổi bên trong ISR nhưng lại được đọc trong `loop()`.

Ví dụ:

```cpp
volatile unsigned long xungTrai = 0;
```

Từ khóa `volatile` thông báo cho trình biên dịch rằng giá trị biến có thể thay đổi ngoài luồng thực thi thông thường.

Điều này giúp tránh một số tối ưu hóa không phù hợp khi đọc biến.

Tuy nhiên, **`volatile` không tự bảo đảm mọi thao tác đọc, ghi hoặc đặt lại bộ đếm đều an toàn khi có ngắt xảy ra đồng thời**.

### 8.2. Vấn đề khi đọc và đặt lại bộ đếm

Giả sử chương trình thực hiện:

```cpp
unsigned long soXung = xungTrai;
xungTrai = 0;
```

Nếu một xung mới xuất hiện giữa hai lệnh, dữ liệu có thể bị mất khi bộ đếm bị đặt lại.

Để tránh tình huống này, chúng ta sử dụng vùng bảo vệ (*critical section*).

### 8.3. Critical section trên ESP32

ESP32 cung cấp cơ chế khóa để bảo vệ dữ liệu dùng chung giữa ISR và chương trình chính.

Khai báo:

```cpp
portMUX_TYPE khoaXung = portMUX_INITIALIZER_UNLOCKED;
```

Trong ISR:

```cpp
portENTER_CRITICAL_ISR(&khoaXung);

// Thao tác với bộ đếm

portEXIT_CRITICAL_ISR(&khoaXung);
```

Trong chương trình chính:

```cpp
portENTER_CRITICAL(&khoaXung);

// Đọc và đặt lại bộ đếm

portEXIT_CRITICAL(&khoaXung);
```

Việc sử dụng cùng một khóa giúp thao tác đọc và đặt lại bộ đếm được thực hiện nhất quán.

Vùng bảo vệ cần ngắn gọn, chỉ chứa những thao tác thực sự cần thiết.

---

## 9. Thực hành đếm xung Encoder

### 9.1. Mục tiêu

Chương trình đầu tiên sẽ:

1. Khởi tạo hai chân Encoder.
2. Cấu hình ngắt RISING.
3. Đếm xung bánh trái và bánh phải.
4. Đọc số xung mỗi giây.
5. Hiển thị kết quả trên Serial Monitor.

### 9.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn **File → New Sketch**.

Lưu chương trình với tên:

```text
ESP32_Encoder
```

Cấu trúc:

```text
ESP32_Encoder/
└── ESP32_Encoder.ino
```

### 9.3. Chương trình hoàn chỉnh

```cpp
// ================= ENCODER =================

const int ENC_L = 26;
const int ENC_R = 22;

// Bo dem xung
volatile unsigned long xungL = 0;
volatile unsigned long xungR = 0;

// Khoa bao ve du lieu
portMUX_TYPE khoaXung = portMUX_INITIALIZER_UNLOCKED;

// ================= INTERRUPT =================

void ARDUINO_ISR_ATTR demXungL() {

  portENTER_CRITICAL_ISR(&khoaXung);

  xungL++;

  portEXIT_CRITICAL_ISR(&khoaXung);
}

void ARDUINO_ISR_ATTR demXungR() {

  portENTER_CRITICAL_ISR(&khoaXung);

  xungR++;

  portEXIT_CRITICAL_ISR(&khoaXung);
}

// ================= DOC XUNG =================

void laySoXung(unsigned long &left,
              unsigned long &right) {

  portENTER_CRITICAL(&khoaXung);

  left = xungL;
  right = xungR;

  xungL = 0;
  xungR = 0;

  portEXIT_CRITICAL(&khoaXung);
}

// ================= TIME =================

unsigned long mocThoiGian = 0;

// ================= SETUP =================

void setup() {

  Serial.begin(115200);

  pinMode(ENC_L, INPUT_PULLUP);
  pinMode(ENC_R, INPUT_PULLUP);

  attachInterrupt(
    digitalPinToInterrupt(ENC_L),
    demXungL,
    RISING
  );

  attachInterrupt(
    digitalPinToInterrupt(ENC_R),
    demXungR,
    RISING
  );

  mocThoiGian = millis();

  Serial.println("Bat dau doc Encoder");
}

// ================= LOOP =================

void loop() {

  unsigned long now = millis();

  if (now - mocThoiGian >= 1000) {

    mocThoiGian = now;

    unsigned long left;
    unsigned long right;

    laySoXung(left, right);

    Serial.print("Encoder L: ");
    Serial.print(left);

    Serial.print(" | Encoder R: ");
    Serial.println(right);
  }
}
```

### 9.4. Chạy thử

Sau khi nạp chương trình:

1. Mở Serial Monitor.
2. Chọn tốc độ 115200 baud.
3. Quay bánh trái bằng tay.
4. Quan sát số xung Encoder trái.
5. Quay bánh phải bằng tay.
6. Quan sát số xung Encoder phải.

Ví dụ:

```text
Bat dau doc Encoder

Encoder L: 0 | Encoder R: 0
Encoder L: 8 | Encoder R: 0
Encoder L: 12 | Encoder R: 0
Encoder L: 0 | Encoder R: 15
Encoder L: 0 | Encoder R: 10
```

Các giá trị chỉ mang tính minh họa.

Nếu quay riêng bánh trái, bộ đếm Encoder phải không nên tăng do chuyển động của bánh trái.

Nếu hai bộ đếm bị đảo, cần kiểm tra lại GPIO26 và GPIO22.

---

## 10. Tính tốc độ quay RPM

### 10.1. Công thức tính tốc độ

Giả sử:

- \(N\): Số xung đo được.
- \(PPR\): Số xung trên một vòng bánh.
- \(T\): Thời gian đo, tính bằng giây.

Số vòng quay trong khoảng thời gian đo:

\[
n = \frac{N}{PPR}
\]

Tốc độ quay theo vòng/phút:

\[
RPM = \frac{N\times60}{PPR\times T}
\]

Ví dụ:

- Số xung đo được: 20.
- PPR: 20.
- Thời gian đo: 1 giây.

Khi đó:

\[
RPM=\frac{20\times60}{20\times1}=60
\]

Kết quả: Bánh xe quay với tốc độ trung bình 60 vòng/phút trong khoảng đo.

### 10.2. Lưu ý về PPR

Trong chương trình ví dụ, chúng ta tạm sử dụng:

```cpp
const float PPR = 20.0f;
```

Đây chỉ là giá trị giả định để minh họa phép tính.

Trước khi sử dụng kết quả tốc độ, cần xác định PPR thực tế của bộ Encoder đang lắp trên robot.

Nếu PPR không đúng, kết quả RPM sẽ sai theo cùng tỷ lệ.

---

## 11. Thực hành đo tốc độ hai bánh xe

### 11.1. Mục tiêu

Chương trình sẽ:

- Đếm xung hai Encoder bằng ngắt.
- Đọc và đặt lại bộ đếm theo từng khoảng thời gian.
- Tính RPM của bánh trái.
- Tính RPM của bánh phải.
- Hiển thị kết quả trên Serial Monitor.

### 11.2. Chương trình hoàn chỉnh

```cpp
// ================= ENCODER =================

const int ENC_L = 26;
const int ENC_R = 22;

// PPR tam thoi - can hieu chuan thuc te
const float PPR = 20.0f;

// Chu ky do (ms)
const unsigned long SAMPLE_TIME = 1000;

// Bo dem xung
volatile unsigned long xungL = 0;
volatile unsigned long xungR = 0;

// Khoa bao ve
portMUX_TYPE khoaXung = portMUX_INITIALIZER_UNLOCKED;

// ================= INTERRUPT =================

void ARDUINO_ISR_ATTR demXungL() {

  portENTER_CRITICAL_ISR(&khoaXung);
  xungL++;
  portEXIT_CRITICAL_ISR(&khoaXung);
}

void ARDUINO_ISR_ATTR demXungR() {

  portENTER_CRITICAL_ISR(&khoaXung);
  xungR++;
  portEXIT_CRITICAL_ISR(&khoaXung);
}

// ================= DOC BO DEM =================

void laySoXung(unsigned long &left,
              unsigned long &right) {

  portENTER_CRITICAL(&khoaXung);

  left = xungL;
  right = xungR;

  xungL = 0;
  xungR = 0;

  portEXIT_CRITICAL(&khoaXung);
}

// ================= TIME =================

unsigned long mocThoiGian = 0;

// ================= SETUP =================

void setup() {

  Serial.begin(115200);

  pinMode(ENC_L, INPUT_PULLUP);
  pinMode(ENC_R, INPUT_PULLUP);

  attachInterrupt(
    digitalPinToInterrupt(ENC_L),
    demXungL,
    RISING
  );

  attachInterrupt(
    digitalPinToInterrupt(ENC_R),
    demXungR,
    RISING
  );

  mocThoiGian = millis();

  Serial.println("Bat dau do toc do banh xe");
}

// ================= LOOP =================

void loop() {

  unsigned long now = millis();
  unsigned long dt = now - mocThoiGian;

  if (dt >= SAMPLE_TIME) {

    mocThoiGian = now;

    unsigned long left;
    unsigned long right;

    laySoXung(left, right);

    // Doi thoi gian sang giay
    float thoiGian = dt / 1000.0f;

    // Tinh RPM
    float rpmL = left * 60.0f / (PPR * thoiGian);
    float rpmR = right * 60.0f / (PPR * thoiGian);

    // Hien thi
    Serial.print("L: ");
    Serial.print(left);
    Serial.print(" xung | ");
    Serial.print(rpmL);
    Serial.print(" RPM");

    Serial.print(" || R: ");
    Serial.print(right);
    Serial.print(" xung | ");
    Serial.print(rpmR);
    Serial.println(" RPM");
  }
}
```

### 11.3. Giải thích chương trình

**Khai báo chân Encoder**

```cpp
const int ENC_L = 26;
const int ENC_R = 22;
```

GPIO26 nhận xung bánh trái, GPIO22 nhận xung bánh phải.

**Khai báo PPR**

```cpp
const float PPR = 20.0f;
```

Giá trị này dùng để chuyển số xung thành số vòng quay.

**Khai báo thời gian đo**

```cpp
const unsigned long SAMPLE_TIME = 1000;
```

Chương trình đo tốc độ theo cửa sổ thời gian khoảng 1 giây.

**Đếm xung bằng ngắt**

```cpp
attachInterrupt(
  digitalPinToInterrupt(ENC_L),
  demXungL,
  RISING
);
```

Mỗi sườn RISING tại GPIO26 sẽ kích hoạt hàm `demXungL()`.

Encoder phải được xử lý tương tự.

**Đọc bộ đếm**

```cpp
laySoXung(left, right);
```

Hàm này đọc số xung hai bánh và đặt lại bộ đếm để chuẩn bị cho khoảng đo tiếp theo.

**Tính thời gian thực tế**

```cpp
float thoiGian = dt / 1000.0f;
```

Đổi thời gian từ mili giây sang giây.

**Tính tốc độ**

```cpp
float rpmL = left * 60.0f / (PPR * thoiGian);
float rpmR = right * 60.0f / (PPR * thoiGian);
```

Kết quả là tốc độ quay trung bình trong khoảng đo.

### 11.4. Kết quả mong đợi

Ví dụ, với PPR = 20 và thời gian đo 1 giây:

```text
L: 20 xung | 60.00 RPM || R: 20 xung | 60.00 RPM
```

Nếu bánh trái quay nhanh hơn bánh phải:

```text
L: 30 xung | 90.00 RPM || R: 20 xung | 60.00 RPM
```

Nếu hai bánh đứng yên:

```text
L: 0 xung | 0.00 RPM || R: 0 xung | 0.00 RPM
```

Các kết quả trên giả định PPR đã được xác định đúng.

---

## 12. Tính tốc độ tuyến tính của bánh xe

### 12.1. Chu vi bánh xe

Để chuyển tốc độ quay thành tốc độ tuyến tính, cần biết đường kính bánh xe.

Gọi:

- \(D\): Đường kính bánh xe, tính bằng mét.
- \(C\): Chu vi bánh xe, tính bằng mét.

Công thức:

\[
C=\pi D
\]

Ví dụ, bánh xe có đường kính 65 mm:

\[
D=0{,}065\text{ m}
\]

Chu vi bánh xe:

\[
C=\pi\times0{,}065\approx0{,}2042\text{ m}
\]

Như vậy, khi bánh xe quay một vòng và lăn không trượt, quãng đường di chuyển xấp xỉ 0,2042 m.

### 12.2. Công thức tính tốc độ tuyến tính

Từ số xung Encoder:

\[
v=\frac{N\times C}{PPR\times T}
\]

Trong đó:

- \(v\): Tốc độ tuyến tính, đơn vị m/s.
- \(N\): Số xung trong khoảng đo.
- \(C\): Chu vi bánh xe, đơn vị m.
- \(PPR\): Số xung trên một vòng bánh.
- \(T\): Thời gian đo, đơn vị giây.

Hoặc từ RPM:

\[
v=\frac{RPM\times C}{60}
\]

### 12.3. Ví dụ tính toán

Giả sử:

- Đường kính bánh xe: 65 mm.
- PPR: 20.
- Số xung trong một giây: 20.

Tốc độ quay:

\[
RPM=60
\]

Chu vi bánh:

\[
C\approx0{,}2042\text{ m}
\]

Tốc độ tuyến tính:

\[
v=\frac{60\times0{,}2042}{60}
\]

\[
v\approx0{,}2042\text{ m/s}
\]

Kết quả: Tốc độ tuyến tính tương ứng khoảng 0,204 m/s, nếu bánh lăn không trượt.

### 12.4. Bổ sung tốc độ tuyến tính vào chương trình

Trong chương trình đo RPM, khai báo thêm:

```cpp
const float WHEEL_DIAMETER = 0.065f;
```

Giá trị 0,065 m chỉ là ví dụ. Cần thay bằng đường kính bánh xe thực tế.

Sau khi tính RPM, bổ sung:

```cpp
const float PI_VALUE = 3.14159265f;

float chuViBanh = PI_VALUE * WHEEL_DIAMETER;

float speedL = left * chuViBanh / (PPR * thoiGian);
float speedR = right * chuViBanh / (PPR * thoiGian);
```

Hiển thị:

```cpp
Serial.print("Speed L: ");
Serial.print(speedL);
Serial.print(" m/s");

Serial.print(" | Speed R: ");
Serial.print(speedR);
Serial.println(" m/s");
```

Ví dụ:

```text
Speed L: 0.204 m/s | Speed R: 0.204 m/s
```

**Lưu ý:** Đây là tốc độ suy ra từ chuyển động quay của bánh. Nếu bánh bị trượt trên mặt sàn, tốc độ di chuyển thực tế của robot có thể khác.

---

## 13. Hiệu chuẩn PPR thực tế

### 13.1. Tại sao cần hiệu chuẩn?

Không phải mọi Encoder đều có cùng số xung trên một vòng quay.

PPR phụ thuộc vào:

- Số khe trên đĩa Encoder.
- Vị trí lắp Encoder.
- Tỷ số truyền của hộp giảm tốc.
- Chế độ đếm RISING, FALLING hoặc CHANGE.

Vì vậy, cần xác định PPR thực tế trước khi sử dụng kết quả RPM hoặc tốc độ tuyến tính.

### 13.2. Phương pháp hiệu chuẩn bằng tay

Thực hiện như sau:

1. Ngắt nguồn động cơ.
2. Đánh dấu một vị trí trên bánh xe.
3. Đưa bánh về vị trí mốc.
4. Đặt lại bộ đếm xung.
5. Quay bánh đúng một vòng.
6. Ghi lại tổng số xung Encoder.
7. Lặp lại nhiều lần để kiểm tra.

Nếu bánh quay chậm và phép đo kéo dài qua nhiều cửa sổ thời gian, cần cộng số xung của tất cả các cửa sổ.

Một cách thuận tiện hơn là sử dụng bộ đếm tích lũy không đặt lại sau mỗi giây trong quá trình hiệu chuẩn.

### 13.3. Ví dụ hiệu chuẩn

Giả sử sau khi quay đúng một vòng bánh, thu được:

```text
Lần 1: 20 xung
Lần 2: 20 xung
Lần 3: 20 xung
```

Có thể xác định:

```cpp
const float PPR = 20.0f;
```

Nếu số xung thực tế là 600 thì phải sử dụng:

```cpp
const float PPR = 600.0f;
```

Không sử dụng giá trị PPR = 20 chỉ vì chương trình ví dụ đang khai báo như vậy.

### 13.4. Hiệu chuẩn riêng hai bánh

Nếu hai Encoder hoặc cơ cấu truyền động khác nhau, PPR của hai bánh có thể không giống nhau.

Khi đó, nên khai báo riêng:

```cpp
const float PPR_L = 20.0f;
const float PPR_R = 20.0f;
```

Sau khi hiệu chuẩn, thay bằng giá trị thực tế của từng bánh.

---

## 14. Ảnh hưởng của chu kỳ đo

### 14.1. Chu kỳ đo 1 giây

Khi sử dụng:

```cpp
const unsigned long SAMPLE_TIME = 1000;
```

Chương trình cập nhật tốc độ khoảng một lần mỗi giây.

Ưu điểm:

- Số xung trong mỗi khoảng đo thường nhiều hơn.
- Sai số lượng tử do đếm xung ít ảnh hưởng hơn.
- Kết quả dễ quan sát.

Nhược điểm:

- Tốc độ cập nhật chậm.
- Khó theo dõi thay đổi tốc độ nhanh.

### 14.2. Chu kỳ đo 200 ms

Nếu thay bằng:

```cpp
const unsigned long SAMPLE_TIME = 200;
```

Chương trình cập nhật khoảng 5 lần mỗi giây.

Ưu điểm:

- Phát hiện thay đổi tốc độ nhanh hơn.
- Phù hợp hơn với các hệ thống cần phản hồi nhanh.

Nhược điểm:

- Số xung trong mỗi cửa sổ đo ít hơn.
- Kết quả có thể dao động rõ hơn ở tốc độ thấp.

### 14.3. Ví dụ so sánh

Giả sử bánh xe quay ở tốc độ 60 RPM và PPR = 20.

Trong 1 giây:

```text
Số xung ≈ 20
```

Trong 0,2 giây:

```text
Số xung ≈ 4
```

Nếu phép đo 0,2 giây chênh lệch chỉ một xung, tốc độ tính toán đã thay đổi đáng kể.

Do đó, cần lựa chọn chu kỳ đo phù hợp với tốc độ bánh xe, độ phân giải Encoder và yêu cầu điều khiển.

---

## 15. Những giới hạn của Encoder một kênh

### 15.1. Không tự xác định chiều quay

Với một tín hiệu D0, chương trình chỉ đếm số xung.

Nếu quay bánh tiến hoặc quay bánh lùi, bộ đếm vẫn tăng.

Vì vậy, tốc độ RPM tính được là **độ lớn tốc độ quay**, không có dấu biểu thị chiều quay.

Trong chương trình điều khiển robot, có thể kết hợp trạng thái lệnh động cơ để ước lượng chiều quay, nhưng đó không phải phép đo chiều quay độc lập từ Encoder.

### 15.2. Không đo trực tiếp vận tốc thực tế của robot

Encoder đo chuyển động quay.

Nếu bánh xe bị trượt, số vòng quay không còn tương ứng chính xác với quãng đường robot di chuyển.

Ví dụ, bánh xe quay khi robot bị kẹt vẫn có thể tạo ra xung Encoder.

Do đó, quãng đường suy ra từ Encoder là quãng đường ước lượng theo chuyển động quay của bánh.

### 15.3. Độ chính xác phụ thuộc PPR

Nếu PPR khai báo sai, toàn bộ kết quả tốc độ sẽ sai.

Ví dụ, PPR thực tế là 40 nhưng chương trình sử dụng 20, tốc độ tính toán sẽ lớn gấp đôi giá trị đúng.

Vì vậy, hiệu chuẩn PPR là bước bắt buộc khi cần đo tốc độ chính xác.

---

## 16. Các lỗi thường gặp

### 16.1. Bánh quay nhưng không có xung

**Hiện tượng:**

```text
Encoder L: 0 | Encoder R: 0
```

Dù bánh xe đang quay.

**Nguyên nhân có thể:**

- Encoder chưa được cấp nguồn.
- Dây D0 bị lỏng.
- Chân GPIO khai báo sai.
- Đĩa Encoder không nằm đúng vị trí đầu đọc.
- Khoảng cách giữa đĩa và cảm biến không phù hợp.
- Tín hiệu đầu ra không thay đổi.
- Chế độ ngắt không phù hợp với tín hiệu thực tế.

**Cách xử lý:**

1. Kiểm tra VCC và GND.
2. Kiểm tra GPIO26 và GPIO22.
3. Kiểm tra vị trí đĩa Encoder.
4. Quan sát tín hiệu đầu ra khi quay bánh.
5. Kiểm tra mức HIGH/LOW bằng đồng hồ hoặc thiết bị đo phù hợp.

### 16.2. Encoder tăng xung khi bánh đứng yên

Nguyên nhân có thể:

- Tín hiệu D0 bị nhiễu.
- Dây tín hiệu không ổn định.
- Điện trở kéo lên không phù hợp.
- Nguồn cấp bị nhiễu.
- Cảm biến nằm sát ngưỡng chuyển trạng thái.

Cần kiểm tra nguyên nhân phần cứng trước khi bổ sung cơ chế lọc xung bằng phần mềm.

Không nên tùy tiện bỏ các xung có khoảng cách thời gian ngắn vì có thể làm mất xung hợp lệ khi bánh quay nhanh.

### 16.3. Tốc độ tính toán cao gấp đôi

Nguyên nhân thường gặp là PPR không nhất quán với chế độ đếm.

Ví dụ:

- PPR được hiệu chuẩn với RISING.
- Chương trình chuyển sang CHANGE.
- PPR vẫn giữ nguyên.

Khi đó, số xung đếm được có thể tăng gần gấp đôi.

Cần hiệu chuẩn lại PPR theo chế độ đếm đang sử dụng.

### 16.4. Chỉ một Encoder hoạt động

Nếu chỉ Encoder trái có xung:

- Kiểm tra nguồn Encoder phải.
- Kiểm tra GPIO22.
- Kiểm tra dây D0.
- Kiểm tra đĩa Encoder phải.

Nếu chỉ Encoder phải có xung, thực hiện kiểm tra tương tự với GPIO26.

### 16.5. Tốc độ dao động nhiều

Nguyên nhân có thể:

- Chu kỳ đo quá ngắn.
- PPR thấp.
- Bánh quay không đều.
- Có nhiễu xung.
- Động cơ thay đổi tốc độ thực tế.

Có thể thử tăng chu kỳ đo để quan sát xu hướng tốc độ rõ hơn.

Trong các bài nâng cao, có thể áp dụng bộ lọc hoặc phương pháp đo thời gian giữa các xung.

### 16.6. ESP32 hoạt động không ổn định

Cần kiểm tra:

- Điện áp nguồn.
- Mức logic đầu ra Encoder.
- GND chung.
- Nhiễu từ động cơ.
- Dây kết nối.
- Các GPIO đang được sử dụng.

Không đưa tín hiệu 5 V trực tiếp vào GPIO ESP32.

---

## 17. Bài tập thực hành

### Bài tập 1: Đếm xung hai bánh

Nạp chương trình đếm xung.

Thực hiện:

1. Quay riêng bánh trái.
2. Quay riêng bánh phải.
3. Quay đồng thời hai bánh.
4. Quan sát số xung tương ứng.

Giải thích kết quả thu được.

### Bài tập 2: Hiệu chuẩn PPR

Đánh dấu vị trí trên bánh xe.

Quay đúng một vòng và đếm tổng số xung.

Thực hiện ít nhất ba lần.

Ghi kết quả:

| Lần đo | Encoder trái | Encoder phải |
|---|---|---|
| 1 | … | … |
| 2 | … | … |
| 3 | … | … |
| Trung bình | … | … |

Xác định PPR cho từng bánh.

### Bài tập 3: Tính RPM

Giả sử:

- PPR = 20.
- Thời gian đo = 1 giây.
- Encoder trái đếm được 30 xung.
- Encoder phải đếm được 25 xung.

Hãy tính RPM của từng bánh.

### Bài tập 4: Tính tốc độ tuyến tính

Đo đường kính bánh xe thực tế.

Bổ sung vào chương trình:

```cpp
const float WHEEL_DIAMETER = 0.065f;
```

Thay 0,065 bằng đường kính bánh thực tế, tính bằng mét.

Tính và hiển thị tốc độ tuyến tính của hai bánh.

### Bài tập 5: Thay đổi chu kỳ đo

Thử hai giá trị:

```cpp
const unsigned long SAMPLE_TIME = 1000;
```

Và:

```cpp
const unsigned long SAMPLE_TIME = 200;
```

So sánh:

- Tần suất cập nhật.
- Mức dao động kết quả.
- Khả năng theo dõi thay đổi tốc độ.

Giải thích vì sao chu kỳ đo ngắn có thể làm kết quả dao động rõ hơn.

### Bài tập 6: Tìm hiểu chiều quay

Quay bánh xe theo chiều tiến và chiều lùi.

Quan sát số xung Encoder.

Trả lời:

1. Bộ đếm có tăng trong cả hai chiều không?
2. Vì sao Encoder một kênh không tự xác định được chiều quay?
3. Muốn đo chiều quay trực tiếp, cần loại Encoder nào?

### Bài tập 7: Ứng dụng trong điều khiển robot

Giả sử hai bánh xe được cấp cùng PWM nhưng Encoder cho kết quả:

```text
Left:  80 RPM
Right: 95 RPM
```

Hãy trả lời:

1. Hai bánh có đang quay cùng tốc độ không?
2. Vì sao cấp cùng PWM nhưng tốc độ khác nhau?
3. Nếu muốn hai bánh quay cùng tốc độ, cần sử dụng thông tin Encoder như thế nào?

Đây là cơ sở để tìm hiểu điều khiển phản hồi và PID trong các bài tiếp theo.

---

## 18. Kiểm tra trước khi bắt đầu bài tiếp theo

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã hiểu Encoder là gì.
- [ ] Đã hiểu nguyên lý hoạt động của Encoder quang.
- [ ] Đã phân biệt Encoder một kênh và hai kênh.
- [ ] Đã biết cách kết nối hai Encoder với ESP32.
- [ ] Đã kiểm tra mức điện áp tín hiệu an toàn cho ESP32.
- [ ] Đã hiểu RISING, FALLING và CHANGE.
- [ ] Đã biết sử dụng `attachInterrupt()`.
- [ ] Đã hiểu vai trò của ISR.
- [ ] Đã hiểu ý nghĩa của `volatile`.
- [ ] Đã biết đọc và đặt lại bộ đếm bằng critical section.
- [ ] Đã đếm được xung bánh trái và bánh phải.
- [ ] Đã biết xác định PPR thực tế.
- [ ] Đã tính được RPM.
- [ ] Đã tính được tốc độ tuyến tính.
- [ ] Đã hiểu ảnh hưởng của chu kỳ đo.
- [ ] Đã biết giới hạn của Encoder một kênh.

---

## 19. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu cách sử dụng cảm biến Encoder để đo tốc độ quay của bánh xe bằng ESP32.

Những nội dung quan trọng bao gồm:

- Nguyên lý tạo xung của Encoder quang.
- Sự khác biệt giữa Encoder một kênh và hai kênh.
- Cách kết nối Encoder với GPIO26 và GPIO22.
- Đếm xung bằng ngắt ngoài.
- Sử dụng `volatile` và critical section để bảo vệ bộ đếm.
- Hiệu chuẩn PPR theo một vòng quay thực tế của bánh xe.
- Tính tốc độ quay theo RPM.
- Tính tốc độ tuyến tính theo m/s.
- Đo tốc độ độc lập cho hai bánh.
- Hiểu các nguyên nhân gây sai số khi đo tốc độ.

Encoder đóng vai trò quan trọng trong các hệ thống robot di động vì cung cấp thông tin phản hồi về chuyển động thực tế của bánh xe.

Ở các bài học nâng cao, dữ liệu Encoder sẽ được kết hợp với điều khiển động cơ và thuật toán PID để giúp robot duy trì tốc độ ổn định, giảm sai lệch giữa hai bánh và cải thiện khả năng di chuyển theo đường line.

Ở bài tiếp theo, chúng ta sẽ tìm hiểu **cách sử dụng Wi-Fi trên ESP32 để điều khiển robot thông qua giao diện web**.

---

[Bài trước: Cảm biến dò line TCRT5000](07-do-line.md) · [Lộ trình bài học](../index.md) · [Bài tiếp: Điều khiển robot qua Wi-Fi](09-wifi.md)