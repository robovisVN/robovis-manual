# Bài 1: Giới thiệu xe ESP32 CH340 Type-C

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Phân biệt vi điều khiển ESP32, chip USB CH340 và cổng Type-C.
- Nhận diện driver/cảm biến của robot và mức logic 3,3 V.
- Giải thích quá trình nạp mã và kết nối điều khiển Wi-Fi.

Robot trong [bộ tài liệu ESP32 Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt) dùng bo CH340 Type-C, board mở rộng, L298N, dò line 5 kênh, encoder và HC-SR04. Bộ mã tạo Wi-Fi **ESP32-Car** và giao diện web với **Manual / Line follow**. Hướng dẫn bàn giao chọn **ESP32 Dev Module**. Xem [bài sử dụng robot chung](08-su-dung-robot.md) để đi từ lắp ráp tới chạy thử.

## 1. ESP32 trong robot

ESP32 là họ vi điều khiển của Espressif. Vi điều khiển chạy mã, đọc cảm biến và gửi tín hiệu điều khiển. ESP32 classic có Wi-Fi và Bluetooth; khả năng kết nối của các họ ESP32 khác nhau, nên không suy ra tính năng chỉ từ tên ESP32.

Bo phát triển bổ sung nguồn, cổng USB, nút reset và hàng chân để bạn dễ đấu mạch. ESP32-WROOM-32 là tên module thường nằm dưới nắp kim loại trên bo; nó khác tên chip USB CH340.

## 2. Đường đi của chương trình

```mermaid
flowchart LR
    A[Arduino IDE trên máy tính] --> B[Cáp USB Type-C]
    B --> C[CH340: USB sang Serial]
    C --> D[ESP32: chạy chương trình]
    D --> E[Cảm biến / driver robot]
```

CH340 giúp máy tính giao tiếp với ESP32 qua cổng nối tiếp. Type-C mô tả đầu cắm; cáp vẫn phải có truyền dữ liệu mới dùng để nạp mã được. Arduino IDE có thể lập trình ESP32 sau khi cài đúng board package.

## 3. Khác Nano ở đâu?

| Nội dung | Nano classic ATmega328P | ESP32 classic WROOM-32 |
| --- | --- | --- |
| Mức logic | 5 V | 3,3 V |
| Gói hỗ trợ IDE | Arduino AVR Boards | esp32 by Espressif Systems |
| Tên chân trong mã | D2 thường viết `2` | IO23/GPIO23 viết `23` |
| Kết nối không dây tích hợp | Không | Wi-Fi và Bluetooth |
| Chọn Processor Old Bootloader | Có thể cần | Không dùng lựa chọn của Nano |

Không chuyển dây từ mạch Nano sang ESP32 mà giữ nguyên nguồn tín hiệu. USB có thể cấp 5 V vào mạch nguồn của bo, nhưng GPIO ESP32 hoạt động ở mức 3,3 V. Đối chiếu [hướng dẫn bo ESP32 của Espressif](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html) và pinout của đúng bo đang dùng.

## 4. Thực hành nhận diện và bài tập

1. Đọc chữ trên module và chip USB; tìm GND, 3V3 và nút reset.
2. Chỉ driver L298N, HC-SR04, line sensor và encoder trên robot.
3. Giải thích vì sao cổng Type-C không quyết định board trong IDE.
4. Giải thích vì sao USB cấp nguồn 5 V nhưng GPIO không được nhận tín hiệu 5 V trực tiếp.

**Điều kiện học tiếp:** nhận diện đúng board và các mức điện áp. Nếu thấy S3/C3, dùng pinout/board tương ứng; các ví dụ ở lộ trình này theo bo classic trong bộ bàn giao.

[Lộ trình](index.md) · [Bài tiếp: Hướng dẫn lập trình xe](bai-giang/02-lap-trinh.md)
