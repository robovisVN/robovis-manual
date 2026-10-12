# Nạp chương trình ESP32 và dùng Serial Monitor

**Mục tiêu:** thấy thông báo từ bo mà không cần đấu linh kiện ngoài.

## Tạo sketch đầu tiên

Chọn **File → New Sketch**, lưu thành `ESP32Serial`. Thay toàn bộ mã bằng:

```cpp
unsigned long soLan = 0;

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("ESP32 da khoi dong");
}

void loop() {
  Serial.print("Dang chay, lan: ");
  Serial.println(soLan);
  soLan++;
  delay(1000);
}
```

`setup()` chạy một lần khi khởi động/reset, `loop()` chạy lặp lại. `unsigned long` lưu số không âm; `++` tăng một đơn vị. `Serial.print()` in tiếp trên cùng dòng, `println()` thêm xuống dòng. Các chuỗi ví dụ không dấu để dễ đọc log.

## Biên dịch và nạp

1. Xác nhận board và Port như [bài cài đặt](03-cai-arduino-ide.md).
2. Nhấn **Verify**. Biên dịch thành công mới nhấn **Upload**.
3. Chờ nạp hoàn tất rồi mở **Tools → Serial Monitor**.
4. Chọn **115200 baud**; quan sát số đếm mỗi giây.
5. Nhấn EN/RESET: số đếm phải trở về 0. Nếu bỏ lỡ dòng khởi động khi mở Monitor, reset để xem lại.

Bo có mạch tự nạp thường không cần bấm nút. Nếu dừng ở `Connecting...`, giữ **BOOT**, bắt đầu Upload, thả khi IDE bắt đầu ghi. Khi vẫn chưa kết nối, có thể giữ BOOT rồi nhấn/thả EN, sau đó thả BOOT khi kết nối được. Xem [hướng dẫn nạp của Espressif](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html).

## Hiểu kết quả

| Quan sát | Ý nghĩa |
| --- | --- |
| Verify thành công | Mã biên dịch được cho board đã chọn |
| Upload hoàn tất | Mã đã được ghi vào bo |
| Có số đếm đều | Bo đang chạy chương trình và Serial đúng |
| Ký tự lạ | Kiểm tra baud và đúng cổng |
| Khởi động lặp liên tục | Kiểm tra nguồn và log reset, chưa nối tải |

**Bài tập:** đổi thời gian 1000 thành 300 ms, đổi chuỗi thông báo rồi nạp lại. Giữ một bản sketch chạy tốt để kiểm tra cáp/bo về sau.

[Bài trước](03-cai-arduino-ide.md) · [Bài tiếp: Thư viện](05-cai-thu-vien.md)
