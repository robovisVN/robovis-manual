# Bài 2: Viết và nạp chương trình Arduino đầu tiên

## 1. Giới thiệu

Trong bài học trước, chúng ta đã tìm hiểu các thành phần của xe robot Arduino Nano và chuẩn bị những thiết bị cần thiết để bắt đầu lập trình.

Ở bài học này, chúng ta sẽ thực hành viết chương trình Arduino đầu tiên, nạp chương trình vào board và quan sát kết quả hoạt động thông qua máy tính.

Thông qua bài học, chúng ta sẽ tìm hiểu:

- Cách tạo và lưu một chương trình Arduino.
- Cấu trúc cơ bản của chương trình Arduino.
- Cách sử dụng các hàm `setup()` và `loop()`.
- Cách biên dịch và nạp chương trình vào Arduino Nano.
- Cách sử dụng Serial Monitor để theo dõi dữ liệu.
- Cách sử dụng biến và thực hiện các phép toán đơn giản.

Sau khi hoàn thành, bạn sẽ hiểu được quy trình cơ bản để viết, nạp và kiểm tra một chương trình Arduino.

## 2. Chuẩn bị

Trước khi bắt đầu, chúng ta cần chuẩn bị:

- Máy tính đã cài đặt Arduino IDE.
- Board Arduino Nano.
- Cáp USB có khả năng truyền dữ liệu.
- Driver USB phù hợp nếu máy tính chưa nhận Arduino.

Nếu chưa cài đặt phần mềm, hãy thực hiện theo bài [Cài đặt Arduino IDE](../05-cai-arduino-ide.md).

**Lưu ý:** Trong bài học này, chúng ta chỉ sử dụng Arduino Nano để giao tiếp với máy tính, chưa cần kết nối với các cảm biến hoặc động cơ.

Nếu Arduino Nano đang được lắp trên xe robot, cần tắt nguồn động cơ và ngắt các dây nối từ chân D0, D1 đến driver L298N trước khi thực hành. Hai chân này được sử dụng cho giao tiếp Serial với máy tính.

Nên chụp lại vị trí dây trước khi tháo để có thể khôi phục đúng kết nối sau bài học.

## 3. Tạo chương trình Arduino mới

### 3.1. Mở Arduino IDE

Kết nối Arduino Nano với máy tính thông qua cáp USB.

Sau đó mở phần mềm Arduino IDE.

Trên thanh menu, chọn:

`File → New Sketch`

Arduino IDE sẽ tạo một chương trình mới với cấu trúc mặc định.

### 3.2. Lưu chương trình

Để lưu chương trình, chọn:

`File → Save As`

Đặt tên chương trình:

`NanoThongBao`

Chọn thư mục lưu trữ đã chuẩn bị từ bài học trước.

Sau khi lưu, Arduino IDE sẽ tạo một thư mục chứa tệp chương trình:

```text
HocRobotArduino/
└── NanoThongBao/
    └── NanoThongBao.ino
```

Trong đó:

- `NanoThongBao` là tên chương trình.
- `.ino` là phần mở rộng của tệp chương trình Arduino.

Mỗi bài học nên được lưu thành một chương trình riêng để thuận tiện cho việc chỉnh sửa và sử dụng lại sau này.

## 4. Cấu trúc chương trình Arduino

Một chương trình Arduino cơ bản gồm hai hàm chính:

```cpp
void setup() {

}

void loop() {

}
```

### 4.1. Hàm setup()

Hàm `setup()` được thực hiện một lần khi Arduino khởi động hoặc khi nhấn nút Reset.

Hàm này thường được sử dụng để:

- Cấu hình các chân tín hiệu.
- Khởi tạo giao tiếp Serial.
- Khởi tạo cảm biến và các thiết bị ngoại vi.
- Thiết lập những thông số ban đầu.

Ví dụ:

```cpp
void setup() {
  Serial.begin(9600);
}
```

Trong ví dụ trên, Arduino khởi tạo giao tiếp Serial với tốc độ 9600 baud.

### 4.2. Hàm loop()

Hàm `loop()` được thực hiện liên tục sau khi hàm `setup()` kết thúc.

Khi thực hiện hết các lệnh trong `loop()`, Arduino sẽ quay lại đầu hàm và tiếp tục thực hiện.

Hàm này thường được sử dụng để:

- Đọc dữ liệu cảm biến.
- Xử lý các điều kiện điều khiển.
- Điều khiển động cơ và servo.
- Gửi dữ liệu về máy tính.
- Thực hiện các thuật toán điều khiển robot.

Ví dụ:

