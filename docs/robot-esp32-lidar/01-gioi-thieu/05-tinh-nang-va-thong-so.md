# Tính năng và thông số Robot ESP32 LiDAR

Dùng trang này để tra thông tin phần cứng, phần mềm và tìm bài thực hành tương ứng.

## Phần cứng và phần mềm

| Hạng mục | Thông tin |
| --- | --- |
| Bộ điều khiển trên robot | ESP32 |
| Chuyển động | Hai bánh chủ động, có encoder |
| Cảm biến khoảng cách | LiDAR 2D |
| Kết nối với máy tính | Wi-Fi |
| Hệ điều hành được hướng dẫn | Ubuntu 22.04 LTS |
| Phiên bản ROS 2 | Humble |
| Sử dụng trên Windows | Chạy Ubuntu trong VMware theo [hướng dẫn máy ảo](../02-chuan-bi/04-windows-may-ao-ubuntu.md) |

ESP32 đọc cảm biến và điều khiển động cơ. Máy tính chạy ROS 2, RViz, SLAM và Nav2. Sơ đồ kết nối nằm trong bài [Kiến trúc hệ thống](02-kien-truc-he-thong.md).

## Các bài thực hành

| Bạn muốn làm gì? | Bài hướng dẫn |
| --- | --- |
| Điều khiển tiến, lùi và quay | [Điều khiển bằng tay](../03-van-hanh/03-dieu-khien-bang-tay.md) |
| Xem khoảng cách do LiDAR đo | [Kiểm tra LiDAR](../05-lidar-slam-navigation/01-kiem-tra-lidar.md) |
| Xem robot và dữ liệu trên màn hình | [RViz và TF](../04-ros2-co-ban/03-rviz-va-tf.md) |
| Tạo bản đồ khu vực | [Tạo bản đồ SLAM](../05-lidar-slam-navigation/02-tao-ban-do-slam.md) |
| Lưu bản đồ để dùng lại | [Lưu bản đồ](../05-lidar-slam-navigation/03-luu-va-quan-ly-ban-do.md) |
| Cho robot tự đi đến điểm đã chọn | [Điều hướng bằng Nav2](../05-lidar-slam-navigation/04-dieu-huong-nav2.md) |

## Kết nối Wi-Fi mặc định

| Thông tin | Giá trị |
| --- | --- |
| Tên Wi-Fi | `ESP32_SLAM` hoặc `ESP SLAM`, tùy firmware |
| IP robot | `192.168.4.1` |
| IP Ubuntu theo cấu hình mặc định | `192.168.4.99` |

Làm theo bài [Wi-Fi mặc định](../02-chuan-bi/03-cau-hinh-wifi.md) để cấu hình các địa chỉ trên.

Khi dùng Wi-Fi của phòng học hoặc gia đình, làm theo bài riêng [Sử dụng Wi-Fi ngoài](../02-chuan-bi/05-su-dung-wifi-ngoai.md). Khi đó, IP robot và máy tính có thể khác bảng này. Bài Wi-Fi ngoài cũng có phần dành cho phiên bản lắp thêm ESP32-CAM.

## Các thông số chưa có số liệu

Tài liệu hiện tại chưa xác định kích thước, tải trọng, tốc độ tối đa, thời gian dùng pin và tầm đo cụ thể của LiDAR. Các giá trị này cần được bổ sung theo đúng phiên bản phần cứng.
