# Bài 5: Cài đặt và quản lý thư viện ESP32

## 1. Giới thiệu

Trong các bài học trước, chúng ta đã cài đặt Arduino IDE, driver CH340, gói hỗ trợ ESP32 và thực hành nạp chương trình vào bo mạch.

Tuy nhiên, khi lập trình các chức năng phức tạp hơn như điều khiển servo, giao tiếp Wi-Fi hoặc xây dựng giao diện điều khiển robot, chúng ta thường cần sử dụng thêm các **thư viện lập trình**.

Thư viện cung cấp những hàm và công cụ được xây dựng sẵn, giúp người lập trình sử dụng các chức năng của vi điều khiển mà không phải viết lại toàn bộ chương trình từ đầu.

Trong bài học này, chúng ta sẽ thực hiện:

- Tìm hiểu thư viện Arduino là gì.
- Phân biệt gói hỗ trợ ESP32 và thư viện lập trình.
- Làm quen với Library Manager.
- Cài đặt các thư viện cần thiết cho bộ xe robot ESP32.
- Tìm hiểu cách sử dụng thư viện trong chương trình.
- Kiểm tra thư viện bằng một chương trình đơn giản.
- Xử lý một số lỗi thường gặp khi sử dụng thư viện.

Sau khi hoàn thành, bạn sẽ biết cách chuẩn bị các thư viện cần thiết để lập trình cảm biến, động cơ, servo và các chức năng điều khiển robot qua Wi-Fi.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Hiểu thư viện là gì và vai trò của thư viện trong lập trình ESP32.
- Phân biệt thư viện tích hợp và thư viện cần cài đặt thêm.
- Sử dụng Library Manager để tìm kiếm và cài đặt thư viện.
- Cài đặt thư viện từ tệp ZIP.
- Biết cách khai báo thư viện bằng `#include`.
- Xác định các thư viện cần thiết cho chương trình robot.
- Kiểm tra và quản lý phiên bản thư viện.
- Nhận biết và xử lý lỗi thiếu thư viện khi biên dịch.

---

## 3. Tìm hiểu về thư viện Arduino

### 3.1. Thư viện là gì?

Thư viện (*Library*) là tập hợp các đoạn mã, hàm và lớp đã được xây dựng để thực hiện những chức năng cụ thể.

Ví dụ, khi muốn kết nối ESP32 với Wi-Fi, chúng ta không cần tự viết toàn bộ chương trình điều khiển phần cứng Wi-Fi.

Thay vào đó, có thể sử dụng thư viện `WiFi.h` để thực hiện các thao tác như:

- Khởi tạo Wi-Fi.
- Kết nối đến mạng Wi-Fi.
- Tạo mạng Wi-Fi riêng.
- Kiểm tra trạng thái kết nối.
- Lấy địa chỉ IP.

Tương tự, khi điều khiển servo, chúng ta có thể sử dụng thư viện ESP32Servo để tạo tín hiệu điều khiển phù hợp.

Việc sử dụng thư viện giúp:

- Giảm số lượng mã cần viết.
- Đơn giản hóa việc giao tiếp với phần cứng.
- Dễ dàng tái sử dụng chương trình.
- Thuận tiện khi phát triển các chức năng mới.
- Giảm những lỗi do phải tự xây dựng các chức năng cấp thấp.

### 3.2. Phân biệt Board Package và Library

Khi lập trình ESP32 bằng Arduino IDE, chúng ta cần phân biệt ba thành phần:

| Thành phần | Ví dụ | Chức năng |
|---|---|---|
| Board Package | esp32 by Espressif Systems | Cung cấp công cụ biên dịch, nạp chương trình và hỗ trợ phần cứng ESP32 |
| Thư viện đi kèm ESP32 core | WiFi | Cung cấp các chức năng có sẵn khi cài gói ESP32 |
| Thư viện bên ngoài | ESP32Servo, ESPAsyncWebServer | Bổ sung các chức năng cần thiết cho chương trình |

