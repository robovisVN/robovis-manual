# Bài 12: Rosbag và bài thực hành tổng hợp

Khi một luồng dữ liệu chỉ xuất hiện trong vài giây, chúng ta có thể chưa kịp đọc hết các giá trị hoặc nhận ra thời điểm bất thường. Nếu phải chạy lại toàn bộ hệ thống mỗi lần muốn kiểm tra, việc đối chiếu sẽ mất nhiều thao tác.

Rosbag giúp lưu các message để phát lại cho công cụ phân tích. Trong bài cuối, chúng ta sẽ ghi ví dụ tốc độ đã xây dựng, quan sát lại dữ liệu và lập báo cáo giải thích kết quả của một lần thử.

## 1. Mục tiêu

Chúng ta sẽ ghi hai topic của ví dụ xuyên suốt, phát lại dữ liệu cho node phân tích và lập một báo cáo kiểm tra. Bạn cần hoàn thành bài 4–7. Bài này dùng dữ liệu giả lập trên PC.

**Rosbag** ghi lại các message trên những topic được chọn để chúng ta xem hoặc xử lý lại sau. Dữ liệu ghi được phản ánh các message mà công cụ đã nhận trong lần thử; để hiểu đầy đủ điều kiện tạo ra chúng, chúng ta còn cần lưu mã nguồn, cấu hình và thông tin vận hành liên quan.

## 2. Chuẩn bị lần thử có thể đối chiếu

Nếu chưa có công cụ, cài `ros-humble-rosbag2` khi có Internet. Chạy lại `thuc_hanh.launch.py` của bài 7. Trong các Terminal mới, nạp ROS 2 và workspace thực hành.

Một lần ghi sẽ dễ giải thích hơn nếu chúng ta biết nguồn nào đang chạy và dùng cấu hình nào. Trước khi bắt đầu, kiểm tra tên topic cùng các parameter của bên phát:

```bash
ros2 topic list -t
ros2 param get /thuc_hanh/nguon_toc_do toc_do_co_so
ros2 param get /thuc_hanh/nguon_toc_do chu_ky
```

Hãy ghi lại giá trị parameter, thời điểm và tên đầy đủ của các topic để có dữ liệu đối chiếu sau khi phát lại. Nếu giữ nguyên YAML của bài 7, tốc độ cơ sở là 0,25 m/s và chu kỳ 0,2 giây.

## 3. Ghi hai topic

Chúng ta sẽ ghi cả topic gốc và topic sau cổng. Khi bật, tắt cổng trong cùng lần ghi, số mẫu của hai kênh sẽ giúp quan sát tác dụng của service. Mở Terminal ghi dữ liệu và chạy:

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

Trong kết quả, chúng ta đọc thời lượng, tên topic, kiểu dữ liệu và số message để xác nhận lần ghi có nội dung cần dùng. Thư mục bag chứa cả metadata, tức thông tin mô tả lần ghi, và tệp dữ liệu theo định dạng lưu đang sử dụng. Khi sao chép, hãy giữ cả thư mục để công cụ còn đọc được đầy đủ.

Nếu topic có 0 message hoặc bị thiếu, xem nguồn có thật sự phát trong lúc ghi không. “Đã chạy lệnh record” chưa chứng minh đã ghi được mẫu có ích.

## 5. Phát lại để phân tích

Để kiểm tra dữ liệu đã lưu, chúng ta cho bag thay vai trò nguồn phát và dùng lại node nhận của bài 4. Trước tiên, dừng launch thực hành để hai nguồn trực tiếp và phát lại không cùng gửi trên một topic. Sau đó mở Terminal nhận:

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

Sau lần phát đầu, bạn có thể thử thêm `--rate 0.5` để quan sát chậm hơn. Giá trị các mẫu vẫn lấy từ dữ liệu đã ghi, trong khi nhịp nhận thay đổi. Nếu vẫn có nguồn trực tiếp cùng topic, bên nhận có thể thấy dữ liệu từ cả hai nguồn, khiến chúng ta khó xác định mẫu nào thuộc lần thử đang phân tích.

## 6. Thời gian khi phát lại dữ liệu robot

