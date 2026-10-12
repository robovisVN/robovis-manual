# Bài 9: Điều khiển xe ESP32 qua Wi-Fi và trình duyệt

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Hiểu chế độ Access Point của robot.
- Tạo trang web điều khiển LED để kiểm tra luồng lệnh.
- Sử dụng Manual/Line follow của project main đã bàn giao.

**Trước khi bắt đầu:** Encoder và tốc độ bánh — [mở bài trước](08-encoder.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

ESP32 có thể phát mạng Wi-Fi cục bộ và phục vụ HTTP. Trình duyệt gửi yêu cầu; firmware nhận đường dẫn rồi điều khiển đầu ra. Bài dùng WiFi/WebServer đi cùng core để học nguyên lý; project main dùng ESPAsyncWebServer cho giao diện robot.

## 2. Chuẩn bị, bảng chân và đấu nối

Dùng bo riêng: GPIO23 → điện trở 330 Ω–1 kΩ → anode LED, cathode → GND. Ngắt dây robot và nguồn motor. Không đổi ví dụ này thành điều khiển motor khi chưa có cơ chế dừng và đối chiếu chân.

| Cấu hình bài học | Giá trị |
| --- | --- |
| Wi-Fi bài LED | ESP32-Lesson |
| Mật khẩu bài LED | 12345678 |
| Chân LED | GPIO23 |

Mạng bài học khác mạng ESP32-Car của project sản phẩm, tránh nhầm chương trình đang nạp.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);
const int LED = 23;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
  WiFi.softAP("ESP32-Lesson", "12345678");
  Serial.println(WiFi.softAPIP());
  server.on("/", []() {
    server.send(200, "text/html",
      "<h1>LED</h1><a href='/on'>ON</a> <a href='/off'>OFF</a>");
  });
  server.on("/on", []() {
    digitalWrite(LED, HIGH);
    server.send(200, "text/html", "LED ON <a href='/'>Back</a>");
  });
  server.on("/off", []() {
    digitalWrite(LED, LOW);
    server.send(200, "text/html", "LED OFF <a href='/'>Back</a>");
  });
  server.begin();
}

void loop() {
  server.handleClient();
}
```

## 4. Giải thích chương trình

softAP() tạo mạng, server.on() đăng ký đường dẫn, handleClient() xử lý yêu cầu trong loop. LED giữ trạng thái cuối cho tới lệnh tiếp theo; hành vi này phù hợp LED nhưng chưa đủ cho motor. Không dùng delay dài làm giao diện phản ứng chậm.

## 5. Chạy thử và kết quả mong đợi

Kết nối ESP32-Lesson, giữ mạng dù báo không Internet, mở địa chỉ IP được in ở Monitor 115200 (thường http://192.168.4.1). ON/OFF thay đổi LED. Để dùng robot, nạp lại đủ main.ino/do_line.cpp/do_line.h, kết nối ESP32-Car và xem [giao diện sản phẩm](../08-su-dung-robot.md); trong Line follow, điều khiển tay bị khóa.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Không mở trang | Đúng mạng, nhập http:// vào thanh địa chỉ, đúng IP |
| Điện thoại tự rời mạng | Chọn giữ mạng không Internet |
| Không thấy ESP32-Car | Có đang nạp sketch ESP32-Lesson không |

## 7. Bài tập thực hành

1. Thêm đường /state trả trạng thái LED.
2. Tạo nút web bật LED trong 1 giây rồi tự tắt bằng millis().
3. Giải thích vì sao đóng trình duyệt không tự gửi lệnh dừng.
4. Đọc project main, tìm các route /forward, /stop, /setMode và phân biệt tốc độ Manual với v_base trong do_line.cpp.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](08-encoder.md) · [Lộ trình](../index.md) · [Bài tiếp: Điều khiển xe với PID](10-pid.md)
