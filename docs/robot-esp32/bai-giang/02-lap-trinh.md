# Bài 2: Hướng dẫn lập trình xe ESP32 CH340 Type-C

## 1. Giới thiệu

Trong các bài học trước, chúng ta đã tìm hiểu về bo mạch ESP32, chuẩn bị phần cứng và cài đặt môi trường lập trình Arduino IDE.

Ở bài học này, chúng ta sẽ bắt đầu viết và nạp chương trình cho **ESP32 30P CH340 Type-C** bằng Arduino IDE.

Trước khi lập trình các chức năng của robot như điều khiển động cơ, đọc cảm biến hoặc kết nối Wi-Fi, chúng ta cần hiểu cách một chương trình Arduino hoạt động và cách nạp chương trình từ máy tính vào ESP32.

Trong bài học này, chúng ta sẽ thực hiện:

- Làm quen với cấu trúc chương trình Arduino.
- Tìm hiểu hai hàm `setup()` và `loop()`.
- Tìm hiểu các câu lệnh cơ bản trong lập trình.
- Phân biệt Verify và Upload.
- Tạo và lưu một chương trình mới.
- Chọn đúng bo ESP32 và cổng COM.
- Nạp chương trình vào ESP32.
- Sử dụng Serial Monitor để quan sát kết quả.
- Tìm hiểu cách phát hiện và xử lý lỗi chương trình.

Sau khi hoàn thành, bạn sẽ có thể tự viết, biên dịch và nạp một chương trình đơn giản vào ESP32.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Hiểu cấu trúc cơ bản của một chương trình Arduino.
- Phân biệt chức năng của `setup()` và `loop()`.
- Biết cách khai báo và sử dụng biến.
- Sử dụng các câu lệnh cơ bản như `if`, `delay()` và `Serial.println()`.
- Phân biệt Verify và Upload.
- Tạo, lưu và mở chương trình trong Arduino IDE.
- Chọn đúng **ESP32 Dev Module** và cổng COM.
- Sử dụng Serial Monitor để theo dõi dữ liệu.
- Nhận biết và xử lý một số lỗi lập trình thường gặp.

---

## 3. Nguyên lý hoạt động của chương trình Arduino

### 3.1. Chương trình Arduino là gì?

Chương trình Arduino, còn gọi là *Sketch*, là tập hợp các câu lệnh được viết để điều khiển hoạt động của vi điều khiển.

Ví dụ, một chương trình có thể yêu cầu ESP32:

- Bật hoặc tắt một đèn LED.
- Điều khiển động cơ quay tiến hoặc lùi.
- Đọc dữ liệu từ cảm biến.
- Đo khoảng cách đến vật cản.
- Gửi dữ liệu về máy tính.
- Nhận lệnh điều khiển qua Wi-Fi.

Chương trình được viết trên máy tính bằng Arduino IDE.

Sau khi hoàn thành, chương trình được biên dịch và nạp vào bộ nhớ Flash của ESP32.

Khi ESP32 khởi động, nó sẽ thực hiện chương trình đã được nạp.

### 3.2. Cấu trúc cơ bản của chương trình

Một chương trình Arduino thông thường có cấu trúc:

```cpp
void setup() {

}

void loop() {

}
```

Đây là hai hàm quan trọng nhất trong chương trình Arduino.

**Hàm `setup()`**

Hàm `setup()` được thực hiện một lần khi chương trình bắt đầu chạy.

Hàm này thường được sử dụng để:

- Cấu hình các chân GPIO.
- Khởi tạo giao tiếp Serial.
- Khởi tạo cảm biến.
- Thiết lập kết nối Wi-Fi.
- Cấu hình các thiết bị ngoại vi.

Ví dụ:

```cpp
void setup() {
  Serial.begin(115200);
}
```

Dòng lệnh trên khởi tạo giao tiếp Serial với tốc độ 115200 baud.

**Hàm `loop()`**

Sau khi `setup()` hoàn thành, ESP32 sẽ liên tục thực hiện hàm `loop()`.

Ví dụ:

```cpp
void loop() {
  Serial.println("Hello ESP32");
  delay(1000);
}
```

