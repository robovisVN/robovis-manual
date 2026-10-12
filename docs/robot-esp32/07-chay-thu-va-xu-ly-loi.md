# Chạy thử Robot ESP32 và xử lý lỗi

**Mục tiêu:** áp dụng bài nền tảng vào robot theo cấu hình thật.

Đối chiếu [hướng dẫn sử dụng chung](08-su-dung-robot.md) và [các lỗi trong tài liệu Robovis](https://docs.google.com/document/d/1j4c4cuyZ6She5PE_y6iRa2XHlQhCYCTDqzXxScZGdfg/edit) trước khi chỉnh mã.

## Trước khi dùng mã robot

Ghi tên module ESP32, pinout bo, loại driver, nguồn động cơ/cảm biến và bảng chân trong mã. GPIO23/GPIO18 của bài học không quy định chân sản phẩm. Không đấu động cơ trực tiếp vào GPIO, không đưa tín hiệu 5 V vào đầu vào ESP32.

Ví dụ cảm biến HC-SR04 loại 5 V có Echo mức 5 V: cần hạ mức bằng mạch phù hợp trước khi đưa vào ESP32. Không suy ra mức tín hiệu chỉ từ điện áp cấp nguồn của linh kiện.

## Trình tự chạy thử

1. Giữ bản `ESP32Serial` chạy tốt, sao lưu firmware/mã nguồn được bàn giao nếu có.
2. Ngắt nguồn động cơ; mở sketch đúng tên/thư mục bộ mã robot.
3. Cài core và thư viện theo README, đối chiếu chân, Verify rồi Upload.
4. Xem Serial để kiểm tra từng cảm biến khi robot đứng yên.
5. Kê bánh khỏi sàn, cấp nguồn đúng sơ đồ và thử từng động cơ tốc độ thấp, thời gian ngắn.
6. Kiểm tra lệnh dừng trước khi hạ robot xuống sàn trống. Với điều khiển không dây, mã cần cơ chế dừng khi mất kết nối hoặc quá hạn lệnh.

Bo điều khiển, driver và cảm biến giao tiếp không cách ly cần chung GND. Chỉ nối các đường nguồn dương theo sơ đồ; không cấp nguồn động cơ từ 3V3. Khi chưa có bộ mã/sơ đồ riêng, tiếp tục bài linh kiện rời thay vì thử các chân ngẫu nhiên.

## Lỗi thường gặp

| Hiện tượng | Kiểm tra theo thứ tự |
| --- | --- |
| Đèn nguồn sáng nhưng không có COM | Cáp Type-C dữ liệu → USB → Device Manager → CH340 |
| `Connecting...` kéo dài / `Failed to connect` | Cáp dữ liệu → CH340 → ESP32 Dev Module/COM → thử bo riêng; tài liệu bàn giao yêu cầu không bấm BOOT/RST khi nạp |
| Báo sai loại chip | Đọc module rồi chọn ESP32/S3/C3 tương ứng |
| Cổng bận / access denied | Đóng ứng dụng đang giữ cổng, rút/cắm và chọn Port lại |
| Thiếu `WiFi.h` | Gói ESP32 và board; không cài thư viện WiFi ngẫu nhiên |
| Thiếu thư viện ngoài `.h` | Tên header, tác giả, phiên bản, dependency |
| Không tìm thấy `ledcSetup` | Kiểm tra API core 2.x/3.x, không phải lỗi driver CH340 |
| Thiếu do_line.h hoặc undefined reference tới do_line_setup | Giữ cả main.ino, do_line.cpp và do_line.h trong cùng thư mục main |
| Không mở được trang điều khiển | Kết nối Wi-Fi ESP32-Car, nhập http://192.168.4.1, giữ kết nối dù báo không có Internet |
| Không điều khiển tay được | Kiểm tra đang ở Line follow không; chuyển về Manual |
| Không nhận line | Nền sáng, line tương phản, kiểm tra từng kênh; tài liệu gốc: trên line đèn tắt, ngoài line đèn sáng |
| Xe lắc | Theo tài liệu, thử giảm v_base từ 0.4 xuống 0.35; mã hiện tại đã dùng vF = v_base * 0.90f, không giả định hệ số là 1.0 |
| Không quay hoặc dừng ở điểm rẽ | Kiểm tra pin/encoder; tài liệu đề nghị góc line lớn hơn 90° |
| Serial ký tự lạ hoặc trống | Đúng cổng, 115200 theo mã, nhấn EN để xem lại log |
| LED không sáng | Cực LED, điện trở, GND, đúng GPIO; không giả định LED tích hợp ở GPIO2 |
| `Brownout detector was triggered` / reset khi tải chạy | Ngắt tải, kiểm tra cáp, nguồn, dòng tải và dây GND; không tắt brownout để che lỗi |

## Khi cần hỗ trợ

Gửi tên module/chip USB, ảnh bo rõ nhãn chân, sơ đồ nguồn, hệ điều hành, phiên bản IDE/core/thư viện, cấu hình board và toàn bộ log. Nêu lỗi xuất hiện ở Verify, Upload hay lúc đang chạy. Che mật khẩu Wi-Fi trước khi gửi mã.

**Hoàn thành:** tự kiểm tra COM, nạp Serial, thêm thư viện, đọc nút và chạy PWM. Tiếp tục [ESP32 Camera](../robot-esp32-camera/01-bat-dau/01-tong-quan.md) hoặc [ESP32 LiDAR](../robot-esp32-lidar/index.md) nếu đúng sản phẩm của bạn.

[Bài trước](06-lap-trinh-co-ban.md) · [Lộ trình](index.md) · [Tải tài liệu](../tai-xuong/robot-esp32.md)
