# Bài 9: Điều khiển xe robot ESP32 qua Wi-Fi và trình duyệt Web

## 1. Giới thiệu

Trong các bài học trước, chúng ta đã tìm hiểu cách điều khiển động cơ DC, đọc cảm biến siêu âm HC-SR04, cảm biến dò line TCRT5000 và đo tốc độ bánh xe bằng Encoder.

Ở bài học này, chúng ta sẽ tìm hiểu cách **điều khiển thiết bị từ xa thông qua Wi-Fi**, một trong những tính năng quan trọng của ESP32.

Khác với Arduino Uno thông thường, ESP32 được tích hợp sẵn Wi-Fi. Nhờ đó, ESP32 có thể giao tiếp với điện thoại hoặc máy tính mà không cần sử dụng thêm module Wi-Fi bên ngoài.

Trong bộ xe robot thực hành, Wi-Fi được sử dụng để tạo giao diện điều khiển trên trình duyệt. Người dùng có thể kết nối trực tiếp với mạng Wi-Fi do robot phát ra và gửi các lệnh điều khiển.

Để hiểu nguyên lý hoạt động, chúng ta sẽ bắt đầu bằng một ví dụ đơn giản: **điều khiển bật/tắt LED thông qua trang web**.

Sau đó, chúng ta sẽ tìm hiểu cách sử dụng giao diện Wi-Fi có sẵn trong chương trình robot đã được bàn giao.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Hiểu khả năng giao tiếp Wi-Fi của ESP32.
- Phân biệt chế độ Station và Access Point.
- Hiểu cách ESP32 tạo một mạng Wi-Fi riêng.
- Hiểu nguyên lý giao tiếp HTTP giữa trình duyệt và ESP32.
- Sử dụng thư viện `WiFi.h` và `WebServer.h`.
- Tạo một Web Server đơn giản trên ESP32.
- Thiết kế giao diện web với các nút điều khiển.
- Điều khiển bật/tắt LED bằng điện thoại hoặc máy tính.
- Hiểu cách ESP32 tiếp nhận và xử lý lệnh từ trình duyệt.
- Phân biệt giao diện điều khiển thử nghiệm và giao diện robot thực tế.
- Kết nối và sử dụng các chế độ Manual và Line Follow trên robot.
- Hiểu những yêu cầu an toàn khi điều khiển động cơ qua Wi-Fi.

---

## 3. Tìm hiểu Wi-Fi trên ESP32

### 3.1. ESP32 có thể sử dụng Wi-Fi như thế nào?

ESP32 được tích hợp bộ thu phát Wi-Fi, cho phép kết nối và trao đổi dữ liệu với các thiết bị khác.

Một số ứng dụng phổ biến gồm:

- Điều khiển robot bằng điện thoại.
- Điều khiển thiết bị điện từ xa.
- Thu thập dữ liệu cảm biến.
- Xây dựng hệ thống nhà thông minh.
- Giám sát thiết bị qua trình duyệt.
- Truyền dữ liệu giữa ESP32 và máy tính.

Trong bài học này, chúng ta sử dụng Wi-Fi để xây dựng một hệ thống điều khiển đơn giản thông qua trình duyệt web.

### 3.2. Chế độ Station (STA)

Ở chế độ Station, ESP32 kết nối vào một mạng Wi-Fi có sẵn, chẳng hạn mạng Wi-Fi của gia đình hoặc phòng học.

Sơ đồ:

```text
           Bộ phát Wi-Fi
             (Router)
                 │
          ┌──────┴──────┐
          │             │
        ESP32       Điện thoại
```

ESP32 và điện thoại có thể trao đổi dữ liệu qua cùng một mạng nội bộ.

Ví dụ, ESP32 kết nối vào mạng Wi-Fi có tên `Classroom-WiFi`, sau đó nhận địa chỉ IP do router cấp.

Để sử dụng chế độ này, cần có mạng Wi-Fi bên ngoài.

### 3.3. Chế độ Access Point (AP)

Ở chế độ Access Point, ESP32 tự tạo một mạng Wi-Fi.

Điện thoại hoặc máy tính có thể kết nối trực tiếp với mạng này mà không cần router.

Sơ đồ:

```text
        ESP32 Robot
      (Wi-Fi Access Point)
              │
              │
       Mạng Wi-Fi riêng
              │
      ┌───────┴───────┐
      │               │
  Điện thoại       Máy tính
```

Ví dụ, ESP32 phát mạng:

```text
Tên Wi-Fi: ESP32-Lesson
Mật khẩu: 12345678
```

Người dùng chỉ cần kết nối điện thoại với mạng `ESP32-Lesson` để truy cập trang web điều khiển.

Đây là chế độ được sử dụng trong bài thực hành.

### 3.4. So sánh Station và Access Point

| Tiêu chí | Station | Access Point |
|---|---|---|
| ESP32 kết nối vào Wi-Fi có sẵn | Có | Không bắt buộc |
| ESP32 tự phát mạng Wi-Fi | Không | Có |
| Cần router bên ngoài | Thường có | Không |
| Điện thoại kết nối trực tiếp với ESP32 | Không theo mô hình STA thông thường | Có |
| Phù hợp điều khiển robot độc lập | Tùy hạ tầng mạng | Có |