Chương trình sẽ:

1. Gửi dòng chữ `Hello ESP32`.
2. Chờ 1000 ms.
3. Quay lại đầu hàm `loop()`.
4. Tiếp tục lặp lại.

Nhờ cơ chế này, ESP32 có thể liên tục đọc cảm biến và điều khiển robot trong quá trình hoạt động.

### 3.3. Luồng thực hiện chương trình

```text
Cấp nguồn hoặc Reset ESP32
            |
            v
       Khởi động
            |
            v
        setup()
            |
            v
         loop()
            |
            v
      Thực hiện lệnh
            |
            v
      Quay lại loop()
            |
            +----------------+
                             |
                             v
                           loop()
```

Trong điều kiện hoạt động bình thường, `setup()` chỉ được thực hiện một lần trong mỗi lần khởi động chương trình, còn `loop()` được gọi lặp lại liên tục.

---

## 4. Các kiến thức lập trình cơ bản

### 4.1. Câu lệnh và dấu chấm phẩy

Trong Arduino, nhiều câu lệnh được kết thúc bằng dấu chấm phẩy `;`.

Ví dụ:

```cpp
int speed = 100;
Serial.begin(115200);
delay(1000);
```

Nếu quên dấu `;`, chương trình có thể không biên dịch được.

Ví dụ sai:

```cpp
int speed = 100
```

Ví dụ đúng:

```cpp
int speed = 100;
```

Không phải mọi dòng đều cần dấu chấm phẩy. Ví dụ, phần khai báo hàm `setup()` hoặc `loop()` không có dấu `;` sau dấu ngoặc nhọn đóng.

### 4.2. Biến trong chương trình

Biến được sử dụng để lưu trữ dữ liệu trong quá trình chương trình hoạt động.

Ví dụ:

```cpp
int tocDo = 100;
```

Trong đó:

- `int`: Kiểu dữ liệu số nguyên.
- `tocDo`: Tên biến.
- `100`: Giá trị ban đầu.

Chúng ta có thể thay đổi giá trị biến:

```cpp
tocDo = 150;
```

Một số kiểu dữ liệu thường gặp:

| Kiểu dữ liệu | Chức năng | Ví dụ |
|---|---|---|
| `int` | Lưu số nguyên | `int tocDo = 100;` |
| `float` | Lưu số thực | `float khoangCach = 25.5;` |
| `bool` | Lưu giá trị đúng hoặc sai | `bool coVatCan = false;` |
| `char` | Lưu một ký tự | `char kyTu = 'A';` |
| `unsigned long` | Lưu số nguyên không âm với phạm vi lớn | `unsigned long soLan = 0;` |

Trong các bài học điều khiển robot, biến thường được sử dụng để lưu:

- Tốc độ động cơ.
- Giá trị cảm biến.
- Khoảng cách đến vật cản.
- Số xung Encoder.
- Trạng thái hoạt động của robot.
- Thời gian thực hiện chương trình.

### 4.3. Hằng số

Hằng số được sử dụng khi một giá trị không cần thay đổi trong quá trình chương trình chạy.

Ví dụ:

```cpp
const int LED_PIN = 23;
```

Trong đó:

- `const`: Khai báo giá trị không được thay đổi thông qua biến.
- `int`: Kiểu số nguyên.
- `LED_PIN`: Tên hằng số.
- `23`: Giá trị GPIO được sử dụng.

Việc khai báo hằng số giúp chương trình dễ đọc và dễ chỉnh sửa.

### 4.4. Câu lệnh điều kiện if

Câu lệnh `if` cho phép chương trình thực hiện một hành động khi điều kiện được thỏa mãn.

Cấu trúc:

```cpp
if (dieuKien) {
  // Cac lenh khi dieu kien dung
}
```

Ví dụ:

```cpp
int khoangCach = 15;

if (khoangCach < 20) {
  Serial.println("Phat hien vat can");
}
```

Trong ví dụ trên, nếu khoảng cách nhỏ hơn 20, ESP32 sẽ gửi thông báo phát hiện vật cản.

