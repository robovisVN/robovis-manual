# Lưu và quản lý bản đồ

## Lưu bản đồ

Khi đã quét đủ khu vực, giữ SLAM đang chạy và mở Terminal mới:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/m_map
```

`m_map` là tên bản đồ. Có thể đổi thành tên khác không có khoảng trắng, ví dụ:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/phong_lab
```

## Kiểm tra file

```bash
ls -lh ~/m_map.yaml ~/m_map.pgm
```

Phải có đủ hai file:

| File | Vai trò |
| --- | --- |
| `m_map.yaml` | Thông tin độ phân giải, gốc tọa độ và đường dẫn ảnh |
| `m_map.pgm` | Ảnh lưới chiếm chỗ của bản đồ |

Không chỉ sao chép một file. File YAML tham chiếu tới file ảnh bản đồ.

## Quy tắc đặt tên

Nên dùng:

```text
phong_lab
tang_1
hanh_lang_a
map_2026_09_15
```

Tránh khoảng trắng, dấu tiếng Việt và ký tự đặc biệt trong tên file.

## Tổ chức nhiều bản đồ

Có thể tạo thư mục riêng:

```bash
mkdir -p ~/robot_maps
```

Sau đó lưu:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/robot_maps/phong_lab
```

Khi sao lưu, luôn giữ cặp `.yaml` và `.pgm` cùng nhau.

## Kiểm tra đường dẫn trong YAML

```bash
sed -n '1,10p' ~/m_map.yaml
```

Trường `image` phải trỏ tới đúng file `.pgm`. Nếu đổi tên file ảnh thủ công, cần cập nhật YAML tương ứng.

## Sau khi lưu

1. Kiểm tra đủ hai file.
2. Đưa vận tốc điều khiển về `0`.
3. Dừng Terminal SLAM bằng `Ctrl+C`.
4. Giữ bringup nếu chuyển ngay sang Navigation2.
