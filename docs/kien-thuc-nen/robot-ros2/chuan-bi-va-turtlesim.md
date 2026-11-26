# Bài 2: Môi trường, talker/listener và Turtlesim

Ở bài trước, chúng ta đã chia phần mềm robot thành các thành phần có thể trao đổi dữ liệu. Để quan sát cách trao đổi đó, chúng ta sẽ bắt đầu với hai chương trình có sẵn, chưa cần cảm biến hoặc robot thật.

Sau khi chạy được bên gửi và bên nhận, chúng ta chuyển sang Turtlesim để thấy một lệnh truyền qua ROS 2 có thể tạo ra chuyển động trong mô phỏng như thế nào.

## 1. Mục tiêu và chuẩn bị

Chúng ta sẽ kiểm tra môi trường, chạy hai chương trình trao đổi chuỗi, rồi dùng Turtlesim để quan sát lệnh chuyển động. Bạn cần Ubuntu 22.04 có giao diện desktop, Internet trong lúc cài gói và ROS 2 Humble Desktop đã cài theo [hướng dẫn chính thức](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

Các lệnh bên dưới chạy trong Bash của Ubuntu. Nếu đang dùng Windows với máy ảo, hãy mở Terminal bên trong Ubuntu.

## 2. Vì sao mỗi Terminal cần nạp môi trường?

Một chương trình đã được cài vẫn cần được Terminal tìm thấy trước khi chạy. Tệp `setup.bash` bổ sung các đường dẫn của bản ROS 2 được chọn vào môi trường shell hiện tại. Vì vậy, chúng ta bắt đầu bằng việc nạp tệp này rồi kiểm tra công cụ `ros2`.

```bash
source /opt/ros/humble/setup.bash
printenv ROS_DISTRO
which ros2
ros2 --help
```

Kết quả cần có `humble`, đường dẫn đến công cụ `ros2` và danh sách lệnh con. Nếu `source` báo không có tệp, hãy xử lý việc cài ROS 2 trước. Tạo một tệp trống mang tên `setup.bash` không cung cấp được phần mềm còn thiếu.

Một Terminal đã nạp môi trường không tự sửa môi trường của cửa sổ khác. Trong các bài học, hãy nạp lại ở mỗi Terminal mới. Nếu `~/.bashrc` đã làm việc này, lệnh có thể đã sẵn sàng; vẫn dùng `printenv ROS_DISTRO` để kiểm tra khi nghi ngờ.

## 3. Chuẩn bị các chương trình mẫu

Chúng ta sử dụng `talker` để phát chuỗi và `listener` để nhận chuỗi; Turtlesim sẽ được dùng ở bước sau. Khi nguồn apt của ROS 2 đã được thiết lập đúng, cài và kiểm tra các gói mẫu bằng những lệnh dưới đây:

```bash
sudo apt update
sudo apt install ros-humble-demo-nodes-cpp ros-humble-turtlesim ros-humble-rqt-graph
ros2 pkg executables demo_nodes_cpp
```

Danh sách cần có `talker` và `listener`. Lệnh `ros2 pkg executables` chỉ liệt kê chương trình, chưa khởi chạy chúng.

## 4. Thực hành talker và listener

Ví dụ này sử dụng các Terminal riêng để chúng ta có thể giữ bên phát hoạt động trong khi mở bên nhận và công cụ kiểm tra. Bắt đầu với `talker` trong **Terminal 1**:

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

Khi chạy, `talker` gửi các chuỗi có số đếm và in thông báo trong Terminal. Hãy giữ cửa sổ này mở để nguồn dữ liệu tiếp tục hoạt động trong lúc chúng ta khởi động bên nhận.

Trong **Terminal 2**:

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp listener
```

Bạn cần thấy các dòng thông báo đã nhận chuỗi. Listener khởi động muộn hơn nên có thể bắt đầu từ một số đếm lớn hơn 1. Với cấu hình demo mặc định, nó nhận những mẫu được phát khi đã kết nối, không phải toàn bộ lịch sử từ lúc talker bắt đầu.

Trong **Terminal 3**:

```bash
source /opt/ros/humble/setup.bash
ros2 node list
ros2 topic list -t
ros2 topic echo /chatter --once
```

Kết quả thường có `/talker`, `/listener` và `/chatter` kiểu `std_msgs/msg/String`. Số mẫu và thời điểm nhận không cần giống hệt giữa các cửa sổ.

## 5. Thực hành Turtlesim

Với talker/listener, kết quả trao đổi hiện thành dòng chữ. Turtlesim giúp chúng ta quan sát một tình huống khác: chương trình đọc bàn phím gửi lệnh để một con rùa mô phỏng chuyển động. Dừng talker và listener trước khi chuyển bài thử, rồi chạy trong Terminal 1:

```bash
ros2 run turtlesim turtlesim_node
```

Trong Terminal 2:

```bash
ros2 run turtlesim turtle_teleop_key
```

Chọn Terminal 2 để nó nhận phím, sau đó nhấn các phím mũi tên. Rùa chuyển động trong cửa sổ Turtlesim và để lại nét vẽ.

| Chương trình | Vai trò |
| --- | --- |
| `turtlesim_node` | Cập nhật mô phỏng, vẽ rùa, phát trạng thái |
| `turtle_teleop_key` | Đọc bàn phím, gửi lệnh chuyển động |

Nếu chọn cửa sổ mô phỏng rồi nhấn phím mà rùa không đi, hãy quay lại Terminal teleop. Cửa sổ hiển thị không phải nơi chương trình teleop đọc bàn phím.

## 6. Quan sát bằng đồ thị

Trong Terminal 3:

```bash
rqt_graph
```

Trong đồ thị, hãy tìm chương trình teleop, Turtlesim và kênh kết nối giữa chúng. Nếu chưa thấy các thành phần, thử nút làm mới hoặc kiểm tra bộ lọc. Khi mở thêm một công cụ đọc topic, chúng ta có thể thấy thêm bên nhận dữ liệu vì công cụ đó cũng tham gia hệ thống.

Đồ thị giúp hình dung các chương trình có thể trao đổi qua kênh nào. Để biết chúng thực sự gửi gì và giá trị có phù hợp hay không, chúng ta còn cần đọc message và log; đó là công việc của bài tiếp theo.

## 7. Xử lý lỗi

| Hiện tượng | Kiểm tra đầu tiên |
| --- | --- |
| `ros2: command not found` | Tệp môi trường đã được nạp ở cửa sổ này chưa? |
| Không tìm thấy package | Đúng bản ROS 2 và gói đã được cài chưa? |
| Talker gửi, listener không nhận | Các Terminal có cùng domain và môi trường không? |
| Không có cửa sổ Turtlesim | Phiên Ubuntu có hiển thị đồ họa không? Đọc lỗi ngay trong Terminal |
| Node cũ vẫn xuất hiện ngắn sau khi dừng | Chờ cập nhật discovery, kiểm tra process và log trước khi khởi chạy thêm bản sao |

Đọc thêm: [Configuring environment](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html), [Turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html).

## 8. Tổng kết { #9-tong-ket }

Chúng ta đã nạp môi trường, chạy hai chương trình trao đổi chuỗi và dùng Turtlesim để quan sát lệnh chuyển động. Việc mở được các chương trình là bước đầu; tiếp theo, chúng ta sẽ tìm đúng node, topic và nội dung dữ liệu để giải thích những gì đang diễn ra.

[← Bài 1](00-robot-va-ros2.md) · [Bài 3: Node, topic và công cụ kiểm tra →](01-node-topic-va-lenh.md)