Đây là nguyên lý cơ bản được sử dụng trong các chương trình robot tránh vật cản.

**Lưu ý:** Toán tử `==` được sử dụng để so sánh bằng nhau, còn `=` được sử dụng để gán giá trị.

Ví dụ:

```cpp
if (soLan == 5) {
  Serial.println("Da lap 5 lan");
}
```

### 4.5. Chú thích trong chương trình

Chú thích được sử dụng để giải thích ý nghĩa của các đoạn mã.

Chú thích một dòng bắt đầu bằng `//`.

Ví dụ:

```cpp
// Khoi tao giao tiep Serial
Serial.begin(115200);
```

Chú thích nhiều dòng sử dụng:

```cpp
/*
  Chuong trinh dieu khien robot
  Su dung ESP32
*/
```

Các nội dung chú thích không được thực hiện như câu lệnh chương trình.

### 4.6. Phân biệt chữ hoa và chữ thường

Ngôn ngữ C/C++ phân biệt chữ hoa và chữ thường.

Ví dụ:

```cpp
Serial.begin(115200);
```

Là câu lệnh hợp lệ.

Trong khi:

```cpp
serial.begin(115200);
```

Sẽ gây lỗi nếu không có đối tượng nào tên `serial` được khai báo.

Tương tự, `setup()` và `Setup()` là hai tên khác nhau.

---

## 5. Làm quen với Verify và Upload

### 5.1. Verify là gì?

Verify là thao tác kiểm tra và biên dịch chương trình.

Khi nhấn Verify, Arduino IDE sẽ:

1. Kiểm tra cú pháp chương trình.
2. Tìm các thư viện được sử dụng.
3. Biên dịch chương trình cho bo mạch đã chọn.
4. Hiển thị kết quả biên dịch.

Nếu chương trình có lỗi cú pháp hoặc thiếu thư viện, Arduino IDE sẽ hiển thị thông báo lỗi.

**Verify không nạp chương trình vào ESP32.**

Vì vậy, sau khi Verify thành công, ESP32 vẫn tiếp tục chạy chương trình đã được nạp trước đó.

### 5.2. Upload là gì?

Upload là thao tác biên dịch và nạp chương trình vào ESP32.

Khi nhấn Upload, Arduino IDE sẽ:

1. Biên dịch chương trình.
2. Kết nối với ESP32 qua cổng Serial.
3. Đưa ESP32 vào chế độ nạp chương trình.
4. Ghi chương trình vào bộ nhớ Flash.
5. Hoàn tất quá trình nạp.

Sau khi nạp thành công, ESP32 thường khởi động lại và thực hiện chương trình mới.

### 5.3. So sánh Verify và Upload

| Tiêu chí | Verify | Upload |
|---|---|---|
| Kiểm tra cú pháp | Có | Có |
| Biên dịch chương trình | Có | Có |
| Cần kết nối ESP32 | Không bắt buộc | Có |
| Cần chọn đúng cổng COM | Không | Có |
| Ghi chương trình vào ESP32 | Không | Có |
| Thay chương trình đang lưu trên ESP32 | Không | Có |

**Lưu ý:** Khi Upload chương trình thực hành, chương trình điều khiển robot đã có trên ESP32 sẽ bị thay thế.

Vì vậy, cần giữ lại bộ mã nguồn robot gốc để có thể nạp lại sau khi học.

---

## 6. Chuẩn bị trước khi lập trình

### 6.1. Thiết bị cần thiết

Để thực hiện bài học này, chúng ta cần:

| STT | Thiết bị | Số lượng |
|---|---|---|
| 1 | ESP32 30P CH340 Type-C | 1 |
| 2 | Board mở rộng ESP32 30P | 1 |
| 3 | Máy tính đã cài Arduino IDE | 1 |
| 4 | Cáp USB Type-C có truyền dữ liệu | 1 |

Trong bài này, chúng ta chỉ sử dụng giao tiếp Serial nên không cần kết nối thêm LED, cảm biến hoặc động cơ.

Nếu ESP32 đang được lắp trên robot, nên tắt nguồn động cơ và kiểm tra các kết nối trước khi nạp chương trình thực hành.

