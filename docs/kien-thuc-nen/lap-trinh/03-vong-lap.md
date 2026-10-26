# Vòng lặp

**Mục tiêu:** lặp một công việc đúng số lần và nhận ra điều kiện khiến chương trình không thoát được.

**Cần biết trước:** [câu lệnh điều kiện](02-cau-lenh-dieu-kien.md). Thực hành trên bo rời Nano classic ATmega328P 5 V hoặc ESP32 classic 3,3 V, chỉ nối USB; Serial Monitor 9600 baud. Không đấu thêm phần cứng.

## Phân biệt `loop()` với vòng lặp C/C++

Arduino gọi hàm `loop()` lặp lại sau `setup()`. Đây là quy ước của môi trường Arduino. Bên trong một hàm, C/C++ có các cấu trúc `for`, `while`, `do...while` để lặp một khối lệnh.

**`for`** phù hợp khi biết số lượt: khởi tạo biến đếm → kiểm tra điều kiện → chạy thân → cập nhật biến đếm → kiểm tra lại. **`while`** kiểm tra điều kiện trước mỗi lượt; nếu điều kiện sai ngay đầu, thân không chạy lần nào. Xem [Arduino: for](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Structure/Control%20Structure/for.adoc) và [while](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Structure/Control%20Structure/while.adoc).

## Thực hành: chỉ in năm lượt

```cpp
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  for (int luot = 1; luot <= 5; luot++) {
    Serial.print("Luot ");
    Serial.println(luot);
  }
  Serial.println("Da xong");
}

void loop() {
}
```

Verify và Upload, mở Serial Monitor 9600 rồi Reset. `luot++` tăng biến đếm thêm 1 sau mỗi lượt. Biến `luot` được khai báo trong `for`, chỉ dùng trong phạm vi vòng lặp đó.

**Kết quả mong đợi:** `Luot 1` đến `Luot 5`, sau đó `Da xong`, rồi không in nữa. Lần kiểm tra kế tiếp, `luot` bằng 6 nên điều kiện `luot <= 5` sai.

Nếu đổi `<= 5` thành `< 5`, dự đoán trước khi nạp: chỉ có bốn lượt. Nếu chuyển cả vòng `for` sang `loop()`, cả chuỗi sẽ lặp mãi do Arduino gọi lại `loop()`, không phải do `for` không kết thúc.

## Cùng công việc bằng `while`

Đây là sketch độc lập; thay toàn bộ sketch trước nếu muốn thử:

```cpp
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  int luot = 1;
  while (luot <= 5) {
    Serial.print("Luot ");
    Serial.println(luot);
    luot++;
  }
  Serial.println("Da xong");
}

void loop() {
}
```

Kết quả giống ví dụ `for`. Nếu quên `luot++`, điều kiện không đổi, vòng lặp không tự kết thúc. Không cần nạp thử vòng lặp vô hạn để hiểu lỗi này.

## Khi cần làm nhiều việc

Vòng lặp dài giữ chương trình ở trong thân lặp; các lệnh sau nó chưa được chạy. Ví dụ, chờ nút nhấn bằng một `while` vô hạn có thể khiến phần cập nhật khác không được thực hiện. Với ESP32, vòng lặp bận còn có thể ảnh hưởng cơ chế giám sát của hệ thống.

`break` thoát vòng lặp gần nhất; `continue` bỏ phần thân còn lại của lượt hiện tại. Chưa cần dùng chúng trong bài này: trước tiên hãy viết điều kiện kết thúc rõ ràng. Bài thời gian sẽ chỉ cách kiểm tra công việc theo từng lượt `loop()`.

## Lỗi thường gặp

- Dư dấu `;` sau `for (...)` hoặc `while (...)`: thân lặp thực tế có thể rỗng.
- Biến đếm tăng nhưng điều kiện cần biến giảm, hoặc ngược lại.
- In quá nhiều làm Serial khó đọc: dùng bài mẫu ngắn trong `setup()` để quan sát.
- Dùng tên `luot` ngoài phạm vi khai báo: trình biên dịch báo không tìm thấy biến.

[← Câu lệnh điều kiện](02-cau-lenh-dieu-kien.md) · [Tiếp: Hàm và cách chia chương trình →](04-ham-va-chia-chuong-trinh.md)