**Board Package** được cài đặt thông qua **Boards Manager**.

**Library** thường được quản lý thông qua **Library Manager**.

Một số thư viện đã có sẵn khi cài ESP32 core, trong khi những thư viện khác cần được cài đặt bổ sung.

Ví dụ, `WiFi.h` được cung cấp cùng Arduino-ESP32 core. Vì vậy, không cần tìm và cài một thư viện WiFi không liên quan để thay thế.

Nếu Arduino IDE báo không tìm thấy `WiFi.h`, trước tiên cần kiểm tra đã cài gói ESP32 và chọn đúng bo mạch hay chưa.

---

## 4. Làm quen với Library Manager

### 4.1. Library Manager là gì?

Library Manager là công cụ quản lý thư viện được tích hợp trong Arduino IDE.

Thông qua Library Manager, chúng ta có thể:

- Tìm kiếm thư viện.
- Cài đặt thư viện.
- Kiểm tra phiên bản đang sử dụng.
- Cập nhật thư viện.
- Cài đặt một phiên bản cụ thể khi cần.

Đây là phương pháp thuận tiện để cài đặt các thư viện phổ biến.

### 4.2. Mở Library Manager

Thực hiện:

1. Mở Arduino IDE.
2. Chọn biểu tượng **Library Manager** ở thanh công cụ bên trái.
3. Nhập tên thư viện vào ô tìm kiếm.
4. Quan sát danh sách kết quả.

Ví dụ, nhập:

```text
ESP32Servo
```

Arduino IDE sẽ hiển thị những thư viện phù hợp với từ khóa tìm kiếm.

### 4.3. Cài đặt thư viện

Sau khi tìm được thư viện:

1. Kiểm tra tên thư viện.
2. Kiểm tra tác giả hoặc dự án phát triển.
3. Kiểm tra thư viện có hỗ trợ ESP32 hay không.
4. Chọn phiên bản phù hợp.
5. Nhấn **Install**.
6. Chờ quá trình cài đặt hoàn tất.

Nếu Arduino IDE yêu cầu cài đặt thêm các thư viện phụ thuộc (*dependencies*), cần kiểm tra và cài đặt những thành phần cần thiết.

**Lưu ý:** Có thể tồn tại nhiều thư viện có tên gần giống nhau. Vì vậy, không nên chỉ dựa vào tên tìm kiếm mà cần đối chiếu tác giả và khả năng tương thích.

---

## 5. Các thư viện sử dụng trong bộ xe robot ESP32

Bộ xe robot ESP32 Robovis sử dụng các thư viện để thực hiện những chức năng như kết nối Wi-Fi, tạo giao diện điều khiển web và điều khiển servo.

Chương trình nguồn được cung cấp tại:

