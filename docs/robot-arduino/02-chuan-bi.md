# Chuẩn bị trước khi học Arduino Nano

**Mục tiêu:** biết cần những dụng cụ nào và chuẩn bị xe/bo ở đúng trạng thái cho bài học đầu tiên. Chưa cần đấu thêm tất cả linh kiện cùng lúc.

## Nếu bạn đã có bộ xe lắp sẵn

Giữ nguyên dây cho tới khi chụp lại và đọc sơ đồ. Kiểm tra trong bộ có Nano, board mở rộng, driver, motor, SG90, HC-SR04, line sensor, encoder và HM-10 khi dùng Bluetooth. Các cảm biến có thể được tháo để vận chuyển; xem [lắp lại khi nhận hàng](03-lap-rap.md).

Chưa bật motor chỉ để xem có chạy không: Nano có thể đang giữ một chương trình tự động đã nạp từ trước.

## Dụng cụ cho từng giai đoạn

| Bạn sắp làm gì? | Cần có |
| --- | --- |
| Cài IDE, nạp và thử LED tích hợp | Máy tính, Internet lúc cài, Nano, cáp USB đúng cổng có truyền dữ liệu |
| Thử servo | SG90, dây và nguồn tải phù hợp |
| Đọc cảm biến | Cảm biến tương ứng, dây và nguồn phù hợp module |
| Thử motor | Driver/nguồn của bộ xe và chỗ kê bánh khỏi sàn |
| Thực hành LED/nút rời | Breadboard, LED, điện trở 330 Ω–1 kΩ và nút nhấn |

Đèn nguồn sáng chưa chứng minh cáp có truyền dữ liệu: có cáp chỉ sạc. Lượt đầu nên dùng cáp đã thử truyền dữ liệu và cắm trực tiếp vào máy tính.

**Kết quả cần thấy:** để bắt đầu, bạn chỉ cần Nano/USB/máy tính, không phải mua đủ linh kiện mới học được.

## Bước 1. Chụp và đọc nhãn trước khi rút dây

1. Tắt công tắc robot và rút USB.
2. Chụp các đầu dây đủ rõ để thấy tên chân.
3. Tìm Nano và các đầu kết nối D0/D1. Theo bộ mã, hai đường này đi tới IN1/IN2 của driver.
4. Nếu dùng Nano riêng cho bài đầu, rút Nano khỏi board mở rộng khi đã tắt nguồn, giữ các dây robot tại board và ghi hướng cắm để đặt lại đúng.

Không dùng lực kéo dây để nhấc bo. Nếu không chắc tên chân/hướng bo, đối chiếu [sơ đồ](08-su-dung-robot.md) trước; ảnh màu dây chỉ để ghi nhớ bộ dây của bạn, không thay tên tín hiệu.

## Bước 2. Chọn trạng thái đấu nối theo bài

| Bài học | Trạng thái nên dùng |
| --- | --- |
| LED hoặc học viết mã đầu tiên | Nano riêng, chỉ cắm USB |
| Đọc dữ liệu qua Serial Monitor | Motor ngắt nguồn; driver IN1/IN2 ngắt khỏi D0/D1 Nano; cảm biến cần đọc giữ đúng chân |
| Điều khiển motor theo bảng chân sản phẩm | Nối driver đúng sơ đồ, kê bánh; sketch motor không dùng Serial trên D0/D1 |

**Serial Monitor** là cửa sổ xem dữ liệu Nano gửi về máy tính. Nó dùng đường D0/D1 của Nano, nên các bài đọc log cần giải phóng đường đó khỏi driver. Chỉ tắt nguồn motor không làm dây tín hiệu tự tách ra.

Khi chuyển giữa hai trạng thái, tắt nguồn trước khi nối/rút, dùng ảnh đã chụp để khôi phục. Không vừa thay dây vừa để Nano/robot được cấp điện.

## Bước 3. Phân biệt nguồn và tín hiệu

| Tên chân | Điều cần hiểu trước khi nối |
| --- | --- |
| GND | Mốc điện chung; các thiết bị giao tiếp trong bộ xe cần đường GND chung |
| 5V | Đường nguồn 5 V, không phải nơi cắm điện áp tùy ý từ pin |
| VIN | Đầu nguồn ngoài theo thông số bo; khác 5V, không tự đổi hai chân cho nhau |
| D/A hoặc S trên đầu tín hiệu | Đi tới tín hiệu điều khiển/đọc, không dùng để cấp motor |

Nguồn motor và nguồn servo phải phù hợp tải. Không đưa nguyên điện áp bộ pin vào chân 5V hoặc Signal. Với bo/board chưa biết cách phân phối nguồn, học Nano riêng qua USB trước, chưa nối thêm nguồn ngoài đồng thời.

## Bước 4. Tạo nơi lưu bài học

Trên máy tính, tạo thư mục `HocRobotNano`, ví dụ trong Documents. Trong IDE, mỗi lần Save As với tên bài sẽ tạo một thư mục và tệp .ino chính cùng tên:

```text
HocRobotNano/
├── NanoLED/
│   └── NanoLED.ino
└── NanoKhoangCach/
    └── NanoKhoangCach.ino
```

Lưu riêng bản gốc từ Drive. Không ghi đè bộ mã xe bằng sketch học nếu bạn chưa biết cách lấy lại.

## Khi nào sẵn sàng cài IDE?

- Bạn xác định đúng Nano classic và cáp dữ liệu.
- Nano riêng chỉ cắm USB, hoặc xe đã ngắt nguồn/tín hiệu theo bài.
- Có ảnh/sơ đồ để phục hồi dây, và nơi lưu mã gốc.

Tiếp theo làm [Cài Arduino IDE và nạp Blink](05-cai-arduino-ide.md).
