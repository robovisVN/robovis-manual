# Lưu ý an toàn và bảo quản mã nguồn

## An toàn khi vận hành

- Chỉ sử dụng robot ở nơi khô ráo, nền phẳng và đủ khoảng trống.
- Luôn thử ở tốc độ thấp trước.
- Không sử dụng gần cầu thang, mép bàn hoặc khu vực có nguy cơ rơi.
- Không để tay, tóc, dây điện hoặc vật lạ gần bánh xe đang quay.
- Không đứng chắn trực tiếp phía trước robot khi thử chuyển động.
- Không để robot tự chạy khi không có người giám sát.
- Nếu robot chạy sai hướng hoặc không dừng, tắt nguồn ngay.
- Nếu pin, dây điện, động cơ hoặc mạch nóng bất thường, tắt nguồn và ngừng sử dụng để kiểm tra.

## Bảo vệ ESP32 và cảm biến

- Không nối tín hiệu 5 V trực tiếp vào chân GPIO của ESP32-S3.
- Không thay đổi dây camera khi đang cấp nguồn.
- Hai chương trình đang sử dụng GPIO19 theo hai mục đích khác nhau: chân `STBY` của mạch động cơ trong chương trình dùng với YOLO và đầu vào dò line trong chương trình kiểm tra đầy đủ. Không trộn hai bộ định nghĩa chân.
- Trong chương trình kiểm tra đầy đủ, GPIO20 được dùng cho encoder trái và GPIO44 được dùng cho một mắt dò line.
- GPIO19 và GPIO20 cũng liên quan đến USB native trên ESP32-S3. Không tự ý đấu thêm thiết bị hoặc thay đổi cấu hình USB khi chưa kiểm tra sơ đồ phần cứng.
- Không thay đổi `board_config.h` nếu chưa xác định đúng chân camera.

## Bảo quản firmware gốc

Nạp chương trình mới sẽ ghi đè chương trình đang có trong ESP32. Người dùng không thể lấy lại mã nguồn gốc chỉ bằng cách đọc ngược từ bo mạch.

Trước khi thử mã nguồn khác:

1. Lưu một bản thư mục firmware gốc do ROBOVIS cung cấp.
2. Không đổi tên hoặc xóa `main.ino`, `app_httpd.cpp`, `board_config.h`.
3. Ghi lại phiên bản thư viện và board đang hoạt động ổn định.
4. Chỉ thay đổi từng phần nhỏ và kiểm tra lại sau mỗi lần nạp.

Nếu chưa có firmware gốc hoặc chưa biết cách khôi phục, không nạp một chương trình tải ngẫu nhiên từ Internet.

## Kết thúc phiên sử dụng

1. Nhấn Dừng hoặc phím `Space` để robot đứng yên.
2. Đóng chương trình YOLO hoặc trang điều khiển.
3. Tắt nguồn robot.
4. Ngắt cáp USB nếu không còn sử dụng.
5. Sạc và bảo quản pin theo hướng dẫn đi kèm của bộ nguồn.
