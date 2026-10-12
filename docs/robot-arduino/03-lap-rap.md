# Lắp lại cảm biến khi nhận robot

**Mục tiêu:** lắp những phần tháo khi vận chuyển và kiểm tra gá/dây trước khi cấp điện. Các ảnh dưới lấy từ [hướng dẫn khi nhận hàng của Robovis](https://docs.google.com/document/d/1v15Tzh_bDJ4Tez326MCeS8L-1pQc-sz2sl5fraLJJmo/edit).

## Trước khi làm

Tắt công tắc, rút USB và chưa lắp thêm nguồn ngoài. Đặt xe trên bàn, giữ ốc/gá đi kèm và đọc nhãn các đầu dây. Nếu chưa nhận diện HC-SR04/SG90, xem [bài giới thiệu](01-gioi-thieu.md).

## Bước 1. Xác định vị trí cụm siêu âm và dò line

HC-SR04 có hai đầu tròn nhìn về phía trước, gắn trên gá do servo quay. Cụm dò line ở thấp, phía dưới đầu xe, nhìn xuống mặt sàn.

![Vị trí cụm siêu âm và dò line sau khi lắp theo tài liệu bàn giao](images/nhan-hang-image3.png){ width="420" }

**Kết quả cần thấy:** cảm biến siêu âm nhìn trước, còn dò line nhìn xuống; không đặt hai cụm nhìn cùng một hướng chỉ vì đều gọi là cảm biến.

## Bước 2. Lắp gá, không siết ốc quá sâu

Đặt gá như ảnh gốc và bắt ốc giữ gá chắc. Kiểm tra từ bên cạnh:

![Góc nhìn bên của gá cảm biến và servo](images/nhan-hang-image2.png){ width="420" }

Tài liệu gốc lưu ý đầu ốc gá có thể chạm vỏ servo nếu vặn sâu. Khi đó servo bị kẹt lúc quay. Hai vị trí cần kiểm tra được đánh dấu trong ảnh:

![Vị trí đầu ốc cần giữ khoảng hở với vỏ SG90](images/nhan-hang-image1.png){ width="420" }

**Kết quả cần thấy:** gá giữ chắc nhưng đầu ốc không ép/chạm vỏ servo. Không dùng lực xoay tay để cưỡng bức servo; kiểm tra khoảng hở và tháo/điều chỉnh cơ cấu khi tắt nguồn nếu cần.

## Bước 3. Nối lại theo tên chân

Đối chiếu [bảng chân sản phẩm](08-su-dung-robot.md): servo Signal A5, siêu âm Trig A0/Echo A1, dò line D8–D12. Cấp nguồn VCC/GND đúng linh kiện và board mở rộng.

Một dây bus thường gom nhiều tín hiệu vào cùng vỏ cắm. Cắm vừa khít chưa chứng minh thứ tự đúng: cần kiểm tra Signal/VCC/GND ở cả hai đầu. Không chỉ dùng màu dây trong ảnh để suy ra chức năng.

**Kết quả cần thấy:** đầu cắm đúng chiều, không lệch một chân, nhãn tín hiệu khớp bảng và dây không căng khi gá quay trong khoảng sử dụng.

## Bước 4. Kiểm tra trước khi bật xe

- Không còn ốc/dây có thể chạm bánh hoặc phần quay.
- Dây nguồn đúng cực, không cắm nguồn motor vào chân tín hiệu/5V Nano.
- Cảm biến line nhìn xuống và được cố định.
- Servo/gá có khoảng trống, đầu ốc không gây kẹt.
- Bạn biết chương trình nào đang được nạp; chưa đặt bánh chạm sàn khi chưa rõ hành vi khởi động.

Nếu mục tiêu chỉ là dùng xe đã có mã, tiếp tục [hướng dẫn sử dụng robot](08-su-dung-robot.md). Nếu học từng linh kiện, thực hiện đúng trạng thái nguồn/dây trong bài tương ứng.

## Phần bổ trợ: đấu LED và nút trên Nano riêng

Chỉ làm phần này khi muốn học [nút nhấn và millis](04-lap-trinh.md). **Tháo Nano khỏi board robot** trước: D4/D2 trên xe không phải chân trống để gắn thêm linh kiện.

Rút USB, nối LED:

```text
Nano D4 → điện trở 330 Ω–1 kΩ → anode LED
cathode LED → Nano GND
```

Anode/cathode là hai cực của LED. LED mới thường có chân dài là anode, chân ngắn hoặc phía mép phẳng là cathode; kiểm tra nếu chân đã cắt. Điện trở nằm nối tiếp để hạn dòng, không bỏ qua.

Nối hai phía tiếp điểm nút giữa **D2** và **GND**, không nối nút lên 5V vì mã dùng kéo lên nội. Nút bốn chân có hai cặp nối sẵn: phải chọn hai phía chỉ nối với nhau khi nhấn. Có thể kiểm tra bằng sơ đồ nút hoặc đồng hồ đo thông mạch.

Nếu dùng breadboard, tìm đúng nhóm lỗ nối nhau; hai hàng chân Nano không cắm chung một nhóm điện. Đầu tiên kiểm tra không chập 5V/GND, rồi mới cắm USB và chạy bài đọc nút riêng.

**Kết quả cần thấy khi hoàn thành mạch:** LED có điện trở và GND, nút chỉ nối D2 về GND khi nhấn. LED chưa sáng khi chưa có lệnh bật là bình thường.

[Chuẩn bị nguồn/dây](02-chuan-bi.md) · [Lộ trình](index.md) · [Nút nhấn](04-lap-trinh.md)
