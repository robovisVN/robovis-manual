# Chuẩn bị ESP32 CH340 Type-C

**Mục tiêu:** xác định bo và có đủ dụng cụ cho bài đầu tiên.

## Dụng cụ

| Dụng cụ | Yêu cầu |
| --- | --- |
| ESP32 CH340 Type-C | Đọc được tên module và nhãn chân |
| Máy tính có Internet | Cài công cụ, board package và thư viện |
| Cáp USB Type-C | Có truyền dữ liệu; đèn nguồn sáng chưa đủ xác nhận |
| Breadboard, dây nối | Kiểm tra hàng nối, tránh chạm hai hàng chân bo |
| LED thường và điện trở 330 Ω–1 kΩ | Bài đầu ra ngoài bo |
| Nút nhấn | Bài đầu vào |

Chỉ cần bo và cáp cho bài Serial. LED ngoài dùng sau để không phụ thuộc bo có LED tích hợp ở chân nào.

## Ghi thông tin bo

Đọc chữ trên nắp module: chẳng hạn `ESP32-WROOM-32`, `ESP32-S3-WROOM-1` hoặc `ESP32-C3`. Lấy pinout từ nhà cung cấp đúng phiên bản bo; bo 30 chân và 38 chân có vị trí vật lý khác nhau. Số GPIO là tên tín hiệu, không phải số thứ tự đếm chân.

Ví dụ phía sau dùng GPIO23 cho LED và GPIO18 cho nút trên ESP32 classic WROOM-32. Chỉ đấu nếu bo thật có hai chân này và không dùng chúng cho thiết bị khác. Với bo họ khác, xác định chân phù hợp rồi sửa hằng số trong mã.

## Nguồn và điện áp

Ngắt nguồn động cơ khi nạp thử. Tắt mọi nguồn trước khi đổi dây. GPIO không nhận tín hiệu 5 V trực tiếp; cảm biến có đầu ra 5 V cần chuyển mức phù hợp. Phân biệt chân nguồn 5V/VIN, 3V3 và GND bằng sơ đồ của bo.

Chưa nối USB cùng nguồn ngoài nếu chưa hiểu sơ đồ nguồn. Với mạch giao tiếp không cách ly, nguồn tải và ESP32 cần chung GND; cực dương nguồn tải không tự động nối vào 3V3/5V của bo.

## Lưu bài học

Tạo thư mục `HocRobotESP32`, mỗi sketch có thư mục riêng, ví dụ `ESP32Serial/ESP32Serial.ino`. Tên `.ino` chính trùng tên thư mục. Giữ một bản mã đã chạy tốt trước khi sửa.

**Kiểm tra:** bạn biết tên module, có cáp dữ liệu và đang thử bo riêng với nguồn động cơ ngắt.

[Bài trước](01-gioi-thieu.md) · [Bài tiếp: Cài IDE và driver](03-cai-arduino-ide.md)
