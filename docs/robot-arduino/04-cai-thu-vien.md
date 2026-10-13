# Hướng dẫn cài đặt thư viện cho Arduino Nano

## 1. Giới thiệu

Trong các bài học trước, chúng ta đã tìm hiểu cách cài đặt Arduino IDE, lựa chọn bo mạch Arduino Nano và nạp chương trình đầu tiên.

Để điều khiển những thiết bị như động cơ servo hoặc giao tiếp Bluetooth, chương trình Arduino có thể cần sử dụng thêm các **thư viện lập trình (Library)**.

Thư viện cung cấp các hàm và công cụ đã được xây dựng sẵn, giúp người dùng điều khiển phần cứng mà không phải tự lập trình toàn bộ quá trình giao tiếp ở mức thấp.

Ví dụ:

- Điều khiển góc quay servo SG90 bằng thư viện Servo.
- Nhận dữ liệu từ ứng dụng Dabble bằng thư viện Dabble.
- Sử dụng các chức năng cơ bản của Arduino thông qua những thành phần đã được cung cấp trong Arduino core.

Trong bài học này, chúng ta sẽ tìm hiểu:

- Thư viện Arduino là gì và có vai trò như thế nào.
- Cách nhận biết chương trình cần sử dụng thư viện nào.
- Cách cài đặt thư viện bằng Library Manager.
- Cách cài đặt thư viện Servo.
- Cách cài đặt thư viện Dabble cho Arduino Nano.
- Cách cài thư viện từ tệp ZIP.
- Cách kiểm tra thư viện bằng chức năng Verify.
- Cách xử lý những lỗi thư viện thường gặp.

**Mục tiêu thực hành:** Cài đặt đúng thư viện Servo và Dabble, sau đó biên dịch thành công các chương trình kiểm tra trên Arduino Nano.

Trong bài này, chúng ta chủ yếu sử dụng chức năng Verify để kiểm tra phần mềm. Chưa cần cấp nguồn động cơ hoặc kết nối đầy đủ các thiết bị ngoại vi.

## 2. Tìm hiểu về thư viện Arduino

### 2.1. Thư viện là gì?

Thư viện Arduino là tập hợp các đoạn mã, hàm và lớp lập trình được xây dựng sẵn để thực hiện một hoặc nhiều chức năng nhất định.

Thay vì phải viết lại toàn bộ thuật toán điều khiển, người lập trình có thể sử dụng những chức năng đã được cung cấp trong thư viện.

Ví dụ, để điều khiển servo quay đến góc 90°, chúng ta có thể viết:

```cpp
myServo.write(90);
```

Lệnh này được cung cấp thông qua thư viện Servo.

Nếu không sử dụng thư viện, người lập trình sẽ phải tự xây dựng quá trình tạo tín hiệu điều khiển phù hợp với servo.

Nhờ thư viện, chương trình trở nên ngắn gọn, dễ hiểu và thuận tiện hơn trong quá trình phát triển.

### 2.2. Vai trò của thư viện

Thư viện thường được sử dụng để:

- Điều khiển các thiết bị phần cứng.
- Giao tiếp với cảm biến và module ngoại vi.
- Xử lý dữ liệu nhận được từ thiết bị.
- Cung cấp các thuật toán và chức năng có thể tái sử dụng.
- Giảm thời gian viết và kiểm tra chương trình.

Ví dụ:

| Thư viện | Chức năng |
|---|---|
| Servo | Điều khiển động cơ servo |
| Dabble | Xử lý dữ liệu từ ứng dụng Dabble |
| Wire | Giao tiếp I2C |
| SPI | Giao tiếp SPI |
| EEPROM | Đọc và ghi bộ nhớ EEPROM |

Không phải chương trình nào cũng cần cài thêm thư viện bên ngoài.

Các chức năng cơ bản như `digitalWrite()`, `digitalRead()`, `analogRead()` và `analogWrite()` đã được cung cấp thông qua Arduino core tương ứng với bo mạch.

### 2.3. Khai báo thư viện trong chương trình

Để sử dụng một thư viện, chương trình thường có dòng khai báo:

```cpp
#include <Servo.h>
```

Trong đó:

- `#include`: Chỉ thị yêu cầu trình biên dịch đưa nội dung khai báo từ tệp tương ứng vào chương trình.
- `Servo.h`: Tệp header của thư viện Servo.

Một ví dụ khác:

```cpp
#include <Dabble.h>
```

