# Bài 4: Điều khiển servo SG90 với Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Phân biệt servo vị trí với motor DC.
- Đấu nguồn và tín hiệu servo đúng chân.
- Dùng thư viện đặt góc và thử chuyển động trong khoảng nhỏ.

**Trước khi bắt đầu:** Điều khiển đầu ra bằng LED — [mở bài trước](03-led.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

Servo vị trí có bộ điều khiển và phản hồi bên trong. Bạn gửi xung yêu cầu vị trí, không dùng PWM độ sáng LED để đặt góc. `write(90)` là góc yêu cầu; góc cơ khí thực tế phụ thuộc servo, gá và hành trình.

## 2. Chuẩn bị, bảng chân và đấu nối

Cài Servo của Arduino, như [bài thư viện](../06-cai-thu-vien.md).

| Dây servo | Kết nối |
| --- | --- |
| Signal | A5 |
| VCC | Nguồn servo phù hợp thông số linh kiện |
| GND | GND nguồn servo và GND bo |

Bo cấp bằng USB, servo cấp từ nguồn tải phù hợp, không nối cực dương nguồn ngoài vào 5V/3V3 bo trong mạch học. Xác định dây từ tài liệu servo, không chỉ theo màu. Ngắt nguồn motor và tháo tay đòn/cơ cấu tải trước lần thử đầu.

Robot dùng A5 cho SG90 quét siêu âm; kiểm tra ốc gá như [ảnh bàn giao](../03-lap-rap.md).

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
#include <Servo.h>
Servo servoThu;

void setup() {
  servoThu.attach(A5);
  servoThu.write(90);
  delay(1000);
}

void loop() {
  servoThu.write(75);
  delay(1000);
  servoThu.write(105);
  delay(1000);
}
```

## 4. Giải thích chương trình

`attach()` chọn chân tín hiệu; thư viện tạo xung cho servo. Các lệnh write() thử 75° và 105° thay vì hai đầu hành trình. Servo trên Nano dùng timer có thể ảnh hưởng PWM D9/D10; driver bộ robot dùng D5/D6.

## 5. Chạy thử và kết quả mong đợi

Servo đứng gần giữa, sau đó qua lại trong khoảng nhỏ. Dừng ngay nếu servo kẹt, rung mạnh, nóng hoặc bo reset. Chỉ thử gắn lại cơ cấu sau khi xác nhận hành trình không va chạm.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Thiếu header | Đúng thư viện của Nano/ESP32 |
| Servo rung, bo reset | Nguồn tải, dòng và GND |
| Servo không quay | Chân Signal, nguồn và cơ cấu kẹt |

## 7. Bài tập thực hành

1. Thay 75°/105° bằng 80°/100°.
2. Viết hàm đưa servo về giữa.
3. Giải thích vì sao nguồn USB cho bo không bảo đảm đủ dòng cho servo.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](03-led.md) · [Lộ trình](../index.md) · [Bài tiếp: Motor DC và L298N](05-dong-co.md)
