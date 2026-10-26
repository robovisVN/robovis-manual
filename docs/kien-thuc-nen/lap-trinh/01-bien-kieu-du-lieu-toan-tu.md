# Biến, kiểu dữ liệu và toán tử

**Mục tiêu:** chọn kiểu dữ liệu cho một giá trị nhỏ và dự đoán kết quả phép tính trước khi chạy code.

**Cần biết trước:** đã đọc [mức tín hiệu 3,3 V/5 V](../dien-dien-tu/03-tin-hieu-3v3-va-5v.md). Chuẩn bị IDE theo [hướng dẫn Nano](../../robot-arduino/03-cai-arduino-ide.md) hoặc [ESP32](../../robot-esp32/03-cai-arduino-ide.md). Quy trình tạo sketch, nạp và Serial đã có ở [bài lập trình đầu tiên](../../robot-arduino/bai-giang/02-lap-trinh.md); bài này tập trung vào dữ liệu, không lặp lại quy trình đó.

## Môi trường thực hành

Ví dụ dùng **Arduino Nano classic ATmega328P, logic 5 V**, bo rời chỉ nối USB dữ liệu, không nối cảm biến/driver/nguồn động cơ. Serial Monitor đặt **9600 baud** (tốc độ truyền trùng với code). Nạp sketch mới thay chương trình cũ: giữ mã nguồn bàn giao nếu dùng bo lấy từ robot.

Ví dụ chỉ in Serial nên cũng dùng được với **ESP32 classic, logic 3,3 V**, Arduino core ESP32 và bo rời. Chọn đúng board/cổng theo tài liệu ESP32; kích thước một số kiểu dữ liệu khác Nano.

## Biến chứa dữ liệu, kiểu quyết định cách lưu

**Biến** là vùng nhớ có tên. Trong `int soMau = 7;`, `int` là kiểu số nguyên, `soMau` là tên, `7` là giá trị ban đầu. Dấu `=` gán giá trị; không phải phép so sánh.

| Cách viết | Dùng khi nào? |
| --- | --- |
| `int soMau = 7;` | Số nguyên, như số lần lấy mẫu nhỏ |
| `float nhietDo = 26.5;` | Số có phần thập phân; dùng dấu chấm trong code |
| `bool daSanSang = false;` | Giá trị đúng/sai: `true` hoặc `false` |
| `const int SO_MAU_TOI_DA = 10;` | Giá trị không đổi sau khởi tạo |
| `unsigned long mocThoiGian = 0;` | Số nguyên không âm, thường dùng với `millis()` |

Trên Nano classic ATmega328P, `int` dài 16 bit, từ −32768 đến 32767. Không dùng phạm vi này cho mọi bo; trên ESP32 classic `int` dài 32 bit. `sizeof(int)` cho biết số byte trên nền tảng đang biên dịch. **Bit** là đơn vị nhị phân; trong các bo này một byte có 8 bit.

Không tăng số nguyên có dấu quá phạm vi. Kiểu `float` cũng có độ chính xác hữu hạn, không biểu diễn chính xác mọi số thập phân. Tham khảo [Arduino: kiểu int](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Variables/Data%20Types/int.adoc).

## Toán tử cần dùng trước tiên

`+`, `-`, `*`, `/` là cộng, trừ, nhân, chia; `%` lấy phần dư của phép chia số nguyên. Nhân/chia được thực hiện trước cộng/trừ; dùng ngoặc để nêu rõ ý định.

Nếu hai toán hạng là số nguyên, phép chia bỏ phần lẻ: `7 / 2` cho `3`. Gán kết quả đó vào `float` sau phép chia không khôi phục được phần lẻ. Muốn tính số thực, dùng `7 / 2.0` hoặc chuyển kiểu trước khi chia. Xem [Arduino: phép chia](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Structure/Arithmetic%20Operators/division.adoc).

## Thực hành: so sánh hai cách chia

Đây là sketch đầy đủ; lưu thành một sketch riêng, Verify rồi Upload. Mở Serial Monitor 9600 và nhấn Reset nếu đã bỏ lỡ phần in lúc khởi động.

```cpp
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  int tongMau = 7;
  int soNhom = 2;
  int phanNguyen = tongMau / soNhom;
  float trungBinh = tongMau / 2.0;

  Serial.println(phanNguyen);
  Serial.println(trungBinh, 1);
  Serial.println(tongMau % soNhom);
  Serial.println(sizeof(int));
}

void loop() {
  // In mot lan trong setup(), khong can lap lai.
}
```

**Kết quả mong đợi trên Nano classic:** bốn dòng `3`, `3.5`, `1`, `2`. Dòng cuối trên ESP32 classic là `4`. `Serial.begin()`/`println()` là **API Arduino**, tức công cụ nền tảng cung cấp; kiểu dữ liệu, khai báo và toán tử là kiến thức **C/C++**. `setup()` được môi trường Arduino gọi lúc khởi động, `loop()` được gọi lặp sau đó.

Đổi `tongMau` thành `8`, dự đoán ba dòng đầu rồi nạp lại: `4`, `4.0`, `0`.

## Lỗi thường gặp

- Viết `26,5` thay vì `26.5` trong code.
- Gán `float ketQua = 7 / 2;` rồi ngạc nhiên vì mất phần lẻ.
- Chia cho 0: cần kiểm tra mẫu số trước khi chia.
- Không thấy dữ liệu: kiểm tra Upload, cổng, baud và nhấn Reset.

[← Tín hiệu 3,3 V và 5 V](../dien-dien-tu/03-tin-hieu-3v3-va-5v.md) · [Tiếp: Câu lệnh điều kiện →](02-cau-lenh-dieu-kien.md)
