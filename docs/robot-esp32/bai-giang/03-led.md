# Bài 3: Điều khiển LED tích hợp trên ESP32

## 1. Giới thiệu

Trong bài học trước, chúng ta đã tìm hiểu cấu trúc chương trình Arduino, cách sử dụng `setup()`, `loop()` và cách nạp chương trình vào ESP32.

Ở bài học này, chúng ta sẽ thực hành **điều khiển đèn LED tích hợp trên bo ESP32**.

Đây là một trong những bài thực hành cơ bản nhất khi bắt đầu lập trình vi điều khiển. Thông qua việc điều khiển LED bật, tắt và nhấp nháy, chúng ta sẽ tìm hiểu cách sử dụng chân GPIO để xuất tín hiệu Digital.

Trong bài học này, chúng ta sẽ thực hiện:

- Phân biệt LED nguồn và LED có thể điều khiển bằng chương trình.
- Tìm hiểu tín hiệu Digital HIGH và LOW.
- Sử dụng `pinMode()` để cấu hình chân GPIO.
- Sử dụng `digitalWrite()` để điều khiển LED.
- Tạo hiệu ứng LED nhấp nháy bằng `delay()`.
- Thay đổi thời gian sáng và tắt của LED.
- Tìm hiểu một số lỗi thường gặp khi điều khiển LED.

Sau khi hoàn thành, bạn sẽ hiểu cách ESP32 điều khiển tín hiệu đầu ra Digital, làm nền tảng cho các bài học điều khiển động cơ và thiết bị ngoại vi.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Nhận diện LED tích hợp trên bo ESP32.
- Phân biệt LED báo nguồn và LED điều khiển.
- Hiểu chức năng của chân GPIO ở chế độ OUTPUT.
- Sử dụng `pinMode()` và `digitalWrite()`.
- Hiểu ý nghĩa của hai mức logic HIGH và LOW.
- Viết chương trình LED nhấp nháy.
- Thay đổi tốc độ nhấp nháy của LED.
- Biết cách kiểm tra khi LED không hoạt động như mong đợi.

---

## 3. Nguyên lý hoạt động của LED

### 3.1. LED là gì?

LED (*Light Emitting Diode*) là một loại diode có khả năng phát sáng khi có dòng điện chạy qua theo chiều thuận.

LED được sử dụng phổ biến trong các mạch điện tử để:

- Báo trạng thái nguồn điện.
- Báo trạng thái hoạt động.
- Hiển thị tín hiệu điều khiển.
- Thông báo lỗi.
- Kiểm tra hoạt động của chương trình.

Trong bài học này, chúng ta sử dụng LED được tích hợp sẵn trên bo ESP32, không cần chuẩn bị LED rời hoặc điện trở bên ngoài.

### 3.2. Phân biệt LED nguồn và LED điều khiển

Trên một số bo ESP32, có thể có hai loại LED:

| Loại LED | Chức năng |
|---|---|
| LED nguồn (Power LED) | Báo bo mạch đang được cấp nguồn |
| LED điều khiển (User LED) | Có thể bật, tắt bằng chương trình nếu được nối với GPIO |

**LED nguồn** thường sáng khi bo ESP32 được cấp điện qua USB hoặc nguồn phù hợp. Loại LED này không nhất thiết điều khiển được bằng chương trình.

**LED điều khiển** được kết nối với một chân GPIO hoặc mạch điều khiển riêng. Nếu biết đúng chân kết nối, chúng ta có thể sử dụng chương trình để thay đổi trạng thái của LED.

**Lưu ý quan trọng:** Không phải mọi bo ESP32 30P CH340 Type-C đều có LED điều khiển tích hợp. Một số bo chỉ có LED nguồn. Vị trí và GPIO điều khiển LED cũng có thể khác nhau giữa các phiên bản bo.

Vì vậy, trước khi thực hành, cần xác định bo ESP32 đang sử dụng có LED điều khiển hay không.

### 3.3. Chân GPIO là gì?

GPIO (*General Purpose Input/Output*) là chân vào/ra đa mục đích của vi điều khiển.

GPIO có thể được cấu hình để:

- Đọc tín hiệu đầu vào từ cảm biến hoặc nút nhấn.
- Xuất tín hiệu điều khiển LED, driver hoặc thiết bị khác.

