# Thêm và quản lý thư viện ESP32

**Mục tiêu:** biết khi nào phải cài thư viện, đọc yêu cầu của bộ mã và xử lý lỗi thiếu thư viện.

## Ba thứ khác nhau

| Thành phần | Ví dụ | Cách có được |
| --- | --- | --- |
| Board package | esp32 by Espressif Systems | Boards Manager |
| Thư viện đi cùng core | WiFi | Có khi cài core ESP32 |
| Thư viện ngoài | Thư viện servo/cảm biến theo bộ mã | Library Manager hoặc ZIP |

Không tìm cài một thư viện WiFi ngẫu nhiên để thay `WiFi.h` của ESP32. Nếu thiếu header này, kiểm tra core và board trước.

## Cài theo bộ mã robot

Bộ [main của robot Robovis](https://drive.google.com/drive/folders/1HeAZaW--JOkl67SG3IJOWxS1aPKAO5UB) dùng các thư viện sau. Trong Library Manager có thể tên hiển thị thêm khoảng trắng; đối chiếu tác giả và header:

| Tên tìm kiếm | Tác giả / dự án | Vai trò |
| --- | --- | --- |
| AsyncTCP | ESP32Async | TCP trên ESP32, dependency của web server |
| ESPAsyncWebServer | ESP32Async | Giao diện điều khiển HTTP |
| ESP32Servo | Kevin Harrington / madhephaestus | Servo gắp trong main.ino |

Cài ba thư viện, chấp nhận dependency và Verify **toàn bộ project main** với đúng board. `WiFi.h` đi cùng core ESP32; `do_line.h` nằm cạnh `main.ino`. Xem [ESPAsyncWebServer](https://github.com/ESP32Async/ESPAsyncWebServer) và [ESP32Servo](https://github.com/madhephaestus/ESP32Servo).

!!! note "ESPAsyncTCP trong tài liệu gốc"
    HD nạp code còn liệt kê ESPAsyncTCP. Dự án [ESPAsyncTCP](https://github.com/ESP32Async/ESPAsyncTCP) dành cho ESP8266; ESP32 dùng **AsyncTCP**. Không thay AsyncTCP bằng ESPAsyncTCP và không thêm include thư viện ESP8266 vào bộ main đã đối chiếu.

Đọc README và các dòng `#include`. Với thư viện ngoài, mở **Library Manager**, tìm tên, đối chiếu tác giả, kiến trúc hỗ trợ và phiên bản yêu cầu rồi Install. Cài dependency được đề nghị. Với ZIP thư viện do nhà cung cấp bàn giao, dùng **Sketch → Include Library → Add .ZIP Library**. Xem [cách cài thư viện Arduino](https://support.arduino.cc/hc/en-us/articles/5145457742236-Install-libraries-in-the-Arduino-IDE).

`main.ino` có `ESP32Servo.h`, nên cần cài ESP32Servo dù robot chưa lắp bộ gắp. Không thay bằng Servo của bài Nano; chưa nối servo khi chưa có sơ đồ nguồn phù hợp.

## Kiểm tra thư viện tích hợp

Tạo sketch `ESP32ThuVien`, Verify và Upload:

```cpp
#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  Serial.println("Da khoi tao WiFi o che do tram");
}

void loop() {
  delay(1000);
}
```

Mở Serial Monitor 115200 rồi nhấn EN để xem thông báo. Bài này chỉ khởi tạo chế độ Wi-Fi, chưa kết nối router và không cần nhập mật khẩu. Tham khảo [API Wi-Fi của Espressif](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/wifi.html).

Sketch kiểm tra trên thay chương trình robot khi Upload. Để khôi phục mạng ESP32-Car và giao diện điều khiển, nạp lại bộ `main`; robot thực tế dùng chế độ phát Wi-Fi `WiFi.softAP()`.

## Khi biên dịch lỗi

- `No such file or directory`: kiểm tra đúng tên header, thư viện và dependency.
- Báo không hỗ trợ kiến trúc: kiểm tra thư viện có hỗ trợ ESP32 không.
- `Multiple libraries were found`: xem IDE thực sự dùng bản nào, loại bản trùng không cần thiết sau khi sao lưu.
- Mã cũ dùng `ledcSetup`/`ledcAttachPin`: đối chiếu phiên bản core; đây có thể là thay đổi API, không phải thiếu thư viện.

**Kiểm tra:** Verify được sketch và ghi lại tên/phiên bản core, thư viện ngoài của bộ mã. Khi cập nhật, thử lại ví dụ nhỏ trước khi nạp robot.

[Bài trước](04-nap-code-va-serial.md) · [Bài tiếp: LED, nút và PWM](06-lap-trinh-co-ban.md)
