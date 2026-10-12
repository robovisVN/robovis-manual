# Bài 1: Giới thiệu xe Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Nhận diện Nano classic và các phần của robot.
- Giải thích đường đi từ cảm biến tới quyết định điều khiển motor.
- Phân biệt IDE, sketch, thư viện, Verify và Upload.

Bộ robot trong [tài liệu bàn giao Robovis](https://drive.google.com/drive/folders/1gmMNJcWVTs5gortEIQQb7wWsLAIqWUl-) dùng **Arduino Nano**, board mở rộng, driver, encoder, dò line 5 kênh, HC-SR04 và servo SG90. Mã Bluetooth dùng Dabble và module HM10. Xem [hướng dẫn sử dụng chung](08-su-dung-robot.md) để chọn mã và đối chiếu chân.

## 1. Từ mã lệnh đến chuyển động

Arduino là nền tảng giúp bạn lập trình bo vi điều khiển. Bạn viết mã trên máy tính, biên dịch rồi nạp vào bo. Bo có thể chạy chương trình khi được cấp nguồn, kể cả khi rút khỏi máy tính.

Trong robot, Nano đọc cảm biến, quyết định hành động và gửi tín hiệu tới driver động cơ. Động cơ lấy điện từ nguồn qua driver; chân Nano không cấp điện trực tiếp cho động cơ.

```mermaid
flowchart LR
    A[Cảm biến / nút nhấn] --> B[Arduino Nano]
    B --> C[Driver động cơ]
    C --> D[Động cơ]
    E[Nguồn động cơ] --> C
```

## 2. Nhận diện Nano

Ví dụ dùng **Nano classic ATmega328P**: chân digital D0–D13, analog A0–A7, mức logic 5 V. A6/A7 chỉ là đầu vào analog. D0/RX và D1/TX dùng cho Serial, nên để trống khi học nạp qua USB. Đối chiếu pinout trong [tài liệu Nano của Arduino](https://docs.arduino.cc/hardware/nano/).

Nano tương thích có thể dùng CH340 và cổng USB khác bo gốc. Loại cổng không quyết định vi điều khiển hoặc bootloader. Nếu bo ghi Nano Every, Nano 33 hoặc Nano ESP32, cần hướng dẫn đúng dòng đó.

## 3. Thuật ngữ cơ bản

| Từ | Ý nghĩa |
| --- | --- |
| Sketch | Chương trình Arduino, thường có tệp `.ino` |
| IDE | Ứng dụng viết, biên dịch và nạp mã |
| Board package / core | Gói hỗ trợ một họ bo |
| Library | Thư viện mã có sẵn để sử dụng linh kiện/tính năng |
| Verify | Biên dịch mã trên máy tính |
| Upload | Biên dịch rồi gửi mã vào bo |
| Port / COM | Cổng giao tiếp với bo |

## 4. Thực hành nhận diện và bài tập

1. Tìm tên chip, GND và D13 trên bo/pinout.
2. Chỉ vị trí board mở rộng, driver, encoder, servo và cảm biến trên xe.
3. Vẽ luồng cảm biến → Nano → driver → motor, đánh dấu đường nguồn tải riêng.
4. Giải thích vì sao Verify thành công chưa chứng minh mã đã chạy trên Nano.

**Điều kiện học tiếp:** nhận diện được từng phần và biết sketch sẽ được nạp vào đâu. Nếu không khớp tên bo/phần cứng, xem [chuẩn bị](02-chuan-bi.md) và sơ đồ bàn giao trước khi cấp nguồn.

[Lộ trình](index.md) · [Bài tiếp: Hướng dẫn lập trình xe](bai-giang/02-lap-trinh.md)