```cpp
void loop() {
  Serial.println("Hello Arduino");
  delay(1000);
}
```

Đoạn chương trình trên sẽ gửi dòng chữ `Hello Arduino` về máy tính sau mỗi khoảng thời gian một giây.

### 4.3. Một số quy tắc khi viết chương trình

Khi lập trình Arduino, cần lưu ý một số quy tắc cơ bản:

| Ký hiệu | Ý nghĩa |
|---|---|
| `{ }` | Xác định phạm vi của một khối lệnh |
| `( )` | Chứa tham số truyền vào hàm hoặc biểu thức điều kiện |
| `;` | Kết thúc một câu lệnh |
| `//` | Ghi chú trên một dòng |
| `/* ... */` | Ghi chú trên nhiều dòng |
| `" "` | Bao quanh một chuỗi ký tự |

Ngôn ngữ lập trình Arduino phân biệt chữ hoa và chữ thường.

Ví dụ, `Serial.println()` là cách viết đúng, trong khi `serial.println()` sẽ gây lỗi biên dịch.

## 5. Viết chương trình đầu tiên

Trong ví dụ đầu tiên, chúng ta sẽ lập trình Arduino Nano gửi một dòng thông báo về máy tính sau mỗi giây.

### 5.1. Chương trình mẫu

