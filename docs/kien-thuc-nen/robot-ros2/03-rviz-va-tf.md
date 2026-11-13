# Bài 11: RViz, URDF và kiểm tra dữ liệu

## 1. Mục tiêu

Trong bài này, bạn sẽ tạo mô hình robot nhỏ, phát quan hệ thân–LiDAR và xem trong RViz. Sau đó, chúng ta đối chiếu các bước tương tự khi xem dữ liệu của Robot ESP32 LiDAR thật.

Bạn cần package thực hành của bài 4–7 và kiến thức TF của bài 10. Các tệp mô hình bên dưới chỉ thuộc bài thử trên máy tính.

## 2. RViz và mô phỏng khác nhau thế nào?

RViz hiển thị dữ liệu do các nguồn ROS 2 cung cấp. Turtlesim và các trình mô phỏng thực hiện cập nhật một thế giới mô phỏng. Chỉ mở RViz chưa làm xuất hiện cảm biến, chuyển động hoặc bản đồ.

Trong RViz, mỗi **display** nhận và vẽ một loại dữ liệu. TF vẽ các frame, RobotModel vẽ hình dạng từ mô hình, LaserScan vẽ các mẫu quét, Map hiển thị lưới bản đồ.

## 3. URDF mô tả hình học và quan hệ khớp

URDF dùng các **link** cho bộ phận và **joint** cho quan hệ nối giữa chúng. Một joint cố định thể hiện hai link không thay đổi vị trí tương đối. Joint chuyển động có trạng thái cần cập nhật khi robot vận động.

Cài công cụ khi đang có Internet:

```bash
sudo apt install ros-humble-robot-state-publisher ros-humble-rviz2
```

Trong package `robovis_practice`, tạo thư mục `urdf`, rồi tệp `~/ros2_practice_ws/src/robovis_practice/urdf/robot_hoc.urdf`:

```xml
<?xml version="1.0"?>
<robot name="robot_hoc">
  <link name="base_link">
    <visual>
      <origin xyz="0 0 0.03"/>
      <geometry><box size="0.24 0.18 0.06"/></geometry>
      <material name="xanh"><color rgba="0.1 0.4 0.8 1"/></material>
    </visual>
  </link>
  <link name="base_scan">
    <visual>
      <geometry><cylinder radius="0.03" length="0.03"/></geometry>
      <material name="do"><color rgba="0.8 0.1 0.1 1"/></material>
    </visual>
  </link>
  <joint name="gan_lidar" type="fixed">
    <parent link="base_link"/>
    <child link="base_scan"/>
    <origin xyz="0.08 0 0.09" rpy="0 0 0"/>
  </joint>
</robot>
```

Kích thước dùng mét, góc `rpy` dùng radian. Joint đặt frame LiDAR trước thân 0,08 m và cao 0,09 m. `visual/origin` của thân dịch hình hộp lên trên gốc link; nó không tạo thêm frame con trong TF.

Mô hình này chỉ có hình hiển thị và một khớp cố định. Một mô hình dùng cho mô phỏng vật lý còn cần mô tả va chạm, quán tính và các thông số phù hợp.

## 4. Nạp mô hình bằng launch

Tạo tệp `~/ros2_practice_ws/src/robovis_practice/launch/mo_hinh.launch.py`:

```python
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    model = (
        Path(get_package_share_directory('robovis_practice'))
        / 'urdf' / 'robot_hoc.urdf')
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': model.read_text()}],
            output='screen'),
    ])
```

Trong `setup.py`, bổ sung phần tử cài mô hình vào `data_files`:

```text
('share/' + package_name + '/urdf', glob('urdf/*.urdf')),
```

