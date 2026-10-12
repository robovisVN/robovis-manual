# Bài 3: Điều khiển LED với Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Cấu hình một chân OUTPUT.
- Điều khiển HIGH/LOW và thay đổi nhịp nhấp nháy.
- Giải thích sự khác nhau giữa LED nguồn và LED điều khiển.

**Trước khi bắt đầu:** Tạo và nạp sketch đầu tiên — [mở bài trước](02-lap-trinh.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

LED phát sáng khi có dòng đúng chiều. Điện trở nối tiếp hạn dòng; HIGH/LOW là mức logic, không phải lệnh cấp nguồn cho mọi tải. Đây là bước kiểm tra đầu ra trước khi điều khiển servo và driver.

## 2. Chuẩn bị, bảng chân và đấu nối

Dùng LED **L tích hợp** trên Nano, không cần đấu dây ngoài; LED nguồn sáng liên tục là LED khác. Ngắt nguồn motor và tháo các dây robot khi học. Nếu dùng LED ngoài: D13 → điện trở 330 Ω–1 kΩ → anode, cathode → GND.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
const int LED = LED_BUILTIN;

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(500);
  digitalWrite(LED, LOW);
  delay(500);
}
```

## 4. Giải thích chương trình

`pinMode()` đặt chiều tín hiệu. HIGH bật LED theo cách mắc trên; LOW tắt. Hai lần delay(500) tạo một chu kỳ sáng/tắt dài một giây. Không suy ra LED active-low trên bo khác cũng có cùng hành vi.

## 5. Chạy thử và kết quả mong đợi

LED sáng 0,5 giây và tắt 0,5 giây. Đổi cả hai thời gian thành 200 ms, nạp lại và xác nhận nhịp nhanh hơn.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| LED ngoài không sáng | Chiều LED, điện trở, GND, chân trong mã |
| Chỉ thấy đèn nguồn | Quan sát đúng LED L hoặc LED ngoài |
| Nhịp không đổi | Đã Upload mã mới và chọn đúng bo/cổng chưa |

## 7. Bài tập thực hành

1. Cho LED sáng 1 giây, tắt 0,2 giây.
2. Tạo tín hiệu ba nháy ngắn rồi nghỉ một giây.
3. Viết lại với millis() để không chờ trong loop; tham khảo [bài lập trình nền tảng](../04-lap-trinh.md).

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](02-lap-trinh.md) · [Lộ trình](../index.md) · [Bài tiếp: Servo](04-servo.md)
