# Bài 7: Đọc tín hiệu cảm biến dò line TCRT5000 bằng ESP32

## 1. Giới thiệu

Trong bài học trước, chúng ta đã tìm hiểu cách sử dụng cảm biến siêu âm HC-SR04 để đo khoảng cách và phát hiện vật cản phía trước robot.

Ở bài học này, chúng ta sẽ tìm hiểu **cảm biến dò line TCRT5000**, một loại cảm biến thường được sử dụng trong các robot di chuyển theo vạch kẻ trên mặt sàn.

Cảm biến dò line giúp robot nhận biết sự khác biệt giữa vạch line và nền đường dựa trên khả năng phản xạ ánh sáng hồng ngoại.

Trong bộ xe robot ESP32, chúng ta sử dụng **module dò line gồm 5 mắt cảm biến**, cho phép xác định vị trí tương đối của vạch line so với robot.

Thông qua dữ liệu từ 5 mắt cảm biến, ESP32 có thể nhận biết:

- Line nằm ở giữa robot.
- Line lệch về bên trái.
- Line lệch về bên phải.
- Robot không còn phát hiện được line.
- Nhiều mắt cảm biến cùng phát hiện line, chẳng hạn khi đi qua vạch rộng hoặc giao lộ.

Đây là kiến thức nền tảng để xây dựng chức năng robot tự động di chuyển theo đường line.

Trong bài học này, chúng ta chỉ tập trung **đọc và xử lý tín hiệu cảm biến**, chưa kết hợp điều khiển động cơ.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Hiểu nguyên lý hoạt động của cảm biến phản xạ hồng ngoại TCRT5000.
- Phân biệt cảm biến TCRT5000 riêng lẻ và module dò line 5 mắt.
- Nhận biết các chân tín hiệu của module dò line.
- Kết nối module dò line với board mở rộng ESP32.
- Sử dụng `digitalRead()` để đọc tín hiệu Digital.
- Phân biệt mức HIGH và LOW khi cảm biến gặp line hoặc nền.
- Đọc đồng thời trạng thái của 5 mắt cảm biến.
- Xác định vị trí tương đối của line.
- Tính toán vị trí line bằng phương pháp trọng số.
- Phát hiện trường hợp mất line hoặc nhiều cảm biến cùng phát hiện line.
- Hiểu nguyên tắc sử dụng dữ liệu cảm biến để điều khiển robot trong các bài học tiếp theo.

---

## 3. Tìm hiểu cảm biến dò line TCRT5000

### 3.1. Cảm biến TCRT5000 là gì?

TCRT5000 là cảm biến quang phản xạ sử dụng ánh sáng hồng ngoại để phát hiện vật thể hoặc phân biệt các bề mặt có khả năng phản xạ ánh sáng khác nhau.

Một cảm biến TCRT5000 gồm hai thành phần chính:

- **LED phát hồng ngoại:** Phát ánh sáng hồng ngoại xuống bề mặt cần kiểm tra.
- **Phần tử thu quang:** Nhận ánh sáng hồng ngoại phản xạ trở lại.

Khi đặt cảm biến gần bề mặt, lượng ánh sáng phản xạ nhận được sẽ thay đổi tùy theo màu sắc, vật liệu và khoảng cách.

Ví dụ, với line màu đen trên nền trắng:

- Nền trắng thường phản xạ ánh sáng hồng ngoại mạnh hơn.
- Vạch đen thường hấp thụ nhiều ánh sáng hơn, làm tín hiệu phản xạ yếu đi.

Sự khác biệt này được sử dụng để xác định vị trí vạch line.

### 3.2. Nguyên lý hoạt động

Quá trình phát hiện line diễn ra như sau:

1. LED hồng ngoại phát ánh sáng xuống mặt sàn.
2. Ánh sáng gặp bề mặt và bị phản xạ.
3. Phần tử thu nhận ánh sáng phản xạ.
4. Mạch xử lý trên module xác định trạng thái bề mặt.
5. ESP32 đọc tín hiệu đầu ra để biết cảm biến có phát hiện line hay không.

Sơ đồ nguyên lý:

```text
       Cảm biến TCRT5000
       ┌───────────────┐
       │ Phát      Thu │
       └───┬────────▲──┘
           │        │
           ▼        │
        Ánh sáng    │
        hồng ngoại  │
           │        │
           ▼        │
     ─────────────────────
          Mặt sàn
        Ánh sáng phản xạ
```

Cường độ ánh sáng phản xạ phụ thuộc vào:

- Màu sắc bề mặt.
- Vật liệu bề mặt.
- Khoảng cách giữa cảm biến và mặt sàn.
- Góc đặt cảm biến.
- Ánh sáng môi trường.

Vì vậy, cần kiểm tra và hiệu chỉnh cảm biến theo điều kiện sử dụng thực tế.

### 3.3. Phân biệt cảm biến TCRT5000 và module dò line

TCRT5000 là linh kiện cảm biến quang phản xạ.

Trong khi đó, module dò line thường tích hợp thêm các thành phần điện tử như:

- Mạch xử lý tín hiệu.
- Mạch so sánh ngưỡng.
- LED hiển thị trạng thái.
- Các chân xuất tín hiệu Digital.

Trong bộ xe robot ESP32, chúng ta sử dụng module dò line gồm 5 mắt cảm biến.

Module cung cấp 5 tín hiệu Digital độc lập, tương ứng với vị trí của từng mắt.

