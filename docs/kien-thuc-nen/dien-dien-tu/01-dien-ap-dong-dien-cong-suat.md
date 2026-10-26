# Điện áp, dòng điện và công suất: hiểu để chọn nguồn

**Mục tiêu:** đọc được nhãn nguồn DC và biết thông tin nào phải kiểm tra trước khi cấp nguồn cho mạch.

**Cần biết trước:** chưa cần lập trình. Bài này tính trên giấy, không yêu cầu nối pin hoặc động cơ.

## Ba đại lượng khác nhau

**DC** là điện một chiều. Trong một mạch DC đơn giản:

| Đại lượng | Ý nghĩa | Đơn vị |
| --- | --- | --- |
| Điện áp `U` | Chênh lệch điện thế giữa hai điểm, chẳng hạn hai cực nguồn | V, volt |
| Dòng điện `I` | Lượng điện tích đi qua một vị trí trong mỗi giây khi có đường dẫn kín | A, ampere; 1 A = 1000 mA |
| Công suất `P` | Tốc độ tiêu thụ hoặc chuyển đổi năng lượng | W, watt |

Với tải DC ổn định, `P = U × I`. Một tải dùng 5 V và tiêu thụ 0,2 A có công suất điện vào khoảng `5 × 0,2 = 1 W`.

**Tải** là phần dùng điện, như cảm biến hoặc động cơ. Dòng thực tế phụ thuộc tải và trạng thái hoạt động. Nguồn ghi **5 V – 2 A** thường có nghĩa điện áp danh định 5 V, khả năng cấp dòng tối đa theo điều kiện nhà sản xuất là 2 A; nó không ép mọi tải nhận 2 A. Nguồn sai điện áp vẫn có thể làm hỏng mạch dù định mức dòng rất lớn.

## Điện trở và mạch kín

**Điện trở** cản dòng điện, đơn vị Ω (ohm). Với điện trở thuần, định luật Ohm là `I = U / R`. Giả sử nối điện trở 1 kΩ giữa nguồn DC 5 V và GND, dòng lý tưởng là `5 / 1000 = 0,005 A = 5 mA`. Không áp dụng phép chia này để suy ra dòng của động cơ đang quay hoặc cả bo mạch.

Đường dẫn từ dương nguồn qua tải về âm nguồn phải kín để dòng duy trì. **Ngắn mạch** là đường nối có điện trở rất nhỏ giữa hai cực nguồn; dòng có thể tăng cao và làm nóng dây, nguồn hoặc linh kiện.

## Chọn nguồn theo thứ tự nào?

1. Xác định **điện áp cho phép tại đúng đầu vào** trên sơ đồ/datasheet (bảng thông số của thiết bị). Điện áp cổng USB, chân VIN và GPIO là những thông tin khác nhau.
2. Kiểm tra cực dương/âm, loại đầu nối và bộ chuyển đổi điện áp nếu có.
3. Tính tổng dòng các tải cùng nguồn ở trạng thái sử dụng lớn nhất. Với động cơ, xét cả dòng khởi động hoặc kẹt trục theo thông số thực tế. Chọn nguồn, dây và bảo vệ phù hợp, có dự phòng theo thiết kế.
4. Kiểm tra cách cấp đồng thời USB và nguồn ngoài của **đúng bo**. Không tự nối hai đầu ra nguồn với nhau.

Trong Robot Arduino/ESP32, vi điều khiển gửi tín hiệu cho driver động cơ (mạch cấp và điều khiển dòng cho động cơ); GPIO không phải đầu cấp công suất cho động cơ. Điện áp pin và vị trí cấp nguồn phải lấy từ tài liệu sản phẩm.

## Thực hành nhỏ: đọc nhãn trên giấy

Giả sử hai cảm biến được nhà sản xuất quy định dùng 5 V, mỗi cảm biến tối đa 100 mA. Chúng dùng một nguồn riêng, chưa có động cơ hay bo điều khiển trên đường nguồn này.

- Tổng dòng: `0,1 + 0,1 = 0,2 A`.
- Tổng công suất: `5 × 0,2 = 1 W`.
- So sánh nguồn ổn áp 5 V – 1 A và nguồn 12 V – 2 A: nguồn 5 V có điện áp phù hợp và đủ dòng theo giả định; không nối nguồn 12 V trực tiếp vào cảm biến.

**Kết quả mong đợi:** chọn theo điện áp trước, dòng sau; giải thích được vì sao “nhiều watt hơn” không đồng nghĩa phù hợp hơn. Đây là bài tính, chưa xác nhận một bộ nguồn hay cảm biến cụ thể.

## Lỗi thường gặp

- Nhầm mA với A: 200 mA là 0,2 A.
- Dùng điện áp danh định pin thay cho điện áp tối đa khi sạc đầy: cần kiểm tra cả dải điện áp.
- Chỉ cộng dòng chạy đều của động cơ: có thể hụt dòng lúc khởi động.
- Đo điện áp bằng thang đo dòng: khi đo DC, dùng đúng thang V, que đen ở COM và que đỏ ở cổng V theo hướng dẫn đồng hồ; không đặt đồng hồ ở thang A trực tiếp ngang nguồn.

Tham khảo từ nhà sản xuất: [Adafruit – đo điện áp](https://learn.adafruit.com/multimeters/voltage) và [đo dòng điện](https://learn.adafruit.com/multimeters/current). Giới hạn nguồn của bo xem [tài liệu Arduino Nano](https://docs.arduino.cc/hardware/nano/).

[← Bắt đầu từ đây](../index.md#lo-trinh-a) · [Tiếp: GND và nối chung mass →](02-gnd-va-noi-chung-mass.md)
