# Chạy thử lần đầu

**Mục tiêu:** cho robot tiến, lùi, quay và dừng đúng lệnh.

Trước khi làm, hoàn thành bài [Khởi động và kiểm tra dữ liệu](02-khoi-dong-va-kiem-tra.md). Giữ Terminal chạy bringup mở trong suốt lượt thử.

Đặt robot trên sàn phẳng, có khoảng trống. Lượt thử này dùng điều khiển tay; hãy dừng Nav2 nếu đang chạy.

## Bước 1. Mở cửa sổ điều khiển

Mở thêm một Terminal Ubuntu và chạy:

```bash
ros2 run rqt_robot_steering rqt_robot_steering
```

**Kết quả cần thấy:** cửa sổ điều khiển có hai giá trị:

| Giá trị | Dùng để làm gì? |
| --- | --- |
| **Linear velocity** | Điều chỉnh tốc độ tiến hoặc lùi |
| **Angular velocity** | Điều chỉnh tốc độ quay |

Trước khi thử, đặt **cả hai về 0**. Công cụ cần gửi lệnh tới `/cmd_vel`; nếu robot dùng tên khác như `/robot_1/cmd_vel`, chọn đúng tên đã thấy ở bài kiểm tra dữ liệu.

## Bước 2. Thử từng chuyển động

Thực hiện theo bảng. Sau **mỗi lần thử**, đưa cả hai vận tốc về **0** và chờ robot dừng.

| Lần thử | Thao tác | Kết quả cần thấy |
| --- | --- | --- |
| Tiến | Giữ Angular bằng 0; tăng Linear lên một giá trị dương nhỏ | Robot đi về phía trước |
| Lùi | Giữ Angular bằng 0; đặt Linear âm với độ lớn nhỏ | Robot đi lùi |
| Quay một chiều | Giữ Linear bằng 0; tăng Angular lên một giá trị dương nhỏ | Robot quay tại chỗ |
| Quay chiều ngược lại | Giữ Linear bằng 0; đặt Angular âm với độ lớn nhỏ | Robot quay ngược chiều vừa thử |

Với chuyển động tiến/lùi, có thể bắt đầu trong khoảng **0.02–0.06 m/s** theo [hướng dẫn điều khiển tay](03-dieu-khien-bang-tay.md). Tăng từ mức thấp và quan sát robot thật.

Nếu robot đi sai hướng hoặc chuyển động bất thường, đưa hai giá trị về **0** và dừng lượt thử.

## Bước 3. Xem dữ liệu chuyển động

Sau khi robot dừng, mở Terminal khác và chạy:

```bash
ros2 topic echo /odom --once
```

Lệnh in một bản dữ liệu rồi kết thúc. Nếu tên topic có thêm phần đầu, dùng tên đầy đủ như `/robot_1/odom`.

Tìm hai giá trị **x** và **y** trong phần `pose.pose.position`. Đây là vị trí ước lượng của robot.

1. Chạy lệnh và ghi lại x, y.
2. Cho robot tiến một đoạn ngắn, rồi dừng.
3. Chạy lại lệnh và so sánh x, y với lần trước.

**Kết quả cần thấy:** ít nhất một trong hai giá trị thay đổi. Bước này chỉ kiểm tra phần mềm có nhận ra robot đã di chuyển hay không.

Nếu robot di chuyển mà dữ liệu không thay đổi, xem [Lỗi kết nối và ROS 2](../06-xu-ly-su-co/01-loi-ket-noi-va-ros2.md).

## Khi nào hoàn thành?

- Robot tiến, lùi và quay đúng lệnh.
- Đưa hai vận tốc về 0 thì robot dừng.
- Odometry thay đổi khi robot di chuyển.
- Dữ liệu LiDAR và odometry vẫn cập nhật như ở bài trước.

Đạt các điều kiện trên thì có thể chuyển sang [Kiểm tra LiDAR](../05-lidar-slam-navigation/01-kiem-tra-lidar.md), rồi [Tạo bản đồ SLAM](../05-lidar-slam-navigation/02-tao-ban-do-slam.md).
