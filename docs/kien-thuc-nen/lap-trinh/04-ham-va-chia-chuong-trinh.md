# Hàm và cách chia chương trình

**Mục tiêu:** tách một phép tính thành hàm có đầu vào, đầu ra rõ ràng rồi gọi lại với dữ liệu khác nhau.

**Cần biết trước:** [biến](01-bien-kieu-du-lieu-toan-tu.md), [điều kiện](02-cau-lenh-dieu-kien.md) và [vòng lặp](03-vong-lap.md). Bo rời Nano classic ATmega328P 5 V hoặc ESP32 classic 3,3 V, chỉ USB, Serial Monitor 9600 baud.

## Hàm là một công việc có tên

Một **hàm** gom các lệnh để thực hiện một nhiệm vụ. **Tham số** nhận dữ liệu đưa vào; `return` trả kết quả cho nơi gọi. Hàm có kiểu trả về `void` thực hiện công việc nhưng không trả một giá trị.

Ví dụ `float tinhCongSuat(float dienAp, float dongDien)` nghĩa là hàm nhận hai số thực và trả một số thực. Khi gọi `tinhCongSuat(5.0, 0.2)`, giá trị 5,0 và 0,2 được đưa vào hai tham số tương ứng.

Định nghĩa hàm chưa làm hàm chạy. Phải có lời gọi hàm. Bài này đặt định nghĩa trước nơi gọi để dễ đọc và không phụ thuộc việc Arduino tự sinh khai báo hàm.

## Thực hành: tính rồi in kết quả

```cpp
#include <Arduino.h>

float tinhCongSuat(float dienAp, float dongDien) {
  return dienAp * dongDien;
}

void inCongSuat(float congSuat) {
  Serial.print("Cong suat: ");
  Serial.print(congSuat, 2);
  Serial.println(" W");
}

void setup() {
  Serial.begin(9600);
  float ketQua = tinhCongSuat(5.0, 0.2);
  inCongSuat(ketQua);
  inCongSuat(tinhCongSuat(3.3, 0.1));
}

void loop() {
}
```

Các số là dữ liệu giả định, đơn vị V và A; chương trình không đo nguồn thật. Verify/Upload rồi mở Serial Monitor 9600, Reset nếu cần.

**Kết quả mong đợi:**

```text
Cong suat: 1.00 W
Cong suat: 0.33 W
```

`tinhCongSuat()` chỉ tính, không in. `inCongSuat()` chỉ trình bày kết quả. Nhờ tách hai việc, sau này có thể đổi cách hiển thị mà không sửa phép tính.

## Phạm vi và thay đổi giá trị

`ketQua` khai báo trong `setup()` là **biến cục bộ**, chỉ tồn tại trong lần gọi và phạm vi hàm đó. Tham số `dienAp`, `dongDien` cũng là biến cục bộ. Với kiểu số trong ví dụ, tham số được **truyền theo giá trị**: hàm nhận một bản sao, sửa tham số không tự sửa biến của nơi gọi.

Các hàm do bạn viết, tham số, `return` và phạm vi biến là C/C++. `Serial` là API Arduino. `setup()` và `loop()` cũng là các hàm C++, nhưng được Arduino gọi theo quy ước của nền tảng. Tham khảo [Arduino API – Sketch và return](https://docs.arduino.cc/learn/programming/reference).

## Tự thực hành

Thêm một lời gọi `inCongSuat(tinhCongSuat(5.0, 0.1));` trong `setup()`. Dự đoán: thêm dòng `Cong suat: 0.50 W`. Giữ các lời gọi cũ để kiểm tra việc dùng lại hàm.

**Hoàn thành khi:** giải thích được dữ liệu đi vào đâu, kết quả đi ra đâu và vì sao chỉ có hàm in dùng `Serial`.

## Lỗi thường gặp

- Quên `return` ở hàm cần trả kết quả.
- Gọi sai số lượng tham số hoặc đảo thứ tự dữ liệu; trong bài này cả hai số cùng kiểu nên trình biên dịch không phát hiện mọi nhầm lẫn về ý nghĩa.
- Định nghĩa hàm mới bên trong `setup()`: C++ không cho định nghĩa hàm thông thường lồng như vậy.
- Dùng biến cục bộ từ một hàm khác: cần truyền qua tham số hoặc trả kết quả.

[← Vòng lặp](03-vong-lap.md) · [Tiếp: delay() và millis() →](05-delay-va-millis.md)