Trong bài học này, GPIO được cấu hình ở chế độ **OUTPUT**.

Khi xuất tín hiệu Digital, GPIO thường có hai trạng thái:

| Trạng thái | Ý nghĩa |
|---|---|
| HIGH | Mức logic cao, xấp xỉ 3,3 V |
| LOW | Mức logic thấp, xấp xỉ 0 V |

Đối với LED được mắc theo kiểu active-high, HIGH làm LED sáng và LOW làm LED tắt.

Đối với LED mắc theo kiểu active-low, hành vi có thể ngược lại.

### 3.4. Nguyên lý LED nhấp nháy

Để tạo hiệu ứng nhấp nháy, chương trình cần thực hiện tuần tự:

1. Đưa chân điều khiển LED về trạng thái bật.
2. Chờ một khoảng thời gian.
3. Đưa chân điều khiển LED về trạng thái tắt.
4. Chờ một khoảng thời gian.
5. Lặp lại quá trình.

Ví dụ:

```text
Bật LED
   |
   v
Chờ 500 ms
   |
   v
Tắt LED
   |
   v
Chờ 500 ms
   |
   +------> Lặp lại
```

Nếu LED sáng trong 500 ms và tắt trong 500 ms, một chu kỳ nhấp nháy kéo dài một giây.

---

## 4. Chuẩn bị thiết bị

### 4.1. Thiết bị cần thiết

| STT | Thiết bị | Số lượng |
|---|---|---|
| 1 | ESP32 30P CH340 Type-C có LED điều khiển tích hợp | 1 |
| 2 | Board mở rộng ESP32 30P | 1 |
| 3 | Máy tính đã cài Arduino IDE | 1 |
| 4 | Cáp USB Type-C có truyền dữ liệu | 1 |

Trong bài học này, chúng ta không cần đấu nối thêm LED hoặc điện trở.

Nếu ESP32 đang gắn trên robot, cần tắt nguồn động cơ và kiểm tra các kết nối trước khi nạp chương trình.

### 4.2. Xác định chân điều khiển LED

Đối với nhiều bo ESP32 DevKit sử dụng module ESP32-WROOM-32, LED điều khiển tích hợp thường được nối với **GPIO2**.

Tuy nhiên, đây không phải cấu hình chung cho tất cả các bo ESP32.

Trong ví dụ của bài học, chúng ta sử dụng GPIO2 với điều kiện bo thực tế có LED điều khiển được nối vào chân này.

| Thành phần | GPIO |
|---|---|
| LED tích hợp | GPIO2, nếu bo sử dụng cấu hình này |

**Đặc biệt lưu ý với robot Robovis:** Trong cấu hình điều khiển động cơ của robot, GPIO2 được sử dụng cho L298N. Nếu ESP32 vẫn đang kết nối với driver, việc điều khiển GPIO2 có thể tác động đến tín hiệu điều khiển động cơ.

Vì vậy, bài thực hành LED tích hợp nên được thực hiện khi ESP32 đã được tách khỏi các kết nối điều khiển động cơ của robot, hoặc khi đã xác nhận việc sử dụng GPIO2 không gây xung đột.

Nếu bo chỉ có LED nguồn hoặc LED điều khiển nằm ở GPIO khác, cần điều chỉnh bài thực hành theo sơ đồ phần cứng thực tế.

---

## 5. Các câu lệnh điều khiển LED

### 5.1. Hàm pinMode()

Hàm `pinMode()` được sử dụng để cấu hình chế độ hoạt động của chân GPIO.

Cú pháp:

```cpp
pinMode(pin, mode);
```

Trong đó:

- `pin`: Số chân GPIO.
- `mode`: Chế độ hoạt động.

Một số chế độ thường gặp:

| Chế độ | Chức năng |
|---|---|
| INPUT | Đọc tín hiệu đầu vào |
| OUTPUT | Xuất tín hiệu điều khiển |
| INPUT_PULLUP | Đầu vào sử dụng điện trở kéo lên nội, nếu GPIO hỗ trợ |

Ví dụ:

```cpp
pinMode(2, OUTPUT);
```

Câu lệnh trên cấu hình GPIO2 làm chân đầu ra.

### 5.2. Hàm digitalWrite()

Hàm `digitalWrite()` được sử dụng để xuất tín hiệu Digital ra chân GPIO.

