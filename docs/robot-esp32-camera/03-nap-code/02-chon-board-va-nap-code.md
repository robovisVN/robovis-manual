# Chọn board và nạp chương trình

## 1. Kết nối ESP32

1. Cắm ESP32 vào máy tính bằng cáp USB có truyền dữ liệu.
2. Mở **Device Manager → Ports COM and LPT**.
3. Ghi lại cổng COM của `USB-SERIAL CH340`, ví dụ `COM5`.
4. Đóng Serial Monitor nếu đang mở ở phần mềm khác.

## 2. Chọn cấu hình trong Arduino IDE

Thiết lập đúng ba mục sau:

| Mục | Giá trị cần chọn |
| --- | --- |
| **Tools → Board** | `ESP32S3 Dev Module` |
| **Tools → Port** | Cổng COM của ESP32, ví dụ `COM5` |
| **Tools → PSRAM** | `OPI PSRAM` |

Không chọn `DOIT ESP32 DEVKIT V1`. Đây là ESP32-S3 Camera nên phải chọn `ESP32S3 Dev Module`.

## 3. Biên dịch thử

Nhấn nút **Verify** có biểu tượng dấu kiểm. Chờ Arduino IDE biên dịch xong.

Chỉ tiếp tục khi cuối Console không có dòng lỗi màu đỏ. Cảnh báo màu vàng không phải lúc nào cũng làm quá trình nạp thất bại.

## 4. Nạp chương trình

1. Nhấn nút **Upload** có biểu tượng mũi tên hướng sang phải.
2. Chờ Arduino IDE biên dịch rồi kết nối với ESP32.
3. Theo dõi phần Console phía dưới.
4. Khi thấy dòng sau, chương trình đã được nạp thành công:

```text
Hard resetting via RTS pin...
```

5. Chờ khoảng 5 đến 10 giây để ESP32 khởi động.

## Khi Console dừng ở Connecting

Nếu Console hiện `Connecting...` rồi báo lỗi:

1. Nhấn **Upload** lại.
2. Khi Console bắt đầu hiện `Connecting...`, nhấn và giữ nút **BOOT** trên ESP32.
3. Tiếp tục giữ đến khi Console bắt đầu hiện `Writing at...`.
4. Nhả nút **BOOT**.
5. Chờ đến khi thấy `Hard resetting via RTS pin...`.

Sau khi nạp xong, có thể tháo cáp USB và cấp nguồn robot theo cách sử dụng bình thường.

