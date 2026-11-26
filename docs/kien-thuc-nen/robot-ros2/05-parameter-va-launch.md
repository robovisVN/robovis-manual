# Bài 7: Parameter, launch và namespace

Khi ví dụ có nhiều node, chúng ta phải mở nhiều Terminal và nhớ các giá trị cần dùng cho từng lần chạy. Nếu muốn đổi tốc độ cơ sở hoặc chạy lại cùng một cấu hình, sửa trực tiếp mã nguồn sẽ khiến việc đối chiếu khó hơn.

Trong bài này, chúng ta sẽ dùng parameter để cấu hình node, YAML để lưu giá trị và launch file để khởi động các thành phần cùng nhau. Namespace giúp nhóm những tên liên quan trong ví dụ.

## 1. Mục tiêu

Bạn đã có các node trong package `robovis_practice`. Bài này sẽ đưa cấu hình ra khỏi mã, đặt các node vào một namespace và khởi động bộ phát, bộ nhận cùng cổng dữ liệu bằng một launch file.

## 2. Parameter thuộc về node

**Parameter** là một giá trị cấu hình thuộc về node, có tên và kiểu dữ liệu xác định. Chẳng hạn, node `nguon_toc_do` ở bài 4 khai báo `toc_do_co_so` kiểu số thực với giá trị mặc định 0,2 m/s. Chúng ta có thể xem và thay đổi giá trị này qua công cụ ROS 2 nếu node hỗ trợ.

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

Việc thay đổi một parameter có tác dụng khi chương trình sử dụng giá trị mới. Trong `BoPhat`, tốc độ cơ sở được đọc ở mỗi lần phát, còn `chu_ky` chỉ được đọc một lần lúc tạo timer. Vì vậy, thay `chu_ky` bằng CLI có thể cập nhật giá trị lưu trong node nhưng chưa thay lịch gọi callback của timer đã tạo.

Muốn áp dụng `chu_ky` ở phiên bản ví dụ này, dừng node và chạy lại với giá trị mới:

```bash
ros2 run robovis_practice bo_phat --ros-args -p chu_ky:=0.5 -p toc_do_co_so:=0.35
```

Đo `/toc_do_do`: tần số cần gần 2 Hz. Để hỗ trợ đổi timer ngay khi đang chạy, chương trình phải có thêm logic kiểm tra và cập nhật timer. Đây là hành vi do mã của node quyết định.

## 4. Lưu cấu hình bằng YAML

Sau khi tìm được bộ giá trị phù hợp, chúng ta cần lưu lại để các lần chạy dùng cùng thiết lập. Tệp YAML giúp đặt những giá trị này bên ngoài mã nguồn và nạp chúng khi khởi động node.

Trong package, tạo thư mục `config` và tệp `~/ros2_practice_ws/src/robovis_practice/config/thuc_hanh.yaml`:

```yaml
/thuc_hanh/nguon_toc_do:
  ros__parameters:
    toc_do_co_so: 0.25
    chu_ky: 0.2
```

Dòng đầu của tệp chỉ ra tên đầy đủ của node sẽ nhận cấu hình sau khi đặt namespace. Bên dưới khóa `ros__parameters` là các parameter cùng giá trị cần nạp. Chúng ta dùng dấu cách để thụt lề vì cấp lồng nhau là một phần cấu trúc của YAML.

Tệp này giúp chạy lại cùng một cấu hình. Thay giá trị bằng CLI trong một phiên không tự ghi ngược vào YAML. Có thể dùng `ros2 param dump NODE` để xem cấu hình đang có; khi dùng lại cần kiểm tra các giá trị chỉ đọc và tên node.

## 5. Viết launch file

Tệp YAML mới chỉ lưu cấu hình. Để khởi động cả bên phát, bên nhận và cổng dữ liệu bằng một lệnh, chúng ta viết **launch file**, tức tệp mô tả các thành phần cần chạy và thiết lập đi kèm.

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

Khi dùng launch file, hệ thống gọi `generate_launch_description` để lấy mô tả các thành phần. Với mỗi `Node`, `package` và `executable` chọn chương trình, còn `name` và `namespace` đặt tên node trong hệ thống đang chạy. Bên phát nhận thêm `parameters` để sử dụng tệp YAML vừa tạo.

Đường dẫn cấu hình được tìm qua thư mục share của package đã cài, nên lệnh launch không phụ thuộc bạn đang đứng ở thư mục nào.

## 6. Cài launch và cấu hình cùng package

Các tệp mới đang nằm trong mã nguồn, nhưng lệnh launch tìm package đã được cài trong workspace. Vì vậy, chúng ta cần bổ sung quy tắc để quá trình build đưa launch file và YAML đến đúng vị trí.

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

**Namespace** nhóm các tên bằng cách thêm phần đầu cho tên tương đối. Trong ví dụ, các node đều sử dụng `toc_do_do` không có dấu `/` ở đầu. Khi chạy trong namespace `thuc_hanh`, tên kênh được hiểu là `/thuc_hanh/toc_do_do`, nên các node vẫn kết nối với nhau trong nhóm đó.

Nếu cần thay một tên cụ thể, chúng ta dùng **remapping**, tức ánh xạ tên mà chương trình sử dụng sang tên mong muốn khi chạy. Ví dụ, có thể mở thêm một bên nhận ở ngoài namespace nhưng cho nó đọc kênh bên trong namespace:

```bash
ros2 run robovis_practice bo_nhan --ros-args -r __node:=bo_nhan_ngoai -r toc_do_do:=/thuc_hanh/toc_do_do
```

Node mới đọc cùng dữ liệu với bộ nhận trong launch. Đổi tên node bằng `__node` không tự đổi mọi tên topic. Khi thiết kế nhiều robot, cần lên kế hoạch tên topic và frame; namespace topic không tự làm mọi tên frame TF thành duy nhất.

Nếu có hai node cùng tên, kiểm tra các Terminal cũ và dừng đúng process trước khi chạy lại.

Đọc thêm: [ROS 2 — Parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html), [Launch integration](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Launch-system.html).

## 9. Tổng kết { #10-tong-ket }

Parameter cấu hình hành vi của node, YAML lưu các giá trị cần dùng lại, còn launch file mô tả cách khởi động các thành phần. Namespace và remapping giúp tổ chức tên khi hệ thống lớn dần. Tiếp theo, chúng ta sẽ liên hệ các giá trị vận tốc trong message với chuyển động của hai bánh xe.

[← Bài 6](04-service-va-action.md) · [Bài 8: Động học và odometry →](08-dong-hoc-va-odometry.md)
