# Cài Arduino IDE và nạp thử vào Nano

**Mục tiêu:** máy tính nhận được Nano và bạn nạp một chương trình làm LED L nhấp nháy. Hoàn thành bước này rồi mới học servo, motor và cảm biến.

Hướng dẫn chính dùng **Windows** và **Nano classic ATmega328P** như bộ bàn giao. Trên macOS/Linux, dùng [hướng dẫn cài IDE tương ứng của Arduino](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/); các bước chọn board và nạp trong IDE có cùng ý nghĩa.

## Trước khi cài

Chuẩn bị máy có Internet, cáp USB dữ liệu và Nano riêng chỉ cấp USB. Nếu dùng Nano đang gắn trên xe, thực hiện [chuẩn bị nguồn/dây D0-D1](02-chuan-bi.md). Giữ nguồn motor ngắt.

## Bước 1. Cài và mở Arduino IDE 2

1. Trên máy tính, mở [trang Arduino Software](https://www.arduino.cc/en/software).
2. Chọn bản Arduino IDE phù hợp Windows của bạn và tải bộ cài.
3. Chạy bộ cài, làm theo các bước trên màn hình.
4. Mở Arduino IDE từ Start menu hoặc biểu tượng ứng dụng.

**Kết quả cần thấy:** cửa sổ IDE có vùng viết mã, nút dấu kiểm và mũi tên ở phía trên. Bạn chưa cần tạo tài khoản để làm các bài nạp bằng IDE trên máy tính này.

| Khu vực/nút | Việc dùng trong bài |
| --- | --- |
| Vùng mã | Chép hoặc sửa chương trình |
| Verify, dấu kiểm | Kiểm tra/biên dịch mã trên máy tính |
| Upload, mũi tên | Gửi mã vào Nano |
| Output phía dưới | Xem tiến trình và thông báo lỗi |
| Board/Port | Chọn loại bo và đường kết nối |

## Bước 2. Kiểm tra hỗ trợ Nano

**Board package** là gói để IDE biết biên dịch/nạp cho loại bo đó; nó khác thư viện servo/cảm biến.

Mở **Boards Manager** ở thanh bên, tìm **Arduino AVR Boards by Arduino**. Nếu đã cài, giữ gói có sẵn; nếu chưa, nhấn Install và chờ tải xong. Xem [hướng dẫn Boards Manager](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-board-manager/) khi giao diện khác.

Chọn **Tools → Board → Arduino AVR Boards → Arduino Nano**. Không chọn Nano Every hoặc Nano ESP32 chỉ vì cùng có chữ Nano.

**Kết quả cần thấy:** tên board đã chọn là Arduino Nano.

## Bước 3. Xác định cổng COM của Nano

1. Cắm Nano bằng USB.
2. Trên Windows, mở **Device Manager**: có thể nhấn chuột phải nút Start rồi chọn mục này.
3. Mở **Ports (COM & LPT)** và tìm cổng vừa xuất hiện.
4. Rút/cắm Nano để xác nhận chính cổng đó biến mất/xuất hiện. Ghi số COM.

Ví dụ COM4 là tên một cổng, không phải tên loại bo. Máy bạn có thể là COM3, COM7 hoặc số khác; **chọn số đã thấy trên máy bạn**, không chép COM4 từ ví dụ.

Trong IDE mở **Tools → Port** và chọn cổng đó. Nếu tên bo không được tự nhận diện, vẫn có thể chọn Nano và Port thủ công.

**Nếu chưa có COM:** thử cáp dữ liệu khác/cổng USB khác. Với Nano dùng CH340, nếu Device Manager báo thiếu driver, tải [CH341SER của WCH](https://www.wch.cn/downloads/ch341ser_exe.html), cài rồi kết nối lại. Nano khác có thể dùng chip USB khác; chọn driver theo chip thực tế. Xem thêm [bo không được nhận](https://support.arduino.cc/hc/en-us/articles/4412955149586-If-your-board-is-not-detected-by-Arduino-IDE).

## Bước 4. Chọn Processor

Mở **Tools → Processor → ATmega328P**, đúng lựa chọn trong hướng dẫn bàn giao.

Một số Nano dùng bootloader cũ, là phần nhỏ giúp nhận mã qua USB. Nếu board/cổng/cáp đúng mà vẫn nạp lỗi, có thể thử **ATmega328P (Old Bootloader)**. Không chọn mục đó chỉ vì bo có CH340; chip USB không quyết định bootloader. Xem [hướng dẫn lựa chọn Processor](https://support.arduino.cc/hc/en-us/articles/4401874304274-Select-the-right-processor-for-Arduino-Nano).

## Bước 5. Mở chương trình Blink có sẵn

Chọn **File → Examples → 01.Basics → Blink**. Đây là chương trình làm đèn tích hợp nhấp nháy. Chọn **File → Save As**, lưu bản học tên `NanoBlink` trong thư mục HocRobotNano.

**Kết quả cần thấy:** một sketch có các lệnh dùng LED_BUILTIN, HIGH/LOW và delay. Chưa cần hiểu hết mã để kiểm tra kết nối lần đầu.

## Bước 6. Verify rồi Upload

1. Nhấn dấu kiểm **Verify**. Chờ biên dịch xong.
2. Nếu có lỗi, đọc Output; chưa nhấn Upload tiếp khi mã còn sai.
3. Khi Verify thành công, nhấn **Upload**.
4. Chờ báo nạp hoàn tất; đừng rút cáp giữa chừng.

**Kết quả cần thấy:** IDE hoàn tất Upload và LED **L** trên Nano sáng/tắt lặp lại. Đèn nguồn thường sáng liên tục, không phải đèn điều khiển trong Blink.

Dùng Upload bình thường qua USB. Bài này chưa cần chọn programmer, Upload Using Programmer hoặc Burn Bootloader.

## Bước 7. Xác nhận Nano đang chạy chính mã bạn sửa

Trong sketch, đổi **cả hai** `delay(1000)` thành `delay(300)`. Verify rồi Upload lại.

**Kết quả cần thấy:** nhịp sáng/tắt nhanh hơn. Việc quan sát được thay đổi sau Upload giúp xác nhận không chỉ mã biên dịch được mà đúng Nano đang chạy mã mới.

## Khi nào hoàn thành?

- Board là Nano, Processor phù hợp và Port đúng bo.
- Upload thành công.
- LED L đổi nhịp khi sửa và nạp lại.

Nếu chưa đạt, mở [xử lý lỗi theo giai đoạn](07-chay-thu-va-xu-ly-loi.md). Nếu đã đạt, chuyển sang [Bài 2: Viết chương trình đầu tiên](bai-giang/02-lap-trinh.md). Khi cần Servo/Dabble ở bài sau, xem [cài thư viện](06-cai-thu-vien.md).
