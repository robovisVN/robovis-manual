# Bài 6: Viết service, client và làm quen action

Ở ví dụ phát tốc độ, dữ liệu liên tục đi từ bên phát đến bên nhận. Bây giờ, giả sử chúng ta muốn quyết định khi nào một luồng dữ liệu được chuyển tiếp và nhận thông báo xác nhận sau mỗi lần thay đổi.

Đây là nhu cầu khác với việc nhận mẫu liên tục qua topic. Trong bài này, chúng ta sẽ dùng service để thực hiện thao tác bật, tắt và tìm hiểu khi nào một nhiệm vụ cần đến action.

## 1. Mục tiêu và tình huống

Chúng ta sẽ thêm node `cong_du_lieu` vào package `robovis_practice` của bài 4. Node này nhận mẫu từ bên phát và chỉ chuyển tiếp khi được cho phép. Một chương trình khác gửi yêu cầu bật hoặc tắt cổng, rồi đọc phản hồi để biết thao tác đã được xử lý thế nào.

Bạn cần hoàn thành bài 4 và giữ đúng các phụ thuộc `rclpy`, `std_msgs`, `std_srvs`. Mỗi Terminal chạy ví dụ cần nạp ROS 2 và `~/ros2_practice_ws/install/setup.bash`.

## 2. Chọn topic, service hay action?

Trước khi viết mã, chúng ta xác định loại trao đổi cần thực hiện. Nhận số đo liên tục, đổi một trạng thái và giao một nhiệm vụ kéo dài có cách theo dõi khác nhau:

| Nhu cầu | Giao diện phù hợp | Điều cần theo dõi |
| --- | --- | --- |
| Nhận tốc độ liên tục | Topic | Các mẫu dữ liệu |
| Yêu cầu đổi trạng thái bật/tắt | Service | Request và response |
| Yêu cầu robot đi tới một vị trí | Action | Goal, feedback và result |

Với **service**, bên yêu cầu gọi là **client** gửi **request**, còn bên xử lý gọi là **server** trả về **response**. Cách trao đổi này phù hợp với thao tác có phản hồi trong thời gian ngắn, như bật cổng dữ liệu. Nếu giao robot đi tới một vị trí, chúng ta còn cần theo dõi tiến trình và có thể yêu cầu hủy; **action** cung cấp cấu trúc để xử lý loại nhiệm vụ đó.

## 3. Đọc giao diện `SetBool`

Service cũng cần một kiểu giao diện để hai bên hiểu cấu trúc yêu cầu và phản hồi. Ví dụ bật, tắt sử dụng `SetBool`; chúng ta xem định nghĩa trước khi viết server:

```bash
ros2 interface show std_srvs/srv/SetBool
```

Trong định nghĩa, phần trước dấu `---` là yêu cầu với trường `data` kiểu bool. Phần sau là phản hồi, gồm `success` và `message`. Chúng ta quy định `data: true` cho phép chuyển tiếp, còn `data: false` tạm ngừng chuyển tiếp; server sẽ trả thông báo tương ứng sau khi cập nhật trạng thái.

Trạng thái “đã nhận response” và nội dung `success: true` là hai điều khác nhau. Một server vẫn có thể trả response để báo rằng thao tác không được chấp nhận.

## 4. Viết server và cổng dữ liệu

Node mới có hai công việc: nhận mẫu tốc độ để chuyển tiếp khi được phép và xử lý yêu cầu thay đổi trạng thái cổng. Vì hai công việc cùng sử dụng trạng thái `cho_phep`, chúng ta đặt chúng trong cùng một node.

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

Trong chương trình trên, một node đồng thời đảm nhiệm vai trò subscriber, publisher và service server. Mỗi khi có mẫu mới, callback `nhan_mau` kiểm tra trạng thái cổng trước khi phát tiếp. Khi có request, callback service thay đổi trạng thái đó và trả response cho bên yêu cầu.

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

Lệnh CLI giúp chúng ta thử service và quan sát kết quả mà chưa phải viết bên gọi. Khi muốn một ứng dụng tự gửi yêu cầu, chúng ta cần tạo client trong mã. Tạo tệp `~/ros2_practice_ws/src/robovis_practice/robovis_practice/doi_trang_thai.py`:

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

Client gọi `call_async` để gửi yêu cầu và nhận một **future**, đối tượng đại diện cho kết quả sẽ có sau. Trong lúc chờ, executor vẫn cần xử lý sự kiện để nhận response. Chương trình client độc lập này sử dụng `spin_until_future_complete` cho việc đó, rồi đọc kết quả hoặc báo đã hết thời gian chờ.

Timeout phía client chỉ giới hạn thời gian chờ; nó không chứng minh server chưa xử lý yêu cầu. Với tác vụ có tác động thật, ứng dụng phải xem xét khả năng yêu cầu đã được thực hiện dù response chưa về.

## 7. Action qua ví dụ Turtlesim

Để hình dung action, chúng ta quay lại Turtlesim và yêu cầu rùa quay tới một hướng xác định. Mở Turtlesim mặc định, dừng teleop trong lúc thử để tránh nguồn lệnh khác can thiệp, rồi chạy:

```bash
ros2 action list -t
ros2 interface show turtlesim/action/RotateAbsolute
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute '{theta: 1.57}' --feedback
```

Trong lệnh trên, **goal** là yêu cầu rùa quay tới hướng tuyệt đối gần 1,57 rad. Khi thực hiện, action có thể gửi **feedback** về tiến trình, rồi trả **result** khi nhiệm vụ kết thúc. Nếu rùa đã gần hướng được yêu cầu, chuyển động sẽ nhỏ; chúng ta cần đọc cả phản hồi thay vì chỉ nhìn quãng quay.

Phản hồi được gửi trong quá trình chạy; kết quả cho biết nhiệm vụ đã kết thúc thế nào. “Mục tiêu được nhận” chưa đồng nghĩa “đã tới đích”. Khả năng hủy phụ thuộc server chấp nhận và thực hiện yêu cầu hủy.

Đọc thêm: [SetBool](https://github.com/ros2/common_interfaces/blob/humble/std_srvs/srv/SetBool.srv), [ROS 2 — Service/client Python](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html), [Understanding actions](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html).

## 8. Tổng kết { #9-tong-ket }

Chúng ta đã dùng service để điều khiển trạng thái cổng dữ liệu và đọc phản hồi từ server. Qua Turtlesim, chúng ta cũng phân biệt yêu cầu ngắn với nhiệm vụ có tiến trình và kết quả. Bài tiếp theo sẽ tổ chức các node đã viết bằng cấu hình và launch file để thuận tiện chạy lại cả ví dụ.

[← Bài 5](02-cac-topic-cua-robot.md) · [Bài 7: Parameter và launch →](05-parameter-va-launch.md)