Ví dụ tốc độ dùng một số thực không có timestamp. Với dữ liệu robot, mỗi phép đo có thể mang thời điểm và frame riêng, nên chương trình xử lý còn cần TF tương ứng. Chẳng hạn, phát lại riêng `/scan` có thể cung cấp các khoảng cách nhưng vẫn thiếu quan hệ tọa độ để RViz hoặc SLAM đặt chúng vào đúng vị trí.

Khi thiết kế lần ghi cho phân tích LiDAR, xem xét các nguồn cần thiết như `/scan`, `/odom`, `/tf`, `/tf_static`, cấu hình và nguồn thời gian. Transform tĩnh có chính sách lưu giữ cần phù hợp với bên ghi/nhận.

`ros2 bag play --clock` có thể cung cấp `/clock` cho các node dùng `use_sim_time`. Việc chọn thời gian mô phỏng phải nhất quán với toàn bộ quá trình phân tích, không bật ngẫu nhiên ở riêng một node rồi mong các timestamp tự khớp.

Một bag chứa topic lệnh có thể tác động tới phần cứng khi phát lại. Với bài phân tích, hãy chọn rõ các topic dữ liệu và hệ thống nhận được phép chạy.

## 7. Kiểm tra lỗi theo lớp

Đến đây, chúng ta đã gặp nhiều thành phần có thể ảnh hưởng đến kết quả: môi trường, node, giao diện, dữ liệu và TF. Khi một lần thử chưa đạt, hãy lần theo các lớp này để tìm phần đầu tiên chưa có bằng chứng hoạt động đúng.

| Lớp | Cần chứng minh | Bằng chứng nên giữ |
| --- | --- | --- |
| Môi trường | Đúng ROS 2 và workspace | `ROS_DISTRO`, package prefix |
| Khởi động | Node thật sự hoạt động | Log và `node list` |
| Giao diện | Đúng tên, kiểu, QoS | `topic list -t`, `info --verbose` |
| Nội dung | Giá trị và thời điểm hợp lý | Message mẫu, tần số |
| Tọa độ | Có chuỗi TF phù hợp | Frame, nguồn phát, lỗi thời gian |
| Hành vi | Đúng mục tiêu của bài | Quan sát, số liệu, bag |

Khi build thất bại, bắt đầu từ dòng lỗi đầu tiên có ý nghĩa. Một lỗi import có thể dẫn tới hàng loạt thông báo sau đó; không nên sửa tất cả thông báo phụ như những lỗi độc lập.

## 8. Mẫu báo cáo

| Nội dung | Ghi lại |
| --- | --- |
| Môi trường | Ubuntu, ROS 2, workspace |
| Lệnh khởi động | Launch và parameter |
| Luồng dữ liệu | Node nguồn → topic → node nhận |
| Kết quả | Tần số, mẫu điển hình, trạng thái service |
| Hiện tượng lỗi | Thời điểm, log, cách tái hiện |
| Tệp đính kèm | YAML, phiên bản mã và thư mục bag |

Báo cáo cần đi cùng dữ liệu và điều kiện của lần ghi. Dùng [lộ trình Robot ESP32 LiDAR](../../robot-esp32-lidar/index.md) để chuyển từ nguồn giả lập sang robot thật.

Đọc thêm: [ROS 2 — Recording and playing back data](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html), [rosbag2](https://github.com/ros2/rosbag2/tree/humble).

## 9. Tổng kết

Qua series, chúng ta đã đi từ quan sát node có sẵn đến tự xây dựng, cấu hình và kiểm tra một luồng dữ liệu. Rosbag bổ sung khả năng lưu và phát lại message để phân tích, còn báo cáo ghi rõ điều kiện và kết quả của lần thử. Khi chuyển sang Robot ESP32 LiDAR, chúng ta tiếp tục dùng cách lần theo từng nguồn dữ liệu này cùng cấu hình được bàn giao cho sản phẩm.

[← Bài 11](03-rviz-va-tf.md) · [Về lộ trình](index.md) · [Thực hành Robot ESP32 LiDAR →](../../robot-esp32-lidar/index.md)