### 6.2. Kiểm tra Arduino IDE

Trước khi bắt đầu, cần đảm bảo:

- Đã cài Arduino IDE.
- Đã cài driver CH340 nếu máy tính cần.
- Đã cài gói `esp32 by Espressif Systems`.
- Đã chọn đúng bo ESP32 Dev Module.
- Đã xác định được cổng COM.

Nếu chưa hoàn thành, tham khảo:

- [Hướng dẫn cài đặt Arduino IDE và driver CH340](../03-cai-arduino-ide.md).
- [Hướng dẫn cài đặt thư viện ESP32](../05-cai-thu-vien.md).

### 6.3. Chọn Board và Port

Kết nối ESP32 với máy tính bằng cáp USB Type-C.

Trong Arduino IDE:

1. Chọn **Tools → Board → ESP32 Dev Module**.
2. Chọn **Tools → Port**.
3. Chọn đúng cổng COM của ESP32.

Ví dụ:

```text
Board: ESP32 Dev Module
Port: COM5
```

Số cổng COM có thể khác nhau trên từng máy tính.

---

## 7. Thực hành chương trình đầu tiên

### 7.1. Mục tiêu thực hành

Chúng ta sẽ viết một chương trình có chức năng:

- Khởi tạo giao tiếp Serial.
- Tạo một biến đếm.
- Tăng biến đếm sau mỗi vòng lặp.
- Gửi giá trị biến đếm về máy tính.
- Lặp lại quá trình sau mỗi giây.

Thông qua bài thực hành này, chúng ta sẽ hiểu rõ cách `setup()` và `loop()` hoạt động.

### 7.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn **File → New Sketch**.

Lưu chương trình với tên:

```text
ESP32Serial
```

Arduino IDE sẽ tạo thư mục và tệp:

```text
ESP32Serial/
└── ESP32Serial.ino
```

Tên tệp `.ino` chính phải trùng với tên thư mục chứa chương trình.

### 7.3. Chương trình hoàn chỉnh

Nhập chương trình sau vào Arduino IDE:

```cpp
unsigned long soLan = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.print("So lan lap: ");
  Serial.println(soLan);

  soLan++;

  delay(1000);
}
```

Chương trình này không cần cài đặt thêm thư viện ngoài.

---

## 8. Giải thích chương trình

### 8.1. Khai báo biến đếm

```cpp
unsigned long soLan = 0;
```

Dòng lệnh khai báo một biến tên `soLan`.

Trong đó:

- `unsigned long`: Kiểu dữ liệu số nguyên không âm.
- `soLan`: Tên biến.
- `0`: Giá trị khởi tạo.

Biến được khai báo bên ngoài `setup()` và `loop()` nên có thể được sử dụng trong cả hai hàm.

Trong chương trình này, biến được sử dụng để đếm số lần thực hiện vòng lặp.

### 8.2. Khởi tạo giao tiếp Serial

```cpp
void setup() {
  Serial.begin(115200);
}
```

Khi ESP32 khởi động, hàm `setup()` được thực hiện.

Lệnh:

```cpp
Serial.begin(115200);
```

Khởi tạo giao tiếp Serial với tốc độ 115200 baud.

Serial được sử dụng để gửi dữ liệu từ ESP32 đến máy tính và nhận dữ liệu từ máy tính khi chương trình có xử lý đầu vào.

Trong bài này, chúng ta chỉ gửi dữ liệu từ ESP32 đến Serial Monitor.

### 8.3. In chuỗi ký tự

```cpp
Serial.print("So lan lap: ");
```

Lệnh `Serial.print()` gửi dữ liệu đến Serial Monitor nhưng không tự động xuống dòng sau khi in.

Ví dụ:

```text
So lan lap:
```

Sau đó, lệnh tiếp theo có thể in thêm dữ liệu trên cùng dòng.

### 8.4. In giá trị biến

```cpp
Serial.println(soLan);
```

Lệnh `Serial.println()` gửi giá trị biến `soLan` và kết thúc dòng.

