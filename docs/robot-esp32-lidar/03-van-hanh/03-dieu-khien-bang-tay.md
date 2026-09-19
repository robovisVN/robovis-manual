# Điều khiển robot bằng tay

## Mở giao diện điều khiển

Giữ bringup đang chạy. Mở Terminal mới:

```bash
ros2 run rqt_robot_steering rqt_robot_steering
```

Giao diện cho phép điều chỉnh:

- **Linear velocity:** vận tốc tiến hoặc lùi.
- **Angular velocity:** vận tốc quay.

## Giá trị bắt đầu

| Đại lượng | Giá trị tham khảo |
| --- | --- |
| Linear velocity | `0.02` đến `0.06 m/s` |
| Angular velocity | Tăng từ thấp; một số cấu hình cần gần `2 rad/s` mới quay rõ |
| Dừng | Đưa cả hai giá trị về `0` |

Các giá trị trên chỉ là điểm bắt đầu. Luôn tăng dần và quan sát robot thật.

## Thứ tự thử an toàn

1. Nâng thanh Linear lên một giá trị dương nhỏ để thử tiến.
2. Đưa Linear về `0`.
3. Hạ Linear xuống một giá trị âm nhỏ để thử lùi.
4. Đưa Linear về `0`.
5. Thử Angular dương và âm ở giá trị nhỏ.
6. Đưa tất cả về `0` khi kết thúc.

## Nếu robot đi sai hướng

- Đưa vận tốc về `0` ngay.
- Không tiếp tục tạo bản đồ.
- Ghi lại bánh nào quay sai hoặc hướng nào bị đảo.
- Liên hệ ROBOVIS nếu firmware hoặc cấu hình động cơ chưa đúng với phiên bản phần cứng.

## Không điều khiển đồng thời

Không dùng `rqt_robot_steering` để gửi vận tốc trong lúc Navigation2 đang điều khiển robot. Hai nguồn cùng ghi vào `/cmd_vel` có thể làm chuyển động không đúng dự kiến.
