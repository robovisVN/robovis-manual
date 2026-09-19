# Các topic của robot

## `/cmd_vel` – lệnh vận tốc

`/cmd_vel` thường dùng kiểu message `geometry_msgs/msg/Twist`.

Hai trường quan trọng với robot hai bánh:

- `linear.x`: vận tốc tiến/lùi, đơn vị m/s.
- `angular.z`: vận tốc quay, đơn vị rad/s.

Giá trị dương và âm biểu diễn hai hướng ngược nhau. Các trường còn lại thường bằng `0` với robot chạy trên mặt phẳng.

Kiểm tra ai đang gửi lệnh:

```bash
ros2 topic info /cmd_vel --verbose
```

Nếu có nhiều publisher cùng lúc, robot có thể nhận lệnh không như mong muốn.

## `/scan` – dữ liệu LiDAR

`/scan` thường dùng `sensor_msgs/msg/LaserScan`.

Các trường quan trọng:

| Trường | Ý nghĩa |
| --- | --- |
| `angle_min`, `angle_max` | Giới hạn góc quét |
| `angle_increment` | Khoảng góc giữa hai mẫu |
| `range_min`, `range_max` | Khoảng đo hợp lệ của cấu hình |
| `ranges` | Danh sách khoảng cách theo từng góc |
| `header.frame_id` | Hệ tọa độ gắn với LiDAR |

Xem một message:

```bash
ros2 topic echo /scan --once
```

## `/odom` – odometry

`/odom` thường dùng `nav_msgs/msg/Odometry` và chứa:

- Vị trí ước lượng `pose`.
- Vận tốc ước lượng `twist`.
- Tên frame cha và frame con.

Xem dữ liệu:

```bash
ros2 topic echo /odom
```

Khi robot tiến, vị trí phải thay đổi. Khi robot quay, hướng phải thay đổi. Odometry có thể trôi dần và không thay thế định vị bằng bản đồ.

## Topic có namespace

Nếu `ros2 topic list` hiển thị:

```text
/robot_1/scan
/robot_1/odom
/robot_1/cmd_vel
```

thì mọi lệnh phải sử dụng đúng tên đầy đủ, ví dụ:

```bash
ros2 topic hz /robot_1/scan
```

Không tự đổi tên topic trong launch file chỉ để khớp tài liệu; hãy xác nhận phiên bản workspace trước.
