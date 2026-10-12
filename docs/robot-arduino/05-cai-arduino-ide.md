# Cài Arduino IDE và nạp Blink cho Nano

**Mục tiêu:** LED trên Nano nhấp nháy theo chương trình bạn nạp.

## 1. Cài Arduino IDE 2

Tải bản phù hợp hệ điều hành từ [trang phần mềm Arduino](https://www.arduino.cc/en/software). Trên Windows, chạy trình cài rồi mở IDE. Trên macOS/Linux, làm theo [hướng dẫn chính thức](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/).

Nhận biết **Verify** (dấu kiểm), **Upload** (mũi tên), vùng soạn mã và vùng Output báo lỗi. Cần Internet khi tải gói hỗ trợ bo.

## 2. Cài gói bo Nano

Mở **Boards Manager** ở thanh bên, tìm **Arduino AVR Boards by Arduino**, cài nếu chưa có. Chọn **Tools → Board → Arduino AVR Boards → Arduino Nano**. Không chọn Nano Every/Nano ESP32. Xem [hướng dẫn Boards Manager](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-board-manager/).

## 3. Chọn cổng và kiểm tra driver

Cắm Nano, mở **Tools → Port**, chọn cổng vừa xuất hiện. Windows thường hiển thị `COM3`, `COM4`…; số thực tế tùy máy. Rút bo để xác nhận cổng nào biến mất.

Nếu bo dùng CH340 mà chưa có COM, kiểm tra **Device Manager → Ports (COM & LPT)** và **Other devices**. Cài [driver CH340/CH341 của WCH](https://www.wch.cn/downloads/ch341ser_exe.html), rút/cắm lại. Chọn driver theo chip thực tế vì Nano có thể dùng chip USB khác. Xem [kiểm tra bo không được nhận](https://support.arduino.cc/hc/en-us/articles/4412955149586-If-your-board-is-not-detected-by-Arduino-IDE).

## 4. Chọn Processor

Ở **Tools → Processor**, bắt đầu với **ATmega328P**. Nếu nạp lỗi dù cáp/cổng đúng, thử **ATmega328P (Old Bootloader)**. Một số Nano tương thích dùng bootloader cũ; CH340 không tự quyết định lựa chọn này. Chỉ chọn ATmega168 nếu chip thực tế là ATmega168. Xem [hướng dẫn Processor cho Nano](https://support.arduino.cc/hc/en-us/articles/4401874304274-Select-the-right-processor-for-Arduino-Nano).

## 5. Nạp và kiểm tra Blink

1. Mở **File → Examples → 01.Basics → Blink**.
2. **File → Save As**, lưu thành `NanoBlink`.
3. Nhấn Verify, đọc lỗi nếu có; khi thành công, nhấn Upload.
4. Chờ báo hoàn tất, quan sát LED **L** nhấp nháy. LED nguồn thường sáng liên tục.
5. Đổi cả hai `delay(1000)` thành `delay(300)`, nạp lại và xem nhịp thay đổi.

Blink dùng `LED_BUILTIN` để chọn LED tích hợp. Xem [bài Blink của Arduino](https://docs.arduino.cc/built-in-examples/basics/Blink/).

!!! tip "Nạp qua USB"
    Dùng Upload bình thường; không cần Upload Using Programmer hoặc Burn Bootloader để làm bài.

**Hoàn thành khi:** mã sửa làm LED đổi nhịp. Nếu chưa đạt, xem [xử lý lỗi](07-chay-thu-va-xu-ly-loi.md).

Để nạp mã sản phẩm, xem [hướng dẫn sử dụng chung](08-su-dung-robot.md). [HD nạp code Robovis](https://docs.google.com/document/d/1zUuMvjFEuTOBrwMFcFzYiy-x51EDbZutoixD51jM_8Q/edit) chọn **Nano / ATmega328P / đúng COM**. Tài liệu gọi `main.ino`, nhưng các tệp thực tế tên `test_bluetooth.ino`, `do_line.ino`, `tranh_vat_can.ino`…; mở đúng tệp tải được và giữ thư mục sketch trùng tên.

[Bài trước](02-chuan-bi.md) · [Bài tiếp: Thư viện](06-cai-thu-vien.md)
