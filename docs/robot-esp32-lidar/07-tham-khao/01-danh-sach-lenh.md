# Danh sách lệnh

## Mạng và môi trường

| Mục đích | Lệnh |
| --- | --- |
| Xem địa chỉ IP | `ip -4 addr` |
| Kiểm tra robot | `ping -c 4 192.168.4.1` |
| Xem bản ROS | `printenv ROS_DISTRO` |
| Xem Domain ID | `printenv ROS_DOMAIN_ID` |
| Nạp ROS 2 tạm thời | `source /opt/ros/humble/setup.bash` |
| Nạp SLAM workspace tạm thời | `source ~/slam_toolbox_ws/install/setup.bash` |
| Nạp robot workspace tạm thời | `source ~/robot_ws/install/setup.bash` |

## Workspace

| Mục đích | Lệnh |
| --- | --- |
| Vào workspace | `cd ~/robot_ws` |
| Xem package nguồn | `ls src` |
| Build tuần tự | `colcon build --symlink-install --executor sequential` |
| Kiểm tra package bringup | `ros2 pkg prefix robot_bringup` |
| Kiểm tra package navigation | `ros2 pkg prefix robot_navigation` |

## Khởi động và điều khiển

| Mục đích | Lệnh |
| --- | --- |
| Khởi động robot | `ros2 launch robot_bringup robot_bringup.launch.py` |
| Điều khiển bằng tay | `ros2 run rqt_robot_steering rqt_robot_steering` |
| Khởi động SLAM | `ros2 launch robot_bringup robot_slam.launch.py` |
| Lưu bản đồ | `ros2 run nav2_map_server map_saver_cli -f ~/m_map` |
| Chạy Navigation | `ros2 launch robot_navigation navigation2.launch.py map:=$HOME/m_map.yaml` |

## Kiểm tra ROS 2

| Mục đích | Lệnh |
| --- | --- |
| Liệt kê node | `ros2 node list` |
| Liệt kê topic | `ros2 topic list` |
| Liệt kê topic và kiểu | `ros2 topic list -t` |
| Thông tin `/scan` | `ros2 topic info /scan` |
| Đo tần số LiDAR | `ros2 topic hz /scan` |
| Đo tần số odometry | `ros2 topic hz /odom` |
| Xem một message LiDAR | `ros2 topic echo /scan --once` |
| Xem odometry | `ros2 topic echo /odom` |
| Xem publisher `/cmd_vel` | `ros2 topic info /cmd_vel --verbose` |

## File bản đồ

| Mục đích | Lệnh |
| --- | --- |
| Kiểm tra cặp file | `ls -lh ~/m_map.yaml ~/m_map.pgm` |
| Tạo thư mục bản đồ | `mkdir -p ~/robot_maps` |
| Xem nội dung YAML | `sed -n '1,10p' ~/m_map.yaml` |

## Dừng lệnh

Nhấn:

```text
Ctrl+C
```

trong đúng Terminal đang chạy tiến trình. Luôn đưa vận tốc về `0` hoặc hủy mục tiêu trước khi dừng bringup.
