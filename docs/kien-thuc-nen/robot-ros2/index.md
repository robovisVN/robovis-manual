# Lộ trình nhập môn robot và ROS 2

**Mục tiêu:** hiểu dữ liệu được trao đổi giữa các thành phần ROS 2, làm một bài thử trên máy tính rồi biết thứ tự chuyển sang robot LiDAR.

**Cần biết trước:** đã dùng được Terminal và đường dẫn theo [Ubuntu cơ bản](../../ubuntu-co-ban/index.md), đặc biệt [bài 6 về môi trường](../../ubuntu-co-ban/06-cai-va-chay-phan-mem.md). Không bắt buộc biết viết node C++/Python để bắt đầu.

## Phần nào chạy trên máy tính?

ROS 2 là bộ công cụ để xây dựng phần mềm gồm nhiều thành phần cùng làm việc. Nó không thay thế hệ điều hành, không phải firmware chung để nạp vào mọi vi điều khiển và không tự tạo ra khả năng tự hành chỉ nhờ cài đặt.

Trong cấu hình Robot ESP32 LiDAR hiện có, **PC chạy Ubuntu 22.04 và ROS 2 Humble**, ESP32 đọc cảm biến/điều khiển động cơ; hai bên trao đổi qua Wi-Fi. Sơ đồ và chương trình giao tiếp cụ thể giữ tại [Kiến trúc hệ thống sản phẩm](../../robot-esp32-lidar/01-gioi-thieu/02-kien-truc-he-thong.md).

**Node** là thành phần tính toán của ROS 2; một chương trình có thể chứa một hoặc nhiều node. **Topic** là kênh trao đổi; **message** là dữ liệu có kiểu xác định. Bên gửi gọi là **publisher**, bên nhận là **subscriber**. Cùng tên topic chưa đủ trong mọi cấu hình: kiểu dữ liệu và các thiết lập truyền nhận cũng phải tương thích. Xem [ROS 2 Humble – Understanding nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html) và [Understanding topics](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html).

## Thứ tự học

1. Thực hành truyền nhận mẫu ở phần dưới, **chưa cần robot**.
2. Đọc [Node, topic và lệnh thường dùng](../../robot-esp32-lidar/04-ros2-co-ban/01-node-topic-va-lenh.md). Lệnh kiểm tra dùng chung; tên `/scan`, `/odom`, IP và bringup trong bài thuộc robot LiDAR, chỉ áp dụng khi đã chạy sản phẩm.
3. Học [Hệ tọa độ và TF từ đầu](he-toa-do-va-tf.md), rồi đọc [RViz và hệ tọa độ TF](../../robot-esp32-lidar/04-ros2-co-ban/03-rviz-va-tf.md) để xem dữ liệu của robot.
4. Theo [trang bắt đầu Robot ESP32 LiDAR](../../robot-esp32-lidar/index.md): chuẩn bị workspace, mạng, [khởi động và kiểm tra dữ liệu](../../robot-esp32-lidar/03-van-hanh/02-khoi-dong-va-kiem-tra.md), rồi [các topic của robot](../../robot-esp32-lidar/04-ros2-co-ban/02-cac-topic-cua-robot.md).
5. Chỉ sau khi kiểm tra dữ liệu ổn định mới [chạy thử](../../robot-esp32-lidar/03-van-hanh/01-chay-thu-lan-dau.md), [tạo bản đồ SLAM](../../robot-esp32-lidar/05-lidar-slam-navigation/02-tao-ban-do-slam.md) và [điều hướng Nav2](../../robot-esp32-lidar/05-lidar-slam-navigation/04-dieu-huong-nav2.md). SLAM là vừa xây dựng bản đồ vừa ước lượng vị trí; Nav2 là bộ công cụ điều hướng robot tới đích.

## Thực hành nhỏ: hai chương trình truyền chuỗi

Thực hiện trên **Ubuntu 22.04 đã có ROS 2 Humble**. Nếu chưa cài, dùng [phần cài ROS 2 hiện có](../../robot-esp32-lidar/02-chuan-bi/01-yeu-cau-va-cai-ros2.md); bài thử này chưa cần workspace hay Wi-Fi robot. Không chạy bringup/điều khiển robot trong bài thử.

### 1. Kiểm tra chương trình mẫu

Trong Terminal Ubuntu:

```bash
source /opt/ros/humble/setup.bash
printenv ROS_DISTRO
ros2 pkg executables demo_nodes_cpp
```

`ROS_DISTRO` cần hiện `humble`. Danh sách executable (chương trình chạy được) cần có `talker` và `listener` của gói `demo_nodes_cpp`. Nếu chưa có gói, với nguồn apt ROS 2 đã được thiết lập theo hướng dẫn cài chính thức, kết nối Internet rồi chạy:

```bash
sudo apt update
sudo apt install ros-humble-demo-nodes-cpp
```

Chạy lại lệnh liệt kê. Nếu thiếu `/opt/ros/humble/setup.bash`, quay lại bước cài ROS 2, không tạo tệp rỗng để bỏ qua lỗi.

### 2. Mở bên gửi và bên nhận

Terminal thứ nhất:

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

Giữ Terminal này chạy, mở Terminal thứ hai:

```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp listener
```

**Kết quả mong đợi:** talker báo gửi chuỗi dạng `Hello World` kèm số đếm; listener báo nhận các chuỗi tương ứng. Số bắt đầu và thời điểm nhận có thể khác. Cách chạy dựa trên [ROS 2 Humble – thử talker/listener](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html#try-some-examples); ở đây dùng cả hai chương trình từ gói C++ [demo_nodes_cpp chính thức](https://github.com/ros2/demos/tree/humble/demo_nodes_cpp), không liên quan lệnh động cơ.

### 3. Quan sát dữ liệu

Terminal thứ ba:

```bash
source /opt/ros/humble/setup.bash
ros2 node list
ros2 topic list -t
ros2 topic info /chatter
ros2 topic echo /chatter --once
```

Chạy từng lệnh; với ví dụ mặc định, tìm `/talker`, `/listener` và topic `/chatter` kiểu `std_msgs/msg/String`. Nếu tên đã bị cấu hình đổi, dùng tên thực tế từ danh sách. `--once` đọc một message rồi kết thúc.

**Tự kiểm tra:** dừng talker bằng Ctrl+C trong Terminal thứ nhất. Listener còn chạy nhưng không nhận chuỗi mới. Sau đó dừng listener bằng Ctrl+C; nếu lệnh echo đang chờ, Ctrl+C tại chính cửa sổ đó. Bài này cho thấy bên nhận có thể đang chờ, không nhất thiết bị treo.

## Lỗi thường gặp

- `ros2: command not found`: kiểm tra đúng Terminal Ubuntu và `source` trong từng cửa sổ.
- Không tìm thấy package/executable: kiểm tra gói demo và tên chương trình; chưa cần cài workspace sản phẩm để chữa lỗi demo.
- Talker gửi nhưng listener không nhận: kiểm tra hai Terminal có cùng môi trường ROS 2, `ROS_DOMAIN_ID` và thiết lập truyền nhận; không tự đặt một domain tùy ý rồi chỉ đổi ở một cửa sổ.
- Không có `/scan` khi mới chạy demo: đúng, demo không tạo dữ liệu LiDAR.

[← Bắt đầu từ đây: lộ trình B](../index.md#lo-trinh-b) · [Tiếp: Hệ tọa độ và TF →](he-toa-do-va-tf.md)