Giữ phần cài launch/config ở bài 7. Thêm `<exec_depend>robot_state_publisher</exec_depend>` vào `package.xml`, build lại rồi mở Terminal mới:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_practice_ws/install/setup.bash
ros2 launch robovis_practice mo_hinh.launch.py
```

`robot_state_publisher` đọc mô hình và công bố quan hệ khớp. Với joint cố định, không cần tự phát vị trí khớp. Nếu mô hình có bánh quay, các joint động cần trạng thái từ nguồn phù hợp, thường qua `/joint_states`.

## 5. Hiển thị và kiểm tra

Mở Terminal khác, nạp ROS 2 rồi chạy `rviz2`. Trong cửa sổ:

1. Đặt **Global Options → Fixed Frame** thành `base_link`.
2. Chọn **Add → TF**.
3. Chọn **Add → RobotModel**. Nếu display yêu cầu, chọn nguồn mô tả dạng topic và topic `robot_description` thực tế.
4. Quan sát thân hình hộp và LiDAR hình trụ; đọc trạng thái display nếu chưa thấy.

Gốc `base_scan` cần lệch trước và cao đúng mô hình. Kiểm tra bằng Terminal đã nạp ROS 2:

```bash
ros2 run tf2_ros tf2_echo base_link base_scan
```

Kết quả tịnh tiến cần gần `(0.08, 0, 0.09)`, phép quay là không quay. `Ctrl+C` dừng công cụ.

Nếu một frame đã có quan hệ đúng nhưng hình vẽ lệch, kiểm tra `visual/origin`. Nếu cả frame lẫn hình đều sai, kiểm tra joint và nguồn mô hình được nạp.

## 6. Vì sao Fixed Frame ảnh hưởng kết quả?

Fixed Frame là frame tham chiếu chung mà RViz dùng để biểu diễn dữ liệu. Mô hình bài thử chỉ có cây từ `base_link` tới `base_scan`, nên chọn `base_link`. Mô hình chưa có `odom` hoặc `map`.

| Bối cảnh | Fixed Frame thường dùng |
| --- | --- |
| Bài mô hình cố định trên máy tính | `base_link` |
| Kiểm tra odometry robot | `odom` |
| Đã chạy SLAM hoặc định vị toàn cục | `map` |

RViz cần tra được chuỗi TF từ frame dữ liệu tới Fixed Frame tại thời điểm hợp lệ. Chọn một tên không tồn tại không tạo thêm quan hệ còn thiếu.

## 7. Chuyển sang dữ liệu LiDAR thật

Dừng launch mô hình thử trước khi [khởi động robot thật](../../robot-esp32-lidar/03-van-hanh/02-khoi-dong-va-kiem-tra.md), vì mô hình thử dùng các tên frame có thể trùng sản phẩm.

Mở cấu hình RViz được bàn giao nếu có. Thêm display LaserScan, chọn topic quét thật, rồi kiểm tra:

- Có mẫu quét mới trên topic không?
- `header.frame_id` có frame tương ứng không?
- Chuỗi TF có nối tới Fixed Frame không?
- Timestamp và nguồn thời gian có thống nhất không?
- QoS của display có tương thích publisher không?

Với cảm biến phát best effort, chọn độ tin cậy phù hợp trong thuộc tính display. Thay màu hoặc cỡ điểm không sửa được lỗi nguồn dữ liệu hay TF.

## 8. Bài tập

1. Đổi joint LiDAR thành x = 0,10 m, build và khởi động lại. Kiểm tra bằng `tf2_echo`.
2. Đổi riêng `visual/origin` của thân. Giải thích vì sao quan hệ `base_link → base_scan` không đổi.
3. Chọn nhầm Fixed Frame thành `map` trong bài mô hình; đọc thông báo rồi đưa về đúng frame.
4. Trên robot thật, dùng `Status` của display để mô tả lỗi trước khi sửa cấu hình.

Đọc thêm: [ROS 2 — URDF với robot_state_publisher](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher.html), [RViz User Guide](https://docs.ros.org/en/humble/Tutorials/Intermediate/RViz/RViz-User-Guide/RViz-User-Guide.html).

[← Bài 10](he-toa-do-va-tf.md) · [Bài 12: Rosbag và thực hành tổng hợp →](07-rosbag-va-xu-ly-loi.md)
