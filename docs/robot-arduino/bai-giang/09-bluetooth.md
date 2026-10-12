# Bài 9: Nhận lệnh điện thoại qua Bluetooth HM-10

**Mục tiêu:** nhấn các nút trong ứng dụng Dabble và xem Nano nhận đúng lệnh. Hãy kiểm tra đường truyền trước, rồi mới cho lệnh đó làm bánh xe chạy.

## Điện thoại, HM-10 và Nano làm gì?

| Thành phần | Vai trò |
| --- | --- |
| Điện thoại với Dabble | Hiển thị nút điều khiển và gửi dữ liệu khi bạn nhấn |
| HM-10 | Nhận dữ liệu Bluetooth và chuyển thành tín hiệu nối tiếp |
| Nano với thư viện Dabble | Đọc dữ liệu và biết nút nào được nhấn |
| Driver/motor | Thực hiện chuyển động khi chương trình gửi lệnh |

HM-10 dùng Bluetooth Low Energy, thường gọi là **BLE**. Cổng **UART** ở module là đường nối tiếp RX/TX đi tới Nano. Bạn chưa cần đọc gói dữ liệu bằng tay vì thư viện Dabble làm phần đó.

## Trước khi làm

Có HM-10 phù hợp bộ xe, điện thoại hỗ trợ ứng dụng Dabble và thư viện **Dabble của STEMpedia** trên IDE. Xem [bài thêm thư viện](../06-cai-thu-vien.md) nếu chưa cài.

Ngắt nguồn motor; ngắt IN1/IN2 của driver khỏi D0/D1 để xem log bằng USB. Không đổi chân HM-10 sang D0/D1; bộ xe dùng **A3/A2** cho đường này.

## Bước 1. Đọc RX/TX từ phía Nano

**TX** là phía gửi, **RX** là phía nhận. Dây phải nối bên gửi của thiết bị này sang bên nhận của thiết bị kia:

| HM-10 | Nano | Vì sao? |
| --- | --- | --- |
| TX | A3 | Nano nhận dữ liệu từ module |
| RX | A2, qua hạ mức nếu module yêu cầu | Nano gửi dữ liệu về module |
| GND | GND Nano | Chung mốc tín hiệu |
| VCC | Nguồn đúng module | Kiểm tra breakout thực tế, không mặc định mọi HM-10 nhận 5 V |

Trong `Dabble.begin(9600, A3, A2)`, A3/A2 lần lượt là **RX/TX của Nano**. Đây là giao tiếp nối tiếp được thư viện tạo trên các chân đó, thường gọi SoftwareSerial.

Nano TX mức 5 V không tự nối thẳng vào đầu RX chỉ chịu 3,3 V. Nếu breakout của bạn chưa có chuyển mức, dùng mạch phù hợp. Ví dụ cầu chia áp: A2 → điện trở 1 kΩ → HM-10 RX; từ điểm RX qua điện trở 2 kΩ xuống GND, cho mức gần 3,3 V với đầu vào 5 V. Kiểm tra sơ đồ breakout và mức điện áp trước khi cấp nguồn.

**Kết quả cần thấy trước khi nạp:** TX/RX nối chéo đúng, GND chung, nguồn và mức tín hiệu phù hợp module.

## Bước 2. Nạp chương trình chỉ in lệnh

Tạo sketch `NanoBluetoothDocLenh`, chép toàn bộ:

```cpp
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <Dabble.h>

void setup() {
  Serial.begin(9600);
  Dabble.begin(9600, A3, A2);
}

void loop() {
  Dabble.processInput();
  if (GamePad.isUpPressed()) {
    Serial.println("Tien");
  } else if (GamePad.isDownPressed()) {
    Serial.println("Lui");
  } else if (GamePad.isLeftPressed()) {
    Serial.println("Trai");
  } else if (GamePad.isRightPressed()) {
    Serial.println("Phai");
  } else {
    Serial.println("Dung");
  }
  delay(100);
}
```

Verify rồi Upload. Mở Monitor **9600 baud**. Bạn có thể thấy “Dung” trước khi kết nối ứng dụng; dòng đó **không chứng minh Bluetooth đã kết nối**.

