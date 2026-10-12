# Cài thư viện cho Arduino Nano

**Mục tiêu:** cài đúng thư viện và xác nhận mã cần thư viện đó biên dịch được. Không phải cứ thiếu một tệp là tải mọi thư viện tìm thấy.

## Thư viện là gì?

Khi điều khiển servo, bạn muốn viết lệnh như “đặt góc 90°” thay vì tự tạo từng xung điện. **Thư viện** cung cấp sẵn các lệnh đó. `#include <Servo.h>` trong sketch yêu cầu dùng phần khai báo của thư viện Servo.

**Arduino AVR Boards** giúp IDE hỗ trợ Nano. **Servo/Dabble** giúp sketch dùng linh kiện/tính năng. Cài board package chưa có nghĩa mọi thư viện robot đã được cài.

## Trước khi làm

IDE đã mở, có Internet và chọn đúng Nano. Bài này trước hết dùng **Verify**, chỉ kiểm tra mã trên máy tính. Bạn chưa cần cắm servo hoặc bật nguồn motor.

## Bước 1. Biết chương trình cần thư viện nào

| Bạn muốn nạp | Thư viện cần thêm |
| --- | --- |
| Bài servo hoặc mã tranh_vat_can*.ino | Servo |
| Mã test_bluetooth.ino | Servo và Dabble của STEMpedia |
| Các mã do_line*.ino đã đối chiếu | Không có thư viện ngoài; Arduino.h đi cùng core |

Dấu * trong bảng chỉ phần tên có thể khác giữa các tệp bàn giao. Không gõ cả dấu * vào ô tìm kiếm Library Manager.

## Bước 2. Cài Servo bằng Library Manager

1. Trong IDE, chọn **Tools → Manage Libraries**, hoặc biểu tượng Library Manager ở thanh bên.
2. Gõ **Servo** vào ô tìm kiếm.
3. Tìm thư viện **Servo**, kiểm tra tác giả/dự án **Arduino**.
4. Nhấn Install. Nếu hiện yêu cầu dependency, đó là thư viện phụ cần đi cùng; chấp nhận các mục cần thiết của gói.
5. Chờ hoàn tất, ghi lại phiên bản đang dùng để sau này đối chiếu.

**Kết quả cần thấy:** thư viện Servo có trạng thái đã cài. Xem [hướng dẫn Library Manager của Arduino](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library/) khi nút hiển thị khác.

## Bước 3. Kiểm tra bằng một sketch nhỏ

Tạo sketch `NanoKiemTraServo`:

```cpp
#include <Servo.h>

Servo servoThu;

void setup() {
  servoThu.attach(A5);
  servoThu.write(90);
}

void loop() {
}
```

Chọn Nano rồi nhấn **Verify**. Chưa cần Upload trong bước kiểm tra thư viện.

**Kết quả cần thấy:** không có lỗi thiếu Servo.h, biên dịch hoàn tất. Điều đó xác nhận phần mềm; chưa chứng minh dây/servo/nguồn ngoài hoạt động. Thử phần cứng theo [bài SG90](bai-giang/04-servo.md).

## Bước 4. Cài Dabble khi tới bài Bluetooth

Mở Library Manager, tìm **Dabble**, đối chiếu **STEMpedia** rồi Install. Giữ tên **Dabble**, không chọn **DabbleESP32** cho Nano.

Mở tệp test_bluetooth.ino từ bộ bàn giao hoặc [mã nhỏ ở bài HM-10](bai-giang/09-bluetooth.md), chọn Nano rồi Verify. Các dòng chọn GamePad nằm **trước** include trong mã gốc; giữ nguyên thứ tự này.

**Kết quả cần thấy:** không còn lỗi thiếu Dabble.h. Nếu có lỗi tên hàm, kiểm tra đúng thư viện, phiên bản và tệp đang mở trước khi sửa lệnh điều khiển. [Kho Dabble chính thức](https://github.com/STEMpedia/Dabble) giúp đối chiếu đúng dự án.

## Khi nhà cung cấp gửi thư viện ZIP

1. Xác nhận ZIP là **thư viện**, không phải ZIP tài liệu hoặc cả thư mục chương trình xe.
2. Chọn **Sketch → Include Library → Add .ZIP Library**.
3. Chọn ZIP và chờ cài xong.
4. Mở lại sketch và Verify.

Tệp .ino của xe mở bằng File → Open; không cài như thư viện. Nếu phải giải nén thủ công, xem [cách cài thư viện của Arduino](https://support.arduino.cc/hc/en-us/articles/5145457742236-Install-libraries-in-the-Arduino-IDE) và Sketchbook location trong Preferences. Người mới nên ưu tiên Library Manager khi có thư viện đúng ở đó.

## Khi Verify báo lỗi

| Thông báo | Hiểu và kiểm tra |
| --- | --- |
| Servo.h / Dabble.h: No such file or directory | IDE chưa tìm thấy header; kiểm tra cài đúng thư viện và tên include |
| Multiple libraries were found | Có nhiều bản; xem dòng IDE dùng thư mục nào, không vội xóa tất cả |
| Báo không hỗ trợ board/kiến trúc | Có thể chọn thư viện cho bo khác; kiểm tra Nano và tác giả |
| Cài xong nhưng lỗi vẫn còn | Đọc lỗi đầu tiên đầy đủ; có thể thiếu dependency hoặc sai sketch |

## Khi nào hoàn thành?

Bạn cài đúng thư viện, Verify được sketch và biết Verify mới chỉ kiểm tra phần mềm. Tiếp tục [servo](bai-giang/04-servo.md) hoặc [Bluetooth](bai-giang/09-bluetooth.md) theo bài đang học.