Trong bộ robot thực hành, chế độ Access Point thuận tiện vì người dùng có thể điều khiển robot mà không cần kết nối với mạng Wi-Fi bên ngoài.

---

## 4. Nguyên lý điều khiển ESP32 qua trình duyệt

### 4.1. Web Server là gì?

Web Server là chương trình có nhiệm vụ tiếp nhận yêu cầu từ trình duyệt và gửi dữ liệu phản hồi.

Trong bài học này, ESP32 đóng vai trò Web Server.

Điện thoại hoặc máy tính đóng vai trò thiết bị gửi yêu cầu.

Ví dụ, khi người dùng truy cập:

```text
http://192.168.4.1
```

Trình duyệt gửi yêu cầu HTTP đến ESP32.

ESP32 tiếp nhận yêu cầu và gửi lại nội dung trang web.

### 4.2. Nguyên lý gửi lệnh điều khiển

Giả sử trang web có hai nút:

- ON: Bật LED.
- OFF: Tắt LED.

Khi người dùng nhấn ON, trình duyệt gửi yêu cầu đến đường dẫn `/on`.

ESP32 nhận được yêu cầu và đưa chân GPIO điều khiển LED lên mức HIGH.

Khi người dùng nhấn OFF, trình duyệt gửi yêu cầu đến đường dẫn `/off`.

ESP32 nhận được yêu cầu và đưa GPIO xuống mức LOW.

Sơ đồ hoạt động:

```text
       Người dùng
           │
           ▼
      Trình duyệt
           │
           │ HTTP Request
           ▼
      ESP32 Web Server
           │
           ▼
      Xử lý đường dẫn
           │
      ┌────┴────┐
      │         │
     /on       /off
      │         │
      ▼         ▼
  GPIO HIGH  GPIO LOW
      │         │
      ▼         ▼
   LED sáng   LED tắt
```

Như vậy, trình duyệt không trực tiếp điều khiển GPIO.

Trình duyệt chỉ gửi yêu cầu, còn chương trình trên ESP32 quyết định hành động tương ứng.

### 4.3. HTTP Request và HTTP Response

Một quá trình giao tiếp HTTP cơ bản gồm hai phần.

**HTTP Request:** Yêu cầu do trình duyệt gửi đến ESP32.

Ví dụ:

```text
GET /on HTTP/1.1
```

Yêu cầu này có nghĩa trình duyệt muốn truy cập đường dẫn `/on`.

**HTTP Response:** Phản hồi do ESP32 gửi lại.

Ví dụ:

```text
HTTP/1.1 200 OK
Content-Type: text/html
```

Sau phần thông tin phản hồi là nội dung trang HTML.

Trong Arduino, thư viện WebServer giúp chúng ta xử lý những công việc này mà không cần tự xây dựng toàn bộ giao thức HTTP.

---

## 5. Chuẩn bị thiết bị

### 5.1. Thiết bị cần thiết

| STT | Thiết bị | Số lượng |
|---|---|---|
| 1 | ESP32 30P CH340 Type-C | 1 |
| 2 | Board mở rộng ESP32 30P | 1 |
| 3 | LED đơn | 1 |
| 4 | Điện trở hạn dòng 330 Ω – 1 kΩ | 1 |
| 5 | Dây kết nối | Theo nhu cầu |
| 6 | Máy tính cài Arduino IDE | 1 |
| 7 | Điện thoại hoặc máy tính có Wi-Fi | 1 |
| 8 | Cáp USB Type-C có truyền dữ liệu | 1 |

Trong bài thực hành, chúng ta sử dụng LED để kiểm tra luồng điều khiển qua Wi-Fi trước khi tìm hiểu chương trình điều khiển robot.

### 5.2. Sơ đồ kết nối LED

Sử dụng GPIO23 làm chân điều khiển LED.

```text
ESP32 GPIO23
     │
     │
  Điện trở
  330Ω–1kΩ
     │
     ▼
   Anode (+)
      LED
   Cathode (-)
     │
     ▼
    GND
```

Bảng kết nối:

| Thiết bị | ESP32 |
|---|---|
| LED qua điện trở hạn dòng | GPIO23 |
| Chân âm LED | GND |

Khi GPIO23 ở mức HIGH, LED sáng.

Khi GPIO23 ở mức LOW, LED tắt.

**Lưu ý:** GPIO23 là chân được lựa chọn cho bài thực hành độc lập. Nếu chân này đang được sử dụng bởi thiết bị khác trên robot, cần ngắt kết nối thiết bị đó hoặc thực hành trên ESP32 riêng.

Không kết nối LED trực tiếp với GPIO mà không có điện trở hạn dòng.

### 5.3. Cấu hình Wi-Fi trong bài học

| Thông số | Giá trị |
|---|---|
| Chế độ Wi-Fi | Access Point |
| Tên mạng | ESP32-Lesson |
| Mật khẩu | 12345678 |
| Cổng Web Server | 80 |
| Địa chỉ IP mặc định thường gặp | 192.168.4.1 |
| GPIO điều khiển LED | GPIO23 |

Tên mạng `ESP32-Lesson` được sử dụng để phân biệt với mạng `ESP32-Car` của chương trình robot chính.

---

## 6. Thư viện sử dụng