Kết hợp hai lệnh:

```cpp
Serial.print("So lan lap: ");
Serial.println(soLan);
```

Kết quả:

```text
So lan lap: 0
```

Ở vòng lặp tiếp theo, giá trị sẽ tăng lên.

### 8.5. Tăng biến đếm

```cpp
soLan++;
```

Toán tử `++` được sử dụng để tăng giá trị biến lên một đơn vị.

Ví dụ:

| Giá trị trước | Giá trị sau |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |

Lệnh trên tương đương:

```cpp
soLan = soLan + 1;
```

### 8.6. Tạo thời gian chờ

```cpp
delay(1000);
```

Hàm `delay()` tạo khoảng thời gian chờ tính bằng mili giây.

Trong đó:

- 1000 ms = 1 giây.
- 500 ms = 0,5 giây.
- 2000 ms = 2 giây.

Vì vậy, chương trình sẽ in giá trị biến đếm sau mỗi khoảng thời gian xấp xỉ một giây.

**Lưu ý:** Trong thời gian thực hiện `delay()`, luồng chương trình hiện tại không tiếp tục thực hiện các câu lệnh phía sau cho đến khi hết thời gian chờ.

Đối với robot cần thực hiện đồng thời nhiều chức năng, chẳng hạn đọc cảm biến, điều khiển động cơ và xử lý lệnh Wi-Fi, việc sử dụng `delay()` quá dài có thể làm giảm khả năng phản hồi.

Trong các bài nâng cao, chúng ta sẽ tìm hiểu cách sử dụng `millis()` để quản lý thời gian mà không cần chờ theo cách này.

---

## 9. Biên dịch và nạp chương trình

### 9.1. Kiểm tra chương trình bằng Verify

Sau khi nhập mã:

1. Kiểm tra Board đang chọn là ESP32 Dev Module.
2. Nhấn nút **Verify**.
3. Chờ Arduino IDE biên dịch.

Nếu không có lỗi, Arduino IDE sẽ hiển thị thông báo biên dịch thành công cùng thông tin dung lượng bộ nhớ.

Nếu xuất hiện lỗi, cần đọc thông báo trong cửa sổ Output.

### 9.2. Nạp chương trình bằng Upload

Sau khi Verify thành công:

1. Kết nối ESP32 với máy tính.
2. Chọn đúng cổng COM.
3. Nhấn **Upload**.
4. Chờ Arduino IDE biên dịch và nạp chương trình.

Trong quá trình nạp, Arduino IDE có thể hiển thị các thông báo như:

```text
Connecting...
Writing at ...
Hard resetting via RTS pin...
```

Nội dung thực tế phụ thuộc phiên bản ESP32 core và công cụ nạp.

Nếu quá trình nạp thành công, ESP32 sẽ chạy chương trình mới.

Một số bo có thể cần thao tác với nút BOOT nếu không tự động chuyển được sang chế độ nạp.

### 9.3. Mở Serial Monitor

Sau khi nạp chương trình:

1. Mở **Serial Monitor**.
2. Chọn tốc độ **115200 baud**.
3. Quan sát dữ liệu hiển thị.

Nếu chưa thấy thông báo, nhấn nút **EN/RESET** trên ESP32 để khởi động lại chương trình.

---

## 10. Kết quả chạy thử

Nếu chương trình hoạt động đúng, Serial Monitor sẽ hiển thị:

```text
So lan lap: 0
So lan lap: 1
So lan lap: 2
So lan lap: 3
So lan lap: 4
So lan lap: 5
So lan lap: 6
...
```

Mỗi dòng được in cách nhau khoảng một giây.

Giá trị biến đếm tăng dần vì lệnh:

```cpp
soLan++;
```

Được thực hiện sau mỗi lần in.

Khi nhấn EN/RESET, ESP32 khởi động lại chương trình và biến `soLan` được khởi tạo lại bằng 0.

Kết quả sẽ bắt đầu lại:

```text
So lan lap: 0
So lan lap: 1
So lan lap: 2
...
```

### Thử thay đổi nội dung chương trình

Thay dòng:

