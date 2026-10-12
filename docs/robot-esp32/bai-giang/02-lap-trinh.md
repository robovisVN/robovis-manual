# Bài 2: Hướng dẫn lập trình xe ESP32 CH340 Type-C

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Phân biệt Verify và Upload.
- Tạo sketch độc lập, chọn board/COM và đọc lỗi biên dịch.
- Hiểu setup(), loop(), biến, điều kiện và thời gian chờ.

**Trước khi bắt đầu:** Đọc bài giới thiệu bo và robot — [mở bài trước](../01-gioi-thieu.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

Một sketch là chương trình chạy trên bo. `setup()` khởi tạo một lần; `loop()` được gọi liên tục. `const` đặt hằng số, `if` chọn hành động, `;` kết thúc câu lệnh và `//` ghi chú. Cú pháp phân biệt chữ hoa/thường.

Verify chỉ biên dịch trên máy tính; Upload mới ghi vào bo. Khi lỗi, đọc thông báo lỗi đầu tiên thay vì chỉ dòng “exit status 1”.

## 2. Chuẩn bị, bảng chân và đấu nối

Chỉ cần bo, cáp USB dữ liệu và máy tính. Ngắt dây robot để học Serial với bo riêng.

| Công cụ | Bài cài đặt |
| --- | --- |
| IDE, board và driver | [Mở hướng dẫn](../03-cai-arduino-ide.md) |
| Thư viện | [Mở hướng dẫn](../05-cai-thu-vien.md) |

Chọn ESP32 Dev Module cho bo bàn giao, đúng COM và driver CH340.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
unsigned long soLan = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.print("So lan lap: ");
  Serial.println(soLan);
  soLan++;
  delay(1000);
}
```

## 4. Giải thích chương trình

`unsigned long` lưu số đếm không âm; `++` tăng một đơn vị. `print()` giữ dòng, `println()` xuống dòng. `delay(1000)` làm chương trình chờ một giây; ở bài điều khiển xe nhiều tác vụ sẽ cần dùng millis() thay chờ dài.

## 5. Chạy thử và kết quả mong đợi

Đặt Serial Monitor **115200 baud**. Số đếm tăng mỗi giây; sau khi reset số đếm bắt đầu lại. Đổi chuỗi in, Upload rồi xác nhận log thay đổi.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Thiếu dấu ; / ngoặc | Đọc dòng lỗi và dòng ngay phía trước |
| Ký tự lạ | Baud Monitor trùng Serial.begin |
| Verify đúng nhưng không có log | Upload, COM, cáp và nguồn |

## 7. Bài tập thực hành

1. Đổi thời gian in thành 500 ms.
2. Thêm if để in “Da lap 5 lan” khi soLan bằng 5.
3. Giải thích vì sao sửa mã nhưng chưa Upload thì bo vẫn chạy chương trình cũ.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](../01-gioi-thieu.md) · [Lộ trình](../index.md) · [Bài tiếp: Điều khiển LED](03-led.md)
