# Bài 6: Viết service, client và làm quen action

## 1. Mục tiêu và tình huống

Trong bài 4, bên phát gửi liên tục các mẫu tốc độ. Bây giờ ta muốn bật hoặc tắt việc chuyển tiếp những mẫu đó bằng một yêu cầu có phản hồi. Chúng ta sẽ thêm node `cong_du_lieu` vào package `robovis_practice`.

Bạn cần hoàn thành bài 4 và giữ đúng các phụ thuộc `rclpy`, `std_msgs`, `std_srvs`. Mỗi Terminal chạy ví dụ cần nạp ROS 2 và `~/ros2_practice_ws/install/setup.bash`.

## 2. Chọn topic, service hay action?

| Nhu cầu | Giao diện phù hợp | Điều cần theo dõi |
| --- | --- | --- |
| Nhận tốc độ liên tục | Topic | Các mẫu dữ liệu |
| Yêu cầu đổi trạng thái bật/tắt | Service | Request và response |
| Yêu cầu robot đi tới một vị trí | Action | Goal, feedback và result |

Service có client gửi request và server xử lý để trả response. Giao diện này phù hợp với thao tác trả lời trong thời gian ngắn. Với một nhiệm vụ kéo dài, người dùng thường cần theo dõi tiến trình và có cơ chế yêu cầu hủy; action cung cấp cấu trúc cho việc đó.

## 3. Đọc giao diện `SetBool`

```bash
ros2 interface show std_srvs/srv/SetBool
```

Phần yêu cầu có `data` kiểu bool. Sau dấu `---` là phản hồi gồm `success` và `message`. Trong ví dụ, `data: true` cho phép chuyển tiếp, `data: false` tạm ngừng chuyển tiếp.

Trạng thái “đã nhận response” và nội dung `success: true` là hai điều khác nhau. Một server vẫn có thể trả response để báo rằng thao tác không được chấp nhận.

## 4. Viết server và cổng dữ liệu

Tạo `~/ros2_practice_ws/src/robovis_practice/robovis_practice/cong_du_lieu.py`:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from std_srvs.srv import SetBool


class CongDuLieu(Node):
    def __init__(self):
        super().__init__('cong_du_lieu')
        self.cho_phep = False
        self.pub = self.create_publisher(
            Float64, 'toc_do_cho_phep', 10)
        self.sub = self.create_subscription(
            Float64, 'toc_do_do', self.nhan_mau, 10)
        self.srv = self.create_service(
            SetBool, 'cho_phep_du_lieu', self.doi_trang_thai)

    def nhan_mau(self, message):
        if self.cho_phep:
            self.pub.publish(message)

    def doi_trang_thai(self, request, response):
        self.cho_phep = request.data
        response.success = True
        response.message = (
            'Da bat chuyen tiep' if self.cho_phep
            else 'Da tat chuyen tiep')
        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = CongDuLieu()
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

Node đồng thời là subscriber, publisher và service server. Callback `nhan_mau` chuyển mẫu mới nếu được phép; callback service thay trạng thái rồi trả response.

Khi tắt, node không gửi mẫu 0 và không dừng bên phát. Nó chỉ ngừng chuyển tiếp. Vì vậy, người nhận không được tự hiểu “không có mẫu mới” là “tốc độ bằng 0”. Trong một hệ thống đo thật, bên nhận còn cần kiểm tra độ mới của dữ liệu.

## 5. Đăng ký, build và thử bằng CLI

Thêm vào danh sách `console_scripts` của `setup.py`, giữ hai dòng ở bài 4:

```text
'cong_du_lieu = robovis_practice.cong_du_lieu:main',
```

Build lại:

```bash
source /opt/ros/humble/setup.bash
cd ~/ros2_practice_ws
colcon build --symlink-install --packages-select robovis_practice
```

Mở các Terminal mới, nạp môi trường nền và workspace. Chạy `bo_phat` ở Terminal 1, `cong_du_lieu` ở Terminal 2:

