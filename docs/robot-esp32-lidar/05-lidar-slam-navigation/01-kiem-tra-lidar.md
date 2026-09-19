# Kiểm tra dữ liệu LiDAR

Chỉ bắt đầu SLAM khi LiDAR hoạt động ổn định.

## 1. Kiểm tra topic

Sau khi chạy bringup:

```bash
ros2 topic list | grep scan
```

Nếu thấy `/scan`, kiểm tra kiểu message:

```bash
ros2 topic type /scan
```

Kết quả mong đợi:

```text
sensor_msgs/msg/LaserScan
```

## 2. Kiểm tra tần số

```bash
ros2 topic hz /scan
```

Dữ liệu phải cập nhật liên tục. Nếu tần số hiện một lúc rồi dừng, kiểm tra nguồn robot, kết nối Wi-Fi và log bringup.

## 3. Kiểm tra nội dung

```bash
ros2 topic echo /scan --once
```

Kiểm tra:

- `header.frame_id` không rỗng.
- `ranges` có dữ liệu.
- Phần lớn giá trị không phải `0`, `inf` hoặc `nan` trong môi trường có tường/vật cản.
- Khoảng cách thay đổi khi đưa một tấm bìa lớn tới gần LiDAR.

Không đưa tay hoặc vật vào phần quay của LiDAR.

## 4. Kiểm tra trong RViz

1. Mở RViz bằng launch file ROBOVIS hoặc lệnh phù hợp trong workspace.
2. Đặt Fixed Frame là `odom` hoặc frame hợp lệ của hệ thống.
3. Thêm display **LaserScan**.
4. Chọn topic `/scan`.
5. Đặt robot đứng yên và so sánh hình điểm quét với tường/vật thật.

## Dữ liệu đạt yêu cầu khi

- Quét liên tục, không dừng từng đoạn dài.
- Vật lớn xuất hiện đúng phía tương đối quanh robot.
- Khi robot đứng yên, đám điểm không xoay hoặc trôi mạnh.
- Không có vòng tròn hoặc vệt nhiễu cố định do bộ phận thân robot che LiDAR.

Nếu hướng trái/phải hoặc trước/sau bị đảo, không sửa ngẫu nhiên trong RViz. Ghi lại hiện tượng và kiểm tra cấu hình góc LiDAR của đúng phiên bản firmware/bringup.
