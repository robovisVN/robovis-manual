# Sử dụng phần mềm YOLO

## Các thông số nhận diện

### Model

- `yolov8n.pt`: nhẹ nhất, tốc độ nhanh, nên dùng để bắt đầu.
- `yolov8s.pt`, `yolov8m.pt`, `yolov8l.pt`, `yolov8x.pt`: model lớn dần, có thể chính xác hơn nhưng yêu cầu máy tính mạnh hơn.

Sau khi đổi model, nhấn **Reload model**.

### Conf

`Conf` là ngưỡng tin cậy của kết quả nhận diện, có giá trị từ 0 đến 1.

- Giá trị thấp: nhận được nhiều đối tượng hơn nhưng dễ có nhận diện nhầm.
- Giá trị cao: ít nhận diện nhầm hơn nhưng có thể bỏ sót đối tượng.
- Giá trị nên dùng ban đầu: `0.5`.

### Input size

Đây là kích thước ảnh đưa vào YOLO.

- `320`: chạy nhanh, phù hợp cho thử nghiệm ban đầu.
- Giá trị lớn hơn: có thể tăng khả năng nhận diện vật nhỏ nhưng xử lý chậm hơn.

### Detect person only

- Không đánh dấu: hiển thị các loại vật thể mà model nhận diện được.
- Đánh dấu: chỉ giữ lại đối tượng có nhãn `person`.

## Điều khiển robot

1. Nhấn **Connect WS**.
2. Điều chỉnh `PWM tịnh tiến` và `PWM quay`.
3. Nhấn **Gửi tốc độ**.
4. Giữ nút **Tiến**, **Lùi**, **Trái** hoặc **Phải** để robot chạy.
5. Nhả chuột để dừng.

Có thể dùng các phím:

| Phím | Chức năng |
| --- | --- |
| `↑` | Tiến |
| `↓` | Lùi |
| `←` | Quay trái |
| `→` | Quay phải |
| `Space` | Dừng |

Khi điều khiển bằng bàn phím, hãy nhấp chuột vào cửa sổ phần mềm trước để cửa sổ nhận phím.

## Start Stop và WebSocket

- **Start**: bắt đầu đọc luồng camera và chạy YOLO.
- **Stop**: dừng đọc hình ảnh và dừng nhận diện.
- **Connect WS**: kết nối kênh điều khiển chuyển động.
- **Disconnect WS**: ngắt kênh điều khiển.

Việc nhấn **Stop** không thay thế nút dừng chuyển động. Trước khi dừng phần mềm hoặc đóng cửa sổ, hãy nhấn **Dừng** hoặc phím `Space` để chắc chắn robot đã đứng yên.

## Cách tăng độ ổn định

- Dùng `yolov8n.pt` và `Input size = 320`.
- Giữ camera ở độ phân giải QVGA khi máy tính yếu hoặc Wi-Fi không ổn định.
- Không mở đồng thời quá nhiều cửa sổ xem luồng camera.
- Đóng các phần mềm nặng đang chạy trên máy tính.
- Đặt robot gần máy tính và tránh khu vực có quá nhiều mạng Wi-Fi 2,4 GHz.