```bash
ros2 run robovis_practice cong_du_lieu
```

Ở Terminal 3:

```bash
ros2 service list -t
ros2 service call /cho_phep_du_lieu std_srvs/srv/SetBool '{data: true}'
ros2 topic echo /toc_do_cho_phep
```

Bạn cần thấy response thành công và các mẫu được chuyển tiếp. Dừng `echo` bằng `Ctrl+C`, gọi lại service với `data: false`, rồi thử đọc topic. Lệnh sẽ chờ vì không có mẫu mới; bên phát `/toc_do_do` vẫn hoạt động.

## 6. Viết client bất đồng bộ

CLI thuận tiện để thử, còn ứng dụng cần gọi service từ mã. Tạo `~/ros2_practice_ws/src/robovis_practice/robovis_practice/doi_trang_thai.py`:

```python
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


def main(args=None):
    rclpy.init(args=args)
    node = Node('client_cho_phep')
    client = node.create_client(SetBool, 'cho_phep_du_lieu')
    try:
        if not client.wait_for_service(timeout_sec=5.0):
            node.get_logger().error('Khong tim thay service sau 5 giay')
            return
        request = SetBool.Request()
        request.data = True
        future = client.call_async(request)
        rclpy.spin_until_future_complete(node, future, timeout_sec=5.0)
        if not future.done():
            node.get_logger().error('Chua nhan duoc phan hoi sau 5 giay')
            return
        response = future.result()
        node.get_logger().info(
            f'success={response.success}; {response.message}')
    except KeyboardInterrupt:
        pass
    except Exception as error:
        node.get_logger().error(f'Loi goi service: {error}')
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Thêm entry point `'doi_trang_thai = robovis_practice.doi_trang_thai:main',`, build lại rồi chạy:

```bash
ros2 run robovis_practice doi_trang_thai
```

`call_async` trả về một **future**, đại diện cho kết quả sẽ có sau. Executor vẫn cần xử lý sự kiện để response được nhận. `spin_until_future_complete` phục vụ việc đó trong chương trình client độc lập này.

Timeout phía client chỉ giới hạn thời gian chờ; nó không chứng minh server chưa xử lý yêu cầu. Với tác vụ có tác động thật, ứng dụng phải xem xét khả năng yêu cầu đã được thực hiện dù response chưa về.

## 7. Action qua ví dụ Turtlesim

Mở Turtlesim mặc định, dừng teleop trong lúc thử action:

```bash
ros2 action list -t
ros2 interface show turtlesim/action/RotateAbsolute
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute '{theta: 1.57}' --feedback
```

Goal yêu cầu rùa quay tới hướng tuyệt đối gần 1,57 rad. Action có ba phần: mục tiêu, kết quả và phản hồi tiến trình. Nếu rùa đã ở hướng đó, chuyển động nhỏ là bình thường.

Phản hồi được gửi trong quá trình chạy; kết quả cho biết nhiệm vụ đã kết thúc thế nào. “Mục tiêu được nhận” chưa đồng nghĩa “đã tới đích”. Khả năng hủy phụ thuộc server chấp nhận và thực hiện yêu cầu hủy.

## 8. Bài tập

1. Dừng server rồi chạy client. Lỗi cần xuất hiện ở bước tìm service.
2. Tắt cổng dữ liệu, đo `/toc_do_do` và `/toc_do_cho_phep`; mô tả sự khác nhau.
3. Sửa client để yêu cầu tắt, rồi kiểm tra response và dữ liệu thực tế.
4. Nêu thông tin cần có trong feedback cho nhiệm vụ đi tới một vị trí.

Đọc thêm: [SetBool](https://github.com/ros2/common_interfaces/blob/humble/std_srvs/srv/SetBool.srv), [ROS 2 — Service/client Python](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html), [Understanding actions](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html).

[← Bài 5](02-cac-topic-cua-robot.md) · [Bài 7: Parameter và launch →](05-parameter-va-launch.md)
