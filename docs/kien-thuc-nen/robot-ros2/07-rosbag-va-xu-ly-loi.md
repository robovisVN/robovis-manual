# Bài 12: Rosbag và bài thực hành tổng hợp

## 1. Mục tiêu

Chúng ta sẽ ghi hai topic của ví dụ xuyên suốt, phát lại dữ liệu cho node phân tích và lập một báo cáo kiểm tra. Bạn cần hoàn thành bài 4–7. Bài này dùng dữ liệu giả lập trên PC.

Rosbag ghi các message trên topic được chọn. Nó giúp xem lại một hiện tượng mà không cần lặp lại toàn bộ lần đo, nhưng không tự lưu mã nguồn, trạng thái phần cứng và mọi tệp cấu hình.

## 2. Chuẩn bị lần thử có thể đối chiếu

Nếu chưa có công cụ, cài `ros-humble-rosbag2` khi có Internet. Chạy lại `thuc_hanh.launch.py` của bài 7. Trong các Terminal mới, nạp ROS 2 và workspace thực hành.

Kiểm tra trước khi ghi:

```bash
ros2 topic list -t
ros2 param get /thuc_hanh/nguon_toc_do toc_do_co_so
ros2 param get /thuc_hanh/nguon_toc_do chu_ky
```

Ghi ra giấy giá trị parameter, thời điểm và tên đầy đủ của topic. Nếu YAML chưa đổi, tốc độ cơ sở là 0,25 m/s và chu kỳ 0,2 giây.

## 3. Ghi hai topic

Trong Terminal ghi dữ liệu:

```bash
mkdir -p ~/ros2_practice/bags
cd ~/ros2_practice/bags
ros2 bag record -o toc_do_lan_1 /thuc_hanh/toc_do_do /thuc_hanh/toc_do_cho_phep
```

Nếu `toc_do_lan_1` đã tồn tại, dùng tên mới. Giữ chương trình ghi chạy. Trong Terminal khác:

```bash
ros2 service call /thuc_hanh/cho_phep_du_lieu std_srvs/srv/SetBool '{data: true}'
```

Chờ khoảng 5 giây, gọi service với `data: false`. Chờ thêm khoảng 5 giây, sau đó `Ctrl+C` tại Terminal ghi để hoàn tất bag.

**Kết quả mong đợi:** topic gốc có dữ liệu trong toàn bộ lần ghi; topic sau cổng chỉ có mẫu trong khoảng được cho phép. Số mẫu thực tế phụ thuộc thời điểm discovery, thao tác và thời lượng, nên không yêu cầu đúng một con số cố định.

## 4. Đọc thông tin bag

```bash
ros2 bag info ~/ros2_practice/bags/toc_do_lan_1
```

Đọc thời lượng, danh sách topic, kiểu và số message. Thư mục bag có metadata và tệp dữ liệu theo định dạng lưu đã dùng; giữ cả thư mục khi sao chép.

Nếu topic có 0 message hoặc bị thiếu, xem nguồn có thật sự phát trong lúc ghi không. “Đã chạy lệnh record” chưa chứng minh đã ghi được mẫu có ích.

## 5. Phát lại để phân tích