Dòng này cho phép chương trình sử dụng những chức năng được khai báo trong thư viện Dabble.

Nếu Arduino IDE không tìm thấy tệp thư viện cần thiết, quá trình biên dịch có thể báo lỗi.

Ví dụ:

```text
fatal error: Servo.h: No such file or directory
```

Thông báo này cho biết trình biên dịch không tìm thấy tệp `Servo.h` trong những vị trí tìm kiếm hiện tại.

Nguyên nhân có thể là chưa cài thư viện, cài sai thư viện hoặc cấu trúc thư viện không phù hợp.

## 3. Phân biệt Board Package và Library

Khi lập trình Arduino, người mới thường nhầm lẫn giữa **gói hỗ trợ bo mạch (Board Package)** và **thư viện (Library)**.

Hai thành phần này có chức năng khác nhau.

### 3.1. Board Package

Board Package cung cấp những thành phần cần thiết để Arduino IDE biên dịch và nạp chương trình cho một nhóm bo mạch.

Đối với Arduino Nano classic sử dụng ATmega328P, chúng ta sử dụng:

**Arduino AVR Boards**

Gói này cung cấp cấu hình bo mạch, Arduino core và các công cụ liên quan.

### 3.2. Library

Library cung cấp các chức năng phục vụ chương trình ứng dụng.

Ví dụ:

- Servo: Điều khiển servo SG90.
- Dabble: Nhận và xử lý dữ liệu điều khiển từ điện thoại.

### 3.3. Bảng so sánh

| Tiêu chí | Board Package | Library |
|---|---|---|
| Mục đích | Hỗ trợ lập trình một loại bo mạch | Cung cấp chức năng lập trình |
| Ví dụ | Arduino AVR Boards | Servo, Dabble |
| Công cụ cài đặt | Boards Manager | Library Manager |
| Liên quan đến | Vi điều khiển, core, biên dịch và nạp | Thiết bị hoặc chức năng trong chương trình |
| Có cần cho Nano? | Có | Tùy chương trình |

**Lưu ý:** Cài đặt Arduino AVR Boards không có nghĩa tất cả thư viện dùng cho xe robot đã được cài đặt.

Ngược lại, cài thư viện Servo hoặc Dabble cũng không thay thế việc lựa chọn đúng bo mạch Arduino Nano.

## 4. Xác định thư viện cần sử dụng cho xe robot

Trước khi cài đặt, chúng ta cần biết chương trình đang sử dụng những thư viện nào.

Có thể kiểm tra các dòng `#include` ở đầu chương trình.

Ví dụ:

```cpp
#include <Servo.h>
```

Chương trình này sử dụng thư viện Servo.

Ví dụ:

```cpp
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE

#include <Dabble.h>
#include <Servo.h>
```

Chương trình này sử dụng cả Dabble và Servo.

### 4.1. Các thư viện trong bộ xe Arduino Nano

| Chương trình hoặc chức năng | Thư viện sử dụng |
|---|---|
| Điều khiển servo SG90 | Servo |
| Chương trình tránh vật cản có servo | Servo |
| Điều khiển bằng Bluetooth HM-10 và Dabble | Dabble |
| Chương trình Bluetooth có điều khiển servo | Dabble và Servo |
| Đọc cảm biến dò line Digital | Không cần cài thư viện ngoài |
| Đọc HC-SR04 bằng `pulseIn()` | Không cần cài thư viện ngoài |
| Đọc Encoder bằng ngắt ngoài | Không cần cài thư viện ngoài |
| Điều khiển động cơ L298N bằng chân Digital và PWM | Không cần cài thư viện ngoài |

Các chương trình như `do_line*.ino` có thể sử dụng những hàm Arduino cơ bản mà không cần cài thêm thư viện.

Dấu `*` trong tên trên chỉ những phần tên tệp có thể thay đổi, không phải ký tự cần nhập vào Library Manager.

### 4.2. Có cần cài tất cả thư viện trước không?

Không bắt buộc.

Nên cài những thư viện thực sự được sử dụng trong chương trình.

Ví dụ:

- Khi học servo, cài và kiểm tra Servo.
- Khi học Bluetooth HM-10, cài và kiểm tra Dabble.
- Khi học đọc Encoder, không cần cài thêm thư viện nếu sử dụng chương trình ngắt ngoài như trong tài liệu.