[Bộ mã nguồn robot ESP32 Robovis](https://drive.google.com/drive/folders/1HeAZaW--JOkl67SG3IJOWxS1aPKAO5UB)

### 5.1. Danh sách thư viện

Các thư viện cần thiết cho bộ chương trình gồm:

| STT | Thư viện | Nguồn / tác giả | Chức năng |
|---|---|---|---|
| 1 | WiFi | Arduino-ESP32 core | Kết nối và tạo mạng Wi-Fi |
| 2 | AsyncTCP | ESP32Async | Giao tiếp TCP bất đồng bộ |
| 3 | ESPAsyncWebServer | ESP32Async | Xây dựng web server điều khiển robot |
| 4 | ESP32Servo | Kevin Harrington / madhephaestus | Điều khiển servo trên ESP32 |

Trong đó:

- `WiFi.h` có sẵn khi cài gói hỗ trợ ESP32.
- `AsyncTCP` cần được cài đặt thêm.
- `ESPAsyncWebServer` cần được cài đặt thêm.
- `ESP32Servo` cần được cài đặt thêm.

Ngoài các thư viện trên, chương trình robot còn có thể sử dụng những tệp mã nguồn riêng của sản phẩm, chẳng hạn `do_line.h`.

Các tệp mã nguồn của dự án không nhất thiết là thư viện cần tìm trong Library Manager.

### 5.2. Thư viện WiFi

Thư viện WiFi cho phép ESP32 sử dụng phần cứng Wi-Fi tích hợp.

Ví dụ, ESP32 có thể tạo một mạng Wi-Fi riêng để điện thoại kết nối trực tiếp.

Trong chương trình robot, ESP32 tạo mạng Wi-Fi có tên:

**ESP32-Car**

Người dùng kết nối điện thoại hoặc máy tính đến mạng này để sử dụng giao diện điều khiển robot.

Để sử dụng thư viện WiFi, khai báo:

```cpp
#include <WiFi.h>
```

Một số hàm thường gặp:

| Hàm | Chức năng |
|---|---|
| `WiFi.mode()` | Cấu hình chế độ hoạt động Wi-Fi |
| `WiFi.begin()` | Kết nối đến mạng Wi-Fi có sẵn |
| `WiFi.softAP()` | Tạo mạng Wi-Fi Access Point |
| `WiFi.status()` | Kiểm tra trạng thái kết nối |
| `WiFi.localIP()` | Lấy địa chỉ IP ở chế độ Station |
| `WiFi.softAPIP()` | Lấy địa chỉ IP của Access Point |

Thư viện này sẽ được tìm hiểu chi tiết trong bài điều khiển xe qua Wi-Fi.

### 5.3. Thư viện AsyncTCP

AsyncTCP hỗ trợ giao tiếp TCP bất đồng bộ trên ESP32.

TCP là giao thức truyền dữ liệu qua mạng, được sử dụng trong nhiều ứng dụng kết nối Wi-Fi.

Thư viện AsyncTCP thường được sử dụng làm thành phần phụ thuộc của ESPAsyncWebServer.

Để cài đặt:

1. Mở Library Manager.
2. Tìm kiếm `AsyncTCP`.
3. Chọn thư viện thuộc dự án **ESP32Async**.
4. Nhấn Install.

Dự án tham khảo:

https://github.com/ESP32Async/AsyncTCP

**Lưu ý:** Không nhầm `AsyncTCP` dành cho ESP32 với `ESPAsyncTCP` dành cho ESP8266.

Trong tài liệu bàn giao có thể xuất hiện tên ESPAsyncTCP, nhưng đối với bộ mã ESP32 sử dụng AsyncTCP, cần cài đúng thư viện dành cho ESP32.

### 5.4. Thư viện ESPAsyncWebServer

ESPAsyncWebServer được sử dụng để xây dựng web server trên ESP32.

Web server cho phép ESP32 tiếp nhận các yêu cầu từ trình duyệt và gửi dữ liệu phản hồi.

Trong bộ xe robot, thư viện này được sử dụng để xây dựng giao diện điều khiển qua Wi-Fi.

Ví dụ:

- Hiển thị trang điều khiển trên điện thoại.
- Nhận lệnh điều khiển chuyển động.
- Xử lý yêu cầu từ trình duyệt.
- Trao đổi dữ liệu giữa giao diện và ESP32.

Để cài đặt:

1. Mở Library Manager.
2. Tìm kiếm `ESPAsyncWebServer`.
3. Chọn thư viện thuộc dự án **ESP32Async**.
4. Nhấn Install.
5. Cài đặt các dependency cần thiết nếu Arduino IDE yêu cầu.

Dự án tham khảo:

https://github.com/ESP32Async/ESPAsyncWebServer

### 5.5. Thư viện ESP32Servo

ESP32Servo là thư viện hỗ trợ điều khiển động cơ servo bằng ESP32.

Thư viện cung cấp các chức năng như:

- Khởi tạo servo.
- Gắn servo với chân GPIO.
- Điều khiển vị trí servo.
- Thiết lập tín hiệu điều khiển phù hợp.

Để cài đặt:

1. Mở Library Manager.
2. Tìm kiếm `ESP32Servo`.
3. Chọn thư viện thuộc dự án của Kevin Harrington / madhephaestus.
4. Nhấn Install.

Dự án tham khảo:

https://github.com/madhephaestus/ESP32Servo

Trong chương trình, thư viện thường được khai báo:

```cpp
#include <ESP32Servo.h>
```

Ví dụ khởi tạo đối tượng servo:

```cpp
Servo myServo;
```

Để sử dụng servo thực tế, cần kết nối đúng chân tín hiệu và nguồn cấp phù hợp.

**Lưu ý:** Bộ mã `main.ino` của robot có sử dụng `ESP32Servo.h`. Vì vậy, thư viện ESP32Servo vẫn cần được cài đặt để biên dịch chương trình, kể cả khi phiên bản robot hiện tại chưa lắp cơ cấu gắp.

Không thay thế thư viện này bằng thư viện Servo dành cho Arduino Nano ATmega328P.

---

## 6. Cài đặt thư viện từ tệp ZIP

Ngoài Library Manager, Arduino IDE còn hỗ trợ cài đặt thư viện từ tệp ZIP.

Phương pháp này thường được sử dụng khi:

- Nhà sản xuất cung cấp thư viện riêng.
- Thư viện không có trong Library Manager.
- Cần sử dụng một phiên bản thư viện cụ thể.
- Bộ mã nguồn đi kèm thư viện dưới dạng tệp ZIP.

### 6.1. Các bước thực hiện

1. Tải tệp ZIP của thư viện về máy tính.
2. Mở Arduino IDE.
3. Chọn **Sketch → Include Library → Add .ZIP Library**.
4. Chọn tệp ZIP vừa tải.
5. Xác nhận để Arduino IDE thực hiện cài đặt.

Sau khi hoàn thành, Arduino IDE sẽ thông báo kết quả cài đặt.

### 6.2. Kiểm tra thư viện đã cài

Có thể kiểm tra bằng cách:

1. Mở Library Manager.
2. Tìm tên thư viện.
3. Kiểm tra trạng thái và phiên bản nếu thư viện được Library Manager nhận diện.

Ngoài ra, có thể mở chương trình sử dụng thư viện và nhấn Verify.

Nếu chương trình biên dịch thành công, các tệp thư viện cần thiết đã được trình biên dịch tìm thấy và sử dụng.

Tuy nhiên, việc biên dịch thành công chưa đảm bảo phần cứng sẽ hoạt động đúng khi chạy thực tế.

Hướng dẫn chính thức của Arduino:

https://support.arduino.cc/hc/en-us/articles/5145457742236-Install-libraries-in-the-Arduino-IDE

---

## 7. Sử dụng thư viện trong chương trình

### 7.1. Khai báo thư viện

Trong Arduino, thư viện thường được khai báo bằng chỉ thị:

```cpp
#include <TenThuVien.h>
```

Ví dụ:

```cpp
#include <WiFi.h>
```

Dòng lệnh trên cho phép chương trình sử dụng các khai báo và chức năng do thư viện WiFi cung cấp.

Tương tự:

```cpp
#include <ESP32Servo.h>
```

Cho phép sử dụng các thành phần của thư viện ESP32Servo.

### 7.2. Vị trí khai báo thư viện

Các dòng `#include` thường được đặt ở đầu chương trình.

Ví dụ:

```cpp
#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <ESP32Servo.h>

void setup() {

}

void loop() {

}
```

Đây là ví dụ minh họa cách khai báo thư viện, chưa phải một chương trình điều khiển hoàn chỉnh.

Khi biên dịch, Arduino IDE cần tìm được các thư viện tương ứng.

Nếu thiếu một thư viện, quá trình biên dịch có thể thất bại.

### 7.3. Thư viện và tệp mã nguồn trong dự án

Một chương trình Arduino có thể được chia thành nhiều tệp.

Ví dụ:

```text
main/
├── main.ino
├── do_line.h
└── do_line.cpp
```

Đây là ví dụ minh họa cấu trúc dự án có nhiều tệp; các tệp thực tế phải được xác định theo bộ mã nguồn bàn giao.

Trong đó:

- `main.ino` là tệp chương trình chính.
- `do_line.h` có thể chứa các khai báo phục vụ chức năng dò line.
- `do_line.cpp`, nếu có, có thể chứa phần triển khai các hàm tương ứng.

Không phải mọi tệp `.h` đều là thư viện phải cài từ Library Manager.

Nếu một tệp `.h` được cung cấp cùng chương trình, cần giữ đúng cấu trúc thư mục của dự án.

Với bộ mã robot Robovis, cần tải **toàn bộ thư mục `main`**, không chỉ tải riêng tệp `main.ino`.

---

## 8. Thực hành kiểm tra thư viện WiFi

### 8.1. Mục tiêu thực hành

Trong phần này, chúng ta sẽ viết một chương trình đơn giản để kiểm tra thư viện WiFi có hoạt động với ESP32 hay không.

Chương trình sẽ:

1. Khởi tạo giao tiếp Serial.
2. Thiết lập Wi-Fi ở chế độ Station.
3. Gửi thông báo đến Serial Monitor.

Chúng ta chưa cần kết nối ESP32 với router và chưa cần nhập mật khẩu Wi-Fi.

### 8.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn:

**File → New Sketch**

Lưu chương trình với tên:

```text
ESP32ThuVien
```

Arduino IDE sẽ tạo tệp:

```text
ESP32ThuVien.ino
```

### 8.3. Chương trình mẫu

Nhập chương trình sau:

```cpp
#include <WiFi.h>

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);

  Serial.println("Da khoi tao WiFi o che do Station");
}

void loop() {
  delay(1000);
}
```

### 8.4. Giải thích chương trình

**Khai báo thư viện**

```cpp
#include <WiFi.h>
```

Cho phép sử dụng các chức năng Wi-Fi của ESP32.

**Khởi tạo Serial**

```cpp
Serial.begin(115200);
```

Khởi tạo giao tiếp Serial với tốc độ 115200 baud.

**Thiết lập chế độ Wi-Fi**

```cpp
WiFi.mode(WIFI_STA);
```

Đưa Wi-Fi vào chế độ Station.

Ở chế độ này, ESP32 có thể kết nối đến một mạng Wi-Fi có sẵn khi chương trình cung cấp thông tin kết nối.

Trong ví dụ hiện tại, chúng ta chưa thực hiện kết nối đến mạng nào.

**Gửi thông báo**

```cpp
Serial.println("Da khoi tao WiFi o che do Station");
```

Gửi một dòng thông báo đến Serial Monitor.

**Vòng lặp chính**

```cpp
void loop() {
  delay(1000);
}
```

Chương trình chờ 1000 ms trong mỗi lần lặp và không thực hiện thêm chức năng nào.

### 8.5. Biên dịch chương trình

Trước khi biên dịch:

1. Chọn Board là **ESP32 Dev Module**.
2. Kiểm tra đã cài ESP32 core.
3. Nhấn **Verify**.

Nếu chương trình biên dịch thành công, Arduino IDE sẽ hiển thị thông báo hoàn tất và thông tin dung lượng chương trình.

Điều này cho thấy trình biên dịch đã tìm thấy thư viện WiFi cần thiết.

### 8.6. Nạp và kiểm tra

Sau khi Verify thành công:

1. Kết nối ESP32 với máy tính.
2. Chọn đúng cổng COM.
3. Nhấn **Upload**.
4. Chờ quá trình nạp hoàn tất.
5. Mở Serial Monitor.
6. Chọn tốc độ 115200 baud.
7. Nhấn nút EN/RESET trên ESP32 để chạy lại chương trình.

Kết quả mong đợi:

```text
Da khoi tao WiFi o che do Station
```

Nếu xuất hiện thông báo trên, chương trình đã thực hiện đến lệnh in Serial sau khi gọi hàm thiết lập chế độ Wi-Fi.

### 8.7. Lưu ý khi thực hành trên robot

Chương trình kiểm tra thư viện là một sketch độc lập.

Khi Upload, chương trình này sẽ thay thế chương trình ứng dụng robot đang lưu trên ESP32.

Do đó, sau khi thực hành, robot sẽ không tự động tạo mạng **ESP32-Car** hoặc chạy giao diện điều khiển cũ.

Để khôi phục chức năng robot, cần nạp lại bộ chương trình `main` đã được bàn giao.

Trong chương trình robot, chế độ tạo mạng Wi-Fi riêng được thực hiện thông qua các chức năng như `WiFi.softAP()`.

---

## 9. Kiểm tra thư viện của chương trình robot

Sau khi cài đặt các thư viện cần thiết, chúng ta nên kiểm tra khả năng biên dịch của bộ mã robot.

### 9.1. Chuẩn bị mã nguồn

Tải bộ mã nguồn từ:

[Thư mục chương trình robot ESP32 Robovis](https://drive.google.com/drive/folders/1HeAZaW--JOkl67SG3IJOWxS1aPKAO5UB)

Giữ nguyên toàn bộ các tệp trong thư mục `main`.

Không chỉ mở một tệp mã riêng lẻ rồi bỏ qua các tệp còn lại.

### 9.2. Mở chương trình

Trong Arduino IDE:

1. Chọn **File → Open**.
2. Tìm đến thư mục `main`.
3. Mở `main.ino`.
4. Kiểm tra các tệp khác của dự án được giữ đúng vị trí.

### 9.3. Kiểm tra cấu hình

Chọn:

- Board: **ESP32 Dev Module**.
- ESP32 core: Phiên bản phù hợp với bộ mã.
- Các thư viện ngoài: Đã cài đầy đủ.

Sau đó nhấn **Verify**.

Nếu xuất hiện lỗi, cần đọc thông báo để xác định nguyên nhân.

Không nên cập nhật đồng loạt tất cả thư viện khi chưa biết thư viện nào gây lỗi.

---

## 10. Các lỗi thường gặp khi sử dụng thư viện

### 10.1. Lỗi No such file or directory

Ví dụ:

```text
fatal error: ESP32Servo.h: No such file or directory
```

Lỗi này cho biết trình biên dịch không tìm thấy tệp header được yêu cầu.

Nguyên nhân có thể:

- Chưa cài thư viện.
- Cài sai thư viện.
- Tên tệp trong `#include` không đúng.
- Thư viện được cài sai vị trí.
- Thiếu tệp mã nguồn đi kèm dự án.

**Cách xử lý:**

1. Kiểm tra tên header trong chương trình.
2. Mở Library Manager.
3. Tìm đúng thư viện.
4. Kiểm tra tác giả và phiên bản.
5. Cài đặt thư viện còn thiếu.
6. Verify lại chương trình.

Nếu tệp bị thiếu là `do_line.h`, cần kiểm tra bộ mã nguồn `main` thay vì tìm một thư viện bất kỳ có tên tương tự.

### 10.2. Lỗi thiếu WiFi.h

Ví dụ:

```text
fatal error: WiFi.h: No such file or directory
```

Với ESP32, thư viện WiFi thường được cung cấp cùng ESP32 core.

**Cách xử lý:**

1. Kiểm tra đã cài `esp32 by Espressif Systems`.
2. Kiểm tra Board đang chọn là ESP32 Dev Module.
3. Kiểm tra gói ESP32 đã cài đặt hoàn chỉnh.
4. Verify lại chương trình.

Không nên cài một thư viện WiFi ngẫu nhiên để thay thế thư viện của ESP32 core.

### 10.3. Lỗi thiếu thư viện phụ thuộc

Một thư viện có thể cần các thư viện khác để hoạt động.

Ví dụ, ESPAsyncWebServer sử dụng AsyncTCP trong cấu hình ESP32 tương ứng.

Nếu thiếu dependency, chương trình có thể báo lỗi không tìm thấy header hoặc các thành phần cần thiết.

**Cách xử lý:**

- Kiểm tra tài liệu của thư viện.
- Cài đúng các dependency được yêu cầu.
- Kiểm tra phiên bản tương thích.
- Verify lại chương trình.

### 10.4. Lỗi thư viện không hỗ trợ ESP32

Một số thư viện được phát triển cho Arduino Uno, Nano hoặc ESP8266 nhưng không hỗ trợ ESP32.

Khi sử dụng, Arduino IDE có thể hiển thị cảnh báo kiến trúc không tương thích hoặc phát sinh lỗi biên dịch.

**Cách xử lý:**

1. Kiểm tra thư viện hỗ trợ kiến trúc nào.
2. Đối chiếu với dòng ESP32 đang sử dụng.
3. Tìm phiên bản hoặc thư viện tương ứng dành cho ESP32.
4. Không tự ý thay thế thư viện nếu chương trình phụ thuộc vào API cụ thể.

Ví dụ, bộ mã robot sử dụng ESP32Servo thay vì thư viện Servo dành cho Arduino Nano classic.

### 10.5. Thông báo Multiple libraries were found

Arduino IDE có thể hiển thị:

```text
Multiple libraries were found for "WiFi.h"
```

Thông báo này cho biết trình biên dịch tìm thấy nhiều thư viện có thể cung cấp cùng một header.

Không phải mọi trường hợp đều là lỗi.

Cần kiểm tra:

- Thư viện nào thực sự được sử dụng.
- Đường dẫn thư viện được chọn.
- Thư viện có phù hợp với ESP32 không.
- Có bản cài đặt trùng lặp không cần thiết hay không.

Nếu cần loại bỏ thư viện trùng, nên sao lưu trước khi thay đổi.

### 10.6. Lỗi do khác phiên bản ESP32 core

Một số chương trình cũ sử dụng các hàm PWM như:

```cpp
ledcSetup();
ledcAttachPin();
```

Các API này đã thay đổi trong Arduino-ESP32 core 3.x.

Nếu chương trình được viết cho core 2.x nhưng đang biên dịch bằng core 3.x, có thể xuất hiện lỗi không nhận diện được hàm.

Đây là vấn đề tương thích API, không nhất thiết là lỗi thiếu thư viện.

**Cách xử lý:**

- Kiểm tra phiên bản ESP32 core.
- Kiểm tra yêu cầu của bộ mã nguồn.
- Sử dụng phiên bản core tương thích hoặc cập nhật mã theo API mới.
- Không thay đổi các phần khác của chương trình khi chưa cần thiết.

---

## 11. Quản lý và cập nhật thư viện

Trong quá trình học, chúng ta có thể cần cài đặt thêm hoặc cập nhật thư viện.

Tuy nhiên, phiên bản mới nhất không phải lúc nào cũng tương thích với chương trình đang sử dụng.

### 11.1. Kiểm tra phiên bản

Mở Library Manager, tìm thư viện và kiểm tra phiên bản đã cài.

Đối với những thư viện quan trọng, nên ghi lại:

| Thành phần | Thông tin cần ghi |
|---|---|
| ESP32 core | Phiên bản đã cài |
| AsyncTCP | Phiên bản đã cài |
| ESPAsyncWebServer | Phiên bản đã cài |
| ESP32Servo | Phiên bản đã cài |

### 11.2. Khi nào nên cập nhật thư viện?

Có thể xem xét cập nhật khi:

- Cần sửa lỗi đã được nhà phát triển khắc phục.
- Cần sử dụng chức năng mới.
- Thư viện cũ không tương thích với môi trường hiện tại.
- Có yêu cầu cập nhật từ dự án.

Trước khi cập nhật, nên giữ lại phiên bản chương trình và thông tin thư viện đang hoạt động ổn định.

### 11.3. Kiểm tra sau khi cập nhật

Sau khi cập nhật thư viện:

1. Verify lại chương trình kiểm tra đơn giản.
2. Verify bộ mã robot hoàn chỉnh.
3. Kiểm tra các thông báo biên dịch.
4. Chỉ nạp lên robot sau khi xác nhận cấu hình phù hợp.
5. Thử nghiệm các chức năng phần cứng một cách an toàn.

Không nên thay đổi đồng thời ESP32 core, nhiều thư viện và mã nguồn robot nếu mục đích chỉ là xử lý một lỗi cụ thể.

---

## 12. Bài tập thực hành

### Bài tập 1: Phân biệt các thành phần

Trả lời:

1. Board Package là gì?
2. Library là gì?
3. ESP32 core được cài đặt ở đâu?
4. ESP32Servo được cài đặt bằng công cụ nào?
5. Vì sao không cần cài thêm thư viện WiFi ngẫu nhiên cho ESP32?

### Bài tập 2: Cài đặt thư viện

Sử dụng Library Manager để tìm và cài đặt:

1. AsyncTCP.
2. ESPAsyncWebServer.
3. ESP32Servo.

Với mỗi thư viện, ghi lại tên, tác giả hoặc dự án và phiên bản đã cài.

### Bài tập 3: Kiểm tra WiFi

Thực hiện:

1. Tạo sketch `ESP32ThuVien`.
2. Nhập chương trình kiểm tra WiFi.
3. Verify chương trình.
4. Upload lên ESP32.
5. Mở Serial Monitor với tốc độ 115200 baud.
6. Kiểm tra thông báo sau khi nhấn EN/RESET.

### Bài tập 4: Kiểm tra mã nguồn robot

Mở toàn bộ dự án `main` của robot.

Thực hiện:

1. Xác định các dòng `#include`.
2. Phân biệt thư viện đi kèm ESP32 core và thư viện ngoài.
3. Xác định các tệp mã nguồn riêng của dự án.
4. Verify toàn bộ chương trình.
5. Ghi lại lỗi nếu quá trình biên dịch không thành công.

---

## 13. Kiểm tra trước khi bắt đầu

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã hiểu thư viện là gì.
- [ ] Đã phân biệt Board Package và Library.
- [ ] Đã biết sử dụng Library Manager.
- [ ] Đã cài đặt AsyncTCP.
- [ ] Đã cài đặt ESPAsyncWebServer.
- [ ] Đã cài đặt ESP32Servo.
- [ ] Đã biết `WiFi.h` đi kèm ESP32 core.
- [ ] Đã biết cách khai báo thư viện bằng `#include`.
- [ ] Đã Verify thành công chương trình kiểm tra WiFi.
- [ ] Đã ghi lại phiên bản ESP32 core và các thư viện ngoài.
- [ ] Đã biết cách kiểm tra lỗi thiếu thư viện khi biên dịch.

---

## 14. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu cách cài đặt và quản lý thư viện khi lập trình ESP32.

Những nội dung quan trọng bao gồm:

- Hiểu vai trò của thư viện trong chương trình.
- Phân biệt gói hỗ trợ ESP32 và thư viện lập trình.
- Cài đặt thư viện bằng Library Manager.
- Cài đặt thư viện từ tệp ZIP.
- Tìm hiểu các thư viện WiFi, AsyncTCP, ESPAsyncWebServer và ESP32Servo.
- Sử dụng `#include` để khai báo thư viện.
- Kiểm tra thư viện bằng chương trình mẫu.
- Xử lý các lỗi thiếu thư viện và không tương thích phiên bản.
- Quản lý phiên bản thư viện để đảm bảo chương trình hoạt động ổn định.

Ở bài tiếp theo, chúng ta sẽ bắt đầu **lập trình các chức năng cơ bản trên ESP32, bao gồm điều khiển LED, đọc trạng thái nút nhấn và tìm hiểu tín hiệu PWM**.

---

[Bài trước: Nạp chương trình và sử dụng Serial Monitor](04-nap-code-va-serial.md) · [Bài tiếp: Lập trình LED, nút nhấn và PWM](06-lap-trinh-co-ban.md)