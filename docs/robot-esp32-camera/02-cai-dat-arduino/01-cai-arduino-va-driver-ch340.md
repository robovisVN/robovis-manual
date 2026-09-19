# Cài Arduino IDE và driver CH340

Trang này hướng dẫn cài phần mềm cần thiết để Windows nhận được bo mạch ESP32-S3 Camera và Arduino IDE có thể nạp chương trình.

## 1. Cài driver CH340

Bo mạch của sản phẩm sử dụng chip giao tiếp USB sang UART CH340. Vì vậy cần cài driver CH340, không sử dụng driver CP2102 trong bài hướng dẫn tham khảo.

1. Mở thư mục driver do ROBOVIS cung cấp.
2. Tìm tệp `CH341SER` và giải nén nếu tệp đang ở dạng `.zip`.
3. Mở thư mục vừa giải nén.
4. Nhấp đúp vào `SETUP.EXE`.
5. Chọn **Install** và chờ thông báo cài đặt thành công.
6. Khởi động lại Windows nếu trình cài đặt yêu cầu.

## 2. Cài Arduino IDE

1. Truy cập [trang tải Arduino IDE chính thức](https://www.arduino.cc/en/software).
2. Tải bản Arduino IDE mới nhất dành cho Windows.
3. Chạy tệp cài đặt.
4. Giữ các tùy chọn mặc định và hoàn tất quá trình cài đặt.
5. Mở Arduino IDE sau khi cài xong.

## 3. Kiểm tra nhanh

Kết nối ESP32 với máy tính bằng cáp USB có truyền dữ liệu. Sau đó:

1. Nhấp chuột phải vào **This PC** hoặc **My Computer**.
2. Chọn **Manage**.
3. Mở **Device Manager**.
4. Mở nhóm **Ports COM and LPT**.
5. Tìm cổng có tên liên quan đến `USB-SERIAL CH340` và ghi lại số cổng, ví dụ `COM5`.

Nếu không biết cổng nào thuộc ESP32, hãy quan sát danh sách, rút cáp USB rồi cắm lại. Cổng xuất hiện trở lại là cổng của bo mạch.

## Nếu không thấy mục Ports

- Thử một cổng USB khác trên máy tính.
- Thay bằng cáp USB chắc chắn có truyền dữ liệu; nhiều cáp chỉ dùng để sạc.
- Cài lại driver CH340.
- Kiểm tra đèn nguồn trên bo mạch.

Có thể tham khảo thêm bài [Cách nạp chương trình cho ESP32 bằng Arduino IDE](https://dienthongminhesmart.com/lap-trinh-esp32/bai1-nap-code-esp32/). Tuy nhiên, sản phẩm này dùng **ESP32-S3 Dev Module** và driver **CH340**, không chọn board hoặc driver giống hoàn toàn ví dụ trong bài viết.