Cách này giúp hạn chế cài nhầm thư viện có tên tương tự nhưng không phù hợp với Arduino Nano.

## 5. Làm quen với Library Manager

### 5.1. Library Manager là gì?

Library Manager là công cụ tích hợp trong Arduino IDE, cho phép người dùng tìm kiếm, cài đặt và cập nhật các thư viện.

Đây là phương pháp cài đặt nên ưu tiên đối với những thư viện đã có trong hệ thống quản lý thư viện của Arduino.

### 5.2. Mở Library Manager

Trong Arduino IDE 2, có thể mở Library Manager bằng một trong hai cách:

**Cách 1:** Chọn biểu tượng Library Manager ở thanh bên trái.

**Cách 2:** Chọn:

**Tools → Manage Libraries**

Sau đó, cửa sổ quản lý thư viện sẽ xuất hiện.

### 5.3. Các thao tác cơ bản

Trong Library Manager, chúng ta có thể:

1. Nhập tên thư viện vào ô tìm kiếm.
2. Xem các kết quả phù hợp.
3. Kiểm tra tên và tác giả thư viện.
4. Lựa chọn phiên bản nếu cần.
5. Nhấn Install để cài đặt.
6. Kiểm tra trạng thái thư viện sau khi cài.

Khi tìm kiếm, không nên chỉ dựa vào tên gần giống nhau.

Cần đối chiếu tên thư viện, tác giả và khả năng hỗ trợ bo mạch đang sử dụng.

## 6. Cài đặt thư viện Servo

### 6.1. Giới thiệu thư viện Servo

Servo là thư viện hỗ trợ điều khiển các động cơ servo thông dụng bằng Arduino.

Trong bộ xe robot, servo SG90 được kết nối với chân A5 của Arduino Nano.

Servo có thể được sử dụng để điều chỉnh hướng cảm biến siêu âm hoặc thực hiện những chuyển động cơ khí khác.

Thư viện Servo cung cấp các chức năng như:

- Khởi tạo đối tượng servo.
- Gắn servo với một chân điều khiển.
- Gửi lệnh đặt góc servo.
- Đọc giá trị góc lệnh gần nhất.

### 6.2. Các bước cài đặt

Thực hiện:

1. Mở Arduino IDE.
2. Mở Library Manager.
3. Nhập từ khóa `Servo`.
4. Tìm thư viện có tên **Servo**.
5. Kiểm tra thư viện thuộc dự án Arduino.
6. Nhấn Install.
7. Chờ quá trình cài đặt hoàn tất.

Nếu IDE yêu cầu cài đặt thêm thư viện phụ thuộc, cần kiểm tra và chấp nhận các thành phần cần thiết.

### 6.3. Kiểm tra trạng thái thư viện

Sau khi cài đặt, Library Manager sẽ hiển thị trạng thái đã cài đặt của thư viện.

Nếu thư viện Servo đã có sẵn và hoạt động bình thường, không cần cài đặt lại.

Có thể tham khảo hướng dẫn chính thức:

https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library/

## 7. Ví dụ 1: Kiểm tra thư viện Servo

Sau khi cài đặt, chúng ta sẽ tạo một chương trình ngắn để kiểm tra thư viện có được Arduino IDE nhận diện hay không.

Trong ví dụ này, chỉ cần Verify chương trình. Chưa cần kết nối servo hoặc cấp nguồn cho động cơ.

### 7.1. Chương trình mẫu

Tạo sketch mới với tên `NanoKiemTraServo`.

```cpp
#include <Servo.h>

// ================= SERVO =================
#define SERVO_PIN A5

Servo myServo;

// ================= SETUP =================
void setup() {
  myServo.attach(SERVO_PIN);
  myServo.write(90);
}

// ================= LOOP =================
void loop() {

}
```

### 7.2. Giải thích chương trình

**Khai báo thư viện**

```cpp
#include <Servo.h>
```

Cho phép chương trình sử dụng những chức năng được khai báo trong thư viện Servo.

**Khai báo chân servo**

```cpp
#define SERVO_PIN A5
```

Chân A5 được sử dụng làm chân tín hiệu điều khiển servo theo cấu hình bộ xe.

**Tạo đối tượng Servo**

```cpp
Servo myServo;
```

Lệnh này tạo đối tượng `myServo` để điều khiển servo.

**Gắn servo với chân điều khiển**

```cpp
myServo.attach(SERVO_PIN);
```

