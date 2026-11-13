# Bài 2: Môi trường, talker/listener và Turtlesim

## 1. Mục tiêu và chuẩn bị

Chúng ta sẽ kiểm tra môi trường, chạy hai chương trình trao đổi chuỗi, rồi dùng Turtlesim để quan sát lệnh chuyển động. Bạn cần Ubuntu 22.04 có giao diện desktop, Internet trong lúc cài gói và ROS 2 Humble Desktop đã cài theo [hướng dẫn chính thức](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

Các lệnh bên dưới chạy trong Bash của Ubuntu. Nếu đang dùng Windows với máy ảo, hãy mở Terminal bên trong Ubuntu.

## 2. Vì sao mỗi Terminal cần nạp môi trường?

Khi mở Terminal, hệ điều hành cần biết tìm chương trình và thư viện ở đâu. Tệp `setup.bash` bổ sung các đường dẫn của bản ROS 2 được chọn vào môi trường shell hiện tại.

```bash
source /opt/ros/humble/setup.bash
printenv ROS_DISTRO
which ros2
ros2 --help
```

Kết quả cần có `humble`, đường dẫn đến công cụ `ros2` và danh sách lệnh con. Nếu `source` báo không có tệp, hãy xử lý việc cài ROS 2 trước. Tạo một tệp trống mang tên `setup.bash` không cung cấp được phần mềm còn thiếu.

Một Terminal đã nạp môi trường không tự sửa môi trường của cửa sổ khác. Trong các bài học, hãy nạp lại ở mỗi Terminal mới. Nếu `~/.bashrc` đã làm việc này, lệnh có thể đã sẵn sàng; vẫn dùng `printenv ROS_DISTRO` để kiểm tra khi nghi ngờ.

## 3. Chuẩn bị các chương trình mẫu

Khi nguồn apt của ROS 2 đã được thiết lập đúng:

```bash
sudo apt update
sudo apt install ros-humble-demo-nodes-cpp ros-humble-turtlesim ros-humble-rqt-graph
ros2 pkg executables demo_nodes_cpp
```

Danh sách cần có `talker` và `listener`. Lệnh `ros2 pkg executables` chỉ liệt kê chương trình, chưa khởi chạy chúng.

## 4. Thực hành talker và listener

Trong **Terminal 1**:

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

Chương trình tiếp tục chạy và gửi chuỗi có số đếm. Giữ Terminal 1 mở.

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

### Tự làm một phép thử

Dừng talker bằng `Ctrl+C`. Listener vẫn chạy nhưng không còn chuỗi mới. Chạy talker lại, chờ kết nối rồi quan sát dữ liệu tiếp tục.

Qua thử nghiệm này, hãy phân biệt “process vẫn chạy”, “node đã được phát hiện” và “đang có message mới”. Ba trạng thái đó không hoàn toàn giống nhau.

## 5. Thực hành Turtlesim

Dừng talker và listener trước khi chuyển bài thử. Trong Terminal 1:

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

Quan sát kết nối giữa teleop và Turtlesim. Có thể dùng nút làm mới hoặc thay bộ lọc nếu chưa thấy các thành phần. Khi mở thêm công cụ đọc topic, đồ thị có thể xuất hiện thêm bên nhận dữ liệu.

Đồ thị giúp xem mối liên hệ, nhưng không thay thế việc đọc message và log. Một mũi tên không chứng minh dữ liệu đang có giá trị đúng.

## 7. Xử lý lỗi

| Hiện tượng | Kiểm tra đầu tiên |
| --- | --- |
| `ros2: command not found` | Tệp môi trường đã được nạp ở cửa sổ này chưa? |
| Không tìm thấy package | Đúng bản ROS 2 và gói đã được cài chưa? |
| Talker gửi, listener không nhận | Các Terminal có cùng domain và môi trường không? |
| Không có cửa sổ Turtlesim | Phiên Ubuntu có hiển thị đồ họa không? Đọc lỗi ngay trong Terminal |
| Node cũ vẫn xuất hiện ngắn sau khi dừng | Chờ cập nhật discovery, kiểm tra process và log trước khi khởi chạy thêm bản sao |

## 8. Bài tập

Chụp hoặc ghi lại đồ thị của talker/listener, sau đó của Turtlesim. Chỉ ra bên gửi, bên nhận và dữ liệu trao đổi. Dừng từng chương trình rồi mô tả phần nào còn hoạt động.

Đọc thêm: [Configuring environment](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html), [Turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html).

[← Bài 1](00-robot-va-ros2.md) · [Bài 3: Node, topic và công cụ kiểm tra →](01-node-topic-va-lenh.md)
