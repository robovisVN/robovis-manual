# Bài 8: Động học robot hai bánh và odometry

## 1. Mục tiêu và giả thiết

Chúng ta sẽ liên hệ vận tốc hai bánh với vận tốc thân robot và tính một bước odometry từ encoder. Bài tính dùng mô hình **dẫn động vi sai**: hai bánh chủ động có trục song song, robot đổi hướng bằng chênh lệch tốc độ bánh.

Giả sử robot chạy trên mặt phẳng, bánh lăn không trượt, bán kính hai bánh bằng nhau và khoảng cách hai bánh đã biết. Robot nhiều bánh vẫn có thể được xấp xỉ bằng mô hình này, nhưng trượt khi quay có thể làm sai số lớn hơn.

## 2. Thống nhất đại lượng và đơn vị

| Ký hiệu | Ý nghĩa | Đơn vị |
| --- | --- | --- |
| `r` | Bán kính bánh xe | m |
| `L` | Khoảng cách giữa hai vệt bánh theo mô hình | m |
| `wL`, `wR` | Vận tốc góc bánh trái, phải | rad/s |
| `uL`, `uR` | Vận tốc dài của từng bánh | m/s |
| `v` | Vận tốc tiến của thân robot | m/s |
| `w` | Vận tốc quay quanh trục z | rad/s |

Quy ước bánh quay tiến có vận tốc dương. Với hệ trục x trước, y trái, z lên, `w` dương là quay trái khi nhìn từ trên xuống. Trước khi dùng công thức, phải hiệu chỉnh dấu encoder và chiều động cơ theo quy ước này.

## 3. Động học thuận: từ bánh tới thân

Vận tốc dài của một bánh bằng bán kính nhân vận tốc góc:

```text
uL = r × wL
uR = r × wR
v  = (uR + uL) / 2
w  = (uR - uL) / L
```

Khi hai bánh cùng tiến bằng nhau, hiệu bằng 0 nên robot đi thẳng. Khi bánh phải nhanh hơn, robot quay trái. Khi hai bánh bằng nhau về độ lớn nhưng trái dấu, trung bình bằng 0 nên mô hình cho chuyển động quay tại chỗ.

### Ví dụ có số

Cho `r = 0,035 m`, `L = 0,18 m`, bánh trái quay `4 rad/s`, bánh phải `6 rad/s`:

```text
uL = 0,035 × 4 = 0,140 m/s
uR = 0,035 × 6 = 0,210 m/s
v  = (0,210 + 0,140) / 2 = 0,175 m/s
w  = (0,210 - 0,140) / 0,18 ≈ 0,389 rad/s
```

Robot vừa tiến vừa quay trái. Đây là kết quả lý tưởng từ vận tốc bánh, chưa gồm trượt hay sai số đường kính.

## 4. Động học nghịch: từ lệnh thân tới bánh

Với lệnh mong muốn `v`, `w`:

```text
uL = v - w × L / 2
uR = v + w × L / 2
wL = uL / r
wR = uR / r
```

Ví dụ `v = 0,20 m/s`, `w = 0,50 rad/s` cho `uL = 0,155 m/s`, `uR = 0,245 m/s`. Bánh phải cần quay nhanh hơn bánh trái.

Các kết quả này là **giá trị đặt vận tốc bánh**, không phải PWM. Muốn bánh đáp ứng vận tốc đặt, bộ điều khiển còn cần đo phản hồi và điều chỉnh công suất. Cùng PWM không bảo đảm cùng vận tốc ở mọi tải.

Nếu một bánh vượt giới hạn, cắt riêng từng giá trị có thể đổi tỷ lệ quay của robot. Có thể cần giảm đồng thời hai giá trị theo cùng tỷ lệ để giữ độ cong đường đi, tùy thiết kế bộ điều khiển.

## 5. Từ xung encoder tới quãng đường

