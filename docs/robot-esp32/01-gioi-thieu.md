# ESP32, CH340 và cổng Type-C là gì?

**Mục tiêu:** hiểu cấu tạo bo và chọn đúng hướng học.

Robot trong [bộ tài liệu ESP32 Robovis](https://drive.google.com/drive/folders/12f-LH2PU0DGoAqXQk_d91QdnKpCADnDt) dùng bo CH340 Type-C, board mở rộng, L298N, dò line 5 kênh, encoder và HC-SR04. Bộ mã tạo Wi-Fi **ESP32-Car** và giao diện web với **Manual / Line follow**. Hướng dẫn bàn giao chọn **ESP32 Dev Module**. Xem [bài sử dụng robot chung](08-su-dung-robot.md) để đi từ lắp ráp tới chạy thử.

## ESP32 trong robot

ESP32 là họ vi điều khiển của Espressif. Vi điều khiển chạy mã, đọc cảm biến và gửi tín hiệu điều khiển. ESP32 classic có Wi-Fi và Bluetooth; khả năng kết nối của các họ ESP32 khác nhau, nên không suy ra tính năng chỉ từ tên ESP32.

Bo phát triển bổ sung nguồn, cổng USB, nút reset và hàng chân để bạn dễ đấu mạch. ESP32-WROOM-32 là tên module thường nằm dưới nắp kim loại trên bo; nó khác tên chip USB CH340.

## Đường đi của chương trình

```mermaid
flowchart LR
    A[Arduino IDE trên máy tính] --> B[Cáp USB Type-C]
    B --> C[CH340: USB sang Serial]
    C --> D[ESP32: chạy chương trình]
    D --> E[Cảm biến / driver robot]
```

CH340 giúp máy tính giao tiếp với ESP32 qua cổng nối tiếp. Type-C mô tả đầu cắm; cáp vẫn phải có truyền dữ liệu mới dùng để nạp mã được. Arduino IDE có thể lập trình ESP32 sau khi cài đúng board package.

## Khác Nano ở đâu?

| Nội dung | Nano classic ATmega328P | ESP32 classic WROOM-32 |
| --- | --- | --- |
| Mức logic | 5 V | 3,3 V |
| Gói hỗ trợ IDE | Arduino AVR Boards | esp32 by Espressif Systems |
| Tên chân trong mã | D2 thường viết `2` | IO23/GPIO23 viết `23` |
| Kết nối không dây tích hợp | Không | Wi-Fi và Bluetooth |
| Chọn Processor Old Bootloader | Có thể cần | Không dùng lựa chọn của Nano |

Không chuyển dây từ mạch Nano sang ESP32 mà giữ nguyên nguồn tín hiệu. USB có thể cấp 5 V vào mạch nguồn của bo, nhưng GPIO ESP32 hoạt động ở mức 3,3 V. Đối chiếu [hướng dẫn bo ESP32 của Espressif](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html) và pinout của đúng bo đang dùng.

**Tự kiểm tra:** đọc chữ trên module và chip USB. Nếu thấy ESP32-S3 hoặc ESP32-C3, ghi lại để chọn board tương ứng; các ví dụ GPIO23/GPIO18 phía sau cần điều chỉnh theo pinout.

[Lộ trình](index.md) · [Bài tiếp: Chuẩn bị](02-chuan-bi.md)
