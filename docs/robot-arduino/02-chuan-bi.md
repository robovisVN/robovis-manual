# Chuẩn bị trước khi học Arduino Nano

**Mục tiêu:** có đủ dụng cụ để nạp mã và làm mạch đơn giản.

| Dụng cụ | Công dụng |
| --- | --- |
| Máy tính có Internet | Cài IDE, gói bo và thư viện |
| Nano classic ATmega328P | Chạy các ví dụ |
| Cáp USB đúng cổng Nano, có truyền dữ liệu | Cấp nguồn và nạp mã |
| Breadboard và dây nối | Lắp mạch không hàn |
| LED thường, điện trở 330 Ω–1 kΩ | Thử đầu ra |
| Nút nhấn | Thử đầu vào |
| Servo vị trí và nguồn phù hợp, nếu có | Thực hành thư viện |

Chỉ cần Nano và cáp để chạy Blink. Đèn nguồn sáng không chứng minh cáp có truyền dữ liệu. Nếu Nano chưa hàn chân, cần hàn chân trước khi cắm breadboard; không dựa vào tiếp xúc lỏng.

## Chuẩn bị nguồn và robot

Robot bàn giao có board mở rộng Nano, dò line 5 kênh, HC-SR04, SG90, encoder và HM10 khi dùng Bluetooth. [Tài liệu khi nhận hàng](https://docs.google.com/document/d/1v15Tzh_bDJ4Tez326MCeS8L-1pQc-sz2sl5fraLJJmo/edit) cho biết cảm biến được tháo để vận chuyển; cần lắp lại trước khi chạy. Bài LED/nút nhấn dùng Nano riêng, không thêm linh kiện vào chân robot đang sử dụng.

1. Tắt nguồn trước khi đổi dây; ghi lại sơ đồ đang có.
2. Xác định loại driver, nhãn chân và thông số nguồn.
3. Ngắt nguồn động cơ, thử Nano riêng qua USB trước.
4. Chưa nối nguồn ngoài đồng thời với USB nếu chưa rõ cách phân phối nguồn của bo.

Phân biệt **5V**, **VIN**, **GND**. Không đưa điện áp pin động cơ vào chân 5V hoặc chân tín hiệu. Chọn nguồn theo thông số bo, không suy ra điện áp từ hình dạng đầu cắm.

## Lưu các bài học

Tạo thư mục `HocRobotNano`. Mỗi bài là một sketch riêng, chẳng hạn `NanoBlink/NanoBlink.ino`. Tên tệp `.ino` chính cần trùng tên thư mục sketch. Giữ bản mã đã chạy tốt trước khi sửa.

**Kiểm tra:** biết loại Nano, có cáp đúng cổng và đã ngắt nguồn động cơ. Hãy nạp Blink trước khi đấu linh kiện ngoài.

[Bài trước](01-gioi-thieu.md) · [Bài tiếp: Cài IDE](05-cai-arduino-ide.md)
