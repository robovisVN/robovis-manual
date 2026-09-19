# Đánh giá chất lượng bản đồ

Một bản đồ lưu thành công chưa chắc đã đủ tốt để điều hướng. Hãy đánh giá trước khi dùng với Nav2.

## Tiêu chí bản đồ đạt

| Tiêu chí | Đạt | Cần quét lại hoặc bổ sung |
| --- | --- | --- |
| Tường | Liền và đúng hình dạng thực tế | Đứt đoạn hoặc có nhiều lớp song song |
| Góc phòng | Rõ, không méo mạnh | Cong, lệch hoặc bị kéo dài |
| Cửa và hành lang | Khoảng trống đúng vị trí | Bị che kín hoặc quá hẹp |
| Vòng di chuyển | Quay lại điểm cũ vẫn khớp | Bản đồ tách thành hai vùng lệch nhau |
| Khu vực cần chạy | Có đủ lối và vị trí đích | Thiếu đoạn hoặc có vùng chưa quét |
| Vùng trống | Đủ rộng cho thân robot | Chỉ vừa điểm LiDAR nhưng không đủ robot đi qua |

## Dấu hiệu odometry không tốt

- Robot đi thẳng nhưng bản đồ cong dần.
- Sau một vòng, vị trí mới không trùng điểm xuất phát.
- Tường bị nhân đôi sau khi quay.
- Bản đồ xoay hoặc dịch chuyển đột ngột.

Trong trường hợp này:

1. Giảm tốc độ.
2. Tránh quay tại chỗ quá nhanh.
3. Kiểm tra bánh xe có trượt không.
4. Kiểm tra `/odom` khi chạy thẳng và quay.
5. Tạo lại bản đồ từ đầu nếu lỗi đã lớn.

## Chọn môi trường tạo bản đồ

Môi trường dễ tạo bản đồ thường có:

- Nhiều tường, góc và vật cố định.
- Ít kính hoặc gương lớn.
- Nền phẳng, bánh xe không trượt.
- Không có nhiều người hoặc đồ vật di chuyển.

Môi trường khó thường là phòng trống lớn, hành lang dài giống nhau, nhiều kính hoặc khu vực liên tục thay đổi.

## Thử trước khi sử dụng chính thức

1. Chạy Navigation trên một đích gần.
2. Kiểm tra robot có định vị đúng sau khi quay không.
3. Gửi đích ở vài hướng khác nhau.
4. Hủy mục tiêu và đặt lại vị trí để kiểm tra khả năng phục hồi.
5. Chỉ dùng bản đồ cho thử nghiệm dài hơn khi các lần chạy ngắn ổn định.
