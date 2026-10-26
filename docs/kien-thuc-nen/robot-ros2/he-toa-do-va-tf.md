# Hệ tọa độ và TF từ đầu

**Mục tiêu:** giải thích được một tọa độ đang được đo từ đâu và vì sao dữ liệu có topic vẫn có thể không hiển thị trong RViz.

**Cần biết trước:** [lộ trình ROS 2](index.md), hiểu node/topic/message. Bài đầu làm trên giấy; phần quan sát RViz cần robot LiDAR đã được chuẩn bị và khởi động theo tài liệu sản phẩm.

## Một tọa độ luôn cần mốc

“Vật ở phía trước 1 m” chưa đủ: phía trước cảm biến hay phía trước thân robot? **Frame** là hệ tọa độ gồm một gốc và các trục. Cùng một vật có tọa độ khác nhau nếu đổi frame.

Quy ước phổ biến cho thân robot ROS: trục **x hướng trước**, **y hướng trái**, **z hướng lên**; chiều quay dương tuân theo quy tắc bàn tay phải. Với robot trên mặt phẳng, quay dương quanh z là quay ngược chiều kim đồng hồ khi nhìn từ trên xuống. Đơn vị thường dùng là m và radian; 180° tương ứng π radian. Camera có thể dùng optical frame với quy ước khác, không áp dụng trục thân robot cho mọi cảm biến. Xem [REP 103 – đơn vị và hệ tọa độ](https://www.ros.org/reps/rep-0103.html).

## TF biểu diễn quan hệ giữa các frame

**TF/tf2** là hệ thống lưu và tra cứu quan hệ vị trí, hướng giữa các frame theo thời gian. Một **transform** mô tả phép tịnh tiến và quay giữa hai frame. Tên topic `/scan` là tên kênh dữ liệu; `header.frame_id` trong message cho biết dữ liệu ấy gắn với frame nào. Hai tên này không phải cùng một khái niệm.

Quan hệ thường gặp ở robot di động:

```text
map → odom → base_link → frame của LiDAR
```

| Frame | Vai trò |
| --- | --- |
| `base_link` | Mốc gắn với thân robot |
| `odom` | Mốc chuyển động cục bộ, liên tục nhưng có thể trôi theo thời gian |
| `map` | Mốc bản đồ; quá trình định vị có thể hiệu chỉnh quan hệ với odom |

Trong tài liệu LiDAR hiện có, frame LiDAR được minh họa là `base_scan`; tên và vị trí thật phụ thuộc workspace. `map` chưa nhất thiết tồn tại khi chỉ chạy phần kiểm tra ban đầu. Xem [REP 105 – các frame của robot di động](https://www.ros.org/reps/rep-0105.html).

## Thực hành nhỏ trên giấy

Giả sử LiDAR nằm trước gốc `base_link` 0,10 m, cùng hướng trục, không có phép quay. LiDAR thấy một điểm ở `(1,00; 0; 0)` m trong frame của nó.

- Trong `base_link`, điểm đó ở `(1,10; 0; 0)` m.
- Nếu chỉ gắn nhãn điểm đó thành `base_link` mà không biến đổi tọa độ, vị trí bị lệch 0,10 m.

**Kết quả mong đợi:** bạn cộng được độ lệch khi trục cùng hướng và hiểu rằng đổi tên frame không thay thế phép biến đổi. Khi có góc quay, không chỉ cộng các tọa độ như ví dụ này.

## Quan sát trên robot, không tạo thêm transform thử

Theo [Khởi động và kiểm tra dữ liệu](../../robot-esp32-lidar/03-van-hanh/02-khoi-dong-va-kiem-tra.md) để có đúng môi trường, kết nối và các node. Bài này không gửi lệnh chuyển động; giữ robot ở trạng thái thử an toàn theo hướng dẫn sản phẩm.

1. Trong Terminal đã nạp môi trường ROS 2/workspace, dùng lệnh đọc dữ liệu trong [Các topic của robot](../../robot-esp32-lidar/04-ros2-co-ban/02-cac-topic-cua-robot.md), xem `header.frame_id` của LaserScan.
2. Mở cấu hình RViz theo [RViz và hệ tọa độ TF](../../robot-esp32-lidar/04-ros2-co-ban/03-rviz-va-tf.md). RViz là ứng dụng hiển thị, không tự tạo TF còn thiếu.
3. Thêm display TF, tìm frame của LiDAR và chuỗi nối về Fixed Frame (frame tham chiếu chính của RViz).
4. Với chế độ kiểm tra odometry, tài liệu dùng `odom`; khi chạy SLAM/định vị và đã có chuỗi TF tương ứng mới dùng `map`.

**Kết quả mong đợi:** dữ liệu LaserScan hiển thị khi RViz nhận được dữ liệu và tra được chuỗi transform hợp lệ tại thời điểm dữ liệu. Thấy topic có message chỉ xác nhận phần truyền dữ liệu, chưa xác nhận TF đầy đủ.

## Lỗi thường gặp

- `No transform`: kiểm tra frame thật, Fixed Frame, node cung cấp TF và thời gian; không đổi ngẫu nhiên các tên trong launch.
- Chọn `map` trước khi chạy thành phần tạo bản đồ/định vị: mốc này có thể chưa có.
- Gõ `/scan` vào Fixed Frame: đó thường là topic, không phải tên frame.
- Tự phát thêm transform để hết cảnh báo: có thể tạo quan hệ sai hoặc nhiều nguồn cùng công bố một quan hệ. Đối chiếu workspace trước.

Chi tiết hệ thống TF: [ROS 2 Humble – tf2](https://docs.ros.org/en/humble/Concepts/Intermediate/About-Tf2.html).

[← Lộ trình ROS 2](index.md) · [Tiếp: Thực hành Robot ESP32 LiDAR →](../../robot-esp32-lidar/index.md)
