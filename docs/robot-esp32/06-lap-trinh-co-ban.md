# Lập trình ESP32: LED, nút nhấn và PWM

**Mục tiêu:** đọc đầu vào, điều khiển LED và thay đổi độ sáng.

**Phạm vi chân:** ESP32 classic WROOM-32 có GPIO23 và GPIO18 còn trống. Bo S3/C3 hoặc robot đã nối thiết bị cần chọn chân theo pinout rồi sửa mã. Không đếm vị trí chân để suy ra số GPIO; xem [hướng dẫn GPIO](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/gpio.html).

## 1. Đấu mạch khi đã ngắt nguồn

```text
GPIO23 → điện trở 330 Ω–1 kΩ → anode LED
cathode LED → GND
GPIO18 → nút nhấn → GND
```

LED mới thường có chân dài là anode, chân ngắn/mép phẳng là cathode. Nút bốn chân có hai cặp nối sẵn; chọn hai phía tiếp điểm thật. Không nối nút lên 5V. Tạm để nguồn động cơ ngắt.

## 2. Giữ nút để bật LED

Lưu sketch `ESP32NutNhan`:

```cpp
const int CHAN_LED = 23;
const int CHAN_NUT = 18;

void setup() {
  pinMode(CHAN_LED, OUTPUT);
  pinMode(CHAN_NUT, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  bool dangNhan = (digitalRead(CHAN_NUT) == LOW);
  digitalWrite(CHAN_LED, dangNhan ? HIGH : LOW);
  Serial.println(dangNhan ? "Dang nhan" : "Da tha");
  delay(100);
}
```

`const int` đặt tên chân cố định; `bool` chứa true/false. `==` so sánh, `=` gán. `INPUT_PULLUP` kéo đầu vào lên khi thả nút; nhấn nối GND nên đọc LOW. Biểu thức `điều_kiện ? giá_trị_đúng : giá_trị_sai` chọn mức xuất LED.

Verify, Upload, mở Monitor **115200 baud**. Giữ nút LED sáng, thả LED tắt, log đổi tương ứng. Nếu luôn báo nhấn, kiểm tra cặp chân nút và GPIO18 có chạm GND không.

## 3. PWM: đổi độ sáng LED

PWM bật/tắt tín hiệu nhanh, tỷ lệ thời gian bật làm thay đổi độ sáng trung bình. Ví dụ dưới dùng **Arduino-ESP32 core 3.x**: thay toàn bộ sketch, giữ mạch LED, nút không dùng trong bài này.

```cpp
const int CHAN_LED = 23;
bool pwmSanSang = false;

void setup() {
  Serial.begin(115200);
  pwmSanSang = ledcAttach(CHAN_LED, 5000, 8);
  if (!pwmSanSang) {
    Serial.println("Khong khoi tao duoc PWM");
  }
}

void loop() {
  if (!pwmSanSang) {
    delay(1000);
    return;
  }
  for (int doSang = 0; doSang <= 255; doSang++) {
    ledcWrite(CHAN_LED, doSang);
    delay(10);
  }
  for (int doSang = 254; doSang >= 0; doSang--) {
    ledcWrite(CHAN_LED, doSang);
    delay(10);
  }
}
```

`ledcAttach()` đặt tần số 5000 Hz, độ phân giải 8 bit; `ledcWrite()` đặt duty 0–255 theo **chân GPIO**. LED phải sáng dần rồi tối dần. API core 2.x khác: không chép nguyên `ledcSetup()`/`ledcAttachPin()` vào ví dụ 3.x. Xem [API LEDC của Espressif](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/ledc.html).

## Bài tập và áp dụng

Đổi khoảng nghỉ 10 ms thành 5 ms rồi quan sát tốc độ đổi sáng. Ở bài nút, sửa để nhấn tắt LED. Sau đó đọc [ví dụ millis của Nano](../robot-arduino/04-lap-trinh.md) để hiểu cách bỏ thời gian chờ; đổi chân và mức baud khi áp dụng ESP32.

PWM có thể điều khiển đầu vào driver động cơ khi driver hỗ trợ, nhưng ví dụ LED không phải mã động cơ. Cần đối chiếu chân, nguồn và mức logic trước khi chuyển sang robot. Nếu bật/tắt theo từng lần nhấn, học thêm chống dội nút.

[Bài trước](05-cai-thu-vien.md) · [Bài tiếp: Chạy thử và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md)
