# GND là gì? Khi nào cần nối chung mass?

**Mục tiêu:** xác định điểm tham chiếu của tín hiệu và biết khi nào cần nối GND giữa hai mạch.

**Cần biết trước:** [điện áp và dòng điện](01-dien-ap-dong-dien-cong-suat.md). Chưa cần nạp chương trình.

## GND là mốc đo điện áp

**GND** (ground, thường gọi là mass trong mạch điện tử) là điểm được chọn làm mốc 0 V của mạch. Khi nói “chân tín hiệu 3,3 V”, ta cần hiểu là 3,3 V **so với GND nào**.

GND trên bo mạch không tự động là dây nối đất bảo vệ của hệ thống điện nhà. Trong bài này chỉ xét mạch DC điện áp thấp; không nối dây điện lưới hay dây tiếp địa để thử.

Cực âm pin thường được dùng làm GND của mạch chạy bằng pin đó. GND vẫn là đường dẫn có điện trở, không phải nơi có thể đưa dòng bao nhiêu cũng được.

## Khi hai mạch truyền tín hiệu trực tiếp

Giả sử một bo **ESP32 classic, logic 3,3 V**, đọc đầu ra digital (tín hiệu số) của cảm biến đã xác nhận dùng nguồn 3,3 V và xuất tín hiệu tương thích 3,3 V. Với kết nối không cách ly:

```text
ESP32 3V3  ---------- VCC cảm biến
ESP32 GND  ---------- GND cảm biến
ESP32 GPIO đầu vào -- OUT cảm biến
```

Đường GND giúp bên nhận có cùng mốc để xác định OUT là mức cao hay thấp. **GPIO** là chân vào/ra đa mục đích; chân cụ thể phải còn trống và hỗ trợ đầu vào theo bo đang dùng. Đây là sơ đồ nguyên lý, không phải sơ đồ thay dây robot.

Trong sơ đồ, **VCC** là chân cấp nguồn dương của cảm biến; **OUT** là chân xuất tín hiệu. Luôn đối chiếu ký hiệu trên đúng module.

Nếu cảm biến dùng nguồn DC riêng phù hợp, GND cảm biến và GND ESP32 thường vẫn cần nối chung cho đường tín hiệu trực tiếp. **Không vì nối chung GND mà nối cả hai cực dương nguồn với nhau.** Điện áp OUT cũng phải tương thích; nối GND không biến 5 V thành 3,3 V.

## Khi nào không nối tùy tiện?

- Với **cách ly điện**, tín hiệu đi qua phần tử cách ly và hai phía có thể được thiết kế không chung GND. Làm đúng sơ đồ bộ cách ly; nối tắt GND có thể làm mất tác dụng cách ly.
- Hai hệ thống nguồn chưa rõ quan hệ với đất hoặc mức điện áp không nên ghép GND thử để “xem có chạy không”. Xác minh sơ đồ trước.
- USB có thể đã tạo đường GND giữa máy tính và bo. Không giả định hai mạch hoàn toàn độc lập chỉ vì dùng hai nguồn khác nhau.

## Dòng động cơ và dòng tín hiệu

Dòng lớn từ động cơ gây sụt áp và nhiễu trên dây dẫn. Đưa dòng động cơ qua dây GND mảnh của cảm biến có thể làm tín hiệu sai hoặc bo reset. Với bộ xe, giữ cách đi dây và đường nguồn của sản phẩm; không gom lại toàn bộ dây theo một sơ đồ minh họa.

## Thực hành nhỏ: tìm đường tham chiếu

Trên giấy, vẽ bo điều khiển và cảm biến digital dùng nguồn riêng. Đánh dấu VCC, GND và OUT, rồi trả lời:

1. Nếu chỉ có dây OUT, bên nhận đang so sánh tín hiệu với mốc nào?
2. Nối thêm GND có cho phép đưa OUT 5 V vào ESP32 không?
3. Có cần nối hai cực dương của hai nguồn với nhau không?

**Kết quả mong đợi:** thêm đường tham chiếu GND cho tín hiệu không cách ly; trả lời “không” cho câu 2 và 3. Nếu kiểm tra thông mạch trên bo thật, tắt nguồn và rút USB trước; đường dẫn qua linh kiện có thể làm tiếng bíp khó diễn giải.

## Lỗi thường gặp

- Thấy đèn nguồn sáng rồi cho rằng tín hiệu đã có chung mốc: hai việc khác nhau.
- Nối GND xong vẫn đọc sai: kiểm tra điện áp OUT, chế độ GPIO và chân thực tế.
- Nối GND vào VIN hoặc VCC: đó là đường nguồn dương, không phải GND.

Đối chiếu vị trí chân trên [pinout Arduino Nano](https://docs.arduino.cc/resources/pinouts/A000005-full-pinout.pdf) hoặc [datasheet ESP32, phần nguồn và đặc tính điện](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf). Các ví dụ đo điện áp đều cần hai điểm đo: [Adafruit – Voltage](https://learn.adafruit.com/multimeters/voltage).

[← Điện áp, dòng điện và công suất](01-dien-ap-dong-dien-cong-suat.md) · [Tiếp: Tín hiệu 3,3 V và 5 V →](03-tin-hieu-3v3-va-5v.md)
