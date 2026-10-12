# Thực hành bổ trợ: nút nhấn, Serial và millis

**Mục tiêu:** giữ một nút để bật LED, sau đó học cách không để chương trình chờ lâu. Bài này có thể làm sau [bài LED](bai-giang/03-led.md); chưa cần để sử dụng chương trình robot có sẵn.

## Trước khi làm

Dùng **Nano rời khỏi board robot**, mạch LED/nút ở [bài đấu nối](03-lap-rap.md). LED ở D4 qua điện trở, nút nối D2 với GND. D4/D2 của xe đang dùng cho driver/encoder nên không cắm thêm mạch này lên robot đã nối sẵn.

Bạn đã biết mở Monitor 9600 và nạp sketch. Rút USB trước khi thay dây.

## Bước 1. Đọc nút trước, chưa điều khiển LED

Tạo `NanoDocNut`:

```cpp
void setup() {
  pinMode(2, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  Serial.println(digitalRead(2));
  delay(100);
}
```

Upload và mở Monitor 9600.

| Thao tác | Kết quả cần thấy |
| --- | --- |
| Thả nút | 1 / HIGH |
| Giữ nút | 0 / LOW |

INPUT_PULLUP kéo đầu vào lên bằng điện trở nội khi thả. Nhấn nút nối chân về GND, nên **nhấn là LOW**, không phải HIGH. Không nối nút lên 5V trong mạch này.

Nếu luôn 0, kiểm tra nút bốn chân: hai chân cùng cặp đã nối sẵn, chọn hai phía của tiếp điểm chứ không chọn cùng cặp. Nếu luôn 1, kiểm tra nút có thật sự nối D2 về GND khi nhấn không.

## Bước 2. Dùng if để điều khiển LED

Tạo `NanoNutLED`, thay toàn bộ sketch:

```cpp
void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(4, OUTPUT);
}

void loop() {
  int trangThaiNut = digitalRead(2);
  if (trangThaiNut == LOW) {
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }
}
```

`==` so sánh; `=` lưu một giá trị. Đọc câu if: **nếu nút đang LOW thì bật LED, nếu không thì tắt**. Mã này không in log; kiểm tra bằng LED ngoài, không chờ thông báo trên Monitor.

**Kết quả cần thấy:** giữ nút đèn sáng, thả nút đèn tắt. Chưa cần phép viết rút gọn hoặc đếm số lần nhấn.

## Bước 3. Vì sao delay có thể làm chậm phản ứng?

Ở bài LED, delay(1000) giúp đèn giữ trạng thái một giây. Trong thời gian chờ đó, các lệnh đọc nút trong loop chưa được thực hiện tiếp. Nếu cần đọc nút và đổi đèn liên tục, ta xem giờ thay vì đứng chờ.

`millis()` cho số mili giây từ lúc Nano khởi động. Ví dụ, mốc trước là 1000, giờ là 1500: đã qua 500 ms. Có thể đổi đèn khi chênh lệch đủ lớn rồi tiếp tục đọc nút ở mỗi vòng.

## Bước 4. Nhấp nháy khi thả, sáng liên tục khi giữ

Thay toàn bộ sketch bằng:

```cpp
unsigned long mocTruoc = 0;
bool ledSang = false;

void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(4, OUTPUT);
}

void loop() {
  unsigned long hienTai = millis();
  if (digitalRead(2) == LOW) {
    ledSang = true;
    mocTruoc = hienTai;
  } else if (hienTai - mocTruoc >= 500) {
    mocTruoc = hienTai;
    if (ledSang == true) {
      ledSang = false;
    } else {
      ledSang = true;
    }
  }
  if (ledSang == true) {
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }
}
```

`bool` giữ hai giá trị true/false: ở đây là ý định bật/tắt LED. unsigned long giữ thời gian không âm. Mỗi khi đủ 500 ms, mã đổi trạng thái, không có delay chặn loop. Dùng phép **thời gian hiện tại trừ mốc trước** cũng giúp xử lý khi bộ đếm millis quay vòng.

**Kết quả cần thấy:** thả nút đèn nhấp nháy; giữ nút đèn sáng liên tục; thả ra khoảng 500 ms thì bắt đầu đổi trạng thái. Nếu không đúng, quay lại bước đọc nút riêng thay vì sửa mọi phần cùng lúc.

## Bài tập và điều kiện hoàn thành

Đổi 500 thành 200, rồi kiểm tra nhịp nhanh hơn mà nút vẫn phản ứng. Ở bước 2, đảo logic để giữ nút tắt LED. Khi đếm từng lần nhấn sẽ cần chống dội nút, vì tiếp điểm có thể đổi nhanh nhiều lần trong một lần nhấn; bài này chỉ đọc trạng thái giữ/thả.

Bạn hoàn thành khi giải thích được LOW lúc nhấn và sự khác nhau giữa đứng chờ delay với kiểm tra giờ bằng millis.

[Đấu nối](03-lap-rap.md) · [Lộ trình](index.md) · [Xử lý lỗi](07-chay-thu-va-xu-ly-loi.md)
