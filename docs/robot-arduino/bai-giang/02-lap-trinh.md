# Bài 2: Viết và nạp chương trình Arduino đầu tiên

**Mục tiêu:** tự tạo một sketch và nhìn thấy thông báo do Nano gửi về máy tính. Bài này chưa điều khiển bánh xe, chưa cần học công thức hay thuật toán.

## Trước khi làm

Hoàn thành [cài IDE và nạp thử](../05-cai-arduino-ide.md). Có Nano, cáp USB dữ liệu và máy tính. Để học dễ nhất, dùng Nano riêng, chưa nối các thiết bị của robot.

Nếu giữ Nano trên xe, tắt nguồn motor và **ngắt dây từ D0/D1 tới IN1/IN2 của driver**. Hai chân này cũng dùng cho giao tiếp USB với máy tính; tắt nguồn motor thôi chưa giải phóng dây tín hiệu. Chụp lại trước khi rút để nối về đúng sau bài học.

## Bước 1. Tạo và lưu bài mới

Thực hiện trên **máy tính**, trong Arduino IDE:

1. Chọn **File → New Sketch**. Một trang mã mới xuất hiện.
2. Chọn **File → Save As** và đặt tên `NanoThongBao`.
3. Chọn thư mục học của bạn để lưu, chẳng hạn `Documents/HocRobotNano`.

IDE tạo thư mục `NanoThongBao` và tệp `NanoThongBao.ino` bên trong. Một bài học nên có một thư mục riêng để bạn mở lại bản đã chạy đúng.

**Kết quả cần thấy:** tên sketch đang mở là NanoThongBao. Chưa cần tự tạo tệp khác trong thư mục này.

## Bước 2. Hiểu hai phần có sẵn

Sketch mới thường có `setup()` và `loop()`:

| Phần | Khi nào chạy? | Ví dụ việc đặt ở đó |
| --- | --- | --- |
| setup() | Một lần khi Nano khởi động hoặc reset | Bật giao tiếp với máy tính |
| loop() | Lặp lại sau khi setup kết thúc | Gửi một thông báo mỗi giây |

Dấu `{` và `}` bao quanh các lệnh thuộc một phần. Dòng bắt đầu bằng `//` là ghi chú cho người đọc, Nano không thực hiện ghi chú đó. Chưa cần sửa tên setup hoặc loop.

## Bước 3. Chép chương trình nhỏ nhất

Nhấn **Ctrl+A** trong vùng soạn mã để chọn mã cũ, rồi thay bằng toàn bộ đoạn dưới:

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Xin chao tu Nano");
  delay(1000);
}
```

Đọc chương trình theo thứ tự:

1. `Serial.begin(9600);` mở đường gửi thông báo về máy tính. Số 9600 là tốc độ giao tiếp sẽ chọn ở cửa sổ xem.
2. `Serial.println("Xin chao tu Nano");` gửi câu trong dấu ngoặc kép, rồi xuống dòng.
3. `delay(1000);` chờ 1000 mili giây, tức một giây.
4. loop kết thúc rồi chạy lại, nên câu tiếp tục xuất hiện.

Trong mã mẫu, câu thông báo không dấu để dễ nhận ra khi xem log. Dấu `;` ở cuối mỗi lệnh là phần cú pháp; khi chép, giữ nguyên ngoặc kép, ngoặc tròn và dấu chấm phẩy.

## Bước 4. Kiểm tra rồi nạp vào Nano

1. Kiểm tra **Tools → Board → Arduino Nano**, **Processor → ATmega328P** và Port đúng Nano.
2. Nhấn **Verify**, nút dấu kiểm. Chờ IDE biên dịch xong.
3. Nếu không có lỗi, nhấn **Upload**, nút mũi tên.
4. Chờ báo nạp hoàn tất. Đừng rút cáp giữa chừng.

**Kết quả cần thấy:** Upload hoàn tất. Verify thành công chưa có nghĩa Nano đã nhận mã mới; bạn vẫn cần Upload.

## Bước 5. Mở cửa sổ xem thông báo

Chọn **Tools → Serial Monitor**. Đây là cửa sổ hiển thị các dòng Nano gửi qua USB. Tìm ô tốc độ giao tiếp và chọn **9600 baud**.

```text
Xin chao tu Nano
Xin chao tu Nano
Xin chao tu Nano
```

**Kết quả cần thấy:** mỗi giây thêm một dòng. Không cần nhập gì vào ô gửi của Monitor.

Nếu không thấy dòng mới, kiểm tra theo thứ tự: đã Upload chưa, có chọn đúng Port không, Monitor có đặt 9600 không. Nếu ký tự lạ, đổi Monitor về đúng 9600 trước khi sửa mã.

## Bước 6. Tự sửa một giá trị

Đổi `delay(1000)` thành `delay(500)`, nhấn Upload lại.

**Kết quả cần thấy:** các dòng xuất hiện nhanh hơn, khoảng hai dòng mỗi giây. Tiếp theo đổi câu trong dấu ngoặc kép thành tên của bạn và nạp lại.

Đây là chu trình bạn sẽ dùng trong các bài sau: **sửa → Verify → Upload → quan sát**. Sửa trên màn hình nhưng không Upload thì Nano vẫn chạy mã cũ.

## Thực hành thêm: dùng một biến

Sau khi câu thông báo đã chạy đúng, bạn có thể thay toàn bộ sketch bằng:

```cpp
int soLan = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(soLan);
  soLan = soLan + 1;
  if (soLan >= 10) {
    soLan = 0;
  }
  delay(1000);
}
```

**Biến** giống một ô nhớ có tên. `int soLan = 0` tạo ô nhớ chứa số nguyên, ban đầu là 0. `soLan = soLan + 1` lấy giá trị cũ, cộng 1 rồi lưu lại. `if` có nghĩa “nếu”; khi số đạt 10, mã đưa về 0.

**Kết quả cần thấy:** 0, 1, 2…9 rồi quay về 0. Bạn chưa cần học các kiểu số lớn hơn ở bài này.

## Khi gặp lỗi cú pháp

| Thông báo/hiện tượng | Thao tác đầu tiên |
| --- | --- |
| expected ';' | So dòng báo lỗi và dòng phía trên với mã mẫu; tìm dấu ; bị thiếu |
| expected '}' | Kiểm tra dấu đóng ngoặc của setup/loop |
| Tên Serial hoặc println bị báo lỗi | Kiểm tra viết hoa/thường đúng như mẫu |
| Không nạp được | Xem [lỗi cổng và nạp Nano](../07-chay-thu-va-xu-ly-loi.md), chưa sửa phần thuật toán |

## Khi nào hoàn thành?

- Bạn tự lưu, Verify và Upload được sketch.
- Monitor hiện đúng câu/số trong mã.
- Sửa thời gian và nạp lại làm nhịp thông báo thay đổi.

**Bài tập:** làm các dòng xuất hiện mỗi hai giây. Giải thích setup và loop khác nhau thế nào bằng chương trình vừa chạy.

[Bài trước](../01-gioi-thieu.md) · [Lộ trình](../index.md) · [Bài tiếp: Điều khiển LED](03-led.md)