Dừng launch thực hành để không trộn nguồn phát trực tiếp với dữ liệu phát lại. Mở Terminal nhận:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_practice_ws/install/setup.bash
ros2 run robovis_practice bo_nhan --ros-args -r __node:=phan_tich_bag -r toc_do_do:=/thuc_hanh/toc_do_do
```

Trong Terminal khác, nạp ROS 2 rồi chạy:

```bash
ros2 bag play ~/ros2_practice/bags/toc_do_lan_1 --topics /thuc_hanh/toc_do_do
```

Bộ nhận in lại các mẫu và trung bình. Hãy mở bộ nhận trước để giảm khả năng bỏ qua các mẫu đầu trong lúc discovery.

Thử thêm `--rate 0.5` để phát chậm. Nhịp nhận thay đổi, còn giá trị các mẫu vẫn là dữ liệu đã ghi. Nếu đồng thời có nguồn trực tiếp cùng topic, công cụ có thể nhận cả hai luồng và khiến kết quả khó giải thích.

## 6. Thời gian khi phát lại dữ liệu robot

Ví dụ số thực không có timestamp nên chưa bộc lộ vấn đề thời gian. Dữ liệu robot có thể chứa thời điểm đo và cần TF tương ứng. Phát lại một topic `/scan` riêng có thể chưa đủ để RViz hoặc SLAM xử lý.

Khi thiết kế lần ghi cho phân tích LiDAR, xem xét các nguồn cần thiết như `/scan`, `/odom`, `/tf`, `/tf_static`, cấu hình và nguồn thời gian. Transform tĩnh có chính sách lưu giữ cần phù hợp với bên ghi/nhận.

`ros2 bag play --clock` có thể cung cấp `/clock` cho các node dùng `use_sim_time`. Việc chọn thời gian mô phỏng phải nhất quán với toàn bộ quá trình phân tích, không bật ngẫu nhiên ở riêng một node rồi mong các timestamp tự khớp.

Một bag chứa topic lệnh có thể tác động tới phần cứng khi phát lại. Với bài phân tích, hãy chọn rõ các topic dữ liệu và hệ thống nhận được phép chạy.

## 7. Kiểm tra lỗi theo lớp

| Lớp | Cần chứng minh | Bằng chứng nên giữ |
| --- | --- | --- |
| Môi trường | Đúng ROS 2 và workspace | `ROS_DISTRO`, package prefix |
| Khởi động | Node thật sự hoạt động | Log và `node list` |
| Giao diện | Đúng tên, kiểu, QoS | `topic list -t`, `info --verbose` |
| Nội dung | Giá trị và thời điểm hợp lý | Message mẫu, tần số |
| Tọa độ | Có chuỗi TF phù hợp | Frame, nguồn phát, lỗi thời gian |
| Hành vi | Đúng mục tiêu của bài | Quan sát, số liệu, bag |

Khi build thất bại, bắt đầu từ dòng lỗi đầu tiên có ý nghĩa. Một lỗi import có thể dẫn tới hàng loạt thông báo sau đó; không nên sửa tất cả thông báo phụ như những lỗi độc lập.

## 8. Bài thực hành tổng hợp

Tự hoàn thành các yêu cầu:

1. Đặt tốc độ cơ sở 0,30 m/s, chu kỳ 0,1 giây bằng YAML.
2. Chạy ba node bằng một launch; xác nhận gần 10 Hz ở topic gốc.
3. Bật cổng bằng client hoặc CLI, nhận một mẫu topic sau cổng.
4. Ghi một lần bật/tắt, giải thích chênh lệch số mẫu giữa hai topic.
5. Dừng nguồn trực tiếp, phát lại bag cho node nhận và đối chiếu giá trị.

### Mẫu báo cáo

| Nội dung | Ghi lại |
| --- | --- |
| Môi trường | Ubuntu, ROS 2, workspace |
| Lệnh khởi động | Launch và parameter |
| Luồng dữ liệu | Node nguồn → topic → node nhận |
| Kết quả | Tần số, mẫu điển hình, trạng thái service |
| Hiện tượng lỗi | Thời điểm, log, cách tái hiện |
| Tệp đính kèm | YAML, phiên bản mã và thư mục bag |

Bạn đạt mục tiêu khi có thể giải thích từng bước bằng dữ liệu, không chỉ cho biết “chương trình chạy được”. Sau đó, dùng [lộ trình Robot ESP32 LiDAR](../../robot-esp32-lidar/index.md) để chuyển từ nguồn giả lập sang robot thật.

Đọc thêm: [ROS 2 — Recording and playing back data](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html), [rosbag2](https://github.com/ros2/rosbag2/tree/humble).

[← Bài 11](03-rviz-va-tf.md) · [Về lộ trình](index.md) · [Thực hành Robot ESP32 LiDAR →](../../robot-esp32-lidar/index.md)
