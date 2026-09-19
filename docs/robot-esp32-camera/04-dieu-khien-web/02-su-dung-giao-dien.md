# Sử dụng giao diện điều khiển

## Giao diện của chương trình dùng với Python YOLO

Mở `http://192.168.4.1:82` khi ESP32 đang phát Wi-Fi `ESP32-Car-01`.

Giao diện này có các chức năng:

- Xem camera.
- Điều khiển tiến, lùi, quay trái và quay phải.
- Nút dừng.
- Thanh chỉnh tốc độ tịnh tiến và tốc độ quay.

Các nút hướng hoạt động theo nguyên tắc **giữ để chạy, nhả để dừng**. Chương trình này không hiển thị HC-SR04, encoder hoặc cảm biến dò line.

## Giao diện của chương trình kiểm tra đầy đủ

Mở `http://192.168.4.1` khi ESP32 đang phát Wi-Fi `ESP32-Car`.

### Xem hình ảnh camera

Khung lớn phía trên hiển thị hình ảnh trực tiếp từ robot. Danh sách độ phân giải cho phép chọn chất lượng hình ảnh khác nhau.

Khuyến nghị bắt đầu với `QVGA 320x240`. Độ phân giải cao hơn cho hình ảnh lớn hơn nhưng có thể làm giảm tốc độ khung hình hoặc khiến luồng camera kém ổn định.

Sau khi chọn độ phân giải, nhấn **Đổi độ phân giải** và chờ hình ảnh tải lại.

### Điều khiển hướng di chuyển

| Nút | Chức năng |
| --- | --- |
| `↑` | Tiến |
| `↓` | Lùi |
| `←` | Quay trái tại chỗ |
| `→` | Quay phải tại chỗ |
| `↖` | Tiến chếch trái |
| `↗` | Tiến chếch phải |
| `↙` | Lùi chếch trái |
| `↘` | Lùi chếch phải |
| `■` | Dừng ngay |

Các nút hướng hoạt động theo nguyên tắc **giữ để chạy, nhả để dừng**. Không cần bấm nút Dừng sau mỗi lần di chuyển thông thường. Nếu robot không dừng đúng lúc, bấm nút `■` hoặc tắt nguồn.

### Điều chỉnh tốc độ

- `Lin +` và `Lin -`: tăng hoặc giảm tốc độ tiến, lùi và đi chéo.
- `Rot +` và `Rot -`: tăng hoặc giảm tốc độ quay trái, quay phải.

Mỗi lần bấm thay đổi 10 đơn vị PWM. Dải tốc độ trong firmware là từ 60 đến 255. Hãy bắt đầu ở tốc độ thấp, đặc biệt khi thử robot trên bàn hoặc trong khu vực hẹp.

### Đọc dữ liệu cảm biến

| Dữ liệu | Ý nghĩa |
| --- | --- |
| `HC-SR04` | Khoảng cách đo được theo centimet |
| `Echo time` | Thời gian xung phản hồi của HC-SR04 theo micro giây |
| `Encoder LEFT` | Tổng xung và số xung mới của bánh trái |
| `Encoder RIGHT` | Tổng xung và số xung mới của bánh phải |
| `Line RAW L2 L1 C R1 R2` | Trạng thái thô của năm mắt dò line từ trái sang phải |
| `Line detected active LOW` | Tên mắt đang phát hiện line; mức `0` là mức kích hoạt |

Nếu `HC-SR04` hiển thị `No echo`, cảm biến không nhận được xung phản hồi trong thời gian chờ. Kiểm tra hướng cảm biến, khoảng cách vật cản và dây kết nối.

Nếu bánh xe quay nhưng encoder không tăng, dừng robot và kiểm tra lại đĩa encoder, khe cảm biến và dây tín hiệu.
