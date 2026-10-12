# Lập trình Nano: LED, nút nhấn và Serial

**Mục tiêu:** viết mã phản ứng với đầu vào. Chuẩn bị mạch ở [bài đấu nối](03-lap-rap.md).

!!! warning "Học trên Nano riêng"
    Ví dụ dùng D4/D2, còn robot dùng hai chân này cho driver/encoder. Tháo Nano khỏi board robot trước khi thử. Serial ở bài này không dùng đồng thời với bộ mã robot sử dụng D0/D1 điều khiển động cơ.

## Cấu trúc sketch

`setup()` chạy một lần khi khởi động/reset; `loop()` được gọi lặp lại. `const` đặt tên chân cố định; `pinMode()` chọn chế độ chân; `digitalRead()` đọc, `digitalWrite()` xuất HIGH/LOW. `;` kết thúc lệnh, `{}` bao quanh khối mã, `//` bắt đầu ghi chú.

## Giữ nút để bật LED

Tạo sketch `NanoNutNhan`:

```cpp
const byte CHAN_LED = 4;
const byte CHAN_NUT = 2;

void setup() {
  pinMode(CHAN_LED, OUTPUT);
  pinMode(CHAN_NUT, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  bool dangNhan = (digitalRead(CHAN_NUT) == LOW);
  digitalWrite(CHAN_LED, dangNhan ? HIGH : LOW);
  Serial.println(dangNhan ? "Dang nhan" : "Da tha");
  delay(100);
}
```

Với kéo lên nội, thả nút đọc HIGH; nhấn nút nối GND đọc LOW. `==` so sánh, `=` gán; `bool` chứa true/false. `điều_kiện ? giá_trị_đúng : giá_trị_sai` chọn một giá trị.

Verify, Upload rồi mở **Tools → Serial Monitor**, đặt **9600 baud** trùng `Serial.begin(9600)`. LED sáng khi giữ nút, tắt khi thả; Serial đổi thông báo. Xem [các ví dụ nền tảng Arduino](https://docs.arduino.cc/built-in-examples/).

## Nhấp nháy mà vẫn đọc nút

`delay()` làm mã chờ. Để đọc đầu vào liên tục, thay toàn bộ sketch bằng bản dưới: giữ nút để LED sáng liên tục, thả để nhấp nháy.

```cpp
const byte CHAN_LED = 4;
const byte CHAN_NUT = 2;
unsigned long mocTruoc = 0;
bool ledSang = false;

void setup() {
  pinMode(CHAN_LED, OUTPUT);
  pinMode(CHAN_NUT, INPUT_PULLUP);
}

void loop() {
  unsigned long hienTai = millis();
  if (digitalRead(CHAN_NUT) == LOW) {
    ledSang = true;
    mocTruoc = hienTai;
  } else if (hienTai - mocTruoc >= 500) {
    mocTruoc = hienTai;
    ledSang = !ledSang;
  }
  digitalWrite(CHAN_LED, ledSang ? HIGH : LOW);
}
```

`millis()` đo thời gian từ lúc khởi động; phép trừ `unsigned long` vẫn dùng được khi bộ đếm quay vòng. `!` đảo trạng thái. Bản này không in Serial.

**Bài tập:** đổi 500 thành 200 ms. Ở bài đầu, sửa để nhấn tắt LED, thả bật LED. Giải thích vì sao nút nối 5V không kéo đầu vào xuống LOW.

Ví dụ giữ nút chưa đếm lần nhấn. Khi bật/tắt theo mỗi lần nhấn, cần chống dội để một lần nhấn không bị đếm nhiều lần.

[Bài trước](03-lap-rap.md) · [Bài tiếp: Chạy thử và xử lý lỗi](07-chay-thu-va-xu-ly-loi.md)