Lệnh `attach()` liên kết đối tượng Servo với chân điều khiển đã khai báo.

**Đặt góc servo**

```cpp
myServo.write(90);
```

Gửi lệnh đặt servo đến vị trí góc 90°.

Góc thực tế còn phụ thuộc vào đặc tính servo, nguồn cấp và cơ cấu cơ khí.

### 7.3. Thực hiện Verify

Trong Arduino IDE:

1. Chọn Board là Arduino Nano.
2. Chọn Processor là ATmega328P.
3. Kiểm tra chương trình.
4. Nhấn nút Verify.
5. Chờ quá trình biên dịch hoàn tất.

**Kết quả mong đợi:** Arduino IDE biên dịch thành công và không xuất hiện lỗi thiếu `Servo.h`.

Điều này xác nhận thư viện Servo đã được nhận diện và có thể sử dụng để biên dịch chương trình cho bo mạch đang chọn.

Tuy nhiên, Verify thành công chưa chứng minh servo đã được đấu dây đúng hoặc có thể hoạt động trên phần cứng.

Để thực hành điều khiển servo thực tế, xem [Bài 4: Điều khiển servo SG90](bai-giang/04-servo.md).

## 8. Cài đặt thư viện Dabble

### 8.1. Giới thiệu thư viện Dabble

Dabble là thư viện được sử dụng cùng ứng dụng Dabble để Arduino có thể xử lý các lệnh điều khiển từ điện thoại.

Trong bộ xe robot, Arduino Nano giao tiếp với module Bluetooth HM-10 để nhận dữ liệu từ ứng dụng.

Thông qua Dabble, chúng ta có thể sử dụng các nút GamePad để thực hiện những chức năng như:

- Điều khiển xe tiến.
- Điều khiển xe lùi.
- Điều khiển xe rẽ trái.
- Điều khiển xe rẽ phải.
- Điều khiển servo.
- Thực hiện các chức năng bổ sung.

### 8.2. Các bước cài đặt

Thực hiện:

1. Mở Arduino IDE.
2. Mở Library Manager.
3. Nhập từ khóa `Dabble`.
4. Tìm thư viện **Dabble** của STEMpedia.
5. Kiểm tra đúng tên và tác giả.
6. Nhấn Install.
7. Chờ quá trình cài đặt hoàn tất.

**Lưu ý:** Bộ xe sử dụng Arduino Nano, không phải ESP32. Không chọn thư viện `DabbleESP32` thay cho thư viện Dabble dành cho các bo Arduino tương thích.

Kho mã nguồn của dự án Dabble:

https://github.com/STEMpedia/Dabble

### 8.3. Khai báo Dabble trong chương trình

Để sử dụng GamePad, chương trình thường khai báo:

```cpp
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE

#include <Dabble.h>
```

Trong đó:

- `CUSTOM_SETTINGS`: Cho phép lựa chọn các chức năng Dabble cần sử dụng.
- `INCLUDE_GAMEPAD_MODULE`: Kích hoạt phần GamePad.
- `#include <Dabble.h>`: Khai báo thư viện Dabble.

Hai dòng `#define` cần được đặt trước dòng `#include <Dabble.h>`.

## 9. Ví dụ 2: Kiểm tra thư viện Dabble

Chúng ta sẽ tạo một chương trình để kiểm tra thư viện Dabble có thể biên dịch trên Arduino Nano hay không.

Trong ví dụ này, chưa cần kết nối điện thoại hoặc module Bluetooth.

### 9.1. Chương trình mẫu

Tạo sketch mới với tên `NanoKiemTraDabble`.

```cpp
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE

#include <Dabble.h>

// ================= BLUETOOTH =================
#define BT_RX A3
#define BT_TX A2

// ================= SETUP =================
void setup() {
  Dabble.begin(9600, BT_RX, BT_TX);
}

// ================= LOOP =================
void loop() {
  Dabble.processInput();

  if (GamePad.isUpPressed()) {
    // Nhan nut Up
  }

  if (GamePad.isDownPressed()) {
    // Nhan nut Down
  }

  if (GamePad.isLeftPressed()) {
    // Nhan nut Left
  }

  if (GamePad.isRightPressed()) {
    // Nhan nut Right
  }
}
```

### 9.2. Giải thích chương trình

**Khai báo chân Bluetooth**

```cpp
#define BT_RX A3
#define BT_TX A2
```

Theo cấu hình của bộ xe:

