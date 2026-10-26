# GPIO, tín hiệu HIGH/LOW và điện trở kéo

**Mục tiêu:** đọc được nút nhấn với `INPUT_PULLUP` và giải thích vì sao nhấn nút lại cho giá trị `LOW`.

**Cần biết trước:** [GND](../dien-dien-tu/02-gnd-va-noi-chung-mass.md), [mức điện áp](../dien-dien-tu/03-tin-hieu-3v3-va-5v.md), [câu lệnh điều kiện](../lap-trinh/02-cau-lenh-dieu-kien.md). Đã biết nạp sketch và dùng Serial Monitor.

## GPIO và hai chiều sử dụng

**GPIO** (General Purpose Input/Output) là chân vào/ra đa mục đích. Ở chế độ **INPUT**, bo đọc trạng thái tín hiệu từ bên ngoài. Ở chế độ **OUTPUT**, bo điều khiển mức tín hiệu. `HIGH` và `LOW` là các hằng Arduino biểu diễn logic cao/thấp, không phải đơn vị volt.

Trên Nano classic ATmega328P chạy 5 V, đầu ra HIGH không tải xấp xỉ 5 V; trên ESP32 classic là 3,3 V. Mỗi bo có giới hạn dòng, ngưỡng điện áp và chân đặc biệt riêng. Không nối hai đầu ra đang điều khiển mức ngược nhau, không nối động cơ trực tiếp vào GPIO.

## Vì sao đầu vào thả nổi đọc không ổn định?

Một chân INPUT không được nối đến mức xác định có thể nhận nhiễu và đổi trạng thái. Đó là **đầu vào thả nổi** (*floating*).

**Điện trở kéo lên** (*pull-up*) nối đầu vào về nguồn logic qua điện trở; **kéo xuống** (*pull-down*) nối về GND qua điện trở. Điện trở giữ mức mặc định nhưng vẫn cho phép nguồn tín hiệu khác đổi mức mà không tạo nối tắt nguồn trực tiếp.

Nano classic hỗ trợ kéo lên nội qua `INPUT_PULLUP`; không có chế độ kéo xuống nội tương đương trên bo này. Điện trở kéo của ESP32 phụ thuộc chân; không áp dụng mọi đặc tính Nano cho ESP32. Tham khảo [Arduino: pinMode()](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Functions/Digital%20IO/pinMode.adoc).

## Chuẩn bị và đấu nút nhấn

Ví dụ chỉ dành cho **Arduino Nano classic ATmega328P, logic 5 V**, bo rời, cấp nguồn USB. Dùng nút nhấn thường hở (thả ra thì hai tiếp điểm chưa nối). Không dùng chân D2 trên robot đang còn nối thiết bị khác.

1. Rút USB và các nguồn khác trước khi đấu dây.
2. Nối một tiếp điểm nút vào **D2**, tiếp điểm còn lại vào **GND**.
3. Không nối nút vào 5 V; bài dùng điện trở kéo lên bên trong bo.
4. Nếu nút có bốn chân, xác định hai tiếp điểm được nối khi nhấn; không lấy hai chân đã nối sẵn bên trong cùng một phía.
5. Kiểm tra rồi cắm USB. LED tích hợp trên Nano classic là D13 (`LED_BUILTIN`), không cần LED ngoài.

```text
Nguồn logic 5 V -- điện trở kéo nội -- D2 -- nút nhấn -- GND
```

Thả nút: điện trở kéo D2 lên HIGH. Nhấn nút: D2 nối về GND nên đọc LOW. Có dòng nhỏ qua điện trở kéo, không phải nối tắt trực tiếp 5 V với GND.

## Thực hành

```cpp
#include <Arduino.h>

const int CHAN_NUT = 2;

void setup() {
  Serial.begin(9600);
  pinMode(CHAN_NUT, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int trangThai = digitalRead(CHAN_NUT);
  if (trangThai == LOW) {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Dang nhan");
  } else {
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("Da tha");
  }
  delay(100);
}
```

Verify, Upload và mở Serial Monitor 9600. **Kết quả mong đợi:** thả nút LED tắt, in `Da tha`; giữ nút LED sáng, in `Dang nhan`. `delay(100)` giảm tốc độ in để quan sát; đây không phải chương trình phản hồi nhanh hay đếm số lần nhấn.

Thử bỏ dây GND của nút **khi đã rút USB**, sau đó cấp lại: nhấn nút không còn kéo được D2 xuống LOW. Khôi phục dây sau khi ngắt nguồn. Bài thử cho thấy đường GND là một phần của mạch tín hiệu.

## Lỗi thường gặp

- Luôn đọc LOW: nút bị nối qua cặp chân thông sẵn hoặc D2 chạm GND.
- Luôn đọc HIGH: dây GND/nút đứt hoặc chọn sai chân.
- Đổi sang INPUT rồi thấy nhiễu: đã tắt điện trở kéo nội mà chưa có điện trở ngoài.
- Một lần nhấn tạo nhiều chuyển trạng thái: tiếp điểm cơ khí có thể **dội** (*bounce*). Bài này đọc trạng thái, chưa triển khai chống dội để đếm lần nhấn.

Đối chiếu [pinout Nano](https://docs.arduino.cc/resources/pinouts/A000005-full-pinout.pdf) và [ví dụ kéo lên nội chính thức của Arduino](https://docs.arduino.cc/built-in-examples/digital/InputPullupSerial/).

[← delay() và millis()](../lap-trinh/05-delay-va-millis.md) · [Tiếp: Digital, ADC và PWM →](02-digital-adc-pwm.md)
