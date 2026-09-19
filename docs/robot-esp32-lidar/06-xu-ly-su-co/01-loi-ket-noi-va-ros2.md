# Lỗi kết nối và ROS 2

## Quy tắc xử lý

Chỉ thay đổi một yếu tố mỗi lần. Kiểm tra theo thứ tự:

```text
Nguồn robot → Wi-Fi → IP/ping → môi trường ROS 2 → workspace → bringup → topic
```

## Không ping được robot

Chạy:

```bash
ip -4 addr
ping -c 4 192.168.4.1
```

Kiểm tra:

- Máy tính có đang kết nối đúng Wi-Fi robot không.
- Wi-Fi robot có tên `ESP32_SLAM` hoặc `ESP SLAM` không.
- IP máy tính có phải `192.168.4.99` không.
- Có thiết bị khác đang dùng trùng `192.168.4.99` không.
- Robot đã bật đủ 20–30 giây chưa.

## `ros2: command not found`

```bash
source /opt/ros/humble/setup.bash
printenv ROS_DISTRO
```

Nếu lệnh hoạt động sau khi source, kiểm tra lại dòng sau trong `~/.bashrc`:

```bash
source /opt/ros/humble/setup.bash
```

## `Package 'robot_bringup' not found`

```bash
cd ~/robot_ws
ls install/setup.bash
source ~/robot_ws/install/setup.bash
ros2 pkg prefix robot_bringup
```

Nếu không có `install/setup.bash`, workspace chưa build thành công.

## Build dừng hoặc máy bị treo

Với máy ít RAM:

```bash
cd ~/robot_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install --executor sequential
```

Gửi nội dung từ dòng lỗi đầu tiên nếu vẫn thất bại.

## Bringup lặp lỗi kết nối

1. Dừng tất cả phiên bringup bằng `Ctrl+C`.
2. Tắt và bật lại robot.
3. Kết nối lại Wi-Fi robot.
4. Ping lại `192.168.4.1`.
5. Chỉ khởi chạy một phiên bringup.

## Không thấy topic

```bash
printenv ROS_DOMAIN_ID
ros2 node list
ros2 topic list
```

Nếu hệ thống dùng `ROS_DOMAIN_ID`, các Terminal cần có cùng giá trị. Tài liệu bàn giao không quy định cố định là `10`. Nếu topic có namespace, sử dụng đúng tên đầy đủ.

## Bảng tra nhanh

| Hiện tượng | Kiểm tra đầu tiên |
| --- | --- |
| Không có Wi-Fi robot | Nguồn robot và thời gian khởi động |
| Có Wi-Fi nhưng không ping | IP tĩnh của máy tính |
| Ping được nhưng không có node | Bringup và môi trường workspace |
| Có node nhưng thiếu topic | Log bringup và tên namespace |
