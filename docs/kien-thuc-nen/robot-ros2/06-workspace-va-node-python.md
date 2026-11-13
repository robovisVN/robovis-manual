# Bài 4: Workspace, publisher và subscriber bằng Python

## 1. Mục tiêu và cấu trúc ví dụ

Trong bài này, bạn sẽ tạo package `robovis_practice`, viết hai node và tự kiểm tra luồng dữ liệu. Một node tạo tốc độ giả lập, node còn lại tính trung bình của tối đa năm mẫu gần nhất.

```text
bo_phat → /toc_do_do → bo_nhan → thông báo trung bình trong Terminal
```

Giá trị trong ví dụ mang quy ước đơn vị m/s. Đây là dữ liệu giả lập phục vụ học lập trình; nó chưa được đo từ encoder và không gửi lệnh tới động cơ.

## 2. Workspace, underlay và overlay

Workspace là thư mục chứa các package đang phát triển. Sau khi build, thường có:

| Thư mục | Vai trò |
| --- | --- |
| `src` | Mã nguồn bạn chỉnh sửa |
| `build` | Tệp trung gian của quá trình build |
| `install` | Chương trình và tệp được cài để ROS 2 tìm thấy |
| `log` | Nhật ký quá trình build |

Môi trường ROS 2 tại `/opt/ros/humble` là underlay. Workspace riêng được nạp sau đó đóng vai trò overlay. Khi chạy `source install/setup.bash`, bạn giúp Terminal tìm thêm package vừa phát triển.

Build package Python còn thực hiện việc cài đặt và đăng ký executable. Vì vậy, dù Python không cần biên dịch như C++, bạn vẫn cần bước build để dùng package đúng cách với `ros2 run`.

## 3. Tạo package

Trong Terminal mới:

```bash
source /opt/ros/humble/setup.bash
sudo apt install python3-colcon-common-extensions
mkdir -p ~/ros2_practice_ws/src
cd ~/ros2_practice_ws/src
ros2 pkg create robovis_practice --build-type ament_python --dependencies rclpy std_msgs std_srvs
```

Nếu package đã có từ lần học trước, giữ thư mục đó và chỉnh đúng các tệp bên dưới. Kiểm tra `package.xml` có phụ thuộc `rclpy`, `std_msgs` và `std_srvs`; bài service sẽ dùng phụ thuộc thứ ba.

| Tệp trong package | Chứa gì? |
| --- | --- |
| `package.xml` | Thông tin package và các phụ thuộc |
| `setup.py` | Quy tắc cài và đăng ký executable |
| `setup.cfg` | Vị trí cài script cho package Python |
| `robovis_practice/__init__.py` | Đánh dấu mô-đun Python |
| `resource/robovis_practice` | Dấu nhận diện trong chỉ mục package |

Giữ các tệp được tạo sẵn. Mã Python sẽ đặt trong thư mục `robovis_practice` nằm **bên trong** package cùng tên.

## 4. Viết bên phát dữ liệu