Xóa nội dung mặc định trong Arduino IDE và nhập chương trình sau:

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Xin chao tu Nano");
  delay(1000);
}
```

### 5.2. Giải thích chương trình

**Lệnh Serial.begin()**

```cpp
Serial.begin(9600);
```

Lệnh này khởi tạo giao tiếp Serial giữa Arduino Nano và máy tính.

Giá trị `9600` là tốc độ truyền dữ liệu, tính bằng baud.

Tốc độ này cần được thiết lập tương ứng trong Serial Monitor để dữ liệu hiển thị chính xác.

**Lệnh Serial.println()**

```cpp
Serial.println("Xin chao tu Nano");
```

Lệnh này gửi chuỗi ký tự `Xin chao tu Nano` về máy tính.

Sau khi gửi xong, Arduino tự động thêm ký tự xuống dòng.

Nhờ đó, mỗi lần gửi dữ liệu sẽ được hiển thị trên một dòng riêng trong Serial Monitor.

**Lệnh delay()**

```cpp
delay(1000);
```

Lệnh `delay()` làm chương trình tạm dừng trong một khoảng thời gian xác định.

Đơn vị thời gian là mili giây (ms).

Ví dụ:

| Giá trị | Thời gian |
|---|---|
| `delay(100)` | 0,1 giây |
| `delay(500)` | 0,5 giây |
| `delay(1000)` | 1 giây |
| `delay(2000)` | 2 giây |

Trong chương trình trên, Arduino gửi một dòng thông báo, chờ một giây rồi tiếp tục gửi thông báo mới.

Do hàm `loop()` được thực hiện liên tục, quá trình này sẽ lặp lại cho đến khi Arduino ngừng hoạt động hoặc được nạp chương trình khác.

## 6. Biên dịch và nạp chương trình

Sau khi viết xong chương trình, chúng ta cần biên dịch và nạp vào Arduino Nano.

### 6.1. Chọn board Arduino

Trên Arduino IDE, chọn:

`Tools → Board → Arduino AVR Boards → Arduino Nano`

Tiếp theo, chọn bộ xử lý:

`Tools → Processor → ATmega328P`

Đối với một số board Nano sử dụng bootloader cũ, có thể cần chọn:

`ATmega328P (Old Bootloader)`

Chỉ thay đổi tùy chọn này khi board sử dụng bootloader tương ứng hoặc gặp lỗi nạp chương trình.

### 6.2. Chọn cổng kết nối

Trên Arduino IDE, chọn:

`Tools → Port`

Sau đó chọn cổng kết nối của Arduino Nano.

Ví dụ:

- Windows: `COM3`, `COM4`, `COM5`...
- Ubuntu: `/dev/ttyUSB0`, `/dev/ttyACM0`...

Tên cổng phụ thuộc vào hệ điều hành và chip giao tiếp USB trên board.

Nếu không biết cổng nào thuộc Arduino, có thể rút cáp USB, kiểm tra danh sách cổng rồi cắm lại. Cổng mới xuất hiện thường là cổng của Arduino.

### 6.3. Kiểm tra chương trình

Nhấn nút **Verify** (biểu tượng dấu kiểm) trên Arduino IDE.

Phần mềm sẽ kiểm tra cú pháp và biên dịch chương trình.

Nếu chương trình không có lỗi, quá trình biên dịch sẽ hoàn tất.

Lưu ý rằng Verify chỉ kiểm tra và biên dịch chương trình, chưa nạp chương trình vào Arduino.

### 6.4. Nạp chương trình

Nhấn nút **Upload** (biểu tượng mũi tên).

Arduino IDE sẽ biên dịch nếu cần, sau đó truyền chương trình vào bộ nhớ của Arduino Nano.

Khi nạp thành công, phần mềm sẽ hiển thị thông báo tương tự:

```text
Done uploading.
```

Lúc này, Arduino Nano đã nhận chương trình mới và bắt đầu thực hiện.

**Lưu ý:** Không rút cáp USB trong quá trình nạp chương trình.

## 7. Quan sát dữ liệu bằng Serial Monitor

### 7.1. Mở Serial Monitor

Serial Monitor là công cụ trong Arduino IDE dùng để theo dõi dữ liệu được Arduino gửi về máy tính thông qua giao tiếp Serial.

Để mở Serial Monitor, chọn:

`Tools → Serial Monitor`

Hoặc sử dụng biểu tượng Serial Monitor trên giao diện Arduino IDE.

Sau đó thiết lập tốc độ truyền dữ liệu là:

`9600 baud`

Giá trị này phải tương ứng với lệnh `Serial.begin(9600)` trong chương trình.

### 7.2. Quan sát kết quả

Nếu chương trình hoạt động đúng, Serial Monitor sẽ hiển thị:

```text
Xin chao tu Nano
Xin chao tu Nano
Xin chao tu Nano
Xin chao tu Nano
```

Cứ sau khoảng một giây, Arduino sẽ gửi thêm một dòng thông báo.

Điều này cho thấy:

- Arduino Nano đã nhận chương trình.
- Hàm `setup()` đã khởi tạo giao tiếp Serial.
- Hàm `loop()` đang thực hiện liên tục.
- Arduino có thể gửi dữ liệu về máy tính.

Serial Monitor là một công cụ rất quan trọng trong quá trình lập trình robot, đặc biệt khi cần kiểm tra dữ liệu cảm biến hoặc tìm nguyên nhân lỗi chương trình.

## 8. Thực hành thay đổi chương trình

### 8.1. Thay đổi thời gian gửi dữ liệu

Trong chương trình ban đầu, chúng ta sử dụng:

```cpp
delay(1000);
```

Hãy thay đổi thành:

```cpp
delay(500);
```

Sau đó nhấn Upload để nạp lại chương trình.

Quan sát Serial Monitor.

Kết quả: Dòng thông báo sẽ xuất hiện nhanh hơn, khoảng hai lần mỗi giây.

Tiếp tục thử các giá trị `200`, `1000` và `2000` để quan sát sự khác biệt.

Qua ví dụ này, chúng ta có thể thấy việc thay đổi tham số trong chương trình sẽ ảnh hưởng trực tiếp đến hoạt động của Arduino.

### 8.2. Thay đổi nội dung thông báo

Thay đổi dòng lệnh:

```cpp
Serial.println("Xin chao tu Nano");
```

Thành:

```cpp
Serial.println("Toi dang hoc Arduino");
```

Nạp lại chương trình và quan sát kết quả.

Serial Monitor sẽ hiển thị nội dung mới:

```text
Toi dang hoc Arduino
Toi dang hoc Arduino
Toi dang hoc Arduino
```

**Lưu ý:** Sau mỗi lần chỉnh sửa chương trình, cần thực hiện Upload để Arduino nhận phiên bản mới. Nếu chỉ sửa mã trên máy tính mà không nạp lại, Arduino vẫn tiếp tục chạy chương trình cũ.

## 9. Làm quen với biến trong Arduino

Trong lập trình, chúng ta thường cần lưu trữ những giá trị như tốc độ động cơ, khoảng cách vật cản hoặc số xung encoder.

Để lưu trữ những giá trị này, chúng ta sử dụng **biến**.

Biến là một vùng nhớ có tên, được sử dụng để lưu dữ liệu trong quá trình chương trình hoạt động.

### 9.1. Khai báo biến

Ví dụ:

```cpp
int soLan = 0;
```

Trong đó:

- `int`: Kiểu dữ liệu số nguyên.
- `soLan`: Tên biến.
- `0`: Giá trị khởi tạo.

Chúng ta có thể thay đổi giá trị của biến trong quá trình chương trình thực hiện.

Ví dụ:

```cpp
soLan = soLan + 1;
```

Lệnh trên lấy giá trị hiện tại của biến `soLan`, cộng thêm 1 và lưu kết quả trở lại biến.

### 9.2. Chương trình đếm số lần thực hiện

Hãy thay toàn bộ chương trình bằng đoạn mã sau:

```cpp
int soLan = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(soLan);

  soLan = soLan + 1;

  if (soLan >= 10) {
    soLan = 0;
  }

  delay(1000);
}
```

### 9.3. Giải thích chương trình

Đầu tiên, chúng ta khai báo biến:

```cpp
int soLan = 0;
```

Biến `soLan` được khởi tạo với giá trị bằng 0.

Trong hàm `loop()`, Arduino gửi giá trị của biến về máy tính:

```cpp
Serial.println(soLan);
```

Sau đó tăng giá trị biến thêm 1:

```cpp
soLan = soLan + 1;
```

Tiếp theo, chương trình kiểm tra điều kiện:

```cpp
if (soLan >= 10) {
  soLan = 0;
}
```

Lệnh `if` được sử dụng để kiểm tra một điều kiện.

Trong ví dụ này, nếu giá trị `soLan` lớn hơn hoặc bằng 10, chương trình sẽ đưa biến trở về 0.

Kết quả hiển thị trên Serial Monitor:

```text
0
1
2
3
4
5
6
7
8
9
0
1
2
3
```

Chương trình sẽ tiếp tục đếm từ 0 đến 9 và lặp lại.

Thông qua ví dụ này, chúng ta đã làm quen với ba nội dung quan trọng:

- Khai báo và sử dụng biến.
- Thực hiện phép toán.
- Sử dụng câu lệnh điều kiện `if`.

Đây là những kiến thức sẽ được sử dụng thường xuyên khi lập trình điều khiển robot.

## 10. Một số lỗi thường gặp

Trong quá trình viết và nạp chương trình, có thể gặp một số lỗi sau:

| Lỗi | Nguyên nhân và cách xử lý |
|---|---|
| `expected ';'` | Thiếu dấu `;` ở cuối câu lệnh |
| `expected '}'` | Thiếu dấu ngoặc nhọn đóng |
| `'serial' was not declared` | Viết sai `Serial`, cần phân biệt chữ hoa và chữ thường |
| Không tìm thấy cổng COM | Kiểm tra cáp USB, driver và kết nối |
| Upload thất bại | Kiểm tra Board, Processor, Port và kết nối D0/D1 |
| Serial Monitor không hiển thị | Kiểm tra chương trình đã Upload và chọn đúng Port |
| Serial Monitor hiển thị ký tự lạ | Kiểm tra tốc độ baud |
| Arduino vẫn chạy chương trình cũ | Kiểm tra quá trình Upload đã thành công hay chưa |

Khi gặp lỗi biên dịch, hãy đọc thông báo lỗi và kiểm tra dòng được Arduino IDE chỉ ra.

Đôi khi lỗi xuất phát từ dòng phía trước, ví dụ thiếu dấu chấm phẩy hoặc dấu ngoặc.

## 11. Bài tập thực hành

Sau khi hoàn thành các ví dụ, hãy thực hiện những bài tập sau.

**Bài tập 1: Thay đổi thời gian**

Viết chương trình gửi dòng thông báo:

```text
Arduino dang hoat dong
```

Sau mỗi hai giây.

**Bài tập 2: Đếm số lần thực hiện**

Viết chương trình đếm từ 0 đến 20, sau đó quay trở lại 0.

Mỗi giá trị được gửi về Serial Monitor sau một giây.

**Bài tập 3: Thay đổi bước đếm**

Chỉnh sửa chương trình để hiển thị:

```text
0
2
4
6
8
10
0
2
4
```

Gợi ý: Thay đổi phép toán tăng giá trị của biến và điều kiện đưa biến trở về 0.

## 12. Tổng kết

Qua bài học này, chúng ta đã thực hiện được những thao tác lập trình Arduino cơ bản:

- Tạo và lưu một chương trình Arduino.
- Hiểu cấu trúc hai hàm `setup()` và `loop()`.
- Sử dụng `Serial.begin()` và `Serial.println()` để truyền dữ liệu.
- Sử dụng `delay()` để tạo khoảng thời gian chờ.
- Biên dịch và nạp chương trình vào Arduino Nano.
- Theo dõi dữ liệu bằng Serial Monitor.
- Khai báo biến và sử dụng câu lệnh điều kiện `if`.

Đây là những kiến thức nền tảng để tiếp tục lập trình các thiết bị trên xe robot.

Ở bài tiếp theo, chúng ta sẽ thực hành **điều khiển đèn LED bằng Arduino Nano**, qua đó tìm hiểu cách cấu hình và điều khiển các chân Digital.