Hai dòng define yêu cầu thư viện dùng phần GamePad và phải nằm trước include. `Dabble.begin()` chọn đường nối module, còn `Serial.begin()` chọn đường log USB. Cùng số 9600 nhưng là hai đường riêng; baud HM-10 phải phù hợp cấu hình 9600 trong mã.

## Bước 3. Kết nối Dabble trên điện thoại

1. Bật Bluetooth trên điện thoại, mở Dabble và cho ứng dụng các quyền kết nối cần thiết khi hệ điều hành yêu cầu.
2. Mở chức năng kết nối của Dabble, chọn đúng module HM-10 của xe.
3. Chờ ứng dụng báo kết nối, mở **GamePad** và chọn giao diện nút digital.
4. Giữ một nút hướng, nhìn Monitor trên máy tính.

Tên nút kết nối/quyền có thể khác theo phiên bản ứng dụng. Bộ bàn giao không quy định một tên hoặc mật khẩu Bluetooth cố định; không mặc định mọi module là HC-05 hoặc có mật khẩu 1234. Xem [hướng dẫn GamePad của STEMpedia](https://ai.thestempedia.com/docs/dabble-app/gamepad-module/) khi giao diện khác.

## Bước 4. Thử từng nút, không giữ nhiều nút cùng lúc

| Thao tác trên điện thoại | Kết quả cần thấy trong Monitor |
| --- | --- |
| Giữ Up | Tien |
| Giữ Down | Lui |
| Giữ Left | Trai |
| Giữ Right | Phai |
| Thả các nút hướng | Dung |

Chỉ khi **thông báo thay đổi theo chính nút bạn nhấn**, bạn mới xác nhận được luồng điện thoại → HM-10 → Nano.

`processInput()` cập nhật dữ liệu ứng dụng. `if / else if / else` chọn một nhánh. Nếu giữ nhiều nút, nhánh nằm trước được ưu tiên; bài này chưa xử lý tổ hợp nút.

## Bước 5. Chuyển từ in thông báo sang điều khiển xe

Chưa ghép motor khi bốn hướng còn chưa đọc đúng. Khi đã đọc đúng, xem [bài motor](05-dong-co.md) và bảng ý tưởng:

| Nhánh | Việc cần gọi trong sketch robot |
| --- | --- |
| Up / Down | Lệnh tiến / lùi |
| Left / Right | Lệnh rẽ hoặc quay theo thiết kế |
| Không giữ hướng | Lệnh dừng |

Trong sketch ghép, bỏ phần Hardware Serial vì D0/D1 lại dùng điều khiển driver. Giữ Dabble trên A3/A2. Để thử ngay bộ mã có sẵn, nạp `test_bluetooth.ino` theo [hướng dẫn sử dụng robot](../08-su-dung-robot.md); đừng cắm lại driver khi vẫn đang chạy sketch in log ở trên.

Mã đọc nút không tự biết mọi tình huống mất kết nối. Không coi đóng app/tắt Bluetooth là cách dừng chắc chắn; thử gần, kê bánh ban đầu và chủ động ngắt nguồn motor nếu xe không dừng.

## Nếu chưa nhận được lệnh

| Hiện tượng | Bắt đầu kiểm tra ở đâu? |
| --- | --- |
| Thiếu Dabble.h lúc Verify | Cài đúng Dabble của STEMpedia, không phải DabbleESP32 |
| Không tìm thấy module | Nguồn HM-10, Bluetooth/quyền app, đúng loại BLE |
| App báo kết nối nhưng log chỉ Dung | TX/RX, A3/A2, baud module, GamePad đúng chế độ |
| Log ký tự lạ | Monitor 9600; baud log USB khác vấn đề baud HM-10 |

## Khi nào hoàn thành?

Bốn nút tạo đúng bốn thông báo và thả nút đổi về “Dung”. Bạn giải thích được TX nối RX và hai đường giao tiếp trong sketch.

**Bài tập:** thêm một nhánh cho Start để in “Ve giua”. Chỉ thêm sau khi bốn hướng chạy đúng. Trong mã bàn giao, Cross tăng góc servo, Triangle giảm; đọc hàm kiểm tra thực tế vì comment có chỗ bị ngược.

[Bài trước](08-encoder.md) · [Lộ trình](../index.md) · [Bài tiếp: Làm quen PID](10-pid.md)