Gọi `N` là số đếm encoder hiệu dụng cho **một vòng bánh** theo cách đọc đang dùng. Nếu encoder gắn trên trục trước hộp số, cần tính thêm tỷ số truyền; nếu dùng nhiều sườn xung, số đếm cũng thay đổi.

```text
dsL = 2 × pi × r × dcountL / N
dsR = 2 × pi × r × dcountR / N
ds = (dsR + dsL) / 2
dtheta = (dsR - dsL) / L
```

Ví dụ `N = 600`, trong `0,1 s` bánh trái tăng 20 đếm, bánh phải tăng 30 đếm:

```text
dsL ≈ 0,00733 m
dsR ≈ 0,01100 m
ds ≈ 0,00916 m
dtheta ≈ 0,02036 rad
v ≈ 0,0916 m/s
w ≈ 0,2036 rad/s
```

Các thông số này chỉ dùng để tính ví dụ. Đọc thông số và hiệu chuẩn robot thực tế trước khi dùng chúng trong workspace sản phẩm.

## 6. Cập nhật pose trên mặt phẳng

Robot đang ở `(x, y, theta)`. Với bước dịch chuyển nhỏ, có thể dùng hướng giữa bước:

```text
x_moi = x + ds × cos(theta + dtheta / 2)
y_moi = y + ds × sin(theta + dtheta / 2)
theta_moi = theta + dtheta
```

Đây là phép xấp xỉ tích phân theo bước, phù hợp khi chu kỳ đủ nhỏ so với biến đổi chuyển động. Khoảng thời gian `dt` dùng để tính vận tốc cần lấy từ thời điểm đo thực tế và phải lớn hơn 0.

Có thể kiểm tra một bước bằng Python:

```python
from math import cos, pi, sin


def buoc_odometry(x, y, theta, dem_trai, dem_phai,
                  ban_kinh, khoang_banh, dem_moi_vong):
    if min(ban_kinh, khoang_banh, dem_moi_vong) <= 0:
        raise ValueError('Thong so hinh hoc va so dem phai duong')
    ds_trai = 2 * pi * ban_kinh * dem_trai / dem_moi_vong
    ds_phai = 2 * pi * ban_kinh * dem_phai / dem_moi_vong
    ds = (ds_trai + ds_phai) / 2
    dtheta = (ds_phai - ds_trai) / khoang_banh
    huong_giua = theta + dtheta / 2
    return (
        x + ds * cos(huong_giua),
        y + ds * sin(huong_giua),
        theta + dtheta,
    )
```

## 7. Vì sao odometry vẫn trôi?

Encoder đo chuyển động trục, còn ta quan tâm chuyển động của thân trên sàn. Bánh trượt, lốp biến dạng, đường kính lệch và mặt sàn không phẳng đều làm phép suy ra có sai số. Sai số tích lũy khi tích phân nhiều bước.

Do đó, odometry thường cung cấp chuyển động cục bộ liên tục. LiDAR hoặc các nguồn khác hỗ trợ định vị và hiệu chỉnh vị trí trên bản đồ. Bài TF sẽ giải thích cách chia vai trò cho `odom` và `map`.

## 8. Bài tập và kiểm tra thực tế

1. Tính `v`, `w` khi hai bánh quay `5 rad/s` và `-5 rad/s` với thông số ví dụ. Robot quay theo hướng nào?
2. Tăng đồng thời cả hai bán kính giả định thêm 10%. Những kết quả nào bị ảnh hưởng?
3. Khi robot đứng yên, encoder có đếm bất thường không? Khi đi thẳng, dấu hai bên có cùng quy ước không?
4. Khi thử robot thật, so sánh quãng đường đo trên sàn và odometry ở tốc độ thấp theo hướng dẫn sản phẩm. Không sửa PPR và bán kính cùng lúc vì sẽ khó xác định nguồn sai số.

Đọc thêm: [REP 103 — đơn vị và trục](https://www.ros.org/reps/rep-0103.html).

[← Bài 7](05-parameter-va-launch.md) · [Bài 9: ROS 2 qua mạng →](09-ros2-qua-mang.md)
