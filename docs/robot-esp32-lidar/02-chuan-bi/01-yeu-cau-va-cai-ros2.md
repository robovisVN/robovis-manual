# Cài đặt trên Ubuntu 22.04

!!! tip "Dành cho người mới"
    Nếu chưa quen Ubuntu, xem [series Ubuntu cơ bản](../../ubuntu-co-ban/index.md). Riêng thao tác nhập và dừng lệnh có trong bài [Làm quen với Terminal](../../ubuntu-co-ban/04-terminal.md).

Hướng dẫn này dành cho máy tính đã chạy **Ubuntu 22.04 LTS**. Nếu đang dùng Windows, hãy mở [hướng dẫn máy ảo Ubuntu](04-windows-may-ao-ubuntu.md); bản máy ảo được cung cấp đã chuẩn bị sẵn ROS 2 và workspace.

## Yêu cầu máy tính

| Hạng mục | Tối thiểu | Khuyến nghị |
| --- | --- | --- |
| RAM | 8 GB | 16 GB nếu cần build thường xuyên |
| Dung lượng trống | 30 GB | 50 GB trở lên |
| Kết nối | Wi-Fi hoạt động | Có thể chuyển giữa Internet và Wi-Fi robot |

Phần mềm bàn giao đã được hướng dẫn và thử với ROS 2 Humble trên Ubuntu 22.04. Các phiên bản Ubuntu hoặc ROS 2 khác cần kiểm tra lại khả năng tương thích.

## Chuẩn bị trước khi cài

1. Kết nối máy tính với Internet và tải hai thư mục `robot_ws`, `slam_toolbox_ws` do ROBOVIS cung cấp. Nếu nhận tệp ZIP, giải nén trước khi build.
2. Đảm bảo tài khoản có thể dùng `sudo`. Cắm nguồn cho laptop nếu quá trình cài hoặc build kéo dài.
3. Chưa chuyển sang Wi-Fi robot: mạng do robot phát có thể không cung cấp Internet.

## Cài ROS 2 Humble

Làm theo [hướng dẫn cài ROS 2 Humble bằng gói Debian trên Ubuntu 22.04](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html). Cài bản **Desktop** và các công cụ phát triển được yêu cầu trong hướng dẫn chính thức. Sau khi cài, mở Terminal:

```bash
source /opt/ros/humble/setup.bash
ros2 --help
printenv ROS_DISTRO
```

`ROS_DISTRO` phải hiển thị `humble` và lệnh `ros2` phải chạy được. Nếu máy đã được ROBOVIS cài ROS 2, chỉ cần kiểm tra các lệnh này.

Tiếp theo: [đặt và build workspace](02-cai-dat-workspace.md), rồi [kết nối Wi-Fi robot](03-cau-hinh-wifi.md).
