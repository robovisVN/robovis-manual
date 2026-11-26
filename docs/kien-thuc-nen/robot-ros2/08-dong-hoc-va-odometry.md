# Bài 8: Động học robot hai bánh và odometry

Trong các bài trước, chúng ta đã đọc lệnh vận tốc tiến và vận tốc quay của thân robot. Tuy nhiên, động cơ tác động lên từng bánh xe. Để robot đi thẳng hoặc quay theo yêu cầu, hệ thống cần chuyển đổi giữa chuyển động của thân và chuyển động hai bánh.

Chúng ta sẽ tìm hiểu mối liên hệ này bằng mô hình hai bánh, rồi sử dụng số đếm encoder để ước lượng một bước dịch chuyển của robot.

## 1. Mục tiêu và giả thiết

Bài tính sử dụng mô hình **dẫn động vi sai**: hai bánh chủ động có trục song song, robot đổi hướng nhờ chênh lệch tốc độ giữa chúng. Từ vận tốc hoặc số đếm của hai bánh, chúng ta sẽ tính chuyển động thân và một bước **odometry**, tức ước lượng chuyển động dựa trên dữ liệu đó.

Giả sử robot chạy trên mặt phẳng, bánh lăn không trượt, bán kính hai bánh bằng nhau và khoảng cách hai bánh đã biết. Robot nhiều bánh vẫn có thể được xấp xỉ bằng mô hình này, nhưng trượt khi quay có thể làm sai số lớn hơn.

## 2. Thống nhất đại lượng và đơn vị

Trước khi thay số vào công thức, chúng ta thống nhất ký hiệu và đơn vị. Bán kính hoặc khoảng cách bánh nhập theo milimét trong một công thức dùng mét sẽ làm kết quả sai dù phép tính đã thực hiện đúng.

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

Nếu biết bánh quay nhanh bao nhiêu và bán kính bánh, chúng ta tính được vận tốc dài tại vành bánh. Sau đó, trung bình và chênh lệch vận tốc hai bên cho biết vận tốc tiến và quay của thân:

```text
uL = r × wL
uR = r × wR
v  = (uR + uL) / 2
w  = (uR - uL) / L
```

Có thể đọc ý nghĩa công thức qua các tình huống quen thuộc. Nếu hai bánh cùng tiến bằng nhau, hiệu vận tốc bằng 0 và robot đi thẳng. Nếu bánh phải nhanh hơn, robot quay trái theo quy ước đã chọn. Khi hai bánh quay ngược chiều với cùng độ lớn, vận tốc tiến trung bình bằng 0, tạo chuyển động quay tại chỗ trong mô hình.

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

Ở chiều ngược lại, bộ điều khiển nhận lệnh mong muốn cho thân là `v` và `w`, rồi cần tìm vận tốc đặt cho từng bánh. Chúng ta sử dụng các quan hệ sau:

```text
uL = v - w × L / 2
uR = v + w × L / 2
wL = uL / r
wR = uR / r
```

Ví dụ `v = 0,20 m/s`, `w = 0,50 rad/s` cho `uL = 0,155 m/s`, `uR = 0,245 m/s`. Bánh phải cần quay nhanh hơn bánh trái.

Kết quả vừa tính là **giá trị đặt vận tốc bánh**. Để đạt giá trị đó, bộ điều khiển động cơ còn phải đọc phản hồi và điều chỉnh công suất, chẳng hạn thông qua PWM. Do tải và điều kiện vận hành có thể thay đổi, cùng một mức PWM chưa bảo đảm bánh luôn quay cùng vận tốc.

Nếu một bánh vượt giới hạn, cắt riêng từng giá trị có thể đổi tỷ lệ quay của robot. Có thể cần giảm đồng thời hai giá trị theo cùng tỷ lệ để giữ độ cong đường đi, tùy thiết kế bộ điều khiển.

## 5. Từ xung encoder tới quãng đường

Encoder cung cấp số đếm theo chuyển động trục. Để đổi số đếm thành quãng đường bánh, chúng ta cần biết `N`, số đếm hiệu dụng cho **một vòng bánh** với cách đọc đang dùng. Nếu encoder gắn trước hộp số, phải tính thêm tỷ số truyền; số sườn xung được đọc cũng ảnh hưởng đến `N`.

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

Khi đã biết quãng đường và góc quay trong một bước, chúng ta cần cập nhật pose, gồm vị trí và hướng của robot trên mặt phẳng. Nếu pose hiện tại là `(x, y, theta)`, có thể sử dụng hướng giữa bước để xấp xỉ vị trí mới khi bước dịch chuyển đủ nhỏ:

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

Các công thức trên suy ra chuyển động thân từ chuyển động bánh. Trong thực tế, encoder đo chuyển động trục, còn bánh có thể trượt hoặc biến dạng khi tiếp xúc với sàn. Sai lệch đường kính và bề mặt không phẳng cũng ảnh hưởng phép suy ra. Khi cộng dồn nhiều bước, những sai số này tích lũy khiến vị trí odometry lệch dần.

Do đó, odometry thường cung cấp chuyển động cục bộ liên tục. LiDAR hoặc các nguồn khác hỗ trợ định vị và hiệu chỉnh vị trí trên bản đồ. Bài TF sẽ giải thích cách chia vai trò cho `odom` và `map`.

Khi kiểm tra odometry trên robot thật, dùng tốc độ thấp theo hướng dẫn sản phẩm. Không sửa PPR và bán kính cùng lúc vì sẽ khó xác định nguồn sai số.

Đọc thêm: [REP 103 — đơn vị và trục](https://www.ros.org/reps/rep-0103.html).

## 8. Tổng kết { #9-tong-ket }

Động học thuận giúp suy ra vận tốc thân từ hai bánh; động học nghịch giúp tính vận tốc bánh từ lệnh chuyển động thân. Từ encoder, chúng ta còn ước lượng được quãng đường và cập nhật pose, với sai số phụ thuộc mô hình và điều kiện thực tế. Bài tiếp theo sẽ chuyển sang cách dữ liệu và lệnh đi giữa các máy qua mạng.

[← Bài 7](05-parameter-va-launch.md) · [Bài 9: ROS 2 qua mạng →](09-ros2-qua-mang.md)
