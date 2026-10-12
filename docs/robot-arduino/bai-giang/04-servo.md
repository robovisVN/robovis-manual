# Bài 4: Điều khiển servo SG90

**Mục tiêu:** đưa servo về vị trí giữa rồi quay qua lại một khoảng nhỏ. Trước khi cho cảm biến quét trái/phải, bạn cần chắc rằng servo nhận đúng lệnh và gá không bị kẹt.

## Servo làm gì trên xe?

Servo SG90 là động cơ có phần điều khiển vị trí bên trong. Với servo vị trí, bạn ra lệnh một góc, servo sẽ cố giữ ở góc đó. Trên bộ xe, servo quay gá HC-SR04 để cảm biến nhìn sang hai bên.

Servo khác motor bánh xe: motor bánh chạy liên tục theo chiều và mức điện bạn điều khiển; servo vị trí dùng để đặt một vị trí. Các ví dụ ở đây không áp dụng nguyên xi cho servo đã sửa thành loại quay liên tục.

## Trước khi làm

- Bạn đã nạp được mã LED ở [bài 3](03-led.md).
- Cài **Servo của Arduino** theo [hướng dẫn thêm thư viện](../06-cai-thu-vien.md).
- Ngắt nguồn motor. Thử servo rời trước, hoặc tháo cơ cấu tải khi kiểm tra lần đầu.

Nếu servo đã gắn trên xe, xem [ảnh gá trong tài liệu bàn giao](../03-lap-rap.md). Ốc quá dài/vặn quá sâu có thể chạm vỏ servo, làm cơ cấu không quay được dù mã đúng.

## Bước 1. Hiểu ba dây của servo

| Dây | Vai trò | Kết nối trong bài |
| --- | --- | --- |
| Signal | Nhận lệnh góc từ Nano | A5, đúng chân servo của bộ xe |
| VCC | Cấp điện cho servo | Nguồn đúng thông số servo, thường nguồn 5 V đã ổn áp cho SG90 phù hợp |
| GND | Đường chung của nguồn và tín hiệu | GND nguồn servo nối với GND Nano |

Màu dây thường giúp nhận diện, nhưng cần xác nhận theo đúng servo. Không cắm theo màu nếu đầu nối đã được đổi thứ tự.

Trong mạch học, Nano lấy nguồn USB, servo lấy nguồn tải phù hợp. **Chỉ nối chung GND**, không nối cực dương nguồn servo vào 5V Nano khi Nano đang cấp USB trong sơ đồ thử này. Nguồn motor hoặc pin nhiều cell không đưa trực tiếp vào dây VCC servo.

**Kết quả cần thấy trước khi cấp điện:** Signal ở A5, có GND chung, đúng điện áp nguồn servo và cơ cấu có khoảng trống để quay.

## Bước 2. Đưa servo về giữa

Tạo sketch `NanoServo`, chép:

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

Verify, Upload khi nguồn motor đã ngắt. Cấp nguồn servo theo sơ đồ đã kiểm tra.

| Dòng mã | Ý nghĩa |
| --- | --- |
| #include <Servo.h> | Cho sketch dùng các lệnh của thư viện Servo |
| Servo servoThu | Đặt tên servo đang điều khiển là servoThu |
| servoThu.attach(A5) | Chọn A5 làm chân tín hiệu |
| servoThu.write(90) | Yêu cầu góc 90°, vị trí giữa để bắt đầu |

**Kết quả cần thấy:** nếu đang lệch giữa, servo chuyển tới vị trí gần giữa rồi giữ ở đó. Nếu ban đầu đã giữa, nó có thể gần như không di chuyển. Đừng kết luận lỗi chỉ vì không thấy quay nhiều.

## Bước 3. Thử một khoảng quay nhỏ

Giữ các dòng phía trên, thay **chỉ phần loop** bằng:

```cpp
void loop() {
  servoThu.write(75);
  delay(1000);
  servoThu.write(105);
  delay(1000);
}
```

Không thêm một loop thứ hai: sketch chỉ có một `void loop()`. Upload lại.

**Kết quả cần thấy:** servo luân phiên qua hai vị trí gần giữa, mỗi vị trí giữ một giây. Từ 75° tới 105° là khoảng yêu cầu 30°, không phải một vòng quay.

Các con số là góc yêu cầu, không phải phép đo góc thực. Gá, tay đòn và giới hạn servo quyết định hành trình sử dụng được. Chưa thử ngay 0°/180°; dừng nếu cơ cấu bị ép, rung mạnh, nóng hoặc chạm vật khác.

## Bước 4. Liên hệ với chương trình xe

Trong mã xe, chân vẫn là A5. Khi tránh vật cản, chương trình đặt các góc để cảm biến quét. Chỉ dùng góc lớn sau khi đã xác nhận gá quay tự do và dây cảm biến không kéo căng.

Thư viện Servo tạo xung phù hợp cho servo. Bạn chưa cần tính xung bằng tay. Trên Nano, thư viện dùng timer có thể ảnh hưởng PWM D9/D10; PWM motor của bộ xe nằm ở D5/D6 nên cần giữ đúng bảng chân khi ghép bài.

## Khi nào cần dừng và kiểm tra?

| Hiện tượng | Việc cần làm |
| --- | --- |
| Không biên dịch, thiếu Servo.h | Cài thư viện Servo rồi Verify lại; chưa sửa dây |
| Không chuyển vị trí | Kiểm tra Signal A5, nguồn và GND chung |
| Nano reset khi servo quay | Ngắt servo, kiểm tra nguồn tải và dòng cấp |
| Servo kêu/rung nhưng không quay | Tắt nguồn, kiểm tra ốc gá, cơ cấu và dây; chưa tăng góc |

## Khi nào hoàn thành?

Bạn đưa servo về giữa và thử được hai vị trí nhỏ, Nano không reset và cơ cấu không kẹt.

**Bài tập:** thay 75°/105° bằng 80°/100°, rồi mô tả khoảng quay thay đổi thế nào. Đổi thời gian giữ góc sang hai giây và kiểm tra chỉ tốc độ đổi vị trí bị ảnh hưởng.

[Bài trước](03-led.md) · [Lộ trình](../index.md) · [Bài tiếp: Động cơ và L298N](05-dong-co.md)