### 6.1. Thư viện WiFi.h

Thư viện `WiFi.h` cung cấp các chức năng kết nối và quản lý Wi-Fi trên ESP32.

Trong bài học này, chúng ta sử dụng:

```cpp
#include <WiFi.h>
```

Một số hàm quan trọng:

| Hàm | Chức năng |
|---|---|
| `WiFi.mode()` | Chọn chế độ hoạt động Wi-Fi |
| `WiFi.softAP()` | Tạo mạng Wi-Fi Access Point |
| `WiFi.softAPIP()` | Lấy địa chỉ IP của Access Point |

### 6.2. Thư viện WebServer.h

Thư viện `WebServer.h` cho phép ESP32 tạo một HTTP Server đơn giản.

Khai báo:

```cpp
#include <WebServer.h>
```

Một số hàm quan trọng:

| Hàm | Chức năng |
|---|---|
| `server.on()` | Đăng ký đường dẫn và hàm xử lý |
| `server.send()` | Gửi phản hồi đến trình duyệt |
| `server.begin()` | Khởi động Web Server |
| `server.handleClient()` | Tiếp nhận và xử lý yêu cầu HTTP |

Hai thư viện trên được cung cấp cùng bộ Arduino-ESP32 core khi cài đặt ESP32 đúng cách trong Arduino IDE.

Vì vậy, bài thực hành không cần cài thêm thư viện Web Server bên ngoài.

---

## 7. Thực hành điều khiển LED qua Wi-Fi

### 7.1. Mục tiêu

Chúng ta sẽ xây dựng chương trình có các chức năng:

1. ESP32 tạo mạng Wi-Fi `ESP32-Lesson`.
2. Điện thoại kết nối vào mạng này.
3. ESP32 cung cấp một trang web điều khiển.
4. Trang web có hai nút ON và OFF.
5. Nhấn ON để bật LED.
6. Nhấn OFF để tắt LED.

### 7.2. Tạo chương trình mới

Mở Arduino IDE.

Chọn **File → New Sketch**.

Lưu chương trình với tên:

```text
ESP32_WiFi_Control
```

Cấu trúc thư mục:

```text
ESP32_WiFi_Control/
└── ESP32_WiFi_Control.ino
```

### 7.3. Chương trình hoàn chỉnh

```cpp
#include <WiFi.h>
#include <WebServer.h>

// ================= WIFI =================

const char* WIFI_SSID = "ESP32-Lesson";
const char* WIFI_PASS = "12345678";

// ================= LED =================

const int LED_PIN = 23;

// ================= WEB SERVER =================

WebServer server(80);

// ================= HTML =================

const char PAGE_HTML[] = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1">

  <title>ESP32 WiFi Control</title>

  <style>
    body {
      font-family: Arial;
      text-align: center;
      margin-top: 50px;
    }

    button {
      width: 140px;
      padding: 15px;
      margin: 10px;
      font-size: 20px;
      cursor: pointer;
    }
  </style>
</head>

<body>

  <h2>ESP32 WiFi Control</h2>

  <p>Dieu khien LED qua WiFi</p>

  <a href="/on">
    <button>LED ON</button>
  </a>

  <a href="/off">
    <button>LED OFF</button>
  </a>

</body>
</html>
)rawliteral";

// ================= WEB HANDLERS =================

void handleRoot() {

  server.send(200, "text/html", PAGE_HTML);
}

void handleOn() {

  digitalWrite(LED_PIN, HIGH);

  Serial.println("LED ON");

  server.sendHeader("Location", "/");
  server.send(303, "text/plain", "");
}

void handleOff() {

  digitalWrite(LED_PIN, LOW);

  Serial.println("LED OFF");

  server.sendHeader("Location", "/");
  server.send(303, "text/plain", "");
}

// ================= SETUP =================

void setup() {

  Serial.begin(115200);

  // Khoi tao LED
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Khoi tao WiFi Access Point
  WiFi.mode(WIFI_AP);

  bool apOK = WiFi.softAP(WIFI_SSID, WIFI_PASS);

  if (!apOK) {
    Serial.println("Khong tao duoc WiFi AP");
    return;
  }

  Serial.println("WiFi AP started");

  Serial.print("SSID: ");
  Serial.println(WIFI_SSID);

  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());

  // Dang ky cac duong dan
  server.on("/", HTTP_GET, handleRoot);
  server.on("/on", HTTP_GET, handleOn);
  server.on("/off", HTTP_GET, handleOff);

  // Khoi dong Web Server
  server.begin();

  Serial.println("Web Server started");
}

// ================= LOOP =================

void loop() {

  server.handleClient();
}
```

### 7.4. Kết quả mong đợi

Sau khi nạp chương trình, mở Serial Monitor ở tốc độ 115200 baud.

Ví dụ:

```text
WiFi AP started
SSID: ESP32-Lesson
IP Address: 192.168.4.1
Web Server started
```

ESP32 bắt đầu phát mạng Wi-Fi.

Khi người dùng nhấn nút LED ON:

```text
LED ON
```

LED sáng.

Khi người dùng nhấn nút LED OFF:

```text
LED OFF
```

LED tắt.

---

## 8. Giải thích chương trình

### 8.1. Khai báo thông tin Wi-Fi

