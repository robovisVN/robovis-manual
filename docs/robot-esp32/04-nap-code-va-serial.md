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

Theo [HD nạp code của Robovis](https://docs.google.com/document/d/1kt_3J2K9uy3t73HraCWzz_dliXwaGpwbH0eBLzfxwZQ/edit), **không bấm BOOT hoặc RST khi đang nạp** trên bo bàn giao. Chờ cơ chế tự nạp hoàn tất. Nếu lỗi kết nối, kiểm tra cáp, driver, board và COM trước; thao tác reset ở bước 5 chỉ thực hiện sau khi nạp xong.

## Hiểu kết quả

| Quan sát | Ý nghĩa |
| --- | --- |
| Verify thành công | Mã biên dịch được cho board đã chọn |
| Upload hoàn tất | Mã đã được ghi vào bo |
| Có số đếm đều | Bo đang chạy chương trình và Serial đúng |
| Ký tự lạ | Kiểm tra baud và đúng cổng |
| Khởi động lặp liên tục | Kiểm tra nguồn và log reset, chưa nối tải |

**Bài tập:** đổi thời gian 1000 thành 300 ms, đổi chuỗi thông báo rồi nạp lại. Giữ một bản sketch chạy tốt để kiểm tra cáp/bo về sau.

## Nạp chương trình robot thực tế

Tải toàn bộ [thư mục main](https://drive.google.com/drive/folders/1HeAZaW--JOkl67SG3IJOWxS1aPKAO5UB), giải nén và giữ đúng cấu trúc:

```text
main/
├── main.ino
├── do_line.cpp
└── do_line.h
```

`main.ino` chứa Wi-Fi, giao diện và điều khiển tay; `do_line.cpp` xử lý dò line/tránh vật cản; `do_line.h` khai báo hàm kết nối hai phần. Đây là tệp project, không cài `do_line.h` qua Library Manager.

Ngắt nguồn động cơ, cài [thư viện sản phẩm](05-cai-thu-vien.md), mở **File → Open → main/main.ino**, chọn **ESP32 Dev Module** và đúng COM, Verify rồi Upload. Không chỉ tải riêng `main.ino`. Khi Upload báo hoàn tất và xuất hiện `Hard resetting via RTS pin...`, mở Monitor 115200 để kiểm tra dòng `Hotspot IP:`. Tiếp tục [hướng dẫn sử dụng robot](08-su-dung-robot.md).

[Bài trước](03-cai-arduino-ide.md) · [Bài tiếp: Thư viện](05-cai-thu-vien.md)
