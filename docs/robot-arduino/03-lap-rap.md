# Đấu LED và nút nhấn với Nano

**Mục tiêu:** tạo mạch linh kiện rời cho bài lập trình. Các chân dưới đây là ví dụ học, không phải sơ đồ riêng của robot.

## Đấu LED

Rút USB và tắt nguồn trước khi đổi dây:

```text
Nano D4 → điện trở 330 Ω–1 kΩ → anode LED
cathode LED → Nano GND
```

LED mới thường có chân dài là anode (+), chân ngắn là cathode (−); mép phẳng thường đánh dấu cathode. Nếu chân đã cắt, xem dấu hoặc kiểm tra bằng đồng hồ. Điện trở mắc nối tiếp để hạn dòng; không nối LED trực tiếp từ GPIO xuống GND.

## Đấu nút nhấn

Nối hai phía tiếp điểm của nút với **D2** và **GND**. Mã sẽ dùng `INPUT_PULLUP`, không cần nối nút lên 5V.

Nút bốn chân có hai cặp nối sẵn. Xác định bằng đồng hồ hoặc sơ đồ linh kiện; nếu chọn hai chân cùng cặp, mã luôn thấy nút đang nhấn. Có thể dùng hai dây chạm nhau để kiểm tra trước.

## Kiểm tra trước khi cấp điện

- Hai hàng chân Nano không nằm cùng nhóm nối trên breadboard.
- LED có điện trở nối tiếp, cathode về GND.
- D2 chỉ nối với GND khi nhấn nút.
- 5V không chạm GND, nguồn động cơ vẫn ngắt.

**Kết quả:** mạch sẵn sàng cho bài tiếp. LED chưa sáng khi chưa có mã điều khiển là bình thường.

[Bài trước](06-cai-thu-vien.md) · [Bài tiếp: Lập trình](04-lap-trinh.md)