Tạo tệp `~/ros2_practice_ws/src/robovis_practice/robovis_practice/bo_phat.py`:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class BoPhat(Node):
    def __init__(self):
        super().__init__('nguon_toc_do')
        self.declare_parameter('toc_do_co_so', 0.2)
        self.declare_parameter('chu_ky', 0.2)
        chu_ky = self.get_parameter('chu_ky').value
        if chu_ky <= 0.0:
            raise ValueError('chu_ky phai lon hon 0')
        self.pub = self.create_publisher(Float64, 'toc_do_do', 10)
        self.sai_lech = [-0.02, 0.0, 0.02, 0.0]
        self.chi_so = 0
        self.timer = self.create_timer(chu_ky, self.gui_mau)

    def gui_mau(self):
        co_so = self.get_parameter('toc_do_co_so').value
        message = Float64()
        message.data = co_so + self.sai_lech[self.chi_so]
        self.pub.publish(message)
        self.chi_so = (self.chi_so + 1) % len(self.sai_lech)
        self.get_logger().info(f'Do: {message.data:.3f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = BoPhat()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
```

### Giải thích theo luồng chạy

Khi tạo `BoPhat`, hàm khởi tạo đặt tên node là `nguon_toc_do`, khai báo parameter và tạo publisher. `Float64` có một trường `data` kiểu số thực; đơn vị m/s do ví dụ này quy định.

Timer gọi `gui_mau()` mỗi 0,2 giây theo giá trị mặc định, tương ứng khoảng 5 Hz. Mỗi callback đọc tốc độ cơ sở, cộng một độ lệch rồi phát message. Dãy độ lệch lặp lại nên bạn có thể tính trước kết quả.

Số `10` trong `create_publisher` là độ sâu hàng đợi theo cấu hình QoS được tạo từ tham số này, không phải tần số phát. `spin()` cho executor xử lý timer và các callback khác; nếu tạo node rồi thoát ngay, timer chưa có cơ hội hoạt động.

## 5. Viết bên nhận và lọc dữ liệu

Tạo tệp `~/ros2_practice_ws/src/robovis_practice/robovis_practice/bo_nhan.py`:

```python
from collections import deque

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class BoNhan(Node):
    def __init__(self):
        super().__init__('theo_doi_toc_do')
        self.mau = deque(maxlen=5)
        self.sub = self.create_subscription(
            Float64, 'toc_do_do', self.nhan_mau, 10)

    def nhan_mau(self, message):
        self.mau.append(message.data)
        trung_binh = sum(self.mau) / len(self.mau)
        self.get_logger().info(
            f'Nhan: {message.data:.3f}; '
            f'TB {len(self.mau)} mau: {trung_binh:.3f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = BoNhan()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Subscriber gọi `nhan_mau()` khi có message. `deque(maxlen=5)` tự bỏ mẫu cũ nhất khi đã đầy. Lúc mới chạy, cửa sổ chưa đủ năm mẫu nên ta chia cho `len(self.mau)`, tránh coi các mẫu chưa có là số 0.

Trung bình trượt làm dữ liệu bớt dao động nhưng cũng làm phản ứng chậm hơn khi giá trị đổi đột ngột. Đây là đánh đổi cần xem xét khi dùng bộ lọc trong điều khiển.

## 6. Đăng ký executable

Trong `setup.py`, giữ thông tin và cấu trúc package đang có, sửa phần `entry_points` thành:

```python
entry_points = {
    'console_scripts': [
        'bo_phat = robovis_practice.bo_phat:main',
        'bo_nhan = robovis_practice.bo_nhan:main',
    ],
}
```

Đây là giá trị cho đối số `entry_points` **bên trong lời gọi `setup(...)`**. Trong tệp thật, giữ dấu phẩy ngăn với các đối số khác. Không đặt thêm một khối độc lập rồi bỏ qua đối số đang có.

Mỗi dòng có dạng `executable = package.module:function`. Khi gõ `ros2 run robovis_practice bo_phat`, ROS 2 tìm entry point rồi gọi `main` trong mô-đun `bo_phat`.

## 7. Build, nạp môi trường và chạy

Terminal build:

```bash
source /opt/ros/humble/setup.bash
cd ~/ros2_practice_ws
colcon build --symlink-install --packages-select robovis_practice
```

Chờ `Summary` kết thúc không có package thất bại. Mở **Terminal 1**:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_practice_ws/install/setup.bash
ros2 run robovis_practice bo_phat
```

Mở **Terminal 2**, nạp hai môi trường tương tự rồi chạy:

```bash
ros2 run robovis_practice bo_nhan
```

Terminal 1 in các giá trị quanh 0,2 m/s; Terminal 2 in mẫu nhận và trung bình. Vì thời điểm kết nối khác nhau, mẫu đầu mà bên nhận thấy có thể không phải 0,18.

Terminal kiểm tra:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_practice_ws/install/setup.bash
ros2 pkg executables robovis_practice
ros2 node info /nguon_toc_do
ros2 topic hz /toc_do_do
```

Độ lệch nhỏ quanh 5 Hz là bình thường. `Ctrl+C` dừng từng chương trình. Nếu đã sửa entry point nhưng chưa build lại, executable mới chưa được cài.

## 8. Lỗi thường gặp

| Lỗi | Hướng kiểm tra |
| --- | --- |
| `Package not found` | Build thành công và đã nạp `install/setup.bash` chưa? |
| `No executable found` | Entry point có đúng tên, đã build lại chưa? |
| `ModuleNotFoundError` | Tên thư mục Python, tên tệp và đường dẫn mô-đun có khớp không? |
| Có log bên phát nhưng bên nhận im lặng | Tên topic, kiểu, domain và nguồn đang chạy |
| Sửa mã không thấy đổi | Xác định package đang được tìm từ workspace nào bằng `ros2 pkg prefix` |

## 9. Bài tập có kết quả đối chiếu

1. Với bốn mẫu `0,18; 0,20; 0,22; 0,20`, trung bình là bao nhiêu? Kết quả là 0,20 m/s.
2. Giảm `maxlen` xuống 2, rồi tăng lên 10. Quan sát độ mượt và độ trễ khi thay tốc độ cơ sở ở bài parameter.
3. Khởi động bên nhận trước bên phát. Vì sao bên nhận chỉ chờ chứ không tự tạo dữ liệu?
4. Đổi topic ở riêng bên nhận. Dùng công cụ bài 3 để tìm chỗ không khớp.

Đọc thêm: [ROS 2 — Publisher/subscriber Python](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html), [Creating a package](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

[← Bài 3](01-node-topic-va-lenh.md) · [Bài 5: Đọc message của robot →](02-cac-topic-cua-robot.md)