Cú pháp:

```cpp
digitalWrite(pin, value);
```

Trong đó:

- `pin`: Chân GPIO cần điều khiển.
- `value`: HIGH hoặc LOW.

Ví dụ:

```cpp
digitalWrite(2, HIGH);
```

Đưa GPIO2 lên mức logic cao.

```cpp
digitalWrite(2, LOW);
```

Đưa GPIO2 xuống mức logic thấp.

Đối với LED tích hợp mắc theo kiểu active-high, hai trạng thái này tương ứng với bật và tắt LED.

### 5.3. Hàm delay()

Hàm `delay()` tạo khoảng thời gian chờ trong chương trình.

Cú pháp:

```cpp
delay(time);
```

Trong đó `time` là thời gian tính bằng mili giây.

Ví dụ:

```cpp
delay(500);
```

Chờ 500 ms, tương đương 0,5 giây.

```cpp
delay(1000);
```

Chờ 1000 ms, tương đương một giây.

---

## 6. Thực hành điều khiển LED nhấp nháy

### 6.1. Mục tiêu thực hành

Chúng ta sẽ viết chương trình để:

- Bật LED tích hợp trong 0,5 giây.
- Tắt LED trong 0,5 giây.
- Lặp lại liên tục.

### 6.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn **File → New Sketch**.

Lưu chương trình với tên:

```text
ESP32Blink
```

Cấu trúc thư mục:

```text
ESP32Blink/
└── ESP32Blink.ino
```

### 6.3. Chương trình hoàn chỉnh

Chương trình dưới đây áp dụng cho bo có LED điều khiển tích hợp nối với GPIO2 và hoạt động ở mức HIGH.

```cpp
// GPIO dieu khien LED tich hop
const int LED_PIN = 2;

void setup() {
  // Cau hinh GPIO2 la dau ra
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Bat LED
  digitalWrite(LED_PIN, HIGH);
  delay(500);

  // Tat LED
  digitalWrite(LED_PIN, LOW);
  delay(500);
}
```

Chương trình không cần cài đặt thêm thư viện.

---

## 7. Giải thích chương trình

### 7.1. Khai báo chân LED

```cpp
const int LED_PIN = 2;
```

Dòng lệnh khai báo một hằng số tên `LED_PIN` có giá trị bằng 2.

Trong đó:

- `const`: Khai báo hằng số.
- `int`: Kiểu dữ liệu số nguyên.
- `LED_PIN`: Tên hằng số.
- `2`: Số GPIO điều khiển LED.

Việc sử dụng tên `LED_PIN` giúp chương trình dễ đọc hơn.

Nếu bo ESP32 sử dụng một GPIO khác cho LED tích hợp, chúng ta chỉ cần sửa giá trị tương ứng.

### 7.2. Cấu hình chân đầu ra

```cpp
void setup() {
  pinMode(LED_PIN, OUTPUT);
}
```

Hàm `setup()` được thực hiện một lần khi ESP32 khởi động.

Lệnh:

```cpp
pinMode(LED_PIN, OUTPUT);
```

Cấu hình chân điều khiển LED ở chế độ đầu ra.

Sau khi cấu hình, ESP32 có thể xuất tín hiệu HIGH hoặc LOW qua chân này.

### 7.3. Bật LED

```cpp
digitalWrite(LED_PIN, HIGH);
```

Lệnh này đưa chân điều khiển lên mức logic cao.

Đối với LED active-high, LED sẽ sáng.

### 7.4. Giữ LED sáng trong 500 ms

```cpp
delay(500);
```

Chương trình chờ 500 ms trước khi thực hiện lệnh tiếp theo.

Trong khoảng thời gian này, chân GPIO vẫn giữ trạng thái đã được thiết lập.

### 7.5. Tắt LED

```cpp
digitalWrite(LED_PIN, LOW);
```

Lệnh này đưa chân điều khiển về mức logic thấp.

Đối với LED active-high, LED sẽ tắt.

### 7.6. Giữ LED tắt trong 500 ms

```cpp
delay(500);
```

Chương trình tiếp tục chờ 500 ms.

Sau đó, hàm `loop()` được gọi lại và LED tiếp tục bật.

Quá trình này tạo ra hiệu ứng LED nhấp nháy liên tục.

---

## 8. Biên dịch và nạp chương trình

