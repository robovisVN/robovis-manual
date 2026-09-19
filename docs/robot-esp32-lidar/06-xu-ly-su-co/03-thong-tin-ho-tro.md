# Thông tin cần gửi khi yêu cầu hỗ trợ

Thông tin đầy đủ giúp xác định lỗi nhanh hơn và tránh phải hỏi lại nhiều lần.

## 1. Mô tả hiện tượng

Nêu rõ:

- Bạn đang thực hiện bước nào.
- Robot đã hoạt động đúng tới bước nào.
- Lỗi xuất hiện ngay hay sau một thời gian.
- Robot đứng yên, mất kết nối hay di chuyển sai.
- Bạn đã thay đổi cấu hình nào trước khi lỗi xuất hiện.

## 2. Ảnh và video

Gửi:

- Video thấy đồng thời robot thật và màn hình nếu lỗi liên quan chuyển động.
- Ảnh toàn bộ RViz nếu lỗi bản đồ hoặc định vị.
- Ảnh Terminal từ dòng lỗi đầu tiên.
- Ảnh kết nối Wi-Fi/IP nếu lỗi mạng.

Không chỉ chụp dòng `Failed` cuối cùng của quá trình build; nguyên nhân thường nằm ở các dòng phía trên.

## 3. Kết quả lệnh kiểm tra

Chạy và gửi nguyên kết quả:

```bash
lsb_release -a
printenv ROS_DISTRO
printenv ROS_DOMAIN_ID
ip -4 addr
ping -c 4 192.168.4.1
ros2 node list
ros2 topic list -t
```

Nếu lỗi LiDAR hoặc odometry, gửi thêm:

```bash
ros2 topic hz /scan
ros2 topic hz /odom
```

Mỗi lệnh `hz` cần chạy trong khoảng 10–20 giây rồi nhấn `Ctrl+C`.

## 4. Thông tin sản phẩm

- Tên hoặc mã phiên bản robot.
- Tên Wi-Fi robot đang sử dụng.
- Phiên bản workspace hoặc ngày nhận bộ source.
- Có nạp firmware khác lên ESP32 hay không.
- Có sửa launch file, YAML hoặc topic remap hay không.

## Mẫu mô tả

```text
Hiện tượng:
Bước đang thực hiện:
Thời điểm bắt đầu lỗi:
Robot có ping được không:
/scan có dữ liệu không:
/odom có dữ liệu không:
Thay đổi gần nhất:
Ảnh/video/log đính kèm:
```