```cpp
const char* WIFI_SSID = "ESP32-Lesson";
const char* WIFI_PASS = "12345678";
```

Hai biến này lưu tên mạng và mật khẩu Wi-Fi mà ESP32 sẽ phát ra.

Mật khẩu Access Point WPA2 thông thường cần ít nhất 8 ký tự.

Trong bài học, chúng ta sử dụng mật khẩu đơn giản để thuận tiện thực hành. Khi triển khai thực tế, nên thay bằng mật khẩu mạnh hơn.

### 8.2. Khởi tạo Web Server

```cpp
WebServer server(80);
```

Lệnh trên tạo Web Server sử dụng cổng 80.

Đây là cổng mặc định thường được sử dụng cho HTTP.

Vì vậy, khi truy cập địa chỉ:

```text
http://192.168.4.1
```

Trình duyệt sẽ gửi yêu cầu HTTP đến Web Server của ESP32.

### 8.3. Tạo mạng Wi-Fi

```cpp
WiFi.mode(WIFI_AP);

WiFi.softAP(WIFI_SSID, WIFI_PASS);
```

`WiFi.mode(WIFI_AP)` cấu hình ESP32 hoạt động ở chế độ Access Point.

`WiFi.softAP()` khởi tạo mạng Wi-Fi với tên và mật khẩu đã khai báo.

Sau khi tạo mạng thành công, các thiết bị khác có thể tìm thấy và kết nối với mạng `ESP32-Lesson`.

### 8.4. Lấy địa chỉ IP

```cpp
WiFi.softAPIP();
```

Hàm này trả về địa chỉ IP của ESP32 trong mạng Access Point.

Địa chỉ mặc định thường là:

```text
192.168.4.1
```

Tuy nhiên, nên sử dụng địa chỉ thực tế được in trên Serial Monitor thay vì mặc định luôn là 192.168.4.1.

### 8.5. Tạo giao diện HTML

Trong chương trình, nội dung giao diện được lưu trong biến:

```cpp
const char PAGE_HTML[] = R"rawliteral(
...
)rawliteral";
```

Cú pháp `R"rawliteral(... )rawliteral"` cho phép khai báo chuỗi nhiều dòng, thuận tiện khi viết mã HTML trong Arduino.

Giao diện gồm:

- Tiêu đề trang.
- Hai nút điều khiển.
- Các đường dẫn gửi yêu cầu đến ESP32.

Ví dụ:

```html
<a href="/on">
  <button>LED ON</button>
</a>
```

Khi người dùng nhấn nút LED ON, trình duyệt truy cập đường dẫn `/on`.

### 8.6. Đăng ký đường dẫn

```cpp
server.on("/", HTTP_GET, handleRoot);
server.on("/on", HTTP_GET, handleOn);
server.on("/off", HTTP_GET, handleOff);
```

Các lệnh này đăng ký ba đường dẫn:

| Đường dẫn | Hàm xử lý | Chức năng |
|---|---|---|
| `/` | `handleRoot()` | Hiển thị trang web |
| `/on` | `handleOn()` | Bật LED |
| `/off` | `handleOff()` | Tắt LED |

Ví dụ, khi trình duyệt truy cập `/on`, Web Server gọi hàm `handleOn()`.

### 8.7. Xử lý lệnh bật LED

```cpp
void handleOn() {

  digitalWrite(LED_PIN, HIGH);

  Serial.println("LED ON");

  server.sendHeader("Location", "/");
  server.send(303, "text/plain", "");
}
```

Khi nhận yêu cầu `/on`:

1. ESP32 đưa GPIO23 lên HIGH.
2. LED sáng.
3. ESP32 in thông báo trên Serial Monitor.
4. Web Server yêu cầu trình duyệt quay lại trang chính.

### 8.8. Xử lý lệnh tắt LED

```cpp
void handleOff() {

  digitalWrite(LED_PIN, LOW);

  Serial.println("LED OFF");

  server.sendHeader("Location", "/");
  server.send(303, "text/plain", "");
}
```

Khi nhận yêu cầu `/off`, ESP32 đưa GPIO23 xuống LOW và LED tắt.

### 8.9. Xử lý yêu cầu trong loop()

```cpp
void loop() {

  server.handleClient();
}
```

Hàm `server.handleClient()` kiểm tra và xử lý các yêu cầu HTTP từ trình duyệt.

Trong ví dụ sử dụng `WebServer`, hàm này cần được gọi thường xuyên.

Nếu chương trình sử dụng các lệnh `delay()` dài hoặc có tác vụ chặn lâu, việc xử lý yêu cầu có thể bị chậm.

---

## 9. Kết nối điện thoại với ESP32

### 9.1. Bước 1: Nạp chương trình

Trong Arduino IDE:

1. Chọn board **ESP32 Dev Module**.
2. Chọn đúng cổng COM.
3. Nhấn Verify để kiểm tra chương trình.
4. Nhấn Upload để nạp vào ESP32.
5. Mở Serial Monitor ở tốc độ 115200 baud.

Kiểm tra ESP32 đã tạo mạng Wi-Fi thành công.

### 9.2. Bước 2: Kết nối Wi-Fi

Trên điện thoại:

1. Mở phần cài đặt Wi-Fi.
2. Tìm mạng `ESP32-Lesson`.
3. Nhập mật khẩu `12345678`.
4. Chờ điện thoại kết nối thành công.

Do ESP32 chỉ phát mạng Wi-Fi nội bộ và không cung cấp Internet, điện thoại có thể hiển thị thông báo:

```text
Connected without Internet
```

Hoặc:

```text
Mạng Wi-Fi không có kết nối Internet
```

Đây là hiện tượng bình thường.

Nếu điện thoại hỏi có tiếp tục sử dụng mạng này hay không, hãy chọn giữ kết nối.

### 9.3. Bước 3: Mở giao diện điều khiển

Mở trình duyệt trên điện thoại.

Nhập địa chỉ:

```text
http://192.168.4.1
```

Hoặc địa chỉ IP thực tế được in trên Serial Monitor.

Lưu ý sử dụng `http://`, không phải `https://`.

Giao diện hiển thị hai nút:

```text
     ESP32 WiFi Control

     Dieu khien LED qua WiFi

       ┌───────────┐
       │  LED ON   │
       └───────────┘

       ┌───────────┐
       │  LED OFF  │
       └───────────┘
```

### 9.4. Bước 4: Kiểm tra điều khiển

Nhấn **LED ON**.

Quan sát:

- LED sáng.
- Serial Monitor hiển thị `LED ON`.

Nhấn **LED OFF**.

Quan sát:

- LED tắt.
- Serial Monitor hiển thị `LED OFF`.

Nếu kết quả đúng, chúng ta đã xây dựng thành công một hệ thống điều khiển thiết bị qua Wi-Fi.

---

## 10. Từ điều khiển LED đến điều khiển robot

### 10.1. Nguyên lý tương tự

Ở ví dụ LED, trình duyệt gửi yêu cầu để điều khiển một GPIO.

Đối với robot, nguyên lý giao tiếp cũng tương tự.

Thay vì bật hoặc tắt LED, ESP32 nhận lệnh để điều khiển động cơ.

Ví dụ, một giao diện điều khiển robot có thể cung cấp các chức năng:

- Tiến.
- Lùi.
- Rẽ trái.
- Rẽ phải.
- Dừng.
- Thay đổi tốc độ.
- Chuyển chế độ hoạt động.

Sơ đồ tổng quát:

```text
         Điện thoại
              │
              ▼
       Giao diện Web
              │
              ▼
         Lệnh điều khiển
              │
              ▼
        ESP32 Wi-Fi
              │
              ▼
      Chương trình xử lý
              │
              ▼
       Driver L298N
              │
        ┌─────┴─────┐
        ▼           ▼
    Motor trái   Motor phải
```

### 10.2. Khác biệt quan trọng giữa LED và động cơ

Đối với LED, khi nhận lệnh ON, LED có thể tiếp tục sáng cho đến khi nhận lệnh OFF.

Tuy nhiên, cách hoạt động này không đủ an toàn cho động cơ.

Ví dụ:

1. Người dùng nhấn nút tiến.
2. Robot bắt đầu di chuyển.
3. Điện thoại mất kết nối Wi-Fi.
4. Robot không nhận được lệnh dừng.

Nếu chương trình chỉ giữ trạng thái cuối, robot có thể tiếp tục di chuyển.

Vì vậy, khi điều khiển robot qua Wi-Fi, cần thiết kế thêm các cơ chế an toàn như:

- Lệnh dừng ưu tiên.
- Giới hạn thời gian hiệu lực của lệnh di chuyển.
- Dừng khi không nhận được lệnh điều khiển mới trong thời gian quy định.
- Kiểm soát trạng thái hoạt động.
- Xử lý chuyển đổi giữa các chế độ.
- Kiểm tra điều kiện trước khi cho phép động cơ hoạt động.

**Không nên thay trực tiếp các lệnh bật/tắt LED trong bài thực hành thành lệnh điều khiển động cơ nếu chưa bổ sung các cơ chế an toàn phù hợp.**

---

## 11. Sử dụng giao diện Wi-Fi của robot ESP32

### 11.1. Chương trình robot chính

Bộ robot ESP32 đã được bàn giao chương trình điều khiển tích hợp nhiều chức năng.

Chương trình này sử dụng Wi-Fi để cung cấp giao diện điều khiển robot qua trình duyệt.

Khác với ví dụ LED sử dụng `WebServer.h`, chương trình robot sử dụng thư viện **ESPAsyncWebServer** để xây dựng Web Server bất đồng bộ.

Các thư viện liên quan gồm:

- `WiFi.h`.
- `AsyncTCP.h`.
- `ESPAsyncWebServer.h`.

Cần phân biệt `AsyncTCP` dành cho ESP32 với thư viện `ESPAsyncTCP` thường sử dụng trên ESP8266.

### 11.2. Mạng Wi-Fi của robot

Trong chương trình robot chính, tên mạng Wi-Fi được cấu hình là:

```text
ESP32-Car
```

Đây là mạng Wi-Fi riêng của robot.

Sau khi nạp chương trình chính và khởi động robot, người dùng có thể tìm mạng `ESP32-Car` trên điện thoại.

Tên mạng này khác với mạng `ESP32-Lesson` trong ví dụ LED.