### 8.1. Kiểm tra cấu hình

Trước khi nạp chương trình:

1. Kết nối ESP32 với máy tính bằng cáp USB Type-C.
2. Mở Arduino IDE.
3. Chọn **Tools → Board → ESP32 Dev Module**.
4. Chọn đúng cổng COM trong **Tools → Port**.
5. Kiểm tra ESP32 đã được cấp nguồn.

### 8.2. Biên dịch chương trình

Nhấn **Verify**.

Arduino IDE sẽ kiểm tra và biên dịch chương trình.

Nếu chương trình không có lỗi, quá trình biên dịch sẽ hoàn tất.

### 8.3. Nạp chương trình

Nhấn **Upload**.

Chờ Arduino IDE nạp chương trình vào ESP32.

Sau khi nạp thành công, ESP32 sẽ thực hiện chương trình mới.

### 8.4. Quan sát kết quả

Nếu bo sử dụng LED active-high trên GPIO2, kết quả mong đợi là:

- LED sáng trong 0,5 giây.
- LED tắt trong 0,5 giây.
- Quá trình lặp lại liên tục.

Nếu LED không nhấp nháy, cần kiểm tra xem LED đang quan sát có thực sự là LED điều khiển hay chỉ là LED nguồn.

---

## 9. Thay đổi tốc độ nhấp nháy

### 9.1. LED nhấp nháy nhanh

Thay hai lệnh:

```cpp
delay(500);
```

Thành:

```cpp
delay(200);
```

Khi đó:

- LED sáng trong 200 ms.
- LED tắt trong 200 ms.
- Một chu kỳ kéo dài 400 ms.

LED sẽ nhấp nháy nhanh hơn.

### 9.2. LED nhấp nháy chậm

Thay hai lệnh `delay()` thành:

```cpp
delay(1000);
```

Khi đó:

- LED sáng trong một giây.
- LED tắt trong một giây.
- Một chu kỳ kéo dài hai giây.

LED sẽ nhấp nháy chậm hơn.

### 9.3. Thời gian sáng và tắt khác nhau

Chúng ta cũng có thể thiết lập thời gian sáng và tắt khác nhau.

Ví dụ:

```cpp
const int LED_PIN = 2;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(1000);

  digitalWrite(LED_PIN, LOW);
  delay(200);
}
```

Kết quả:

- LED sáng trong một giây.
- LED tắt trong 0,2 giây.
- Quá trình lặp lại liên tục.

Đây là ví dụ đơn giản về việc tạo tín hiệu điều khiển có thời gian bật và tắt khác nhau.

---

## 10. Các lỗi thường gặp

### 10.1. LED không nhấp nháy

**Nguyên nhân có thể:**

- Bo ESP32 không có LED điều khiển tích hợp.
- LED tích hợp không được nối với GPIO2.
- LED hoạt động theo kiểu active-low.
- Chương trình chưa được nạp thành công.
- Đang quan sát nhầm LED nguồn.

**Cách xử lý:**

1. Kiểm tra đúng loại bo ESP32.
2. Xác định LED điều khiển và GPIO tương ứng.
3. Kiểm tra kết quả Upload.
4. Thử nhấn EN/RESET để khởi động lại.
5. Nếu LED là active-low, thử đảo mức HIGH và LOW trong chương trình.

Không nên thử lần lượt các GPIO ngẫu nhiên khi ESP32 vẫn đang kết nối với driver và các thiết bị của robot.

### 10.2. LED luôn sáng

Nếu LED luôn sáng ngay khi cắm USB, đó có thể là LED báo nguồn.

LED nguồn thường không thay đổi trạng thái theo lệnh `digitalWrite()`.

Cần kiểm tra bo có LED điều khiển riêng hay không.

### 10.3. LED sáng và tắt ngược với chương trình

Một số bo sử dụng LED active-low.

Khi đó:

- LOW có thể làm LED sáng.
- HIGH có thể làm LED tắt.

Nếu xác nhận LED tích hợp là active-low, có thể đảo hai mức điều khiển:

```cpp
digitalWrite(LED_PIN, LOW);   // Bat LED active-low
delay(500);

digitalWrite(LED_PIN, HIGH);  // Tat LED active-low
delay(500);
```

### 10.4. LED không thay đổi tốc độ nhấp nháy