- A3: Arduino nhận dữ liệu từ HM-10.
- A2: Arduino gửi dữ liệu đến HM-10.

**Khởi tạo Dabble**

```cpp
Dabble.begin(9600, BT_RX, BT_TX);
```

Lệnh này khởi tạo giao tiếp Dabble với tốc độ 9600 baud trên hai chân đã khai báo, đối với phiên bản thư viện hỗ trợ cú pháp này.

**Xử lý dữ liệu Dabble**

```cpp
Dabble.processInput();
```

Hàm này xử lý dữ liệu nhận được để cập nhật trạng thái các nút và chức năng của Dabble.

**Kiểm tra trạng thái GamePad**

```cpp
if (GamePad.isUpPressed()) {
  // Nhan nut Up
}
```

Điều kiện này kiểm tra trạng thái nút Up.

Trong chương trình kiểm tra thư viện, chúng ta chưa cần viết lệnh điều khiển động cơ bên trong điều kiện.

### 9.3. Thực hiện Verify

Thực hiện:

1. Chọn Arduino Nano.
2. Kiểm tra Processor.
3. Nhấn Verify.
4. Quan sát thông báo biên dịch.

**Kết quả mong đợi:** Chương trình biên dịch thành công và không xuất hiện lỗi thiếu `Dabble.h`.

Nếu xuất hiện lỗi liên quan đến hàm `Dabble.begin()` hoặc `GamePad`, cần kiểm tra phiên bản thư viện, loại bo và cú pháp được thư viện hỗ trợ.

Không nên thay đổi sơ đồ chân Bluetooth hoặc các lệnh điều khiển robot chỉ để xử lý lỗi cài đặt thư viện.

Để thực hành kết nối điện thoại và điều khiển robot, xem [Bài 9: Bluetooth HM-10 và Dabble](bai-giang/09-bluetooth.md).

## 10. Cài đặt thư viện từ tệp ZIP

Ngoài Library Manager, Arduino IDE còn hỗ trợ cài đặt thư viện từ tệp ZIP.

Phương pháp này thường được sử dụng khi:

- Nhà sản xuất cung cấp thư viện riêng.
- Thư viện chưa có trong Library Manager.
- Cần sử dụng một phiên bản thư viện cụ thể.
- Thư viện được tải từ kho mã nguồn chính thức.

### 10.1. Chuẩn bị tệp ZIP

Trước tiên, tải tệp ZIP của thư viện từ nguồn phù hợp.

Cần phân biệt:

- ZIP chứa thư viện Arduino.
- ZIP chứa chương trình mẫu.
- ZIP chứa toàn bộ dự án hoặc tài liệu.

Không phải mọi tệp ZIP đều có thể cài bằng chức năng Add .ZIP Library.

### 10.2. Cài đặt từ ZIP

Trong Arduino IDE, chọn:

**Sketch → Include Library → Add .ZIP Library**

Sau đó:

1. Chọn tệp ZIP đã tải.
2. Nhấn Open.
3. Chờ Arduino IDE xử lý và cài đặt.
4. Kiểm tra thông báo kết quả.
5. Mở chương trình sử dụng thư viện.
6. Nhấn Verify để kiểm tra.

### 10.3. Kiểm tra sau khi cài

Nếu thư viện được cài đúng, Arduino IDE có thể tìm thấy các tệp header tương ứng khi biên dịch.

Ví dụ:

```cpp
#include <Servo.h>
```

Hoặc:

```cpp
#include <Dabble.h>
```

Nếu thư viện đã cài nhưng vẫn báo lỗi, cần kiểm tra cấu trúc thư viện, tên tệp và phiên bản đang được IDE sử dụng.

### 10.4. Không nhầm thư viện với chương trình Arduino

Tệp `.ino` là tệp chương trình Arduino.

Ví dụ:

```text
test_bluetooth.ino
```

Tệp này thường được mở bằng:

**File → Open**

Không sử dụng Add .ZIP Library để cài một chương trình `.ino` thông thường.

Tương tự, một thư mục chứa nhiều sketch của xe robot không nhất thiết là thư viện Arduino.

## 11. Cách kiểm tra thư viện đã được cài đặt

Có nhiều cách kiểm tra thư viện trong Arduino IDE.

### 11.1. Kiểm tra bằng Library Manager

Mở Library Manager và tìm tên thư viện.

Nếu thư viện đã được cài đặt, IDE sẽ hiển thị trạng thái tương ứng.

