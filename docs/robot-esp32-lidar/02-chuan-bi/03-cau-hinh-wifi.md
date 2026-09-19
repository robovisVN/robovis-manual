# Cấu hình Wi-Fi robot

Sau khi đã cài ROS 2 và build workspace, hãy chuyển máy tính sang mạng Wi-Fi do robot phát.

## Thông số mặc định

| Trường | Giá trị |
| --- | --- |
| Tên Wi-Fi | `ESP32_SLAM` hoặc `ESP SLAM` tùy phiên bản |
| Mật khẩu | `12345678` |
| IP robot | `192.168.4.1` |
| IP máy tính | `192.168.4.99` |
| Netmask | `255.255.255.0` |
| Gateway | `192.168.4.1` |

## 1. Kết nối Wi-Fi

1. Bật nguồn robot.
2. Chờ khoảng 20–30 giây.
3. Nhấn biểu tượng mạng ở góc trên bên phải Ubuntu.
4. Chọn `ESP32_SLAM` hoặc `ESP SLAM`.
5. Nhập mật khẩu `12345678`.
6. Nếu Ubuntu báo mạng không có Internet, chọn tiếp tục giữ kết nối.

Việc mạng robot không có Internet là bình thường. Mạng này được dùng để trao đổi dữ liệu giữa robot và máy tính.

## 2. Đặt IP tĩnh cho máy tính

1. Mở **Settings → Wi-Fi**.
2. Nhấn biểu tượng bánh răng cạnh Wi-Fi robot.
3. Chọn thẻ **IPv4**.
4. Chọn **Manual**.
5. Nhập:
   - Address: `192.168.4.99`
   - Netmask: `255.255.255.0`
   - Gateway: `192.168.4.1`
6. Nhấn **Apply**.
7. Tắt rồi kết nối lại Wi-Fi robot.

Không đặt máy tính thành `192.168.4.1` vì địa chỉ đó đã được robot sử dụng.

## 3. Kiểm tra kết nối

```bash
ip -4 addr
ping -c 4 192.168.4.1
```

Chỉ tiếp tục khi:

- Máy tính có địa chỉ `192.168.4.99` trên card Wi-Fi đang dùng.
- Lệnh ping nhận phản hồi từ `192.168.4.1`.

!!! warning
    Khi ping chưa thành công, không sửa ROS 2, SLAM hoặc Nav2. Hãy xử lý lớp mạng trước.

## Khi dùng Wi-Fi ngoài

Nếu muốn chuyển robot sang mạng của gia đình, trường học hoặc phòng lab, làm theo [hướng dẫn sử dụng Wi-Fi ngoài](05-su-dung-wifi-ngoai.md). Khi dùng mạng ngoài, IP robot và PC có thể khác cấu hình mặc định trên trang này.

