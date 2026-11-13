# Bài 7: Parameter, launch và namespace

## 1. Mục tiêu

Bạn đã có các node trong package `robovis_practice`. Bài này sẽ đưa cấu hình ra khỏi mã, đặt các node vào một namespace và khởi động bộ phát, bộ nhận cùng cổng dữ liệu bằng một launch file.

## 2. Parameter thuộc về node

Parameter là một giá trị cấu hình có tên và kiểu, chẳng hạn `toc_do_co_so` kiểu số thực. Trong bài 4, node `nguon_toc_do` khai báo giá trị mặc định là 0,2 m/s.

Chạy `bo_phat` như bài 4. Trong Terminal đã nạp môi trường:

```bash
ros2 param list /nguon_toc_do
ros2 param describe /nguon_toc_do toc_do_co_so
ros2 param get /nguon_toc_do toc_do_co_so
ros2 param set /nguon_toc_do toc_do_co_so 0.35
```

Quan sát mẫu mới chuyển sang quanh 0,35 m/s. Mã `gui_mau()` đọc lại parameter trong mỗi callback, vì vậy thay đổi được dùng ở lần phát tiếp theo.

Nếu đặt `0` thay vì `0.0`, bạn đang truyền số nguyên thay vì số thực. Hãy xem kiểu và thông báo phản hồi; cùng một cách viết gần giống nhau không có nghĩa cùng kiểu parameter.

## 3. Giá trị đã đổi nhưng hành vi có đổi không?

Trong `BoPhat`, `chu_ky` được đọc một lần để tạo timer. Thay parameter này bằng CLI không tự tạo lại timer. Lệnh có thể cập nhật giá trị được lưu, trong khi lịch gọi callback vẫn giữ như trước.

Muốn áp dụng `chu_ky` ở phiên bản ví dụ này, dừng node và chạy lại với giá trị mới:

```bash
ros2 run robovis_practice bo_phat --ros-args -p chu_ky:=0.5 -p toc_do_co_so:=0.35
```

Đo `/toc_do_do`: tần số cần gần 2 Hz. Để hỗ trợ đổi timer ngay khi đang chạy, chương trình phải có thêm logic kiểm tra và cập nhật timer. Đây là hành vi do mã của node quyết định.

## 4. Lưu cấu hình bằng YAML

Trong package, tạo thư mục `config` và tệp `~/ros2_practice_ws/src/robovis_practice/config/thuc_hanh.yaml`:

```yaml
/thuc_hanh/nguon_toc_do:
  ros__parameters:
    toc_do_co_so: 0.25
    chu_ky: 0.2
```

Đường dẫn đầu là tên đầy đủ của node sau khi đặt namespace. `ros__parameters` là khóa cấu hình, còn các trường bên trong là parameter của node. Dùng dấu cách để thụt lề.

Tệp này giúp chạy lại cùng một cấu hình. Thay giá trị bằng CLI trong một phiên không tự ghi ngược vào YAML. Có thể dùng `ros2 param dump NODE` để xem cấu hình đang có; khi dùng lại cần kiểm tra các giá trị chỉ đọc và tên node.

## 5. Viết launch file

Tạo thư mục `launch`, rồi tệp `~/ros2_practice_ws/src/robovis_practice/launch/thuc_hanh.launch.py`:

```python
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config = str(
        Path(get_package_share_directory('robovis_practice'))
        / 'config' / 'thuc_hanh.yaml')
    return LaunchDescription([
        Node(
            package='robovis_practice', executable='bo_phat',
            name='nguon_toc_do', namespace='thuc_hanh',
            parameters=[config], output='screen'),
        Node(
            package='robovis_practice', executable='bo_nhan',
            name='theo_doi_toc_do', namespace='thuc_hanh',
            output='screen'),
        Node(
            package='robovis_practice', executable='cong_du_lieu',
            name='cong_du_lieu', namespace='thuc_hanh',
            output='screen'),
    ])
```

`generate_launch_description` tạo mô tả những thành phần cần chạy. `package` và `executable` xác định chương trình; `name` và `namespace` xác định tên node khi chạy. `parameters` đưa tệp YAML vào bên phát.

Đường dẫn cấu hình được tìm qua thư mục share của package đã cài, nên lệnh launch không phụ thuộc bạn đang đứng ở thư mục nào.

## 6. Cài launch và cấu hình cùng package

Ở đầu `setup.py`, bổ sung:

```python
from glob import glob
```

Trong danh sách `data_files` đang có, thêm hai phần tử sau, giữ các phần tử cài `resource` và `package.xml`:

```text
('share/' + package_name + '/launch', glob('launch/*.launch.py')),
('share/' + package_name + '/config', glob('config/*.yaml')),
```

Trong `package.xml`, thêm các phụ thuộc chạy nếu chưa có:

```xml
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
<exec_depend>ament_index_python</exec_depend>
```

Build lại `robovis_practice` như bài 4. Nếu quên cài tệp, `ros2 run` có thể vẫn hoạt động nhưng `ros2 launch` báo không tìm thấy launch hoặc YAML.

## 7. Chạy và kiểm tra tên đầy đủ

Dừng các node thực hành chạy riêng trước đó. Trong Terminal mới:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_practice_ws/install/setup.bash
ros2 launch robovis_practice thuc_hanh.launch.py
```

Trong Terminal kiểm tra, cũng nạp hai môi trường rồi chạy:

```bash
ros2 node list
ros2 topic list -t
ros2 param get /thuc_hanh/nguon_toc_do toc_do_co_so
ros2 service call /thuc_hanh/cho_phep_du_lieu std_srvs/srv/SetBool '{data: true}'
ros2 topic echo /thuc_hanh/toc_do_cho_phep --once
```

Kết quả cần có namespace `/thuc_hanh`, tốc độ cơ sở `0.25` và mẫu được chuyển tiếp sau khi bật cổng. Cổng bắt đầu ở trạng thái tắt theo mã bài 6.

## 8. Namespace khác remapping thế nào?

Namespace thêm phần đầu cho các tên tương đối. Các node đều dùng `toc_do_do` không có `/` đầu nên khi ở namespace `thuc_hanh`, chúng kết nối qua `/thuc_hanh/toc_do_do`.

Remapping thay một tên cụ thể. Ví dụ chạy bên nhận ở ngoài namespace nhưng yêu cầu nó đọc kênh trong namespace:

```bash
ros2 run robovis_practice bo_nhan --ros-args -r __node:=bo_nhan_ngoai -r toc_do_do:=/thuc_hanh/toc_do_do
```

Node mới đọc cùng dữ liệu với bộ nhận trong launch. Đổi tên node bằng `__node` không tự đổi mọi tên topic. Khi thiết kế nhiều robot, cần lên kế hoạch tên topic và frame; namespace topic không tự làm mọi tên frame TF thành duy nhất.

## 9. Bài tập và xử lý lỗi

1. Đổi YAML thành chu kỳ 0,4 giây. Build, khởi động lại launch và kiểm tra gần 2,5 Hz.
2. Đổi tốc độ cơ sở bằng CLI, rồi khởi động lại launch. Giải thích vì sao giá trị quay về YAML.
3. Cố ý viết sai tên node trong YAML. Dùng `param get` để phát hiện cấu hình chưa được áp dụng.
4. Nếu có hai node cùng tên, kiểm tra các Terminal cũ và dừng đúng process trước khi chạy lại.

Đọc thêm: [ROS 2 — Parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html), [Launch integration](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Launch-system.html).

[← Bài 6](04-service-va-action.md) · [Bài 8: Động học và odometry →](08-dong-hoc-va-odometry.md)