Đây là cách đơn giản để kiểm tra việc cài đặt.

### 11.2. Kiểm tra bằng chương trình mẫu

Một số thư viện cung cấp chương trình ví dụ.

Có thể mở thông qua:

**File → Examples**

Sau đó tìm nhóm ví dụ của thư viện đã cài.

Ví dụ, thư viện Servo có các chương trình minh họa điều khiển servo.

### 11.3. Kiểm tra bằng Verify

Đây là bước quan trọng nhất trong bài học.

Ví dụ:

```cpp
#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(A5);
}

void loop() {

}
```

Nếu chương trình biên dịch thành công cho Arduino Nano, có thể xác nhận thư viện đang được IDE sử dụng phù hợp với chương trình kiểm tra này.

**Lưu ý:** Verify thành công chỉ xác nhận quá trình biên dịch phần mềm. Nó không xác nhận module ngoại vi đã được kết nối hoặc hoạt động chính xác.

## 12. Một số lỗi thường gặp khi sử dụng thư viện

### 12.1. Lỗi không tìm thấy tệp thư viện

Ví dụ:

```text
fatal error: Servo.h: No such file or directory
```

Hoặc:

```text
fatal error: Dabble.h: No such file or directory
```

**Nguyên nhân có thể gồm:**

- Chưa cài thư viện.
- Cài sai thư viện.
- Tên tệp trong `#include` không đúng.
- Thư viện chưa được IDE nhận diện.
- Thư viện được cài vào sai cấu trúc thư mục.

**Cách xử lý:**

1. Mở Library Manager.
2. Tìm đúng tên thư viện.
3. Kiểm tra trạng thái cài đặt.
4. Kiểm tra dòng `#include`.
5. Biên dịch lại chương trình.

### 12.2. Có nhiều thư viện cùng tên

Arduino IDE có thể hiển thị thông báo:

```text
Multiple libraries were found for "Servo.h"
```

Thông báo này cho biết IDE tìm thấy nhiều thư viện có khả năng cung cấp tệp header tương ứng.

Cần kiểm tra đường dẫn thư viện mà IDE đã lựa chọn sử dụng.

Không nên xóa toàn bộ thư viện chỉ vì xuất hiện thông báo này.

Nếu chương trình biên dịch thành công và sử dụng đúng thư viện mong muốn, thông báo có thể không phải lỗi cần xử lý.

### 12.3. Thư viện không hỗ trợ bo mạch

Một số thư viện chỉ được thiết kế cho những dòng vi điều khiển nhất định.

Ví dụ, thư viện dành riêng cho ESP32 có thể sử dụng các hàm hoặc phần cứng không tồn tại trên Arduino Nano ATmega328P.

Khi đó, quá trình biên dịch có thể xuất hiện lỗi liên quan đến kiến trúc hoặc những hàm không được hỗ trợ.

**Cách xử lý:**

- Kiểm tra Board đang chọn.
- Kiểm tra tác giả và phiên bản thư viện.
- Đọc thông tin tương thích của thư viện.
- Sử dụng thư viện phù hợp với Arduino Nano.

### 12.4. Đã cài thư viện nhưng chương trình vẫn báo lỗi

Không phải mọi lỗi sau khi cài thư viện đều do thiếu thư viện.

Ví dụ:

- Sai tên hàm.
- Sai số lượng tham số.
- Sử dụng cú pháp của phiên bản thư viện khác.
- Thiếu một thư viện phụ thuộc.
- Chọn sai loại bo mạch.
- Chương trình có lỗi cú pháp ở phần khác.

Khi gặp trường hợp này, cần đọc **thông báo lỗi đầu tiên có ý nghĩa** trong Output thay vì chỉ xem dòng thông báo biên dịch thất bại ở cuối.

### 12.5. Chương trình biên dịch thành công nhưng thiết bị không hoạt động

Nếu Verify thành công nhưng servo hoặc Bluetooth không hoạt động, cần kiểm tra phần cứng và chương trình điều khiển.

Ví dụ:

- Servo chưa được cấp nguồn đúng.
- Dây tín hiệu servo nối sai chân.
- Module Bluetooth chưa được cấp nguồn.
- TX/RX nối không đúng.
- Tốc độ baud của module không phù hợp.
- Điện thoại chưa kết nối Dabble.
- Chương trình chưa xử lý dữ liệu như mong muốn.

Không nên cài lại thư viện ngay khi chưa xác định nguyên nhân.