| Chương trình | Tên Wi-Fi |
|---|---|
| Bài thực hành điều khiển LED | ESP32-Lesson |
| Chương trình robot chính | ESP32-Car |

Nếu ESP32 đang chạy bài thực hành LED, mạng `ESP32-Car` sẽ không xuất hiện.

Muốn sử dụng lại robot, cần nạp lại chương trình chính.

### 11.3. Kết nối với robot

Các bước thực hiện:

1. Nạp chương trình robot chính.
2. Cấp nguồn cho robot theo hướng dẫn.
3. Mở Wi-Fi trên điện thoại.
4. Kết nối với mạng `ESP32-Car`.
5. Mở trình duyệt.
6. Truy cập địa chỉ IP của robot.
7. Sử dụng giao diện điều khiển.

Địa chỉ IP cần được xác nhận từ cấu hình chương trình hoặc Serial Monitor.

Nếu sử dụng cấu hình Access Point mặc định của ESP32, địa chỉ thường gặp là `192.168.4.1`.

Xem thêm: [Hướng dẫn sử dụng robot](../08-su-dung-robot.md).

---

## 12. Các chế độ điều khiển của robot

### 12.1. Chế độ Manual

Manual là chế độ điều khiển bằng tay.

Trong chế độ này, người dùng gửi các lệnh điều khiển thông qua giao diện web.

Các lệnh có thể gồm:

- Tiến.
- Lùi.
- Rẽ trái.
- Rẽ phải.
- Dừng.

Chương trình ESP32 tiếp nhận lệnh và điều khiển hai động cơ thông qua L298N.

Người dùng có thể điều chỉnh tốc độ theo chức năng được cung cấp trên giao diện.

### 12.2. Chế độ Line Follow

Line Follow là chế độ robot tự động di chuyển theo vạch line.

Trong chế độ này, ESP32 sử dụng tín hiệu từ module dò line TCRT5000 để xác định vị trí vạch line.

Dữ liệu cảm biến được đưa vào thuật toán điều khiển để điều chỉnh tốc độ hai bánh.

Sơ đồ:

```text
       Cảm biến dò line
               │
               ▼
          ESP32 đọc
        trạng thái line
               │
               ▼
       Thuật toán điều khiển
               │
               ▼
        Tốc độ hai bánh
               │
               ▼
          Driver L298N
               │
               ▼
          Robot di chuyển
```

Trong chế độ này, chương trình robot khóa điều khiển di chuyển bằng tay để tránh xung đột giữa lệnh người dùng và thuật toán dò line.

### 12.3. So sánh Manual và Line Follow

| Tiêu chí | Manual | Line Follow |
|---|---|---|
| Nguồn lệnh di chuyển | Người dùng | Thuật toán dò line |
| Điều khiển hướng | Qua giao diện web | Theo cảm biến |
| Điều chỉnh tốc độ | Theo cấu hình Manual | Theo thuật toán dò line |
| Vai trò cảm biến line | Không phải nguồn điều khiển hướng chính | Dữ liệu đầu vào quan trọng |
| Lệnh di chuyển bằng tay | Được sử dụng | Bị khóa trong cấu hình robot |

### 12.4. Chuyển đổi chế độ

Khi chuyển từ Manual sang Line Follow, chương trình cần bàn giao quyền điều khiển động cơ cho thuật toán tự động.

Khi chuyển từ Line Follow về Manual, chương trình cần kết thúc hoạt động tự động trước khi tiếp nhận các lệnh di chuyển bằng tay.

Điều quan trọng là không để hai nguồn điều khiển cùng phát lệnh xung đột đến động cơ.

Khi thực hành, nên kê bánh xe khỏi mặt sàn để kiểm tra phản ứng của từng chế độ trước khi cho robot chạy thực tế.

---

## 13. Tìm hiểu cấu trúc chương trình robot

### 13.1. Phần xử lý Wi-Fi

Trong chương trình chính, tìm các đoạn liên quan đến:

```cpp
#include <WiFi.h>
```

Và:

```cpp
WiFi.softAP(...);
```

Đây là những thành phần dùng để khởi tạo mạng Wi-Fi của robot.

### 13.2. Phần Web Server

Tìm khai báo:

```cpp
#include <ESPAsyncWebServer.h>
```

Và các đoạn đăng ký đường dẫn điều khiển.

Ví dụ, với các route như:

```text
/forward
/stop
/setMode
```

Cần xác định:

- Đường dẫn được đăng ký ở đâu?
- Trình duyệt gửi phương thức HTTP nào?
- Hàm nào được gọi khi nhận lệnh?
- Hàm xử lý có điều khiển động cơ trực tiếp hay chỉ cập nhật trạng thái?
- Có kiểm tra chế độ Manual hoặc Line Follow trước khi xử lý không?

**Lưu ý:** Các route trên là những đường dẫn cần tìm và đối chiếu trong phiên bản chương trình đang sử dụng. Không mặc định mọi phiên bản firmware đều có cùng tên route hoặc cách xử lý.

### 13.3. Phần điều khiển động cơ

Khi nhận được lệnh di chuyển, chương trình sẽ sử dụng các chân điều khiển L298N.

Trong cấu hình robot:

| Chân | GPIO |
|---|---|
| ENA | 13 |
| IN1 | 12 |
| IN2 | 14 |
| ENB | 15 |
| IN3 | 4 |
| IN4 | 2 |

Các chân ENA và ENB dùng để điều chỉnh PWM, còn các chân IN dùng để xác định chiều quay của động cơ.

Cần đối chiếu lại với chương trình và dây kết nối của robot thực tế.

### 13.4. Phân biệt tốc độ Manual và tốc độ Line Follow

Trong chương trình robot, tốc độ khi điều khiển bằng tay và tốc độ khi dò line có thể sử dụng các biến hoặc tham số khác nhau.

Ví dụ:

- Manual: Giá trị tốc độ theo lệnh người dùng.
- Line Follow: Tốc độ cơ sở của thuật toán, chẳng hạn `v_base`, kết hợp với giá trị hiệu chỉnh hướng.

Vì vậy, thay đổi tốc độ Manual không nhất thiết làm thay đổi tốc độ cơ sở khi robot chạy Line Follow.

Cần tìm và đối chiếu các biến tương ứng trong chương trình chính và phần xử lý dò line.

---

## 14. Các lỗi thường gặp

### 14.1. Không tìm thấy mạng Wi-Fi

**Hiện tượng:** Điện thoại không tìm thấy mạng `ESP32-Lesson`.

Nguyên nhân có thể:

- ESP32 chưa được cấp nguồn.
- Chương trình chưa được nạp thành công.
- ESP32 khởi động lỗi.
- Access Point chưa được tạo.
- ESP32 đang chạy chương trình khác.

Cách xử lý:

1. Kiểm tra nguồn.
2. Mở Serial Monitor.
3. Kiểm tra thông báo khởi tạo Wi-Fi.
4. Xác nhận chương trình đang được nạp.
5. Khởi động lại ESP32 nếu cần.

### 14.2. Điện thoại báo không có Internet

Đây là hiện tượng bình thường khi kết nối với mạng Access Point của ESP32.

ESP32 đang cung cấp mạng nội bộ để điều khiển thiết bị, không nhất thiết cung cấp kết nối Internet.

Cần chọn giữ kết nối với mạng Wi-Fi của ESP32.

### 14.3. Không mở được trang web

Nguyên nhân có thể:

- Điện thoại chưa kết nối đúng Wi-Fi.
- Địa chỉ IP không chính xác.
- Trình duyệt tự chuyển sang HTTPS.
- Web Server chưa khởi động.
- Chương trình không xử lý yêu cầu HTTP.

Cách xử lý:

1. Kiểm tra tên Wi-Fi đang kết nối.
2. Kiểm tra địa chỉ IP trên Serial Monitor.
3. Nhập đầy đủ `http://`.
4. Kiểm tra thông báo Web Server đã khởi động.
5. Thử tải lại trang.

### 14.4. Trang web mở được nhưng LED không sáng

Kiểm tra:

- GPIO23.
- Chiều lắp LED.
- Điện trở hạn dòng.
- Dây GND.
- Lệnh ON/OFF trên Serial Monitor.

Nếu Serial Monitor đã nhận lệnh nhưng LED không thay đổi, nguyên nhân có thể nằm ở phần đấu nối.

### 14.5. Giao diện phản hồi chậm

Đối với chương trình sử dụng `WebServer.h`, cần kiểm tra:

- Có sử dụng `delay()` dài trong `loop()` không?
- Có tác vụ nào chặn chương trình không?
- `server.handleClient()` có được gọi thường xuyên không?
- Kết nối Wi-Fi có ổn định không?

Trong các hệ thống phức tạp, cần tổ chức chương trình để tránh làm chậm việc tiếp nhận lệnh.

### 14.6. Không thấy mạng ESP32-Car

Nếu trước đó đã nạp chương trình LED, ESP32 sẽ phát mạng:

```text
ESP32-Lesson
```

Thay vì:

```text
ESP32-Car
```

Để sử dụng lại robot, cần nạp lại chương trình chính.

### 14.7. Robot không nhận lệnh di chuyển bằng tay

Nếu giao diện đang ở chế độ Line Follow, các lệnh di chuyển Manual có thể bị khóa theo logic chương trình.

Cần kiểm tra chế độ hoạt động hiện tại.

Không nên bỏ điều kiện khóa lệnh chỉ để robot nhận đồng thời cả điều khiển tay và điều khiển tự động.

---

## 15. Bài tập thực hành

### Bài tập 1: Điều khiển LED qua Wi-Fi

Nạp chương trình thực hành.

Kết nối điện thoại với mạng `ESP32-Lesson`.

Mở giao diện và kiểm tra:

- Nhấn ON: LED sáng.
- Nhấn OFF: LED tắt.

Giải thích luồng dữ liệu từ trình duyệt đến GPIO23.

### Bài tập 2: Thay đổi tên mạng Wi-Fi

Thay đổi:

```cpp
const char* WIFI_SSID = "ESP32-Lesson";
```

Thành một tên mạng khác.

Nạp lại chương trình và kiểm tra tên Wi-Fi mới trên điện thoại.

### Bài tập 3: Bổ sung chức năng xem trạng thái LED

Thêm đường dẫn:

```text
/state
```

Khi truy cập, ESP32 trả về trạng thái LED hiện tại.

