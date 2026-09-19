# Thuật ngữ

| Thuật ngữ | Ý nghĩa trong hệ thống |
| --- | --- |
| ROS 2 | Nền tảng phần mềm robot chạy trên PC/Laptop |
| Node | Một chương trình ROS 2 đảm nhiệm một chức năng |
| Topic | Kênh truyền dữ liệu giữa các node |
| Message | Cấu trúc dữ liệu được gửi qua topic |
| Publisher | Node gửi dữ liệu lên topic |
| Subscriber | Node nhận dữ liệu từ topic |
| Bringup | Nhóm tiến trình khởi động kết nối phần cứng và các node nền |
| LiDAR | Cảm biến đo khoảng cách bằng ánh sáng laser |
| LaserScan | Kiểu message ROS biểu diễn một vòng quét LiDAR 2D |
| Encoder | Cảm biến đo chuyển động quay của bánh xe |
| Odometry | Ước lượng chuyển động tương đối của robot, thường từ encoder |
| `/cmd_vel` | Topic lệnh vận tốc tiến/lùi và quay |
| `/scan` | Topic dữ liệu LiDAR |
| `/odom` | Topic dữ liệu odometry |
| TF | Hệ thống mô tả quan hệ giữa các hệ tọa độ |
| `map` | Hệ tọa độ bản đồ |
| `odom` | Hệ tọa độ odometry cục bộ |
| `base_link` | Hệ tọa độ gắn với thân robot |
| `base_scan` | Hệ tọa độ gắn với LiDAR |
| RViz | Công cụ hiển thị dữ liệu robot và tương tác với Nav2 |
| SLAM | Tạo bản đồ đồng thời ước lượng vị trí robot |
| Map server | Thành phần nạp hoặc lưu bản đồ lưới 2D |
| Localization | Ước lượng vị trí robot trên bản đồ đã có |
| Navigation2/Nav2 | Bộ công cụ lập đường và điều khiển robot tới mục tiêu |
| 2D Pose Estimate | Công cụ đặt vị trí và hướng ban đầu trong RViz |
| Nav2 Goal | Công cụ gửi vị trí và hướng đích cho robot |
| Footprint | Hình dạng/kích thước thân robot dùng khi tính va chạm |
| Costmap | Bản đồ chi phí dùng để biểu diễn vật cản và vùng an toàn |
| Workspace | Thư mục chứa source, kết quả build và môi trường ROS 2 |
| Package | Đơn vị tổ chức code, launch file và cấu hình trong ROS 2 |
| Launch file | File dùng để khởi động đồng thời nhiều node và cấu hình |
| Namespace | Tiền tố giúp tách topic/node của nhiều robot hoặc nhiều hệ thống |

## Ba khái niệm dễ nhầm

### Odometry không phải vị trí tuyệt đối

Odometry tính chuyển động từ bánh xe và có thể trôi theo thời gian. SLAM hoặc localization dùng thêm LiDAR để hiệu chỉnh vị trí tương đối với môi trường.

### Bản đồ không phải dữ liệu LiDAR trực tiếp

`/scan` là dữ liệu cảm biến tại thời điểm hiện tại. Bản đồ là kết quả thuật toán tổng hợp nhiều lần quét và chuyển động của robot.

### RViz không phải bộ điều khiển robot

RViz hiển thị dữ liệu và cho phép gửi một số thao tác như Pose Estimate hoặc Nav2 Goal. Các node nền vẫn thực hiện SLAM, định vị và điều khiển.
