# Cài đặt workspace trên Ubuntu

Hướng dẫn này áp dụng cho Ubuntu được cài trực tiếp trên PC/laptop. ROBOVIS cung cấp hai thư mục `slam_toolbox_ws` và `robot_ws`; không tạo lại các package bên trong. Nếu đang dùng máy ảo được bàn giao trên Windows, chuyển thẳng sang [kiểm tra kết nối](04-windows-may-ao-ubuntu.md).

## 1. Đặt hai workspace trong Home

Giải nén và di chuyển **cả hai** thư mục vào Home, rồi kiểm tra:

```bash
ls ~/slam_toolbox_ws/src
ls ~/robot_ws/src
```

Nếu một lệnh báo không có thư mục, kiểm tra lại chỗ giải nén. Không đổi tên `src` hoặc package bên trong.

## 2. Build `slam_toolbox_ws`

```bash
cd ~/slam_toolbox_ws
source /opt/ros/humble/setup.bash
colcon build --executor sequential
```

Chờ phần `Summary` kết thúc mà không có package `Failed`. Nếu thiếu thư viện, ghi lại **dòng lỗi đầu tiên** và kiểm tra gói phụ thuộc trước khi thử lại.

## 3. Build `robot_ws`

Mở Terminal mới hoặc tiếp tục Terminal hiện tại; nạp môi trường ROS 2 và workspace vừa build:

```bash
cd ~/robot_ws
source /opt/ros/humble/setup.bash
source ~/slam_toolbox_ws/install/setup.bash
colcon build --executor sequential
```

Nếu `slam_toolbox_ws` của bộ bàn giao chưa tạo `install/setup.bash`, cần xử lý lỗi build ở bước 2 trước. Với máy ít RAM, chế độ tuần tự giảm số tiến trình build đồng thời.

## 4. Nạp môi trường khi mở Terminal

Mở file cấu hình:

```bash
gedit ~/.bashrc
```

Thêm các dòng sau **một lần** ở cuối file và lưu bằng `Ctrl+S`:

```bash
source /opt/ros/humble/setup.bash
source ~/slam_toolbox_ws/install/setup.bash
source ~/robot_ws/install/setup.bash
unset ROS_LOCALHOST_ONLY
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

Đóng và mở lại Terminal. Tài liệu bàn giao Ubuntu không ấn định `ROS_DOMAIN_ID=10`; nếu hệ thống của bạn đã được cấu hình Domain ID riêng, giữ cùng một giá trị ở tất cả Terminal và không tự thay đổi khi chưa kiểm tra.

## 5. Kiểm tra các package

```bash
ros2 pkg prefix robot_bringup
ros2 pkg prefix robot_navigation
```

Mỗi lệnh phải tìm thấy package trong workspace được cung cấp. Nếu báo `package not found`, kiểm tra bước build và các dòng `source` trong `~/.bashrc`.

Tiếp theo: [kết nối Wi-Fi robot](03-cau-hinh-wifi.md), rồi [chạy thử lần đầu](../03-van-hanh/01-chay-thu-lan-dau.md).
