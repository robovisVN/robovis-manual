# Bài 3: Cài đặt Arduino IDE, driver CH340 và gói hỗ trợ ESP32

## 1. Giới thiệu

Sau khi chuẩn bị bo mạch ESP32, board mở rộng và các thiết bị cần thiết, bước tiếp theo là cài đặt môi trường lập trình trên máy tính.

Trong chuỗi bài học này, chúng ta sử dụng **Arduino IDE** để viết, biên dịch và nạp chương trình cho **ESP32 30P CH340 Type-C**.

Để máy tính có thể lập trình ESP32, cần chuẩn bị ba thành phần chính:

- **Arduino IDE:** Phần mềm viết và nạp chương trình.
- **Driver CH340:** Giúp hệ điều hành giao tiếp với chip USB–UART trên bo ESP32.
- **ESP32 Board Package:** Cung cấp công cụ biên dịch và nạp chương trình cho ESP32.

Ba thành phần này có chức năng khác nhau và cần được cấu hình phù hợp.

Trong bài học, chúng ta sẽ thực hiện:

- Tải và cài đặt Arduino IDE.
- Kết nối ESP32 với máy tính bằng USB Type-C.
- Kiểm tra và cài đặt driver CH340 khi cần.
- Cài đặt gói hỗ trợ ESP32 của Espressif.
- Chọn đúng bo mạch và cổng COM.
- Kiểm tra môi trường lập trình trước khi nạp chương trình đầu tiên.

Sau khi hoàn thành, máy tính sẽ sẵn sàng để lập trình ESP32.

## 2. Mục tiêu bài học

Sau bài học này, bạn có thể:

- Cài đặt và sử dụng giao diện cơ bản của Arduino IDE.
- Hiểu chức năng của driver CH340.
- Kiểm tra ESP32 đã được máy tính nhận diện hay chưa.
- Cài đặt gói hỗ trợ ESP32 trong Arduino IDE.
- Chọn đúng **ESP32 Dev Module** cho bộ xe đang sử dụng.
- Xác định đúng cổng COM của ESP32.
- Kiểm tra phiên bản ESP32 core đã cài đặt.
- Xử lý một số lỗi thường gặp trong quá trình cài đặt.

---

## 3. Cài đặt Arduino IDE

### 3.1. Arduino IDE là gì?

Arduino IDE (*Integrated Development Environment*) là môi trường phát triển phần mềm được sử dụng để lập trình các bo mạch Arduino và nhiều dòng vi điều khiển khác, trong đó có ESP32.

Arduino IDE cho phép chúng ta:

- Viết chương trình bằng ngôn ngữ C/C++ theo framework Arduino.
- Kiểm tra và biên dịch chương trình.
- Nạp chương trình vào ESP32.
- Theo dõi dữ liệu gửi từ ESP32.
- Quản lý thư viện và các gói hỗ trợ bo mạch.

Trong bộ tài liệu này, chúng ta sử dụng **Arduino IDE 2.x**.

### 3.2. Tải Arduino IDE

Truy cập trang tải phần mềm chính thức của Arduino:

https://www.arduino.cc/en/software

Tại trang tải xuống, lựa chọn phiên bản phù hợp với hệ điều hành đang sử dụng.

| Hệ điều hành | Phiên bản |
|---|---|
| Windows | Arduino IDE 2 dành cho Windows |
| Ubuntu/Linux | Arduino IDE 2 dành cho Linux |
| macOS | Arduino IDE 2 dành cho macOS |

Đối với Windows, nên sử dụng trình cài đặt phù hợp với hệ điều hành.

### 3.3. Cài đặt Arduino IDE trên Windows

Sau khi tải tệp cài đặt:

1. Mở tệp cài đặt Arduino IDE.
2. Chấp nhận các điều khoản sử dụng.
3. Chọn phạm vi cài đặt nếu trình cài đặt yêu cầu.
4. Chọn thư mục cài đặt hoặc giữ nguyên đường dẫn mặc định.
5. Nhấn **Install**.
6. Chờ quá trình cài đặt hoàn tất.
7. Mở Arduino IDE.

Trong lần khởi động đầu tiên, Arduino IDE có thể cần thêm thời gian để khởi tạo các thành phần cần thiết.

