# Phân biệt tín hiệu digital, ADC và PWM

**Mục tiêu:** chọn đúng cách đọc hoặc xuất tín hiệu, thực hành dùng biến trở thay đổi độ sáng LED.

**Cần biết trước:** [GPIO và điện trở kéo](01-gpio-va-dien-tro-keo.md), [hàm](../lap-trinh/04-ham-va-chia-chuong-trinh.md) và [điện áp tín hiệu](../dien-dien-tu/03-tin-hieu-3v3-va-5v.md).

## Ba khái niệm có nhiệm vụ khác nhau

| Khái niệm | Làm gì? | Ví dụ trên Nano classic ATmega328P chạy 5 V |
| --- | --- | --- |
| Digital (tín hiệu số) | Đọc hoặc xuất hai trạng thái logic | Đọc nút bằng `digitalRead()`, xuất HIGH/LOW bằng `digitalWrite()` |
| ADC (Analog-to-Digital Converter) | Đổi điện áp analog đầu vào thành số | `analogRead(A0)` trả 0–1023 với ADC 10 bit |
| PWM (Pulse Width Modulation) | Tạo chuỗi xung với thời gian HIGH thay đổi | `analogWrite(9, giaTri)` với `giaTri` từ 0–255 |

**Analog** là tín hiệu có điện áp thay đổi liên tục trong phạm vi cho phép. ADC không trả volt trực tiếp. Với tham chiếu mặc định trên Nano classic, khoảng đo gắn với điện áp nguồn 5 V thực tế; không mặc định USB luôn đúng 5,000 V. Xem [Arduino: analogRead()](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Functions/Analog%20IO/analogRead.adoc).

**Duty cycle** là tỷ lệ thời gian HIGH trong một chu kỳ PWM. Tăng tỷ lệ này làm LED ngoài nhận năng lượng trung bình lớn hơn và thường sáng hơn. Ở khoảng 50%, chân vẫn luân phiên gần 0 V và 5 V, không trở thành nguồn DC ổn định 2,5 V. `analogWrite()` trên Nano classic tạo PWM, không tạo điện áp analog bằng DAC (bộ chuyển đổi số sang analog). Xem [Arduino: analogWrite()](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Functions/Analog%20IO/analogWrite.adoc).

## Giới hạn theo bo

Trên Nano classic, các chân PWM là D3, D5, D6, D9, D10, D11. A0–A7 đọc ADC; A6/A7 chỉ là đầu vào analog, không dùng như GPIO digital thông thường. Ví dụ này dùng A0 và D9; không cần sửa thanh ghi hay tần số timer.

ESP32 classic có ADC và phần cứng PWM khác; mức vào, dải đo và API còn phụ thuộc cấu hình/core. Không nối biến trở vào 5 V rồi đưa điểm giữa tới ADC ESP32. Theo [phần chuẩn bị ESP32](../../robot-esp32/02-chuan-bi.md) và ví dụ riêng của nền tảng nếu đổi bo.

## Chuẩn bị và đấu nối

Chỉ dùng **Nano classic ATmega328P 5 V**, bo rời cấp USB, biến trở 10 kΩ, LED ngoài và điện trở nối tiếp **1 kΩ**. Biến trở là điện trở có tiếp điểm trượt để lấy điện áp tại vị trí thay đổi.

Rút USB, tháo các module robot khỏi bo rồi nối:

```text
Nano 5V ---- đầu ngoài 1 của biến trở
Nano GND --- đầu ngoài 2 của biến trở
Nano A0 ---- chân trượt của biến trở

Nano D9 ---- điện trở 1 kΩ ---- anode LED
Nano GND -------------------- cathode LED
```

Anode/cathode là cực dương/âm của LED; đối chiếu linh kiện, không chỉ dựa vào độ dài chân đã cắt. Điện trở 1 kΩ giới hạn dòng; với nguồn 5 V, dòng trong nhánh này nhỏ hơn 5 mA theo mạch lý tưởng, không cấp động cơ qua nhánh LED. Chân trượt thường ở giữa nhưng cần xác nhận đúng mẫu biến trở. Không nối điện áp ngoài vào AREF; bài giữ tham chiếu ADC mặc định.

## Thực hành

```cpp
#include <Arduino.h>

const int CHAN_BIEN_TRO = A0;
const int CHAN_LED_PWM = 9;

void setup() {
  Serial.begin(9600);
  pinMode(CHAN_LED_PWM, OUTPUT);
}

void loop() {
  int giaTriAdc = analogRead(CHAN_BIEN_TRO);
  int giaTriPwm = giaTriAdc / 4;
  analogWrite(CHAN_LED_PWM, giaTriPwm);

  Serial.print("ADC: ");
  Serial.print(giaTriAdc);
  Serial.print(" | PWM: ");
  Serial.println(giaTriPwm);
  delay(100);
}
```

Verify, Upload, mở Serial Monitor 9600. **Kết quả mong đợi:** xoay biến trở làm ADC thay đổi gần 0–1023 và PWM 0–255; LED thay đổi độ sáng. Số đo có thể dao động vài đơn vị; giá trị ADC ở giữa khoảng 512 cho PWM khoảng 128. Chia nguyên cho 4 chuyển dải 10 bit sang dải 8 bit của ví dụ này, không phải công thức chung cho mọi bo.

## Lỗi thường gặp

- ADC nhảy mạnh hoặc kẹt: kiểm tra chân trượt, nguồn và GND.
- LED chỉ bật/tắt: kiểm tra có dùng đúng D9 hỗ trợ PWM không.
- LED không sáng: kiểm tra cực LED, điện trở và dây GND khi đã ngắt nguồn.
- Đo PWM bằng đồng hồ rồi cho là điện áp DC sạch: đồng hồ có thể hiển thị gần trung bình, không cho thấy dạng xung.

Đối chiếu chân trong [pinout Nano chính thức](https://docs.arduino.cc/resources/pinouts/A000005-full-pinout.pdf).

[← GPIO và điện trở kéo](01-gpio-va-dien-tro-keo.md) · [Chọn thực hành Robot Arduino](../../robot-arduino/index.md) · [Chọn thực hành Robot ESP32](../../robot-esp32/index.md) · [Lộ trình ROS 2 nếu đã sẵn sàng →](../robot-ros2/index.md)