Tài liệu tham khảo: [Datasheet TCRT5000 – Vishay](https://www.vishay.com/docs/83760/tcrt5000.pdf).

---

## 4. Module dò line 5 mắt

### 4.1. Cấu tạo

Module dò line 5 mắt gồm 5 cảm biến được bố trí thành một hàng ngang.

Mỗi mắt cảm biến có nhiệm vụ kiểm tra bề mặt ngay phía dưới vị trí của nó.

Trong bài học, chúng ta quy ước thứ tự cảm biến từ trái sang phải theo hướng tiến của robot:

```text
                  PHÍA TRƯỚC ROBOT

    Trái ngoài  Trái trong   Giữa   Phải trong  Phải ngoài
        L2          L1        M         R1          R2
        │           │         │         │           │
        ▼           ▼         ▼         ▼           ▼
       [1]         [2]       [3]       [4]         [5]

                  PHÍA SAU ROBOT
```

Các tên L2, L1, M, R1 và R2 được sử dụng để thuận tiện trong việc đọc và xử lý tín hiệu.

### 4.2. Ý nghĩa của 5 mắt cảm biến

| Cảm biến | Vị trí | Chức năng |
|---|---|---|
| L2 | Trái ngoài | Phát hiện line lệch nhiều về bên trái |
| L1 | Trái trong | Phát hiện line lệch về bên trái |
| M | Giữa | Phát hiện line gần trung tâm robot |
| R1 | Phải trong | Phát hiện line lệch về bên phải |
| R2 | Phải ngoài | Phát hiện line lệch nhiều về bên phải |

Khi robot di chuyển, trạng thái của các mắt sẽ thay đổi theo vị trí của vạch line.

Ví dụ:

- Chỉ M phát hiện line: Line đang ở giữa.
- Chỉ L1 phát hiện line: Line lệch về bên trái.
- Chỉ R1 phát hiện line: Line lệch về bên phải.
- Chỉ L2 phát hiện line: Line lệch nhiều về bên trái.
- Chỉ R2 phát hiện line: Line lệch nhiều về bên phải.

Trong thực tế, nhiều mắt cảm biến có thể cùng phát hiện line tại một thời điểm.

---

## 5. Tín hiệu Digital của cảm biến

### 5.1. Tín hiệu HIGH và LOW

Module dò line xuất tín hiệu Digital với hai trạng thái:

- HIGH: Mức logic cao.
- LOW: Mức logic thấp.

Tuy nhiên, ý nghĩa HIGH và LOW phụ thuộc vào thiết kế mạch của module.

Một số module xuất LOW khi phát hiện line, trong khi những module khác có thể có quy ước ngược lại.

Vì vậy, không nên mặc định tất cả cảm biến TCRT5000 đều có cùng mức logic.

### 5.2. Quy ước trên bộ robot thực hành

Trong chương trình robot ESP32 đang sử dụng, chúng ta quy ước:

| Tín hiệu đọc được | Ý nghĩa |
|---|---|
| LOW (0) | Cảm biến phát hiện line |
| HIGH (1) | Cảm biến không phát hiện line |

Ví dụ:

```cpp
int value = digitalRead(34);
```

Nếu `value == LOW`, chương trình xác định cảm biến đang phát hiện line.

Quy ước này cần được kiểm tra trên module thực tế trước khi sử dụng.

### 5.3. Phân biệt tín hiệu GPIO và trạng thái phát hiện line

Để thuận tiện cho việc xử lý, chúng ta sẽ chuyển tín hiệu Digital thành trạng thái phát hiện line.

Quy ước trong chương trình:

- `1`: Có phát hiện line.
- `0`: Không phát hiện line.

Ví dụ:

```cpp
bool thayLine = (digitalRead(34) == LOW);
```

Khi GPIO34 đọc được LOW:

```text
Tín hiệu GPIO = 0
Trạng thái phát hiện line = 1
```

Khi GPIO34 đọc được HIGH:

```text
Tín hiệu GPIO = 1
Trạng thái phát hiện line = 0
```

Cần phân biệt hai giá trị này để tránh nhầm lẫn khi phân tích kết quả.

---

## 6. Chuẩn bị thiết bị

### 6.1. Thiết bị cần thiết

| STT | Thiết bị | Số lượng |
|---|---|---|
| 1 | ESP32 30P CH340 Type-C | 1 |
| 2 | Board mở rộng ESP32 30P | 1 |
| 3 | Module dò line TCRT5000 5 mắt | 1 |
| 4 | Dây kết nối | Theo nhu cầu |
| 5 | Máy tính đã cài Arduino IDE | 1 |
| 6 | Cáp USB Type-C có truyền dữ liệu | 1 |
| 7 | Mẫu vạch line đen trên nền trắng | 1 |

Trong bài thực hành, chúng ta sử dụng module dò line được lắp trên bộ xe robot.

Không cần sử dụng breadboard hoặc đấu thêm các cảm biến riêng lẻ.

### 6.2. Chuẩn bị bề mặt thử nghiệm

Để kiểm tra cảm biến, cần chuẩn bị:

- Một bề mặt sáng màu, tương đối phẳng.
- Một vạch line màu đen.
- Vạch có chiều rộng phù hợp với khoảng cách giữa các mắt cảm biến.

Có thể sử dụng băng dính đen trên nền trắng hoặc một bản in đường line.

Để kết quả dễ quan sát, nên thử nghiệm trong điều kiện ánh sáng ổn định.

---

## 7. Kết nối module dò line với ESP32

### 7.1. Bảng chân kết nối

Trong cấu hình robot ESP32 đang sử dụng, 5 mắt cảm biến được kết nối như sau:

| Tín hiệu module | GPIO ESP32 | Vị trí |
|---|---|---|
| OUT1 | GPIO34 | Trái ngoài – L2 |
| OUT2 | GPIO32 | Trái trong – L1 |
| OUT3 | GPIO33 | Giữa – M |
| OUT4 | GPIO25 | Phải trong – R1 |
| OUT5 | GPIO27 | Phải ngoài – R2 |
| VCC | Nguồn phù hợp từ board mở rộng | Cấp nguồn cảm biến |
| GND | GND | Mass chung |

Sơ đồ tín hiệu:

```text
MODULE DÒ LINE 5 MẮT          ESP32

OUT1 (L2) ------------------ GPIO34
OUT2 (L1) ------------------ GPIO32
OUT3 (M)  ------------------ GPIO33
OUT4 (R1) ------------------ GPIO25
OUT5 (R2) ------------------ GPIO27

VCC ------------------------ Nguồn phù hợp
GND ------------------------ GND
```

**Lưu ý:** Thứ tự trái/phải được xác định theo hướng tiến của robot. Nếu module được lắp ngược, cần kiểm tra lại vị trí các mắt và dây tín hiệu.

### 7.2. Lưu ý về nguồn cấp và mức logic

ESP32 sử dụng mức logic 3,3 V.

Vì vậy, các tín hiệu Digital đưa vào GPIO của ESP32 phải nằm trong giới hạn điện áp cho phép.

Trong bộ robot thực hành, cần kiểm tra điện áp cấp cho module dò line và mức HIGH thực tế của các chân OUT.

Nếu module được cấp nguồn 3,3 V và hoạt động ổn định, tín hiệu đầu ra có thể được kết nối trực tiếp với GPIO khi đã xác nhận mức điện áp phù hợp.

Nếu module sử dụng nguồn 5 V, không được mặc định các chân OUT đều an toàn cho ESP32. Cần kiểm tra đặc tính đầu ra và sử dụng mạch chuyển mức khi cần thiết.

### 7.3. Lưu ý đối với GPIO34

GPIO34 là chân chỉ hỗ trợ đầu vào.

Vì vậy, chân này phù hợp để đọc tín hiệu Digital từ cảm biến.

Tuy nhiên, GPIO34 không có điện trở kéo lên hoặc kéo xuống nội có thể kích hoạt bằng phần mềm.

Nếu đầu ra module là loại open-collector hoặc open-drain và cần điện trở kéo lên, phải có điện trở kéo lên phù hợp ở phần cứng.

Trong bài học, các chân cảm biến được cấu hình `INPUT`.

### 7.4. Kiểm tra trước khi thực hành

Trước khi nạp chương trình:

1. Kiểm tra nguồn cấp cho module dò line.
2. Kiểm tra GND chung.
3. Kiểm tra đúng các chân GPIO34, 32, 33, 25 và 27.
4. Kiểm tra mức điện áp đầu ra của module.
5. Đảm bảo module được lắp đúng hướng.
6. Ngắt nguồn động cơ để robot không tự di chuyển khi hiệu chỉnh cảm biến.

---

## 8. Đọc tín hiệu Digital bằng ESP32

### 8.1. Hàm digitalRead()

Hàm `digitalRead()` được sử dụng để đọc trạng thái logic tại một chân GPIO.

Cú pháp:

```cpp
digitalRead(pin);
```

Trong đó `pin` là chân GPIO cần đọc.

Giá trị trả về:

- HIGH.
- LOW.

Ví dụ:

```cpp
int value = digitalRead(34);
```

Lệnh trên đọc trạng thái GPIO34.

### 8.2. Cấu hình chân INPUT

Trước khi đọc tín hiệu, cần cấu hình GPIO ở chế độ đầu vào.

Ví dụ:

```cpp
pinMode(34, INPUT);
```

Đối với module dò line 5 mắt, chúng ta cần cấu hình cả 5 GPIO ở chế độ INPUT.

### 8.3. Sử dụng mảng để quản lý cảm biến

Thay vì khai báo riêng từng cảm biến, chúng ta có thể sử dụng mảng:

```cpp
const int SENSOR_PIN[5] = {34, 32, 33, 25, 27};
```

Trong đó:

| Phần tử | GPIO | Vị trí |
|---|---|---|
| `SENSOR_PIN[0]` | 34 | L2 |
| `SENSOR_PIN[1]` | 32 | L1 |
| `SENSOR_PIN[2]` | 33 | M |
| `SENSOR_PIN[3]` | 25 | R1 |
| `SENSOR_PIN[4]` | 27 | R2 |

Sử dụng mảng giúp chương trình dễ mở rộng và xử lý các cảm biến bằng vòng lặp.

---

## 9. Thực hành đọc trạng thái 5 mắt cảm biến

### 9.1. Mục tiêu thực hành

Chúng ta sẽ viết chương trình để:

1. Khởi tạo 5 chân cảm biến.
2. Đọc tín hiệu Digital của từng mắt.
3. Chuyển tín hiệu LOW thành trạng thái phát hiện line.
4. Hiển thị trạng thái của cả 5 mắt trên Serial Monitor.
5. Quan sát sự thay đổi khi di chuyển vạch line qua từng mắt.

### 9.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn **File → New Sketch**.

Lưu chương trình với tên:

```text
ESP32_LineSensor
```

Cấu trúc thư mục:

```text
ESP32_LineSensor/
└── ESP32_LineSensor.ino
```

### 9.3. Chương trình hoàn chỉnh

```cpp
// ================= LINE SENSOR =================

const int SENSOR_PIN[5] = {34, 32, 33, 25, 27};

// ================= SETUP =================

void setup() {

  Serial.begin(115200);

  for (int i = 0; i < 5; i++) {
    pinMode(SENSOR_PIN[i], INPUT);
  }

  Serial.println("Bat dau doc cam bien do line");
}

// ================= LOOP =================

void loop() {

  Serial.print("Line: ");

  for (int i = 0; i < 5; i++) {

    int value = digitalRead(SENSOR_PIN[i]);

    // LOW = phat hien line
    bool thayLine = (value == LOW);

    Serial.print(thayLine ? 1 : 0);
    Serial.print(" ");
  }

  Serial.println();

  delay(100);
}
```

Chương trình không cần cài thêm thư viện ngoài.

### 9.4. Kết quả mong đợi

Mở Serial Monitor ở tốc độ:

```text
115200 baud
```

Khi không có mắt nào phát hiện line:

```text
Line: 0 0 0 0 0
```

Khi mắt giữa phát hiện line:

```text
Line: 0 0 1 0 0
```

Khi mắt trái trong phát hiện line:

```text
Line: 0 1 0 0 0
```

Khi mắt phải ngoài phát hiện line:

```text
Line: 0 0 0 0 1
```

Khi cả 5 mắt đều phát hiện line:

```text
Line: 1 1 1 1 1
```

**Lưu ý:** Các giá trị hiển thị đã được chuyển đổi theo quy ước `1 = phát hiện line`, `0 = không phát hiện line`. Đây không phải giá trị HIGH/LOW gốc đọc trực tiếp từ GPIO.

---

## 10. Xác định vị trí line bằng phương pháp trọng số

### 10.1. Vì sao cần xác định vị trí line?

Việc biết mắt nào phát hiện line mới chỉ cung cấp trạng thái riêng lẻ của từng cảm biến.

Để điều khiển robot di chuyển theo line, chúng ta cần biết line đang lệch về phía nào so với tâm robot.

Ví dụ:

- Line nằm giữa: Robot có thể tiếp tục đi thẳng.
- Line lệch trái: Robot cần điều chỉnh hướng về bên trái.
- Line lệch phải: Robot cần điều chỉnh hướng về bên phải.

Để biểu diễn vị trí line bằng một giá trị số, chúng ta có thể sử dụng phương pháp trọng số.

### 10.2. Gán trọng số cho từng mắt

Gán các trọng số từ trái sang phải:

| Cảm biến | Vị trí | Trọng số |
|---|---|---|
| L2 | Trái ngoài | -2 |
| L1 | Trái trong | -1 |
| M | Giữa | 0 |
| R1 | Phải trong | +1 |
| R2 | Phải ngoài | +2 |

Sơ đồ:

```text
          L2      L1      M      R1      R2
          │       │       │       │       │
         -2      -1       0      +1      +2

       Lệch trái       Giữa       Lệch phải
```

Theo quy ước này:

- Vị trí âm: Line lệch về bên trái.
- Vị trí bằng 0: Line nằm gần trung tâm.
- Vị trí dương: Line lệch về bên phải.

### 10.3. Công thức tính vị trí line

Gọi:

- \(S_i\): Trạng thái phát hiện line của cảm biến thứ \(i\), bằng 0 hoặc 1.
- \(W_i\): Trọng số tương ứng với cảm biến thứ \(i\).

Vị trí line được tính bằng:

\[
P = \frac{\sum_{i=1}^{5} S_i W_i}{\sum_{i=1}^{5} S_i}
\]

Trong đó:

- \(P\): Vị trí line tương đối.
- Tử số: Tổng trọng số của các mắt đang phát hiện line.
- Mẫu số: Số mắt đang phát hiện line.

Công thức chỉ được sử dụng khi có ít nhất một mắt phát hiện line.

Nếu không có mắt nào phát hiện line, mẫu số bằng 0 nên không thể tính vị trí bằng công thức này.

### 10.4. Ví dụ tính vị trí line

**Ví dụ 1: Line ở giữa**

```text
L2 L1 M R1 R2
 0  0 1  0  0
```

Chỉ cảm biến M phát hiện line.

\[
P = \frac{0}{1}=0
\]

Kết quả: Line ở giữa.

**Ví dụ 2: Line lệch trái**

```text
L2 L1 M R1 R2
 0  1 0  0  0
```

Chỉ cảm biến L1 phát hiện line.

\[
P = \frac{-1}{1}=-1
\]

Kết quả: Line lệch về bên trái.

**Ví dụ 3: Line lệch phải**

```text
L2 L1 M R1 R2
 0  0 0  1  0
```

Chỉ cảm biến R1 phát hiện line.

\[
P = \frac{1}{1}=1
\]

Kết quả: Line lệch về bên phải.

**Ví dụ 4: Hai mắt cùng phát hiện line**

```text
L2 L1 M R1 R2
 0  1 1  0  0
```

Hai cảm biến L1 và M cùng phát hiện line.

\[
P = \frac{-1+0}{2}=-0{,}5
\]

Kết quả: Line nằm giữa L1 và M, hơi lệch về bên trái.

**Ví dụ 5: Line lệch nhiều về bên phải**

```text
L2 L1 M R1 R2
 0  0 0  0  1
```

Chỉ cảm biến R2 phát hiện line.

\[
P = \frac{2}{1}=2
\]

Kết quả: Line lệch nhiều về bên phải.

---

## 11. Thực hành tính vị trí line

### 11.1. Mục tiêu

Chúng ta sẽ mở rộng chương trình đọc 5 mắt để:

- Hiển thị trạng thái từng mắt.
- Tính vị trí line theo trọng số.
- Phát hiện trường hợp mất line.
- Phát hiện trường hợp cả 5 mắt cùng thấy line.

### 11.2. Chương trình hoàn chỉnh

```cpp
// ================= LINE SENSOR =================

// Chan ket noi 5 mat cam bien
const int SENSOR_PIN[5] = {34, 32, 33, 25, 27};

// Trong so tu trai sang phai
const int WEIGHT[5] = {-2, -1, 0, 1, 2};

// ================= SETUP =================

void setup() {

  Serial.begin(115200);

  for (int i = 0; i < 5; i++) {
    pinMode(SENSOR_PIN[i], INPUT);
  }

  Serial.println("Bat dau do vi tri line");
}

// ================= LOOP =================

void loop() {

  int tongTrongSo = 0;
  int soMatThayLine = 0;

  Serial.print("Line: ");

  // Doc 5 mat cam bien
  for (int i = 0; i < 5; i++) {

    bool thayLine = (digitalRead(SENSOR_PIN[i]) == LOW);

    Serial.print(thayLine ? 1 : 0);
    Serial.print(" ");

    if (thayLine) {
      tongTrongSo += WEIGHT[i];
      soMatThayLine++;
    }
  }

  // Xu ly trang thai line
  if (soMatThayLine == 0) {

    Serial.println("| Mat line");

  }
  else if (soMatThayLine == 5) {

    Serial.println("| Tat ca cam bien thay line");

  }
  else {

    float viTriLine = (float)tongTrongSo / soMatThayLine;

    Serial.print("| Vi tri line: ");
    Serial.println(viTriLine);
  }

  delay(100);
}
```

### 11.3. Kết quả mong đợi

Khi line nằm ở giữa:

```text
Line: 0 0 1 0 0 | Vi tri line: 0.00
```

Khi line lệch về bên trái:

```text
Line: 0 1 0 0 0 | Vi tri line: -1.00
```

Khi line lệch về bên phải:

```text
Line: 0 0 0 1 0 | Vi tri line: 1.00
```

Khi line nằm giữa hai mắt L1 và M:

```text
Line: 0 1 1 0 0 | Vi tri line: -0.50
```

Khi không có mắt nào phát hiện line:

```text
Line: 0 0 0 0 0 | Mat line
```

Khi cả 5 mắt cùng phát hiện line:

```text
Line: 1 1 1 1 1 | Tat ca cam bien thay line
```

---

## 12. Giải thích chương trình

### 12.1. Khai báo mảng chân cảm biến

```cpp
const int SENSOR_PIN[5] = {34, 32, 33, 25, 27};
```

Mảng `SENSOR_PIN` chứa 5 chân GPIO kết nối với module dò line.

Thứ tự trong mảng tương ứng với thứ tự cảm biến từ trái sang phải.

### 12.2. Khai báo trọng số

```cpp
const int WEIGHT[5] = {-2, -1, 0, 1, 2};
```

Mảng `WEIGHT` chứa trọng số vị trí của từng mắt.

Trọng số âm biểu diễn phía trái, trọng số dương biểu diễn phía phải.

### 12.3. Đọc trạng thái cảm biến

```cpp
bool thayLine = (digitalRead(SENSOR_PIN[i]) == LOW);
```

Câu lệnh trên đọc tín hiệu Digital và kiểm tra xem cảm biến có phát hiện line hay không.

Trong cấu hình robot:

- LOW: Có line.
- HIGH: Không có line.

Kết quả được lưu trong biến `thayLine`.

### 12.4. Tính tổng trọng số

```cpp
if (thayLine) {
  tongTrongSo += WEIGHT[i];
  soMatThayLine++;
}
```

Nếu cảm biến phát hiện line:

1. Cộng trọng số của mắt đó vào tổng.
2. Tăng số lượng mắt phát hiện line.

Ví dụ, nếu L1 và M cùng phát hiện line:

```text
tongTrongSo = -1 + 0 = -1
soMatThayLine = 2
```

### 12.5. Tính vị trí line

```cpp
float viTriLine = (float)tongTrongSo / soMatThayLine;
```

Lệnh trên tính trung bình trọng số của các mắt đang phát hiện line.

Kết quả là một giá trị tương đối nằm trong khoảng từ -2 đến +2 đối với các trường hợp được tính.

Giá trị này không phải khoảng cách thực tế tính bằng centimet.

Nó chỉ biểu diễn vị trí tương đối của line so với dãy cảm biến.

### 12.6. Xử lý mất line

```cpp
if (soMatThayLine == 0) {
  Serial.println("| Mat line");
}
```

Khi không có mắt nào phát hiện line, chương trình thông báo mất line.

Trong trường hợp này, không thể tính vị trí line bằng công thức trung bình trọng số.

Khi kết hợp điều khiển động cơ, cần có phương án xử lý riêng, chẳng hạn dừng robot hoặc tìm lại line theo một chiến lược được thiết kế trước.

### 12.7. Xử lý cả 5 mắt cùng phát hiện line

```cpp
else if (soMatThayLine == 5) {
  Serial.println("| Tat ca cam bien thay line");
}
```

Khi cả 5 mắt đều phát hiện line, robot có thể đang đi qua:

- Vạch line rất rộng.
- Giao lộ.
- Vạch ngang.
- Vùng tối có độ phản xạ tương tự line.

Không nên mặc định đây là trạng thái line nằm giữa và cho robot tiếp tục đi thẳng.

Trong các bài điều khiển nâng cao, trạng thái này cần được xử lý theo yêu cầu của đường chạy.

---

## 13. Phân tích các trạng thái line thường gặp

### 13.1. Bảng trạng thái cơ bản

Quy ước:

- `1`: Cảm biến phát hiện line.
- `0`: Cảm biến không phát hiện line.

| L2 L1 M R1 R2 | Vị trí tính được | Nhận xét |
|---|---|---|
| 0 0 1 0 0 | 0 | Line ở giữa |
| 0 1 0 0 0 | -1 | Line lệch trái |
| 1 0 0 0 0 | -2 | Line lệch nhiều về trái |
| 0 0 0 1 0 | +1 | Line lệch phải |
| 0 0 0 0 1 | +2 | Line lệch nhiều về phải |
| 0 1 1 0 0 | -0,5 | Line giữa L1 và M |
| 0 0 1 1 0 | +0,5 | Line giữa M và R1 |
| 1 1 0 0 0 | -1,5 | Hai mắt trái phát hiện line |
| 0 0 0 1 1 | +1,5 | Hai mắt phải phát hiện line |
| 0 0 0 0 0 | Không xác định | Mất line |
| 1 1 1 1 1 | Xử lý riêng | Tất cả mắt phát hiện line |

### 13.2. Các trạng thái nhiều mắt phát hiện line

Trong thực tế, vạch line có thể rộng hơn khoảng cách giữa các mắt cảm biến.

Khi đó, nhiều mắt có thể cùng phát hiện line.

Ví dụ:

```text
1 1 1 0 0
```

Ba mắt bên trái phát hiện line.

Điều này cho thấy vùng line đang tập trung về phía trái.

Tương tự:

```text
0 0 1 1 1
```

Ba mắt bên phải phát hiện line.

Trong các trường hợp này, phương pháp trọng số vẫn có thể cung cấp một giá trị vị trí tương đối.

Tuy nhiên, không phải mọi tổ hợp nhiều mắt đều biểu diễn một vạch line liên tục.

### 13.3. Các trạng thái bất thường

Ví dụ:

```text
1 0 0 0 1
```

Hai mắt ngoài cùng cùng phát hiện line, trong khi ba mắt giữa không phát hiện.

Nếu tính trung bình trọng số:

\[
P = \frac{-2+2}{2}=0
\]

Kết quả bằng 0, nhưng điều đó không có nghĩa robot đang nằm chính giữa một vạch line đơn.

Trạng thái này có thể xuất hiện khi:

- Có hai vạch line riêng biệt.
- Robot đi qua một khu vực có nhiều đường kẻ.
- Có nhiễu tín hiệu.
- Một hoặc nhiều cảm biến hoạt động không chính xác.

Do đó, **giá trị trung bình trọng số chỉ là một cách ước lượng vị trí, không thể thay thế hoàn toàn việc phân tích tổ hợp trạng thái của 5 mắt cảm biến**.

Đối với robot dò line thực tế, cần kết hợp cả giá trị vị trí và bảng logic trạng thái để xử lý chính xác hơn.

---

## 14. Nguyên tắc điều khiển robot theo vị trí line

Trong bài học này, chúng ta chưa điều khiển động cơ. Tuy nhiên, cần hiểu nguyên tắc sử dụng vị trí line để điều chỉnh hướng robot.

### 14.1. Khi line nằm giữa

Nếu vị trí line gần bằng 0:

```text
Line: 0 0 1 0 0
```

Robot đang ở vị trí tương đối phù hợp với vạch line.

Hướng điều khiển dự kiến: tiếp tục đi thẳng.

### 14.2. Khi line lệch trái

Ví dụ:

```text
Line: 0 1 0 0 0
Vi tri: -1
```

Line đang nằm về phía trái của robot.

Robot cần điều chỉnh hướng sang trái để đưa line trở lại vùng giữa.

### 14.3. Khi line lệch phải

Ví dụ:

```text
Line: 0 0 0 1 0
Vi tri: +1
```

Line đang nằm về phía phải của robot.

Robot cần điều chỉnh hướng sang phải.

### 14.4. Khi mất line

Ví dụ:

```text
Line: 0 0 0 0 0
```

Robot không còn xác định được vị trí line.

Trong trường hợp này, không nên tiếp tục sử dụng giá trị vị trí cũ như một phép đo hiện tại.

Cần có chiến lược xử lý riêng, chẳng hạn:

- Dừng robot.
- Tìm lại line theo hướng đã ghi nhận trước đó.
- Giới hạn thời gian tìm line.
- Chuyển sang trạng thái lỗi nếu không tìm lại được line.

### 14.5. Khi tất cả mắt phát hiện line

Ví dụ:

```text
Line: 1 1 1 1 1
```

Trạng thái này có thể tương ứng với giao lộ hoặc vùng line rộng.

Robot cần có quy tắc xử lý phù hợp với đường chạy.

Không nên mặc định tất cả mắt cùng phát hiện line là robot đang đi đúng giữa đường.

---

## 15. Biên dịch và chạy thử

### 15.1. Kiểm tra trước khi nạp

1. Kiểm tra module dò line đã được kết nối đúng.
2. Kiểm tra nguồn cấp cho cảm biến.
3. Kiểm tra mức điện áp đầu ra phù hợp với ESP32.
4. Kiểm tra đúng thứ tự trái/phải.
5. Ngắt nguồn động cơ.
6. Kết nối ESP32 với máy tính.

### 15.2. Biên dịch chương trình

Trong Arduino IDE:

1. Chọn **ESP32 Dev Module**.
2. Chọn đúng cổng COM.
3. Nhấn **Verify**.
4. Kiểm tra thông báo biên dịch.

### 15.3. Nạp chương trình

Nhấn **Upload**.

Chờ Arduino IDE hoàn tất quá trình nạp.

Sau khi nạp thành công, ESP32 sẽ chạy chương trình mới.

### 15.4. Quan sát trên Serial Monitor

Mở Serial Monitor và chọn:

```text
115200 baud
```

Di chuyển vạch line qua từng mắt cảm biến.

Quan sát sự thay đổi của các giá trị từ trái sang phải.

Kiểm tra:

- L2 có tương ứng với mắt ngoài cùng bên trái không?
- L1 có tương ứng với mắt trái trong không?
- M có tương ứng với mắt giữa không?
- R1 có tương ứng với mắt phải trong không?
- R2 có tương ứng với mắt ngoài cùng bên phải không?

Nếu kết quả ngược với vị trí thực tế, cần kiểm tra hướng lắp module và thứ tự dây kết nối.

---

## 16. Các yếu tố ảnh hưởng đến kết quả dò line

### 16.1. Khoảng cách từ cảm biến đến mặt sàn

TCRT5000 là cảm biến phản xạ ở khoảng cách gần.

Nếu đặt cảm biến quá cao so với mặt sàn, tín hiệu phản xạ có thể yếu.

Nếu đặt quá sát, khả năng phân biệt line và nền cũng có thể bị ảnh hưởng.

Cần điều chỉnh độ cao theo đặc tính của module và kiểm tra thực tế.

### 16.2. Màu sắc và vật liệu bề mặt

Cảm biến hoạt động dựa trên khả năng phản xạ ánh sáng hồng ngoại, không trực tiếp nhận biết màu sắc như camera.

Vì vậy, hai bề mặt có màu nhìn bằng mắt khác nhau vẫn có thể phản xạ hồng ngoại tương tự nhau.

Một số bề mặt bóng cũng có thể làm thay đổi tín hiệu phản xạ theo góc đặt.

### 16.3. Ánh sáng môi trường

Ánh sáng mạnh, đặc biệt các nguồn có thành phần hồng ngoại, có thể ảnh hưởng đến kết quả đọc cảm biến.

Cần hạn chế thay đổi đột ngột điều kiện chiếu sáng trong quá trình hiệu chỉnh.

### 16.4. Ngưỡng so sánh của module

Một số module dò line có biến trở hoặc cơ chế điều chỉnh ngưỡng phát hiện.

Nếu ngưỡng không phù hợp, cảm biến có thể:

- Luôn báo phát hiện line.
- Không phát hiện line.
- Chuyển trạng thái không ổn định.

Cần kiểm tra tín hiệu trên nền và line thực tế để xác định ngưỡng phù hợp.

### 16.5. Rung động khi robot di chuyển

Khi robot di chuyển, khoảng cách từ cảm biến đến mặt sàn có thể thay đổi do rung động.

Điều này có thể làm tín hiệu Digital dao động.

Trong chương trình điều khiển nâng cao, cần xem xét cơ chế lọc tín hiệu và xử lý trạng thái ổn định.

---

## 17. Các lỗi thường gặp

### 17.1. Cảm biến luôn báo có line

**Hiện tượng:**

```text
Line: 1 1 1 1 1
```

Ngay cả khi module được đặt trên nền trắng.

**Nguyên nhân có thể:**

- Ngưỡng so sánh chưa phù hợp.
- Cảm biến đặt quá gần hoặc quá xa mặt sàn.
- Nguồn cấp không ổn định.
- Mức logic phát hiện line bị quy ước ngược.
- Module hoặc một số kênh bị lỗi.

**Cách xử lý:**

1. Kiểm tra mức HIGH/LOW thực tế.
2. Kiểm tra nguồn cấp.
3. Kiểm tra độ cao cảm biến.
4. Điều chỉnh ngưỡng nếu module hỗ trợ.
5. Thử riêng từng mắt trên nền và line.

### 17.2. Cảm biến không phát hiện line

**Hiện tượng:**

```text
Line: 0 0 0 0 0
```

Ngay cả khi đặt line dưới các mắt cảm biến.

**Nguyên nhân có thể:**

- Module chưa được cấp nguồn.
- Dây tín hiệu bị lỏng.
- Khoảng cách cảm biến đến mặt sàn không phù hợp.
- Ngưỡng so sánh chưa đúng.
- Quy ước LOW/HIGH không phù hợp với module.

**Cách xử lý:**

- Kiểm tra nguồn.
- Kiểm tra dây kết nối.
- Kiểm tra từng mắt cảm biến.
- Thử thay đổi độ cao.
- Xác nhận lại mức logic khi gặp line.

### 17.3. Thứ tự trái/phải bị đảo

Nếu đặt line dưới mắt ngoài cùng bên trái nhưng Serial Monitor hiển thị:

```text
Line: 0 0 0 0 1
```

Có thể thứ tự dây hoặc hướng lắp module đang bị đảo.

Cần đối chiếu vị trí vật lý của cảm biến với các chân GPIO trong chương trình.

### 17.4. Kết quả đọc dao động

Ví dụ:

```text
Line: 0 0 1 0 0
Line: 0 1 1 0 0
Line: 0 0 1 0 0
```

Nguyên nhân có thể:

- Line nằm gần ranh giới phát hiện giữa hai mắt.
- Module bị rung.
- Ngưỡng so sánh quá nhạy.
- Ánh sáng môi trường thay đổi.
- Nguồn cấp không ổn định.

Cần kiểm tra điều kiện đo trước khi bổ sung bộ lọc bằng phần mềm.

### 17.5. ESP32 hoạt động không ổn định

Cần kiểm tra:

- Mức điện áp HIGH của module.
- Nguồn cấp.
- GND chung.
- Dây tín hiệu.
- Xung đột GPIO với thiết bị khác.

Đặc biệt, không đưa tín hiệu 5 V trực tiếp vào GPIO của ESP32.

---

## 18. Bài tập thực hành

### Bài tập 1: Đọc trạng thái từng mắt

Đặt vạch line lần lượt dưới:

- L2.
- L1.
- M.
- R1.
- R2.

Ghi lại trạng thái 5 mắt tương ứng.

### Bài tập 2: Kiểm tra mức logic

Viết chương trình in trực tiếp giá trị `digitalRead()` của từng mắt.

So sánh kết quả khi đặt cảm biến trên:

- Nền trắng.
- Line đen.

Xác nhận module đang sử dụng có đúng quy ước LOW là phát hiện line hay không.

### Bài tập 3: Tính vị trí line

Tính thủ công vị trí line cho các trạng thái sau:

```text
0 1 0 0 0
0 1 1 0 0
0 0 1 1 0
0 0 0 1 1
1 1 0 0 0
```

So sánh kết quả với giá trị chương trình hiển thị.

### Bài tập 4: Phân loại vị trí line

Viết chương trình phân loại:

- Vị trí âm: `Line lech trai`.
- Vị trí dương: `Line lech phai`.
- Vị trí bằng 0 với mẫu hợp lệ: `Line o giua`.
- Không có mắt phát hiện: `Mat line`.
- Cả 5 mắt phát hiện: `Vung line rong`.

Lưu ý: Với các mẫu không liên tục hoặc bất thường, giá trị vị trí bằng 0 chưa đủ để kết luận line nằm giữa.

### Bài tập 5: Xử lý các trạng thái đặc biệt

Phân tích các trạng thái:

```text
0 0 0 0 0
1 1 1 1 1
1 0 0 0 1
1 1 1 0 0
0 0 1 1 1
```

Trả lời:

1. Trạng thái nào không thể tính vị trí bằng công thức trung bình?
2. Trạng thái nào có thể là giao lộ hoặc vùng line rộng?
3. Trạng thái nào có nhiều vùng phát hiện không liên tục?
4. Vì sao không nên sử dụng duy nhất giá trị trung bình trọng số để quyết định hướng di chuyển?

### Bài tập 6: Đề xuất logic điều khiển robot

Giả sử robot sử dụng hai động cơ DC điều khiển qua L298N.

Hãy đề xuất nguyên tắc điều khiển:

- Line ở giữa: Robot đi thẳng.
- Line lệch trái: Robot điều chỉnh hướng sang trái.
- Line lệch phải: Robot điều chỉnh hướng sang phải.
- Mất line: Robot chuyển sang trạng thái xử lý mất line.
- Nhiều mắt cùng phát hiện: Phân tích tổ hợp cảm biến trước khi quyết định.

Trong bài này, chỉ cần mô tả logic, chưa cấp nguồn cho động cơ.

---

## 19. Kiểm tra trước khi bắt đầu bài tiếp theo

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã hiểu nguyên lý hoạt động của TCRT5000.
- [ ] Đã phân biệt cảm biến TCRT5000 và module dò line 5 mắt.
- [ ] Đã biết chức năng của 5 mắt cảm biến.
- [ ] Đã biết cách kết nối module với ESP32.
- [ ] Đã kiểm tra mức điện áp tín hiệu phù hợp với ESP32.
- [ ] Đã biết sử dụng `digitalRead()`.
- [ ] Đã xác nhận mức logic khi cảm biến gặp line.
- [ ] Đã đọc được trạng thái của cả 5 mắt.
- [ ] Đã hiểu phương pháp tính vị trí line bằng trọng số.
- [ ] Đã phân biệt vị trí line âm, dương và bằng 0.
- [ ] Đã biết xử lý trường hợp mất line.
- [ ] Đã hiểu vì sao trạng thái nhiều mắt phát hiện line cần được phân tích riêng.
- [ ] Đã biết nguyên tắc sử dụng vị trí line để điều chỉnh hướng robot.

---

## 20. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu cách sử dụng module cảm biến dò line TCRT5000 gồm 5 mắt với ESP32.

Những nội dung quan trọng bao gồm:

- Hiểu nguyên lý phản xạ ánh sáng hồng ngoại.
- Tìm hiểu chức năng của module dò line 5 mắt.
- Kết nối cảm biến với ESP32 theo sơ đồ chân của robot.
- Sử dụng `digitalRead()` để đọc tín hiệu Digital.
- Chuyển đổi mức logic thành trạng thái phát hiện line.
- Hiển thị trạng thái 5 mắt trên Serial Monitor.
- Sử dụng trọng số để tính vị trí tương đối của line.
- Xác định line lệch trái, lệch phải hoặc nằm giữa.
- Phát hiện trường hợp mất line và vùng line rộng.
- Hiểu giới hạn của phương pháp trung bình trọng số.
- Nắm được nguyên tắc sử dụng dữ liệu cảm biến để điều khiển robot dò line.

Đây là kiến thức nền tảng để phát triển chức năng robot di chuyển theo vạch line.

Ở bài tiếp theo, chúng ta sẽ tìm hiểu **cảm biến Encoder**, cách đọc xung từ bánh xe và sử dụng dữ liệu Encoder để xác định tốc độ quay của động cơ.

---

[Bài trước: Cảm biến siêu âm HC-SR04](06-hc-sr04.md) · [Lộ trình bài học](../index.md) · [Bài tiếp: Đọc Encoder](08-encoder.md)