Nếu Windows yêu cầu cho phép cài đặt driver hoặc thành phần hỗ trợ, cần kiểm tra thông tin nhà phát hành trước khi xác nhận.

### 3.4. Làm quen với giao diện Arduino IDE

Sau khi mở Arduino IDE, bạn sẽ thấy các khu vực chính:

| Thành phần | Chức năng |
|---|---|
| Verify | Kiểm tra và biên dịch chương trình |
| Upload | Biên dịch và nạp chương trình |
| Board Selector | Chọn bo mạch và cổng kết nối |
| Code Editor | Khu vực viết chương trình |
| Boards Manager | Cài đặt gói hỗ trợ bo mạch |
| Library Manager | Cài đặt và quản lý thư viện |
| Serial Monitor | Theo dõi dữ liệu Serial |
| Output | Hiển thị thông báo biên dịch và nạp chương trình |

Hai thao tác được sử dụng thường xuyên nhất là:

**Verify:** Kiểm tra chương trình có biên dịch thành công hay không, chưa nạp chương trình vào ESP32.

**Upload:** Biên dịch và nạp chương trình vào ESP32.

Trong bài tiếp theo, chúng ta sẽ thực hành hai thao tác này với một chương trình cụ thể.

---

## 4. Cài đặt driver CH340

### 4.1. Driver CH340 là gì?

Bo ESP32 trong bộ xe sử dụng chip **CH340** để chuyển đổi giao tiếp USB sang UART.

Khi kết nối ESP32 với máy tính bằng cáp USB Type-C, chip CH340 giúp hệ điều hành tạo cổng giao tiếp Serial.

Trên Windows, cổng này thường xuất hiện dưới dạng:

```text
USB-SERIAL CH340 (COM5)
```

Trong đó, `COM5` chỉ là ví dụ. Số cổng COM thực tế phụ thuộc vào máy tính và cổng USB đang sử dụng.

**Lưu ý:** Driver CH340 không phải gói hỗ trợ lập trình ESP32. Đây là hai thành phần riêng biệt.

### 4.2. Kiểm tra driver CH340 trên Windows

Trước khi cài đặt driver, chúng ta nên kiểm tra máy tính đã nhận ESP32 hay chưa.

Thực hiện:

1. Kết nối ESP32 với máy tính bằng cáp USB Type-C có truyền dữ liệu.
2. Nhấn chuột phải vào nút **Start** trên Windows.
3. Chọn **Device Manager**.
4. Tìm mục **Ports (COM & LPT)**.
5. Mở rộng danh sách và kiểm tra thiết bị xuất hiện.

Nếu máy tính đã nhận ESP32, bạn có thể thấy:

```text
Ports (COM & LPT)
    USB-SERIAL CH340 (COM5)
```

Để xác định đúng cổng của ESP32:

1. Quan sát danh sách cổng COM.
2. Rút cáp USB khỏi ESP32.
3. Kiểm tra cổng nào biến mất.
4. Cắm lại cáp USB.
5. Xác định cổng xuất hiện trở lại.

Nếu cổng COM đã hoạt động bình thường, không cần cài lại driver.

### 4.3. Tải driver CH340

Nếu máy tính chưa nhận ESP32 hoặc Device Manager báo lỗi driver, cần cài đặt driver CH340.

Có thể tải từ trang của nhà sản xuất WCH:

https://www.wch.cn/downloads/ch341ser_exe.html

Ngoài ra, bộ tài liệu Robovis cung cấp tệp cài đặt:

