# Bài 8: Đọc encoder và đo tốc độ bánh xe với Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Đếm xung bằng ngắt thay vì thăm dò liên tục.
- Đọc biến volatile an toàn.
- Tính vòng/phút và tốc độ tuyến tính từ số xung đã hiệu chuẩn.

**Trước khi bắt đầu:** Đọc năm mắt dò line — [mở bài trước](07-do-line.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

Encoder quang tạo xung khi đĩa có khe đi qua đầu đọc. Một kênh D0 cho số xung, không tự biết chiều quay. ISR chỉ tăng bộ đếm; không in Serial hay delay trong ISR. RISING đếm một sườn; đổi thành CHANGE thay đổi số đếm trên mỗi vòng, nên phải hiệu chuẩn lại PPR.

## 2. Chuẩn bị, bảng chân và đấu nối

| Encoder | Arduino Nano |
| --- | --- |
| D0 trái | 2 |
| D0 phải | 3 |
| VCC | Theo module, logic đầu ra phù hợp bo |
| GND | GND chung |

Ngắt nguồn motor và quay bánh bằng tay. Tháo đường IN1/IN2 của driver khỏi D0/D1 trong các bài dùng Serial. Chỉ ngắt nguồn động cơ chưa loại bỏ xung đột tín hiệu trên D0/D1. Đặt đĩa đúng khe đọc, không chạm đầu cảm biến.

`PPR = 20` dưới đây là giá trị thử theo loại đĩa thường gặp trong bộ mã; đếm một vòng bánh thật với RISING để xác nhận trước khi tin giá trị tốc độ.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
volatile unsigned long xungL = 0, xungR = 0;
void demL() { xungL++; }
void demR() { xungR++; }

void layXung(unsigned long &l, unsigned long &r) {
  noInterrupts();
  l = xungL; r = xungR;
  xungL = 0; xungR = 0;
  interrupts();
}

const float PPR = 20.0f;
unsigned long moc = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), demL, RISING);
  attachInterrupt(digitalPinToInterrupt(3), demR, RISING);
  moc = millis();
}

void loop() {
  unsigned long now = millis();
  unsigned long dt = now - moc;
  if (dt < 1000) return;
  moc = now;
  unsigned long l, r;
  layXung(l, r);
  float giay = dt / 1000.0f;
  Serial.print("L pulses / rpm: ");
  Serial.print(l); Serial.print(" / ");
  Serial.print(l * 60.0f / (PPR * giay));
  Serial.print(" | R pulses / rpm: ");
  Serial.print(r); Serial.print(" / ");
  Serial.println(r * 60.0f / (PPR * giay));
}
```

## 4. Giải thích chương trình

Nano đọc số nhiều byte trong vùng tạm ngắt để ISR không đổi giữa chừng. Bộ đếm được reset sau mỗi cửa sổ đo. RPM = xung × 60 / (PPR × thời gian giây). Vận tốc m/s = xung × chu vi bánh / (PPR × thời gian giây). Không dùng đường kính theo hình ảnh; đo bánh thật.

## 5. Chạy thử và kết quả mong đợi

Quay riêng bánh trái rồi phải: Monitor 9600 chỉ nhóm tương ứng tăng xung. Quay một vòng bánh trong một cửa sổ đo để kiểm tra PPR, hoặc cộng các cửa sổ nếu quay chậm. Với 20 xung trong một giây và PPR 20, kết quả là 60 rpm. Đứng yên cần gần 0.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Bánh quay nhưng xung 0 | D0, nguồn, GND, đĩa nằm đúng khe |
| Xung khi đứng yên | Dây/nhiễu/ngưỡng, chưa thêm lọc tùy tiện |
| Tốc độ gấp đôi | RISING/CHANGE và PPR có nhất quán không |

## 7. Bài tập thực hành

1. Đếm số xung một vòng bánh và cập nhật PPR.
2. Đo đường kính bánh, thêm dòng in m/s.
3. Giải thích vì sao một kênh encoder không biết xe tiến hay lùi.
4. So sánh cửa sổ đo 1 giây và 0,2 giây: phản ứng nhanh hơn nhưng lượng tử xung rõ hơn.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](07-do-line.md) · [Lộ trình](../index.md) · [Bài tiếp: HM-10 và Bluetooth](09-bluetooth.md)