## 13. Quy trình kiểm tra khi gặp lỗi thư viện

Khi chương trình báo lỗi liên quan đến thư viện, có thể kiểm tra theo trình tự sau:

1. Xác định tên thư viện từ dòng `#include`.
2. Kiểm tra thư viện đã được cài đặt hay chưa.
3. Đối chiếu tên và tác giả thư viện.
4. Kiểm tra khả năng tương thích với Arduino Nano.
5. Kiểm tra phiên bản thư viện.
6. Mở chương trình kiểm tra tối giản.
7. Nhấn Verify.
8. Đọc thông báo lỗi nếu vẫn chưa biên dịch thành công.

Ví dụ:

```text
Chương trình báo thiếu Servo.h
          |
          v
Kiểm tra Library Manager
          |
          v
Đã cài đúng Servo chưa?
          |
     +----+----+
     |         |
    Chưa       Rồi
     |         |
     v         v
Cài Servo   Kiểm tra tên include
     |         |
     +----+----+
          |
          v
Verify sketch kiểm tra
          |
          v
Biên dịch thành công?
          |
     +----+----+
     |         |
    Có        Không
     |         |
     v         v
Tiếp tục    Đọc lỗi đầu tiên,
bài học     kiểm tra phiên bản
            và thư viện phụ thuộc
```

Cách kiểm tra theo từng bước giúp xác định nguyên nhân chính xác hơn so với việc cài thêm nhiều thư viện không liên quan.

## 14. Bài tập thực hành

**Bài tập 1: Tìm hiểu thư viện**

Trả lời các câu hỏi:

1. Thư viện Arduino là gì?
2. Board Package và Library khác nhau như thế nào?
3. Dòng `#include <Servo.h>` có chức năng gì?
4. Verify thành công có chứng minh servo đang hoạt động không?

**Bài tập 2: Cài đặt Servo**

Sử dụng Library Manager để tìm và cài đặt thư viện Servo.

Sau đó, tạo chương trình sử dụng đối tượng Servo và kiểm tra bằng Verify.

**Bài tập 3: Cài đặt Dabble**

Tìm thư viện Dabble của STEMpedia.

Cài đặt thư viện và Verify chương trình kiểm tra GamePad.

**Bài tập 4: Xác định thư viện trong chương trình**

Cho chương trình:

```cpp
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE

#include <Dabble.h>
#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(A5);
}

void loop() {
  Dabble.processInput();
}
```

Hãy xác định:

1. Chương trình sử dụng những thư viện nào?
2. Thư viện nào phục vụ điều khiển servo?
3. Thư viện nào phục vụ nhận dữ liệu từ ứng dụng điện thoại?
4. Chương trình có thể cần những thư viện nào được cài thêm trước khi Verify?

**Bài tập 5: Phân tích lỗi**

Giả sử Arduino IDE báo:

```text
fatal error: Dabble.h: No such file or directory
```

Hãy mô tả các bước cần kiểm tra để xử lý lỗi này.

## 15. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu và thực hành:

- Khái niệm và vai trò của thư viện Arduino.
- Sự khác biệt giữa Board Package và Library.
- Cách xác định thư viện được sử dụng trong chương trình.
- Cách sử dụng Library Manager.
- Cách cài đặt thư viện Servo.
- Cách cài đặt thư viện Dabble.
- Cách cài thư viện từ tệp ZIP.
- Cách sử dụng Verify để kiểm tra thư viện.
- Cách xác định và xử lý những lỗi thư viện thường gặp.

Sau khi hoàn thành, bạn cần đạt được các kết quả:

1. Biết cách tìm và cài đặt đúng thư viện cho Arduino Nano.
2. Biên dịch thành công chương trình kiểm tra Servo.
3. Biên dịch thành công chương trình kiểm tra Dabble với phiên bản thư viện phù hợp.
4. Phân biệt được lỗi thư viện với lỗi kết nối phần cứng.

Việc cài đặt và kiểm tra thư viện đúng cách là bước chuẩn bị quan trọng trước khi thực hành điều khiển servo SG90, sử dụng Bluetooth HM-10 và xây dựng các chương trình điều khiển robot hoàn chỉnh.

---

[Bài điều khiển Servo SG90](bai-giang/04-servo.md) · [Bài Bluetooth HM-10](bai-giang/09-bluetooth.md) · [Xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) · [Lộ trình học](index.md)