```cpp
Serial.print("So lan lap: ");
```

Thành:

```cpp
Serial.print("ESP32 dang chay - Lan: ");
```

Nhấn **Verify**, sau đó **Upload**.

Kết quả mới:

```text
ESP32 dang chay - Lan: 0
ESP32 dang chay - Lan: 1
ESP32 dang chay - Lan: 2
...
```

Qua thử nghiệm này, chúng ta có thể nhận thấy:

- Thay đổi mã nguồn trên máy tính chưa làm thay đổi chương trình trong ESP32.
- Verify chỉ kiểm tra và biên dịch chương trình.
- Cần Upload để ESP32 thực hiện chương trình mới.

---

## 11. Các lỗi thường gặp

### 11.1. Lỗi thiếu dấu chấm phẩy

Ví dụ:

```cpp
unsigned long soLan = 0
```

Chương trình có thể báo lỗi do thiếu dấu `;`.

Cách xử lý:

- Kiểm tra dòng được Arduino IDE báo lỗi.
- Kiểm tra cả dòng ngay phía trước.
- Bổ sung dấu `;` ở vị trí phù hợp.

### 11.2. Lỗi thiếu dấu ngoặc

Ví dụ:

```cpp
void setup() {
  Serial.begin(115200);
```

Đoạn mã trên thiếu dấu `}` để kết thúc hàm.

Cách xử lý:

- Kiểm tra các cặp ngoặc `{` và `}`.
- Kiểm tra dấu `(` và `)`.
- Sử dụng chức năng tự động định dạng mã của Arduino IDE để dễ quan sát cấu trúc chương trình.

### 11.3. Lỗi sai tên hàm

Ví dụ:

```cpp
serial.println("Hello");
```

Trong khi chương trình cần sử dụng:

```cpp
Serial.println("Hello");
```

Ngôn ngữ C/C++ phân biệt chữ hoa và chữ thường.

Vì vậy, cần viết đúng tên hàm và đối tượng.

### 11.4. Verify thành công nhưng Upload thất bại

Nguyên nhân có thể:

- Chọn sai cổng COM.
- Cáp USB không hỗ trợ truyền dữ liệu.
- Driver CH340 chưa hoạt động.
- Cổng COM đang được chương trình khác sử dụng.
- ESP32 không vào được chế độ nạp.

Cách xử lý:

1. Kiểm tra cáp USB.
2. Kiểm tra cổng COM trong Device Manager.
3. Chọn lại Tools → Port.
4. Đóng các phần mềm khác đang sử dụng cổng Serial.
5. Thử nạp lại chương trình.
6. Nếu IDE liên tục dừng ở `Connecting...`, thử thao tác nút BOOT theo hướng dẫn của bo mạch.

### 11.5. Serial Monitor hiển thị ký tự lạ

Ví dụ:

```text
���?���
```

Nguyên nhân có thể là tốc độ Serial Monitor không trùng với tốc độ trong chương trình.

Nếu chương trình sử dụng:

```cpp
Serial.begin(115200);
```

Cần chọn Serial Monitor ở tốc độ 115200 baud.

Một số thông báo khởi động của ESP32 có thể sử dụng tốc độ hoặc định dạng riêng, vì vậy cần phân biệt thông báo khởi động với dữ liệu do chương trình in ra.

### 11.6. Không thấy dữ liệu trên Serial Monitor

Cách kiểm tra:

1. Đảm bảo chương trình đã được Upload thành công.
2. Kiểm tra đúng cổng COM.
3. Kiểm tra tốc độ 115200 baud.
4. Nhấn EN/RESET để chạy lại chương trình.
5. Kiểm tra cáp USB và nguồn cấp.

Nếu chỉ mới nhấn Verify mà chưa Upload, ESP32 vẫn chạy chương trình cũ.

### 11.7. Thông báo exit status 1

Arduino IDE có thể hiển thị:

```text
exit status 1
```

Đây là thông báo tổng quát cho biết quá trình biên dịch hoặc thao tác tương ứng đã thất bại.

Nó không cho biết đầy đủ nguyên nhân.

