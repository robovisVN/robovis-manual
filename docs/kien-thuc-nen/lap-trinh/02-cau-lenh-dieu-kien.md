# Câu lệnh điều kiện

**Mục tiêu:** dùng `if / else if / else` để chọn đúng một hành động dựa trên dữ liệu.

**Cần biết trước:** [biến và toán tử](01-bien-kieu-du-lieu-toan-tu.md). Giữ môi trường của bài trước: Nano classic ATmega328P 5 V hoặc ESP32 classic 3,3 V, bo rời chỉ nối USB, Serial Monitor 9600 baud. Chưa dùng cảm biến thật.

## Chương trình đưa ra quyết định thế nào?

Một **điều kiện** là biểu thức có giá trị đúng (`true`) hoặc sai (`false`). `if` chạy khối lệnh khi điều kiện đúng. `else if` kiểm tra tiếp khi nhánh trước sai; `else` là nhánh còn lại. Trong một chuỗi như vậy, chỉ nhánh đúng đầu tiên được thực hiện.

Ví dụ bài này dùng **khoảng cách giả lập**, đơn vị cm. Chương trình chỉ in phân loại, không phải thuật toán tránh vật cản đã sẵn sàng điều khiển robot.

| Toán tử C/C++ | Ý nghĩa |
| --- | --- |
| `==`, `!=` | Bằng, khác |
| `<`, `<=`, `>`, `>=` | So sánh lớn/nhỏ |
| `&&` | Và: cả hai điều kiện đều đúng |
| `||` | Hoặc: ít nhất một điều kiện đúng |
| `!` | Đảo đúng thành sai và ngược lại |

**`=` gán, `==` so sánh.** Thêm dấu `;` ngay sau `if (...)` tạo một câu lệnh rỗng, khiến khối phía sau không còn thuộc điều kiện như bạn dự định. Xem [Arduino: if](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Structure/Control%20Structure/if.adoc).

## Thực hành: kiểm tra dữ liệu trước khi phân loại

```cpp
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  int khoangCachCm = 25;
  bool duLieuHopLe = true;

  if (!duLieuHopLe || khoangCachCm < 0) {
    Serial.println("Khong dung du lieu nay");
  } else if (khoangCachCm < 20) {
    Serial.println("Gan");
  } else if (khoangCachCm < 40) {
    Serial.println("Trung binh");
  } else {
    Serial.println("Xa");
  }
}

void loop() {
}
```

Verify, Upload, mở Serial Monitor 9600 rồi Reset nếu cần. `if` và toán tử thuộc C/C++; `Serial` thuộc API Arduino.

**Kết quả mong đợi:** in `Trung binh` một lần. Vì 25 không nhỏ hơn 20 nhưng nhỏ hơn 40, chương trình dừng kiểm tra ở nhánh thứ ba.

## Thử các giá trị biên

Mỗi lần đổi giá trị, nạp lại chương trình:

| `khoangCachCm` | `duLieuHopLe` | Kết quả cần thấy |
| --- | --- | --- |
| 19 | `true` | `Gan` |
| 20 | `true` | `Trung binh` |
| 40 | `true` | `Xa` |
| 25 | `false` | `Khong dung du lieu nay` |
| −1 | `true` | `Khong dung du lieu nay` |

Giá trị biên là điểm chuyển nhánh, ở đây là 20 và 40. Việc kiểm tra ngay dưới, đúng tại và ngay trên ngưỡng giúp tìm sai sót `<` với `<=`.

## Lỗi thường gặp

- Kiểm tra `< 40` trước `< 20`: giá trị 10 đã vào nhánh đầu, không tới nhánh `< 20`.
- Dùng nhiều `if` riêng và nghĩ chỉ một nhánh chạy: các `if` độc lập có thể cùng đúng.
- Coi giá trị đo lỗi bằng 0 là vật rất gần: cần quy tắc xác nhận dữ liệu theo cảm biến thật.
- Dùng ví dụ này cho động cơ ngay: bài chưa xử lý mất tín hiệu, quán tính hay giới hạn sản phẩm.

[← Biến và kiểu dữ liệu](01-bien-kieu-du-lieu-toan-tu.md) · [Tiếp: Vòng lặp →](03-vong-lap.md)
