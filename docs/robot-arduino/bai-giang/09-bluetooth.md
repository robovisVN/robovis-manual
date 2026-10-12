# Bài 9: Sử dụng Bluetooth HM-10 và Dabble với Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Phân biệt HM-10 với Bluetooth tích hợp ESP32.
- Đấu RX/TX theo SoftwareSerial của bộ mã.
- Đọc nút GamePad và áp dụng lệnh điều khiển motor.

**Trước khi bắt đầu:** Encoder và tốc độ bánh — [mở bài trước](08-encoder.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

HM-10 truyền dữ liệu BLE qua UART. Dabble trên điện thoại gửi trạng thái GamePad; Nano đọc qua thư viện Dabble. RX/TX trong lệnh Dabble.begin() là chân của Nano, không phải tên chân HM-10. Xem [GamePad của STEMpedia](https://ai.thestempedia.com/docs/dabble-app/gamepad-module/).

## 2. Chuẩn bị, bảng chân và đấu nối

Cài Dabble của STEMpedia, không dùng DabbleESP32.

| HM-10 | Nano |
| --- | --- |
| TX | A3, RX của Nano |
| RX | A2, TX Nano; hạ mức nếu HM-10 yêu cầu 3,3 V |
| VCC | Theo đúng module/breakout, không suy ra mọi HM-10 nhận 5 V |
| GND | GND chung |

Ngắt nguồn motor, tháo driver khỏi D0/D1 để thử Serial. Nếu cần hạ mức RX: A2 → R1 1 kΩ → HM-10 RX; từ điểm RX qua R2 2 kΩ xuống GND. Kiểm tra mức điện áp thực tế và sơ đồ breakout trước khi nối. Baud module phải phù hợp 9600.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <Dabble.h>

void setup() {
  Serial.begin(9600);
  Dabble.begin(9600, A3, A2);
}

void loop() {
  Dabble.processInput();
  static unsigned long moc = 0;
  if (millis() - moc < 100) return;
  moc = millis();
  if (GamePad.isUpPressed()) Serial.println("Tien");
  else if (GamePad.isDownPressed()) Serial.println("Lui");
  else if (GamePad.isLeftPressed()) Serial.println("Trai");
  else if (GamePad.isRightPressed()) Serial.println("Phai");
  else Serial.println("Dung");
}
```

## 4. Giải thích chương trình

Hai define chọn module GamePad trước khi include. processInput() cần được gọi thường xuyên. Bài này chỉ in lệnh, chưa điều khiển motor; không nối lại driver D0/D1 khi còn dùng Hardware Serial. Khi ghép bài motor, bỏ Serial, giữ Dabble trên A3/A2 và đổi các nhánh thành drive().

## 5. Chạy thử và kết quả mong đợi

Kết nối đúng module trong Dabble, mở GamePad và thử chế độ nút digital. Monitor 9600 đổi theo từng nút; thả nút in “Dung”. Tài liệu không quy định tên/mật khẩu Bluetooth cố định. Sau bài đo, nạp test_bluetooth.ino từ bộ bàn giao để thử robot theo [hướng dẫn chung](../08-su-dung-robot.md).

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Không thấy module | Nguồn, loại BLE, quyền Bluetooth của ứng dụng |
| Kết nối nhưng không có lệnh | RX/TX, 9600, GamePad, processInput |
| Không tìm thấy Dabble.h | Thư viện Dabble đúng tác giả |

## 7. Bài tập thực hành

1. In thêm trạng thái Start/Cross.
2. Viết bảng nút → drive() trước khi nạp sketch motor, bỏ Serial khỏi bản ghép.
3. Đọc mã bàn giao: Cross tăng góc, Triangle giảm góc; comment có thể ngược.
4. Nêu vì sao giá trị nút cũ không chứng minh Bluetooth còn kết nối; chỉ ghép tự dừng khi có cách xác nhận gói mới và thời hạn lệnh.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](08-encoder.md) · [Lộ trình](../index.md) · [Bài tiếp: Điều khiển xe với PID](10-pid.md)