Nguyên nhân có thể là chương trình mới chưa được nạp vào ESP32.

Cách xử lý:

1. Kiểm tra đã thay đổi giá trị `delay()`.
2. Nhấn Verify.
3. Nhấn Upload.
4. Chờ nạp thành công.
5. Quan sát lại LED.

### 10.5. Robot có phản ứng khi thử LED

Nếu ESP32 vẫn đang kết nối với robot, GPIO2 có thể đang được sử dụng để điều khiển L298N.

Khi đó, việc thay đổi mức logic GPIO2 có thể ảnh hưởng đến tín hiệu điều khiển động cơ.

Cần ngắt nguồn động cơ và tách các kết nối có khả năng xung đột trước khi thực hành.

---

## 11. Bài tập thực hành

### Bài tập 1: Thay đổi tốc độ nhấp nháy

Sửa chương trình để:

- LED sáng trong 200 ms.
- LED tắt trong 200 ms.

Nạp chương trình và quan sát kết quả.

### Bài tập 2: Thời gian sáng và tắt khác nhau

Sửa chương trình để:

- LED sáng trong một giây.
- LED tắt trong 200 ms.

Giải thích vì sao LED có thời gian sáng dài hơn thời gian tắt.

### Bài tập 3: Nhấp nháy ba lần

Viết chương trình để LED thực hiện:

1. Sáng 100 ms.
2. Tắt 100 ms.
3. Lặp lại ba lần.
4. Nghỉ một giây.
5. Tiếp tục chu kỳ.

### Bài tập 4: Điều khiển LED bằng biến thời gian

Khai báo hai biến:

```cpp
const int LED_PIN = 2;

int thoiGianSang = 500;
int thoiGianTat = 500;
```

Sử dụng hai biến này thay cho các giá trị trực tiếp trong `delay()`.

Thử thay đổi giá trị biến và quan sát kết quả.

### Bài tập 5: Tìm hiểu millis()

Trong chương trình hiện tại, `delay()` được sử dụng để tạo thời gian chờ.

Hãy tìm hiểu hàm `millis()` và thử viết chương trình LED nhấp nháy mà không sử dụng `delay()`.

Gợi ý: Tham khảo [bài lập trình ESP32 cơ bản](../06-lap-trinh-co-ban.md).

---

## 12. Kiểm tra trước khi bắt đầu bài tiếp theo

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã phân biệt LED nguồn và LED điều khiển.
- [ ] Đã xác định bo ESP32 có LED điều khiển tích hợp.
- [ ] Đã biết GPIO điều khiển LED trên bo đang sử dụng.
- [ ] Đã hiểu chế độ OUTPUT.
- [ ] Đã biết sử dụng `pinMode()`.
- [ ] Đã biết sử dụng `digitalWrite()`.
- [ ] Đã hiểu HIGH và LOW.
- [ ] Đã nạp thành công chương trình LED nhấp nháy.
- [ ] Đã thay đổi được thời gian sáng và tắt của LED.
- [ ] Đã hiểu vì sao không được sử dụng tùy ý GPIO đang kết nối với động cơ robot.

---

## 13. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu cách sử dụng ESP32 để điều khiển LED tích hợp.

Những nội dung quan trọng bao gồm:

- Phân biệt LED báo nguồn và LED điều khiển.
- Tìm hiểu chức năng đầu ra Digital của GPIO.
- Sử dụng `pinMode()` để cấu hình chân OUTPUT.
- Sử dụng `digitalWrite()` để xuất tín hiệu HIGH và LOW.
- Sử dụng `delay()` để tạo thời gian chờ.
- Viết chương trình LED nhấp nháy.
- Thay đổi tốc độ và chu kỳ nhấp nháy.
- Kiểm tra các lỗi thường gặp khi điều khiển LED.

Đây là kiến thức nền tảng để điều khiển các thiết bị ngoại vi bằng ESP32.

Ở bài tiếp theo, chúng ta sẽ tìm hiểu **cách điều khiển động cơ servo SG90 bằng ESP32**, bao gồm nguyên lý hoạt động, kết nối servo với board mở rộng và lập trình điều khiển góc quay.

---

[Bài trước: Hướng dẫn lập trình ESP32](02-lap-trinh.md) · [Lộ trình bài học](../index.md) · [Bài tiếp: Điều khiển Servo](04-servo.md)