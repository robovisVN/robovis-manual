# Node, topic và lệnh thường dùng

## Node là gì?

Node là một chương trình đang chạy trong hệ thống ROS 2. Mỗi node thường đảm nhiệm một nhiệm vụ, ví dụ nhận dữ liệu robot, xuất odometry, chạy SLAM hoặc điều hướng.

Liệt kê node:

```bash
ros2 node list
```

Xem thông tin một node:

```bash
ros2 node info /ten_node
```

Hãy thay `/ten_node` bằng tên lấy từ `ros2 node list`.

## Topic là gì?

Topic là kênh dữ liệu cho phép các node gửi và nhận message. Ví dụ:

- Node LiDAR gửi dữ liệu lên `/scan`.
- Node odometry gửi dữ liệu lên `/odom`.
- Công cụ điều khiển gửi lệnh lên `/cmd_vel`.

Liệt kê topic:

```bash
ros2 topic list
```

Liệt kê topic kèm kiểu message:

```bash
ros2 topic list -t
```

## Xem thông tin topic

```bash
ros2 topic info /scan
```

Lệnh cho biết kiểu message, số publisher và số subscriber.

## Xem dữ liệu

```bash
ros2 topic echo /scan --once
```

Với dữ liệu lớn như LiDAR, nên dùng `--once` để chỉ in một message. Để xem odometry liên tục:

```bash
ros2 topic echo /odom
```

Nhấn `Ctrl+C` để dừng.

## Đo tần số

```bash
ros2 topic hz /scan
ros2 topic hz /odom
```

Mỗi lần chỉ chạy một lệnh và nhấn `Ctrl+C` trước khi chuyển sang lệnh tiếp theo.

## Khi lệnh không tìm thấy dữ liệu

Kiểm tra theo thứ tự:

1. Bringup còn chạy không.
2. Máy tính còn kết nối Wi-Fi robot không.
3. `ping -c 4 192.168.4.1` có thành công không.
4. Topic có namespace hoặc tên khác không.
5. Nếu có dùng `ROS_DOMAIN_ID`, giá trị giữa các Terminal chạy ROS 2 có giống nhau không? Xem bằng `printenv ROS_DOMAIN_ID`. Bộ tài liệu bàn giao không quy định phải đặt bằng `10`.
