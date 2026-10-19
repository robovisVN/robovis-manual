# Học và sử dụng Robot ESP32 Camera

Bộ tài liệu hướng dẫn bạn từng bước chuẩn bị thiết bị, cài đặt môi trường, nạp chương trình, xem hình ảnh camera và điều khiển robot qua Wi-Fi. Bạn cũng có thể chạy nhận diện vật thể bằng YOLO trên máy tính Windows.

## 1. Bạn sẽ học được những gì?

- Nhận biết các chức năng và phân biệt hai chương trình ESP32 của robot.
- Cài Arduino IDE, driver CH340, gói board ESP32 và các thư viện cần thiết.
- Chuẩn bị mã nguồn, chọn board và nạp chương trình.
- Kết nối Wi-Fi, xem hình ảnh camera và điều khiển robot bằng trình duyệt.
- Cài môi trường Python và sử dụng phần mềm YOLO trên Windows.
- Kiểm tra lỗi kết nối, lỗi nạp chương trình và vận hành robot an toàn.

## 2. Lộ trình và danh sách bài viết

Các bài viết được chia thành 6 nhóm. Nếu mới bắt đầu, bạn nên đọc theo thứ tự dưới đây.

### Giai đoạn 1: Làm quen với Robot ESP32 Camera

| Bài viết | Nội dung | Kết quả thực hành |
| --- | --- | --- |
| [Bài 1: Tổng quan sản phẩm](01-bat-dau/01-tong-quan.md) | Chức năng, hai cách sử dụng và thông số kết nối | Hiểu vai trò của ESP32, camera và máy tính |
| [Bài 2: Chuẩn bị trước khi sử dụng](01-bat-dau/02-chuan-bi.md) | Thiết bị, mã nguồn và kiểm tra trước khi chạy | Chuẩn bị đủ thiết bị và giữ nguyên bộ mã nguồn |
| [Bài 3: Phân biệt hai chương trình ESP32](01-bat-dau/03-phan-biet-hai-chuong-trinh.md) | Chương trình dùng với YOLO và chương trình kiểm tra đầy đủ | Chọn đúng chương trình theo mục đích sử dụng |

### Giai đoạn 2: Cài đặt môi trường Arduino

| Bài viết | Nội dung | Kết quả thực hành |
| --- | --- | --- |
| [Bài 4: Cài Arduino IDE và driver CH340](02-cai-dat-arduino/01-cai-arduino-va-driver-ch340.md) | Cài phần mềm và kiểm tra cổng COM | Máy tính nhận kết nối ESP32 |
| [Bài 5: Cài board ESP32](02-cai-dat-arduino/02-cai-board-esp32.md) | Thêm và cài gói hỗ trợ ESP32 | Arduino IDE có gói board cần thiết |
| [Bài 6: Cài các thư viện cần thiết](02-cai-dat-arduino/03-cai-thu-vien.md) | Sử dụng Library Manager và kiểm tra thư viện | Chuẩn bị thư viện để biên dịch chương trình |

### Giai đoạn 3: Nạp chương trình cho ESP32

| Bài viết | Nội dung | Kết quả thực hành |
| --- | --- | --- |
| [Bài 7: Chuẩn bị thư mục mã nguồn](03-nap-code/01-chuan-bi-thu-muc-code.md) | Giải nén, giữ cấu trúc tệp và mở project | Mở đúng bộ mã nguồn cần nạp |
| [Bài 8: Chọn board và nạp chương trình](03-nap-code/02-chon-board-va-nap-code.md) | Chọn cấu hình, biên dịch và Upload | Nạp chương trình vào ESP32 |
| [Bài 9: Xử lý lỗi khi nạp chương trình](03-nap-code/03-xu-ly-loi-nap-code.md) | Lỗi COM, kết nối, thư viện và cấu hình camera | Xác định và khắc phục lỗi nạp thường gặp |

### Giai đoạn 4: Xem camera và điều khiển bằng trình duyệt

