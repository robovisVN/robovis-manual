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

Đọc README và các dòng `#include`. Với thư viện ngoài, mở **Library Manager**, tìm tên, đối chiếu tác giả, kiến trúc hỗ trợ và phiên bản yêu cầu rồi Install. Cài dependency được đề nghị. Với ZIP thư viện do nhà cung cấp bàn giao, dùng **Sketch → Include Library → Add .ZIP Library**. Xem [cách cài thư viện Arduino](https://support.arduino.cc/hc/en-us/articles/5145457742236-Install-libraries-in-the-Arduino-IDE).

Mã dùng `ESP32Servo.h` cần thư viện ESP32Servo tương thích core đang cài; không thay bằng `Servo.h` dành cho bài Nano. Chỉ cài khi bài/bộ mã cần đến, chưa nối servo nếu chưa có sơ đồ nguồn.

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

## Khi biên dịch lỗi

- `No such file or directory`: kiểm tra đúng tên header, thư viện và dependency.
- Báo không hỗ trợ kiến trúc: kiểm tra thư viện có hỗ trợ ESP32 không.
- `Multiple libraries were found`: xem IDE thực sự dùng bản nào, loại bản trùng không cần thiết sau khi sao lưu.
- Mã cũ dùng `ledcSetup`/`ledcAttachPin`: đối chiếu phiên bản core; đây có thể là thay đổi API, không phải thiếu thư viện.

**Kiểm tra:** Verify được sketch và ghi lại tên/phiên bản core, thư viện ngoài của bộ mã. Khi cập nhật, thử lại ví dụ nhỏ trước khi nạp robot.

[Bài trước](04-nap-code-va-serial.md) · [Bài tiếp: LED, nút và PWM](06-lap-trinh-co-ban.md)