Ví dụ:

```text
LED ON
```

Hoặc:

```text
LED OFF
```

Gợi ý: Sử dụng một biến để lưu trạng thái LED và cập nhật biến khi nhận lệnh ON/OFF.

### Bài tập 4: Tự động tắt LED sau một giây

Bổ sung chức năng:

1. Người dùng nhấn ON.
2. LED sáng.
3. Sau một giây, LED tự tắt.

Yêu cầu:

- Sử dụng `millis()` để theo dõi thời gian.
- Không sử dụng `delay(1000)` trong hàm xử lý HTTP.
- Web Server vẫn tiếp nhận được yêu cầu trong thời gian LED đang sáng.

### Bài tập 5: Tìm hiểu các đường dẫn điều khiển robot

Mở chương trình robot chính.

Tìm các phần xử lý tương ứng với:

```text
/forward
/stop
/setMode
```

Nếu tên route trong firmware khác với ví dụ, ghi lại tên thực tế.

Trả lời:

1. Route nào dùng để điều khiển robot tiến?
2. Route nào dùng để dừng?
3. Route nào dùng để chuyển chế độ?
4. Chương trình có kiểm tra chế độ trước khi thực hiện lệnh không?

### Bài tập 6: Phân tích chế độ Manual và Line Follow

Trong chương trình robot, xác định:

- Biến lưu chế độ hoạt động.
- Phần tiếp nhận lệnh Manual.
- Phần xử lý dò line.
- Biến tốc độ sử dụng trong Manual.
- Biến tốc độ cơ sở của Line Follow.

Giải thích vì sao hai chế độ cần có cơ chế phân quyền điều khiển động cơ.

### Bài tập 7: Phân tích an toàn khi mất kết nối

Giả sử robot đang di chuyển theo lệnh từ điện thoại.

Sau đó, điện thoại bị mất kết nối Wi-Fi.

Trả lời:

1. ESP32 có tự biết trình duyệt đã đóng hay không?
2. Đóng trình duyệt có luôn gửi lệnh dừng không?
3. Nếu không nhận được lệnh dừng, robot có thể gặp rủi ro gì?
4. Cần thiết kế cơ chế nào để robot tự dừng khi mất lệnh điều khiển?

---

## 16. Kiểm tra trước khi bắt đầu bài tiếp theo

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã hiểu Wi-Fi trên ESP32.
- [ ] Đã phân biệt Station và Access Point.
- [ ] Đã hiểu nguyên lý HTTP Request và HTTP Response.
- [ ] Đã biết sử dụng `WiFi.h`.
- [ ] Đã biết sử dụng `WebServer.h`.
- [ ] Đã tạo được mạng Wi-Fi riêng bằng ESP32.
- [ ] Đã biết cách lấy địa chỉ IP của Access Point.
- [ ] Đã tạo được trang web điều khiển LED.
- [ ] Đã hiểu cách đăng ký các đường dẫn HTTP.
- [ ] Đã điều khiển LED thành công bằng điện thoại.
- [ ] Đã hiểu vai trò của `server.handleClient()`.
- [ ] Đã phân biệt ví dụ WebServer và chương trình robot sử dụng ESPAsyncWebServer.
- [ ] Đã kết nối được với mạng Wi-Fi của robot.
- [ ] Đã hiểu chức năng Manual và Line Follow.
- [ ] Đã biết vì sao phải có cơ chế dừng an toàn khi điều khiển động cơ qua Wi-Fi.

---

## 17. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu cách sử dụng Wi-Fi trên ESP32 để xây dựng hệ thống điều khiển thiết bị thông qua trình duyệt web.

Những nội dung quan trọng gồm:

- Khả năng giao tiếp Wi-Fi của ESP32.
- Hai chế độ Station và Access Point.
- Nguyên lý giao tiếp HTTP.
- Tạo mạng Wi-Fi bằng `WiFi.softAP()`.
- Xây dựng Web Server bằng `WebServer.h`.
- Thiết kế giao diện điều khiển HTML.
- Tiếp nhận và xử lý các lệnh ON/OFF.
- Điều khiển LED thông qua điện thoại.
- Tìm hiểu giao diện điều khiển Wi-Fi của robot.
- Phân biệt chế độ Manual và Line Follow.
- Hiểu yêu cầu an toàn khi điều khiển động cơ qua mạng.

Thông qua bài thực hành LED, chúng ta đã nắm được luồng điều khiển cơ bản:

**Trình duyệt → Wi-Fi → ESP32 Web Server → Xử lý lệnh → GPIO.**

Đối với robot, luồng điều khiển được mở rộng thành:

**Trình duyệt → Wi-Fi → ESP32 → Thuật toán điều khiển → L298N → Động cơ.**

Ở bài học tiếp theo, chúng ta sẽ tìm hiểu **thuật toán PID**, cách sử dụng dữ liệu cảm biến và Encoder để điều chỉnh tốc độ hai bánh, giúp robot di chuyển ổn định và bám đường line tốt hơn.

---

[Bài trước: Đọc Encoder và đo tốc độ bánh xe](08-encoder.md) · [Lộ trình bài học](../index.md) · [Bài tiếp: Điều khiển robot với PID](10-pid.md)