# An toàn và giới hạn

## Trước khi bật robot

- Đặt robot trên sàn phẳng, khô và đủ ma sát.
- Kiểm tra bánh xe không bị kẹt bởi dây điện hoặc vật mềm.
- Bảo đảm khu vực thử không có bậc thang, mép bàn hoặc vật dễ vỡ.
- Kiểm tra pin và kết nối nguồn.
- Đặt robot cách người và vật cản một khoảng đủ để dừng.

## Trong khi vận hành

!!! warning "Luôn giám sát robot thật"
    Không chỉ quan sát RViz. Người vận hành phải nhìn trực tiếp robot và có khả năng dừng robot ngay khi chuyển động bất thường.

- Chạy tốc độ thấp trong lần thử đầu.
- Không đặt tay gần bánh xe khi robot đang được cấp nguồn.
- Không nhấc, kéo hoặc xoay robot bằng tay khi SLAM hoặc Navigation đang chạy.
- Không đồng thời gửi lệnh điều khiển tay và lệnh Navigation2.
- Hủy mục tiêu nếu robot rung, đi sai hướng hoặc tiến quá gần vật cản.

## Giới hạn của cảm biến

LiDAR có thể đo không ổn định với:

- Kính trong suốt.
- Gương và bề mặt phản xạ mạnh.
- Vật màu đen hấp thụ ánh sáng.
- Chân bàn quá mảnh.
- Vật nằm thấp hơn hoặc cao hơn mặt phẳng quét.

Robot không có cảm biến an toàn được chứng nhận. Tính năng tránh vật cản phụ thuộc vào chất lượng LiDAR, bản đồ và tham số Navigation2; không được dùng như lớp bảo vệ duy nhất cho người hoặc tài sản.

## Bảo vệ chương trình gốc

Không nạp chương trình khác, không chọn **Erase Flash** và không thay đổi firmware ESP32 nếu chưa có đúng firmware khôi phục do ROBOVIS cung cấp. Việc ghi firmware mới có thể làm mất chương trình và cấu hình gốc của robot.

## Dừng hệ thống đúng cách

1. Hủy mục tiêu Navigation nếu đang chạy.
2. Đưa vận tốc điều khiển tay về `0`.
3. Nhấn `Ctrl+C` trong Terminal SLAM hoặc Navigation.
4. Nhấn `Ctrl+C` trong Terminal bringup.
5. Đóng RViz và công cụ điều khiển.
6. Tắt nguồn robot.
