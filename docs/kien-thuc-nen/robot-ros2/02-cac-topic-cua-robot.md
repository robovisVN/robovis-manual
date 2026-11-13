# Bài 5: Đọc dữ liệu vận tốc, LiDAR và odometry

## 1. Mục tiêu

Ở bài 4, `Float64` chỉ mang một số thực; cách hiểu số đó do chúng ta quy định. Với robot, cần biết thêm đơn vị, thời điểm đo, hệ tọa độ và ý nghĩa từng trường. Bài này giúp bạn đọc các message thường gặp mà không suy đoán từ tên topic.

Bạn có thể xem định nghĩa ngay trên máy đã cài ROS 2. Để đọc message thật trên `/scan` hoặc `/odom`, cần [khởi động robot](../../robot-esp32-lidar/03-van-hanh/02-khoi-dong-va-kiem-tra.md) hoặc có dữ liệu phát lại.

## 2. Tìm kiểu trước, đọc trường sau

```bash
source /opt/ros/humble/setup.bash
ros2 topic list -t
ros2 interface show geometry_msgs/msg/Twist
ros2 interface show sensor_msgs/msg/LaserScan
ros2 interface show nav_msgs/msg/Odometry
```

`interface show` đọc định nghĩa đã cài, không cần publisher đang hoạt động. `topic echo` thì phải chờ dữ liệu trên topic.

Tên `/cmd_vel` chỉ là tên kênh. Hãy kiểm tra kiểu thực tế: một ứng dụng có thể dùng `Twist`, ứng dụng khác dùng kiểu có timestamp hoặc quy ước khác.

## 3. `Twist`: lệnh vận tốc của thân

`Twist` có hai vector:

| Nhóm | Thành phần | Ý nghĩa |
| --- | --- | --- |
| `linear` | x, y, z | Vận tốc tịnh tiến theo các trục |
| `angular` | x, y, z | Vận tốc quay quanh các trục |

Với robot dẫn động vi sai trên mặt phẳng, thường dùng `linear.x` theo m/s và `angular.z` theo rad/s. `linear.y` thường không dùng vì robot không chủ động trượt ngang.

Ví dụ `linear.x = 0,20`, `angular.z = 0,50` yêu cầu robot vừa tiến vừa quay trái theo quy ước trục thân. Bài 8 sẽ tính vận tốc hai bánh tương ứng.

`Twist` tự nó không có `header`. Frame và thời gian áp dụng phải được giao diện hệ thống quy định. Vì thế không nên lấy một message giống cấu trúc từ nguồn bất kỳ rồi mặc định nó phù hợp điều khiển robot.

Lệnh là giá trị mong muốn. Nếu bánh kẹt hoặc nguồn yếu, vận tốc thực có thể khác; cần đọc phản hồi thay vì dùng lệnh làm kết quả đo.

## 4. `LaserScan`: một vòng quét có cấu trúc

| Trường | Ý nghĩa thực hành |
| --- | --- |
| `header.stamp` | Thời điểm đo tia đầu tiên của lần quét |
| `header.frame_id` | Frame chứa phép đo |
| `angle_min` | Góc của mẫu đầu |
| `angle_increment` | Bước góc giữa hai mẫu |
| `range_min`, `range_max` | Miền khoảng cách hợp lệ |
| `ranges` | Mảng khoảng cách theo mét |

Với chỉ số bắt đầu từ 0:

```text
goc_i = angle_min + i × angle_increment
x_i = ranges[i] × cos(goc_i)
y_i = ranges[i] × sin(goc_i)
```

Các tọa độ này nằm trong frame của LiDAR. Muốn đặt điểm vào frame thân hoặc bản đồ, cần phép biến đổi ở bài TF.

### Ví dụ đọc mẫu

Nếu `angle_min = -1,0 rad`, `angle_increment = 0,01 rad`, mẫu chỉ số 100 có góc `0 rad`. Nếu khoảng cách mẫu đó là `1,5 m`, điểm nằm trên trục x dương của frame quét, ở tọa độ `(1,5; 0)` m.

Một giá trị vô hạn có thể xuất hiện khi không có phản xạ hợp lệ, tùy driver. Khi xử lý cần kiểm tra tính hữu hạn và giới hạn đo, không biến mọi giá trị không hợp lệ thành khoảng cách 0.

Ví dụ hàm tự viết để kiểm tra một mẫu, với góc và khoảng cách theo quy ước của `LaserScan`:

```python
from math import cos, isfinite, sin


def diem_quet(khoang_cach, goc, gioi_han_duoi, gioi_han_tren):
    if not isfinite(khoang_cach):
        return None
    if not gioi_han_duoi <= khoang_cach <= gioi_han_tren:
        return None
    return khoang_cach * cos(goc), khoang_cach * sin(goc)
```

## 5. `Odometry`: pose và twist trong những frame nào?

`Odometry` mô tả ước lượng vị trí và vận tốc. Hai tên frame có vai trò khác nhau:

- Pose được biểu diễn trong frame của `header.frame_id`.
- Twist được biểu diễn theo frame của `child_frame_id`.

Ví dụ phổ biến là `header.frame_id: odom`, `child_frame_id: base_link`. Khi robot quay, thành phần vận tốc trong thân không nhất thiết giống thành phần vận tốc theo trục odom.

Pose gồm vị trí và hướng quaternion. Quaternion có bốn thành phần `x, y, z, w`; không lấy trực tiếp `orientation.z` làm góc quay. Với robot phẳng, nếu quaternion chỉ có quay quanh z và đã chuẩn hóa, hướng yaw có thể tính từ `2 × atan2(z, w)` rồi xử lý miền góc phù hợp.

Hai khối pose và twist còn có covariance để biểu diễn độ không chắc chắn. Mảng covariance 6×6 được xếp phẳng thành 36 số. Các phần tử chéo ứng với độ biến thiên của từng đại lượng; không tự đặt tất cả bằng 0 chỉ để message trông gọn hơn.

## 6. Đọc dữ liệu trên Robot ESP32 LiDAR

Sau bringup, lấy đúng tên thực tế từ danh sách rồi dùng:

```bash
ros2 topic info /scan --verbose
ros2 topic echo /scan --once
ros2 topic echo /odom --once
ros2 topic info /cmd_vel --verbose
```

Nếu topic có namespace, dùng tên đầy đủ. Không cần phát thêm lệnh để chỉ kiểm tra cấu trúc message. Thử chuyển động theo [hướng dẫn điều khiển sản phẩm](../../robot-esp32-lidar/03-van-hanh/03-dieu-khien-bang-tay.md).

Khi kiểm tra một mẫu, ghi lại thời điểm, frame và giá trị chính. Một phép đo nhìn hợp lý nhưng timestamp quá cũ vẫn có thể không dùng được cho xử lý hiện tại.

## 7. Bài tập

1. Dùng hàm `diem_quet` với khoảng cách 2 m và góc pi/2. Kết quả gần `(0; 2)` m.
2. Thử giá trị vô hạn và giá trị lớn hơn `range_max`; hàm cần trả `None`.
3. Giải thích vì sao nhận được `/odom` không bảo đảm đã có TF `odom → base_link`.
4. Tìm trong dữ liệu thật tên frame LiDAR và ghi lại để dùng ở bài 10–11.

Định nghĩa để đối chiếu: [Twist](https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Twist.msg), [LaserScan](https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/LaserScan.msg), [Odometry](https://github.com/ros2/common_interfaces/blob/humble/nav_msgs/msg/Odometry.msg).

[← Bài 4](06-workspace-va-node-python.md) · [Bài 6: Service và action →](04-service-va-action.md)