| Bài viết | Nội dung | Kết quả thực hành |
| --- | --- | --- |
| [Bài 10: Kết nối Wi-Fi và mở giao diện](04-dieu-khien-web/01-ket-noi-va-mo-giao-dien.md) | Xác định chương trình, kết nối Wi-Fi và truy cập robot | Mở đúng trang điều khiển |
| [Bài 11: Sử dụng giao diện điều khiển](04-dieu-khien-web/02-su-dung-giao-dien.md) | Xem camera, điều khiển hướng, tốc độ và đọc cảm biến theo chương trình | Kiểm tra hình ảnh và điều khiển robot |

Nếu robot đã được nạp đúng chương trình, bạn có thể bắt đầu từ nhóm này sau khi đọc phần chuẩn bị và phân biệt hai chương trình.

### Giai đoạn 5: Nhận diện vật thể bằng YOLO trên Windows

| Bài viết | Nội dung | Kết quả thực hành |
| --- | --- | --- |
| [Bài 12: Cài môi trường Python](05-yolo-windows/01-cai-moi-truong-python.md) | Cài Python, tạo môi trường riêng và cài thư viện | Chuẩn bị máy tính để chạy YOLO |
| [Bài 13: Chuẩn bị và chạy chương trình YOLO](05-yolo-windows/02-chay-chuong-trinh-yolo.md) | Kiểm tra tệp, kết nối robot và nhập địa chỉ | Chạy ứng dụng nhận hình ảnh từ robot |
| [Bài 14: Sử dụng phần mềm YOLO](05-yolo-windows/03-su-dung-phan-mem-yolo.md) | Tham số nhận diện, điều khiển robot và WebSocket | Quan sát kết quả nhận diện và điều khiển xe |

YOLO chạy trên máy tính Windows. Trước khi thực hiện nhóm này, cần nạp chương trình **Camera và motor dùng với Python YOLO** và kiểm tra kết nối bằng trình duyệt.

### Giai đoạn 6: Khắc phục lỗi và bảo quản

| Bài viết | Nội dung | Kết quả thực hành |
| --- | --- | --- |
| [Bài 15: Các lỗi thường gặp](06-khac-phuc-loi/01-cac-loi-thuong-gap.md) | Kiểm tra nguồn, Wi-Fi, camera, điều khiển và YOLO | Khoanh vùng lỗi và chuẩn bị thông tin hỗ trợ |
| [Bài 16: Lưu ý an toàn và bảo quản mã nguồn](06-khac-phuc-loi/02-luu-y-an-toan.md) | Vận hành, bảo vệ phần cứng và lưu firmware gốc | Sử dụng robot an toàn và giữ bản mã nguồn để khôi phục |

## 3. Bạn nên bắt đầu từ đâu?

| Nhu cầu | Bài viết nên đọc |
| --- | --- |
| Lần đầu sử dụng Robot ESP32 Camera | [Bài 1: Tổng quan sản phẩm](01-bat-dau/01-tong-quan.md) |
| Chưa biết chọn chương trình nào | [Bài 3: Phân biệt hai chương trình ESP32](01-bat-dau/03-phan-biet-hai-chuong-trinh.md) |
| Cần cài phần mềm để nạp lại ESP32 | [Bài 4: Cài Arduino IDE và driver CH340](02-cai-dat-arduino/01-cai-arduino-va-driver-ch340.md) |
| Robot đã có chương trình, muốn xem camera và điều khiển | [Bài 10: Kết nối Wi-Fi và mở giao diện](04-dieu-khien-web/01-ket-noi-va-mo-giao-dien.md) |
| Muốn chạy nhận diện vật thể trên Windows | [Bài 12: Cài môi trường Python](05-yolo-windows/01-cai-moi-truong-python.md) |
| Gặp lỗi trong quá trình sử dụng | [Bài 15: Các lỗi thường gặp](06-khac-phuc-loi/01-cac-loi-thuong-gap.md) |

---

[Bắt đầu Bài 1: Tổng quan Robot ESP32 Camera](01-bat-dau/01-tong-quan.md)