Khi gặp lỗi, cần đọc những dòng thông báo phía trên để xác định lỗi cụ thể, chẳng hạn:

- Thiếu dấu chấm phẩy.
- Sai tên biến.
- Thiếu thư viện.
- Sai cú pháp.
- Sử dụng hàm không tồn tại.

Không nên chỉ dựa vào dòng `exit status 1` để xác định nguyên nhân.

---

## 12. Bài tập thực hành

### Bài tập 1: Thay đổi thời gian in

Sửa chương trình để Serial Monitor in giá trị biến đếm sau mỗi 500 ms.

Gợi ý:

```cpp
delay(500);
```

Quan sát sự khác biệt so với chương trình ban đầu.

### Bài tập 2: Thêm câu lệnh điều kiện

Sửa chương trình để khi biến `soLan` bằng 5, ESP32 in thêm thông báo:

```text
Da lap 5 lan
```

Gợi ý:

```cpp
if (soLan == 5) {
  Serial.println("Da lap 5 lan");
}
```

Quan sát thông báo xuất hiện ở vòng lặp tương ứng.

### Bài tập 3: Thay đổi giá trị ban đầu

Thay:

```cpp
unsigned long soLan = 0;
```

Thành:

```cpp
unsigned long soLan = 10;
```

Nạp lại chương trình và quan sát kết quả.

Giải thích vì sao giá trị đầu tiên được in ra là 10.

### Bài tập 4: Phân biệt Verify và Upload

Thực hiện:

1. Sửa nội dung chuỗi được in ra Serial Monitor.
2. Nhấn Verify nhưng chưa Upload.
3. Quan sát chương trình đang chạy trên ESP32.
4. Nhấn Upload.
5. Quan sát kết quả mới.

Giải thích vì sao Verify không làm thay đổi chương trình trên ESP32.

### Bài tập 5: Tìm và sửa lỗi

Quan sát chương trình sau:

```cpp
unsigned long soLan = 0

void setup() {
  serial.begin(115200);
}

void loop() {
  Serial.println(soLan)
  soLan++;
  delay(1000);
}
```

Hãy xác định và sửa các lỗi để chương trình biên dịch thành công.

---

## 13. Kiểm tra trước khi bắt đầu bài tiếp theo

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã hiểu cấu trúc chương trình Arduino.
- [ ] Đã phân biệt `setup()` và `loop()`.
- [ ] Đã biết khai báo và sử dụng biến.
- [ ] Đã biết sử dụng câu lệnh `if`.
- [ ] Đã hiểu chức năng của `delay()`.
- [ ] Đã phân biệt Verify và Upload.
- [ ] Đã tạo và lưu được một sketch mới.
- [ ] Đã chọn đúng ESP32 Dev Module và cổng COM.
- [ ] Đã nạp thành công chương trình lên ESP32.
- [ ] Đã đọc được dữ liệu trên Serial Monitor.
- [ ] Đã biết cách tìm thông báo lỗi khi chương trình không biên dịch được.

---

## 14. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu những kiến thức cơ bản nhất để bắt đầu lập trình ESP32 bằng Arduino IDE.

Những nội dung quan trọng bao gồm:

- Hiểu chương trình Arduino là gì.
- Nắm được vai trò của `setup()` và `loop()`.
- Làm quen với biến, hằng số, câu lệnh điều kiện và chú thích.
- Phân biệt Verify và Upload.
- Tạo, lưu và nạp chương trình vào ESP32.
- Sử dụng Serial Monitor để theo dõi hoạt động.
- Nhận biết và xử lý một số lỗi lập trình cơ bản.

Ở bài tiếp theo, chúng ta sẽ bắt đầu **điều khiển LED bằng ESP32**, qua đó tìm hiểu cách cấu hình chân GPIO làm đầu ra Digital và sử dụng các lệnh `pinMode()`, `digitalWrite()` để điều khiển thiết bị ngoại vi.

---

[Bài trước: Giới thiệu xe ESP32](../01-gioi-thieu.md) · [Lộ trình bài học](../index.md) · [Bài tiếp: Điều khiển LED](03-led.md)