[Tải CH341SER.ZIP từ bộ tài liệu Robovis](https://drive.google.com/file/d/11mAAeBN780_u6sukouse0D0uVT7j5VUu/view)

Đối với tệp ZIP trong bộ bàn giao:

1. Tải `CH341SER.ZIP` về máy tính.
2. Giải nén tệp ZIP.
3. Mở thư mục vừa giải nén.
4. Chạy tệp `SETUP.EXE`.
5. Chọn **Install** để cài đặt driver.
6. Chờ thông báo hoàn tất.

Tên CH341SER được sử dụng cho bộ driver hỗ trợ các chip thuộc dòng CH34x, bao gồm CH340.

### 4.4. Kiểm tra sau khi cài driver

Sau khi cài đặt:

1. Rút cáp USB khỏi ESP32.
2. Cắm lại cáp USB.
3. Mở Device Manager.
4. Kiểm tra mục **Ports (COM & LPT)**.

Nếu xuất hiện cổng `USB-SERIAL CH340 (COMx)` mà không có cảnh báo lỗi, máy tính đã nhận được giao tiếp USB–UART của bo.

Ghi nhớ số cổng COM để lựa chọn trong Arduino IDE.

**Lưu ý:** Bộ xe sử dụng CH340, vì vậy không cần cài driver CP2102 chỉ để phục vụ bo này. CP2102 là một loại chip USB–UART khác.

Trên Ubuntu và macOS, cách kiểm tra thiết bị Serial và quyền truy cập sẽ khác Windows. Không sử dụng tệp `SETUP.EXE` của Windows trên các hệ điều hành này.

---

## 5. Cài đặt gói hỗ trợ ESP32

### 5.1. Vì sao cần cài ESP32 Board Package?

Arduino IDE có thể hỗ trợ nhiều dòng vi điều khiển khác nhau.

Tuy nhiên, để lập trình ESP32, cần cài đặt gói hỗ trợ do Espressif cung cấp.

Gói này có tên:

**esp32 by Espressif Systems**

Sau khi cài đặt, Arduino IDE sẽ có các công cụ cần thiết để:

- Biên dịch chương trình cho ESP32.
- Sử dụng các thư viện và API của framework Arduino-ESP32.
- Nạp chương trình vào bộ nhớ Flash.
- Lựa chọn các cấu hình bo mạch ESP32.

### 5.2. Thêm đường dẫn ESP32 Board Manager

Mở Arduino IDE.

Thực hiện:

1. Chọn **File → Preferences** trên Windows.
2. Tìm mục **Additional Boards Manager URLs**.
3. Nhập đường dẫn sau:

```text
https://espressif.github.io/arduino-esp32/package_esp32_index.json
```

4. Nhấn **OK** để lưu cấu hình.

Nếu đã có các đường dẫn khác trong mục này, cần giữ nguyên và bổ sung đường dẫn ESP32, không xóa các đường dẫn đang sử dụng.

Đường dẫn trên giúp Arduino IDE tìm và tải thông tin gói hỗ trợ ESP32 từ Espressif.

### 5.3. Cài đặt ESP32 bằng Boards Manager

Sau khi thêm đường dẫn:

1. Mở **Boards Manager** từ thanh công cụ bên trái.
2. Nhập từ khóa `esp32` vào ô tìm kiếm.
3. Tìm gói **esp32 by Espressif Systems**.
4. Chọn phiên bản phù hợp.
5. Nhấn **Install**.
6. Chờ quá trình tải và cài đặt hoàn tất.

Quá trình cài đặt có thể mất vài phút tùy tốc độ Internet.

Sau khi cài đặt thành công, Boards Manager sẽ hiển thị gói ESP32 đã được cài.

### 5.4. Lựa chọn phiên bản ESP32 core

ESP32 Board Package có nhiều phiên bản, trong đó các phiên bản 2.x và 3.x có một số khác biệt về API.

Ví dụ, cách sử dụng PWM bằng LEDC đã có thay đổi giữa hai dòng phiên bản.

Trong chuỗi bài học này, các ví dụ PWM được xây dựng theo **Arduino-ESP32 core 3.x**.

Vì vậy, nên sử dụng phiên bản 3.x ổn định, tương thích với các bài học.

Tuy nhiên, đối với chương trình robot hoàn chỉnh được bàn giao, cần kiểm tra phiên bản mà mã nguồn yêu cầu.

Không tự ý thay đổi phiên bản core nếu chương trình robot sử dụng các API hoặc thư viện chỉ tương thích với một phiên bản cụ thể.

Để kiểm tra phiên bản đang cài:

1. Mở Boards Manager.
2. Tìm `esp32 by Espressif Systems`.
3. Quan sát số phiên bản được hiển thị.

Nên ghi lại phiên bản này để thuận tiện khi kiểm tra lỗi sau này.

Tài liệu cài đặt chính thức:

https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html

---

## 6. Chọn đúng bo mạch ESP32

### 6.1. Lựa chọn ESP32 Dev Module

Sau khi cài đặt gói ESP32, chúng ta cần chọn loại bo mạch trong Arduino IDE.

Đối với **bộ xe ESP32 30P CH340 Type-C của Robovis**, hướng dẫn bàn giao sử dụng:

**ESP32 Dev Module**

Thực hiện:

1. Mở Arduino IDE.
2. Chọn **Tools → Board**.
3. Tìm nhóm bo mạch ESP32.
4. Chọn **ESP32 Dev Module**.

Tên nhóm menu có thể khác nhau đôi chút tùy phiên bản Arduino IDE và ESP32 core.

**Lưu ý:** CH340 là tên chip giao tiếp USB–UART, không phải tên bo mạch cần chọn trong Arduino IDE.

Tương tự, cổng USB Type-C cũng không quyết định loại bo mạch.

### 6.2. Phân biệt các dòng ESP32

Espressif cung cấp nhiều dòng vi điều khiển ESP32.

| Module hoặc dòng vi điều khiển | Lựa chọn bo mạch tham khảo |
|---|---|
| ESP32-WROOM-32 trên bo phát triển thông dụng | ESP32 Dev Module |
| ESP32-S3 | ESP32S3 Dev Module hoặc bo S3 tương ứng |
| ESP32-C3 | ESP32C3 Dev Module hoặc bo C3 tương ứng |

Đối với robot trong bộ tài liệu này, chúng ta sử dụng cấu hình **ESP32 Dev Module** theo hướng dẫn bàn giao.

Không chọn ESP32-S3 hoặc ESP32-C3 chỉ vì bo có cổng USB Type-C.

### 6.3. Các thông số cấu hình khác

Trong menu Tools, Arduino IDE có thể hiển thị thêm:

- Upload Speed.
- CPU Frequency.
- Flash Frequency.
- Flash Mode.
- Flash Size.
- Partition Scheme.
- PSRAM.

Đối với bài học đầu tiên, nên giữ các thông số mặc định phù hợp với **ESP32 Dev Module**, trừ khi tài liệu của đúng bo hoặc mã nguồn bàn giao yêu cầu cấu hình khác.

Không bật PSRAM nếu phần cứng không có PSRAM.

Không tự ý thay đổi Flash Size hoặc Partition Scheme khi chưa xác định được thông số bộ nhớ và yêu cầu chương trình.

---

## 7. Chọn cổng COM của ESP32

### 7.1. Cổng COM là gì?

Cổng COM là tên giao tiếp nối tiếp mà Windows cung cấp cho các thiết bị Serial.

Khi kết nối ESP32 thông qua CH340, máy tính có thể tạo một cổng COM để Arduino IDE giao tiếp với bo.

Ví dụ:

```text
USB-SERIAL CH340 (COM5)
```

Trong Arduino IDE, cần chọn đúng cổng này để nạp chương trình.

### 7.2. Cách chọn cổng COM

Thực hiện:

1. Kết nối ESP32 với máy tính.
2. Mở Arduino IDE.
3. Chọn **Tools → Port**.
4. Chọn cổng COM đã xác định trong Device Manager.

Ví dụ:

```text
Tools
  └── Port
       └── COM5
```

Nếu Arduino IDE không tự động nhận diện tên bo mạch, bạn vẫn có thể chọn thủ công **ESP32 Dev Module** và cổng COM tương ứng.

### 7.3. Kiểm tra lại sau khi đổi cổng USB

Số cổng COM có thể thay đổi khi:

- Cắm ESP32 sang cổng USB khác.
- Kết nối bo với máy tính khác.
- Hệ điều hành gán lại số cổng.
- Sử dụng thêm các thiết bị USB–UART khác.

Vì vậy, nếu Arduino IDE không kết nối được ESP32, cần kiểm tra lại mục **Tools → Port**.

---

## 8. Kiểm tra môi trường lập trình

Sau khi hoàn thành các bước cài đặt, cần xác nhận:

### 8.1. Kiểm tra Arduino IDE

Arduino IDE mở bình thường, có thể tạo và lưu chương trình mới.

### 8.2. Kiểm tra driver CH340

Trong Device Manager, ESP32 xuất hiện dưới dạng cổng COM và không có cảnh báo lỗi driver.

### 8.3. Kiểm tra gói ESP32

Boards Manager hiển thị:

```text
esp32 by Espressif Systems
Installed
```

Đồng thời có thể kiểm tra phiên bản core đang sử dụng.

### 8.4. Kiểm tra Board và Port

Arduino IDE được cấu hình:

| Thông số | Giá trị |
|---|---|
| Board | ESP32 Dev Module |
| Port | Cổng COM của CH340 |
| Board Package | esp32 by Espressif Systems |
| Cáp kết nối | USB Type-C có truyền dữ liệu |

Đến bước này, môi trường lập trình đã được chuẩn bị.

Việc biên dịch, nạp và chạy thử chương trình sẽ được thực hiện trong bài tiếp theo.

---

## 9. Một số lỗi thường gặp

### 9.1. Máy tính không nhận cổng COM

**Hiện tượng:**

Kết nối ESP32 với máy tính nhưng Device Manager không xuất hiện cổng COM mới.

**Nguyên nhân có thể:**

- Cáp USB chỉ hỗ trợ sạc.
- Driver CH340 chưa được cài đặt.
- Cổng USB gặp vấn đề.
- Bo ESP32 hoặc mạch USB–UART gặp lỗi.

**Cách xử lý:**

1. Thử cáp USB Type-C khác có hỗ trợ truyền dữ liệu.
2. Thử cổng USB khác trên máy tính.
3. Kiểm tra Device Manager.
4. Cài driver CH340 nếu thiếu.
5. Rút và cắm lại ESP32.

### 9.2. Arduino IDE không hiển thị ESP32 Dev Module

**Hiện tượng:**

Trong Tools → Board không tìm thấy ESP32 Dev Module.

**Nguyên nhân có thể:**

- Chưa cài ESP32 Board Package.
- Chưa thêm đường dẫn Board Manager.
- Quá trình cài đặt bị lỗi hoặc chưa hoàn tất.

**Cách xử lý:**

1. Kiểm tra Additional Boards Manager URLs.
2. Mở Boards Manager.
3. Tìm `esp32 by Espressif Systems`.
4. Cài đặt hoặc hoàn tất quá trình cài đặt.
5. Khởi động lại Arduino IDE nếu cần.

### 9.3. Arduino IDE không hiển thị cổng Port

**Hiện tượng:**

Không thấy cổng ESP32 trong Tools → Port.

**Cách xử lý:**

- Kiểm tra cáp USB.
- Kiểm tra driver CH340.
- Kiểm tra Device Manager.
- Thử kết nối lại ESP32.
- Khởi động lại Arduino IDE nếu cổng vừa được nhận diện.

Nếu Windows không nhận cổng COM, cần xử lý vấn đề kết nối USB–UART trước khi thử nạp chương trình.

### 9.4. Lỗi DEADLINE_EXCEEDED khi cài ESP32 core

Trong một số trường hợp, quá trình tải gói ESP32 có thể thất bại với thông báo:

```text
DEADLINE_EXCEEDED
```

Lỗi này có thể liên quan đến thời gian chờ tải xuống hoặc kết nối mạng.

Trước tiên, hãy kiểm tra kết nối Internet và thử cài đặt lại.

Nếu lỗi vẫn xảy ra, có thể điều chỉnh thời gian chờ tải xuống của Arduino CLI theo hướng dẫn trong tài liệu bàn giao.

**Bước 1:** Đóng Arduino IDE.

**Bước 2:** Mở thư mục cấu hình Arduino IDE trên Windows:

```text
C:\Users\<username>\.arduinoIDE\
```

Trong đó `<username>` là tên tài khoản Windows của bạn.

**Bước 3:** Sao lưu tệp:

```text
arduino-cli.yaml
```

**Bước 4:** Mở tệp bằng trình soạn thảo văn bản.

Tìm mục `network`. Nếu chưa có, bổ sung:

```yaml
network:
  connection_timeout: 600s
```

Nếu đã có mục `network`, chỉ bổ sung hoặc sửa `connection_timeout` bên trong mục đó, không tạo hai mục `network` trùng nhau.

**Bước 5:** Lưu tệp, mở lại Arduino IDE và thử cài đặt ESP32 core.

Lưu ý sử dụng khoảng trắng để thụt dòng trong YAML.

Thao tác này chỉ điều chỉnh thời gian chờ của kết nối tải xuống. Nó không thay thế việc cài driver CH340 hoặc lựa chọn đúng cổng COM.

### 9.5. Chọn nhầm driver hoặc loại bo

**Hiện tượng:**

Máy tính nhận cổng COM nhưng Arduino IDE không thể giao tiếp đúng với bo.

**Cần kiểm tra:**

- Bo thực tế sử dụng chip CH340.
- Đã chọn đúng cổng COM.
- Đã chọn ESP32 Dev Module.
- Đã cài đúng gói `esp32 by Espressif Systems`.
- Không chọn nhầm Arduino Nano, ESP32-S3 hoặc ESP32-C3.

Nếu đã xác nhận các thông số trên mà vẫn không nạp được, tiếp tục kiểm tra chế độ BOOT và thông báo lỗi nạp trong bài tiếp theo.

---

## 10. Bài tập thực hành

### Bài tập 1: Nhận diện môi trường lập trình

Mở Arduino IDE và xác định:

1. Nút Verify.
2. Nút Upload.
3. Boards Manager.
4. Library Manager.
5. Serial Monitor.
6. Menu Tools → Board.
7. Menu Tools → Port.

### Bài tập 2: Kiểm tra driver CH340

Thực hiện:

1. Kết nối ESP32 với máy tính.
2. Mở Device Manager.
3. Xác định cổng COM của ESP32.
4. Rút cáp USB và quan sát sự thay đổi.
5. Cắm lại ESP32 và xác nhận cổng COM.

### Bài tập 3: Kiểm tra ESP32 core

Mở Boards Manager và trả lời:

1. Gói hỗ trợ ESP32 có tên gì?
2. Nhà phát triển gói hỗ trợ là ai?
3. Phiên bản ESP32 core đang được cài đặt là bao nhiêu?
4. Vì sao cần cài ESP32 Board Package dù đã có Arduino IDE?

### Bài tập 4: Kiểm tra cấu hình

Trong Arduino IDE, xác nhận:

- Board: ESP32 Dev Module.
- Port: Đúng cổng COM của ESP32.
- ESP32 core: Đã cài đặt thành công.

Chưa cần nạp chương trình trong bài này.

---

## 11. Kiểm tra trước khi bắt đầu

Trước khi chuyển sang bài học tiếp theo, hãy đảm bảo:

- [ ] Đã cài đặt Arduino IDE.
- [ ] Đã kết nối ESP32 với máy tính bằng cáp USB Type-C có truyền dữ liệu.
- [ ] Máy tính nhận được cổng COM của CH340.
- [ ] Đã cài driver CH340 nếu cần.
- [ ] Đã thêm đường dẫn ESP32 Board Manager.
- [ ] Đã cài `esp32 by Espressif Systems`.
- [ ] Đã ghi nhớ phiên bản ESP32 core.
- [ ] Đã chọn ESP32 Dev Module.
- [ ] Đã chọn đúng cổng COM.
- [ ] Đã tắt nguồn động cơ để chuẩn bị nạp chương trình thử nghiệm.

---

## 12. Tổng kết

Qua bài học này, chúng ta đã hoàn thành việc cài đặt môi trường lập trình cho ESP32.

Những nội dung quan trọng bao gồm:

- Cài đặt Arduino IDE 2.
- Kiểm tra và cài đặt driver CH340.
- Xác định cổng COM của ESP32.
- Cài đặt gói hỗ trợ ESP32 của Espressif.
- Chọn đúng ESP32 Dev Module.
- Kiểm tra phiên bản ESP32 core.
- Xử lý một số lỗi thường gặp khi cài đặt.

Cần phân biệt rõ ba thành phần:

- **Arduino IDE:** Môi trường viết và nạp chương trình.
- **CH340 driver:** Giúp máy tính nhận giao tiếp USB–UART.
- **ESP32 Board Package:** Cung cấp công cụ lập trình dành cho ESP32.

Ở bài tiếp theo, chúng ta sẽ thực hành **viết và nạp chương trình đầu tiên, sử dụng Serial Monitor để quan sát dữ liệu và tìm hiểu cách nạp lại chương trình robot được bàn giao**.

---

[Bài trước: Chuẩn bị thiết bị](02-chuan-bi.md) · [Bài tiếp: Nạp chương trình và sử dụng Serial Monitor](04-nap-code-va-serial.md)