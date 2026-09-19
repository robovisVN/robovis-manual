# Lỗi LiDAR, SLAM và Navigation

## Không có dữ liệu LiDAR

```bash
ros2 topic list | grep scan
ros2 topic hz /scan
ros2 topic echo /scan --once
```

Nếu không có `/scan`:

- Kiểm tra LiDAR có được cấp nguồn và quay không.
- Kiểm tra log Terminal bringup.
- Kiểm tra topic có namespace hoặc tên khác không.
- Khởi động lại robot sau khi đã dừng bringup.

## Có `/scan` nhưng RViz không hiển thị

Kiểm tra:

- Display LaserScan đã chọn đúng topic chưa.
- Fixed Frame có hợp lệ không.
- `header.frame_id` của `/scan` có TF nối tới Fixed Frame không.
- RViz có báo `No transform` không.

## Odometry không thay đổi

```bash
ros2 topic echo /odom
```

Điều khiển robot ở tốc độ thấp. Nếu robot chạy nhưng pose không thay đổi, dừng tạo bản đồ và kiểm tra encoder/kết nối dữ liệu.

## Bản đồ bị nhân đôi hoặc lệch

Nguyên nhân thường gặp:

- Robot đi quá nhanh.
- Quay gấp hoặc bánh xe trượt.
- Robot bị nhấc bằng tay.
- Odometry hai bánh không cân bằng.
- Môi trường có ít đặc trưng hoặc nhiều vật di chuyển.

Xử lý:

1. Dừng SLAM.
2. Đưa robot về vị trí khởi đầu bằng tay khi hệ thống đã dừng.
3. Giảm tốc độ.
4. Quét lại theo đường vòng kín.
5. Không tiếp tục dùng bản đồ đã sai rõ rệt.

## Navigation không lập đường

- Kiểm tra đã đặt **2D Pose Estimate** đúng chưa.
- Kiểm tra đích có nằm trong vùng trống trên bản đồ không.
- Kiểm tra bản đồ có bị che kín tại cửa/lối đi không.
- Kiểm tra robot có đủ khoảng trống theo footprint và vùng an toàn không.

## Robot định vị sai

1. Hủy mục tiêu.
2. Cho robot đứng yên.
3. Đặt lại vị trí bằng **2D Pose Estimate**.
4. Kéo đúng hướng đầu robot.
5. Chờ điểm LiDAR chồng khớp với tường.
6. Chỉ gửi mục tiêu mới sau khi vị trí đã đúng.

## Robot rung hoặc tiến gần vật cản

Hủy mục tiêu và dừng robot. Không tiếp tục tăng tốc hoặc thay đổi nhiều tham số Nav2 cùng lúc. Ghi lại video, ảnh RViz và log Terminal để kiểm tra tham số trên đúng workspace.
