# Hướng dẫn cài đặt Arduino IDE và nạp chương trình cho Arduino Nano

## 1. Giới thiệu

Để lập trình và điều khiển xe robot Arduino Nano, trước tiên chúng ta cần cài đặt môi trường lập trình trên máy tính.

Trong bài học này, chúng ta sẽ sử dụng **Arduino IDE**, một phần mềm cho phép viết chương trình, biên dịch và nạp mã vào bo mạch Arduino.

Sau khi cài đặt thành công, chúng ta sẽ thực hiện chương trình đầu tiên để điều khiển đèn LED tích hợp trên Arduino Nano nhấp nháy.

Thông qua bài học, chúng ta sẽ tìm hiểu:

- Arduino IDE là gì và chức năng của phần mềm.
- Cách tải và cài đặt Arduino IDE trên Windows.
- Cách kết nối Arduino Nano với máy tính.
- Cách cài đặt gói hỗ trợ bo mạch Arduino Nano.
- Cách lựa chọn Board, Processor và cổng COM.
- Cách mở và biên dịch chương trình mẫu.
- Cách nạp chương trình vào Arduino Nano.
- Cách kiểm tra và xử lý những lỗi thường gặp.

**Mục tiêu thực hành:** Nạp thành công chương trình Blink và quan sát đèn LED tích hợp trên Arduino Nano nhấp nháy theo thời gian đã lập trình.

Hướng dẫn sử dụng Arduino IDE 2 trên Windows và bo mạch **Arduino Nano classic sử dụng ATmega328P**, tương ứng với bộ xe robot trong tài liệu.

## 2. Chuẩn bị thiết bị và phần mềm

### 2.1. Thiết bị cần chuẩn bị

| Thiết bị | Mục đích |
|---|---|
| Máy tính Windows | Cài đặt và sử dụng Arduino IDE |
| Arduino Nano ATmega328P | Bo mạch thực hành |
| Cáp USB dữ liệu phù hợp với Nano | Kết nối Nano với máy tính |
| Kết nối Internet | Tải phần mềm, gói bo mạch và driver nếu cần |

<AsyncImage query="Arduino Nano ATmega328P classic development board mini USB connector front view" aspectRatio="5:3" maxWidth="420px"/>

Arduino Nano là bo mạch vi điều khiển nhỏ gọn, sử dụng chip ATmega328P trên phiên bản classic.

Bo mạch có các chân vào/ra số, chân analog, chân PWM và các giao tiếp thường được sử dụng trong robot.

Đối với bộ xe trong tài liệu, Arduino Nano đóng vai trò điều khiển trung tâm, kết nối với động cơ, cảm biến và các module ngoại vi.

### 2.2. Lưu ý trước khi kết nối

Nếu sử dụng Arduino Nano đã lắp trên xe robot:

- Ngắt nguồn cấp cho động cơ.
- Kiểm tra dây kết nối và tránh chập nguồn.
- Ngắt các dây từ driver L298N nối vào D0 và D1 khi thực hành nạp chương trình, Serial Monitor.
- Chỉ kết nối USB với Nano trong bài thử LED đầu tiên.

Hai chân D0 và D1 được sử dụng cho giao tiếp Serial phần cứng, nên việc kết nối thêm thiết bị ngoại vi vào hai chân này có thể ảnh hưởng đến quá trình nạp và trao đổi dữ liệu.

Xem thêm [hướng dẫn chuẩn bị thiết bị](02-chuan-bi.md).

## 3. Tìm hiểu về Arduino IDE

### 3.1. Arduino IDE là gì?

Arduino IDE (Integrated Development Environment) là môi trường phát triển tích hợp dành cho việc lập trình các bo mạch Arduino và những bo mạch tương thích.

Phần mềm cho phép người dùng thực hiện các công việc:

1. Viết chương trình điều khiển.
2. Kiểm tra và biên dịch mã nguồn.
3. Kết nối với bo mạch Arduino.
4. Nạp chương trình vào vi điều khiển.
5. Theo dõi dữ liệu và thông báo thông qua Serial Monitor.

Arduino IDE hỗ trợ ngôn ngữ lập trình dựa trên C/C++ với các thư viện và hàm được thiết kế để thuận tiện cho việc lập trình vi điều khiển.

### 3.2. Giao diện Arduino IDE

<AsyncImage query="Arduino IDE 2 desktop application code editor verify upload toolbar screenshot" aspectRatio="16:9"/>

Các thành phần chính của Arduino IDE:

| Thành phần | Chức năng |
|---|---|
| Code Editor | Khu vực viết và chỉnh sửa chương trình |
| Verify | Kiểm tra và biên dịch chương trình |
| Upload | Biên dịch và nạp chương trình vào Arduino |
| Board Selector | Chọn bo mạch và cổng kết nối |
| Boards Manager | Cài đặt gói hỗ trợ các loại bo mạch |
| Library Manager | Cài đặt thư viện mở rộng |
| Serial Monitor | Hiển thị dữ liệu Arduino gửi đến máy tính |
| Output | Hiển thị tiến trình biên dịch, nạp và thông báo lỗi |

Trong bài học đầu tiên, chúng ta chủ yếu sử dụng Code Editor, Verify, Upload và Board Selector.

## 4. Cài đặt Arduino IDE

### 4.1. Tải Arduino IDE

Truy cập trang chính thức của Arduino:

https://www.arduino.cc/en/software

Tại đây, chọn phiên bản Arduino IDE 2 phù hợp với hệ điều hành Windows đang sử dụng.

Các bước thực hiện:

1. Mở trình duyệt trên máy tính.
2. Truy cập trang tải phần mềm Arduino.
3. Tìm mục Arduino IDE.
4. Chọn phiên bản dành cho Windows.
5. Tải bộ cài đặt về máy tính.

Nên sử dụng phiên bản Arduino IDE 2 ổn định từ trang chính thức.

### 4.2. Tiến hành cài đặt

Sau khi tải hoàn tất:

1. Mở tệp cài đặt Arduino IDE.
2. Chấp nhận các điều khoản sử dụng nếu được yêu cầu.
3. Chọn phạm vi cài đặt phù hợp.
4. Chọn thư mục cài đặt hoặc giữ đường dẫn mặc định.
5. Nhấn Install và chờ quá trình cài đặt hoàn tất.
6. Mở Arduino IDE.

Trong quá trình cài đặt, Windows có thể yêu cầu quyền cài đặt một số thành phần hoặc driver. Chỉ chấp thuận khi xác nhận đó là bộ cài từ nguồn đáng tin cậy.

### 4.3. Kiểm tra sau khi cài đặt

Sau khi mở Arduino IDE, cần quan sát được:

- Cửa sổ chỉnh sửa chương trình.
- Nút Verify có biểu tượng dấu kiểm.
- Nút Upload có biểu tượng mũi tên.
- Khu vực lựa chọn bo mạch.
- Thanh công cụ và các menu chức năng.

**Kết quả mong đợi:** Arduino IDE khởi động bình thường và sẵn sàng tạo chương trình mới.

Việc lập trình và nạp chương trình bằng Arduino IDE trên máy tính không yêu cầu tạo tài khoản Arduino.

## 5. Kết nối Arduino Nano với máy tính

### 5.1. Kết nối bằng cáp USB

Arduino Nano classic thường sử dụng cổng Mini-USB, tuy nhiên cần quan sát cổng thực tế trên bo mạch để lựa chọn đúng loại cáp.

Thực hiện:

1. Cắm đầu USB phù hợp vào Arduino Nano.
2. Kết nối đầu còn lại với máy tính.
3. Quan sát đèn nguồn trên Arduino.
4. Chờ Windows nhận diện thiết bị.

<AsyncImage query="Arduino Nano classic board connected to laptop USB mini USB cable" aspectRatio="5:3" maxWidth="420px"/>

Khi được cấp nguồn qua USB, đèn nguồn trên Arduino Nano thường sáng.

Tuy nhiên, đèn nguồn sáng không đồng nghĩa máy tính đã nhận đúng cổng giao tiếp. Chúng ta cần kiểm tra thêm trong Windows.

### 5.2. Kiểm tra cổng COM trong Device Manager

Trên Windows:

1. Nhấn chuột phải vào nút Start.
2. Chọn **Device Manager**.
3. Tìm mục **Ports (COM & LPT)**.
4. Mở danh sách các cổng đang được nhận diện.
5. Tìm thiết bị tương ứng với Arduino Nano.

Ví dụ, thiết bị có thể xuất hiện dưới tên:

```text
USB-SERIAL CH340 (COM4)
```

Hoặc một tên khác tùy chip giao tiếp USB trên bo mạch.

Trong ví dụ này, `COM4` là cổng giao tiếp mà Windows gán cho thiết bị.

Số COM có thể khác trên từng máy tính.

### 5.3. Xác định đúng cổng COM

Nếu máy tính có nhiều cổng COM, có thể xác định cổng của Arduino bằng cách:

1. Quan sát danh sách cổng trước khi kết nối.
2. Cắm Arduino Nano vào máy tính.
3. Kiểm tra cổng mới xuất hiện.
4. Rút cáp USB và xác nhận cổng đó biến mất.
5. Cắm lại Arduino để kiểm tra.

Cổng xuất hiện và biến mất tương ứng với thao tác kết nối thường là cổng cần chọn.

**Kết quả mong đợi:** Xác định được cổng COM của Arduino Nano.

## 6. Cài đặt driver USB nếu cần

### 6.1. Driver USB có vai trò gì?

Arduino Nano sử dụng chip giao tiếp USB để truyền dữ liệu giữa máy tính và vi điều khiển.

Một số bo mạch sử dụng chip CH340 hoặc CH341, trong khi các phiên bản khác có thể sử dụng chip USB khác.

Driver là phần mềm giúp Windows nhận diện và giao tiếp với thiết bị USB đó.

Nếu thiếu driver phù hợp, Arduino Nano có thể không xuất hiện trong danh sách cổng COM.

### 6.2. Kiểm tra chip USB

Trước khi cài driver, cần xác định loại chip giao tiếp USB trên bo mạch.

Với các bo Nano sử dụng CH340/CH341, có thể tải driver từ nhà sản xuất WCH:

https://www.wch.cn/downloads/ch341ser_exe.html

Không nên mặc định mọi Arduino Nano đều sử dụng CH340.

### 6.3. Cài đặt driver CH340/CH341

Nếu đã xác định bo mạch sử dụng chip CH340/CH341 và Windows chưa nhận diện:

1. Tải driver phù hợp.
2. Chạy bộ cài đặt.
3. Thực hiện các bước cài đặt.
4. Ngắt kết nối Arduino Nano.
5. Cắm lại USB.
6. Kiểm tra Device Manager.

Nếu driver hoạt động đúng, thiết bị sẽ xuất hiện dưới một cổng COM.

**Lưu ý:** Nếu Windows đã nhận đúng Nano và cổng COM hoạt động bình thường, không cần cài lại driver.

## 7. Cài đặt gói hỗ trợ Arduino Nano

### 7.1. Board package là gì?

Arduino IDE có thể lập trình nhiều loại bo mạch khác nhau.

Mỗi loại bo sử dụng vi điều khiển, bộ biên dịch và cách nạp chương trình phù hợp.

Để IDE có thể biên dịch và nạp chương trình cho Arduino Nano classic, chúng ta cần gói hỗ trợ:

**Arduino AVR Boards**

Gói này bao gồm các thành phần cần thiết để lập trình nhiều bo Arduino sử dụng vi điều khiển AVR.

Board package khác với thư viện điều khiển servo, cảm biến hoặc Bluetooth.

### 7.2. Cài đặt Arduino AVR Boards

Thực hiện:

1. Mở Arduino IDE.
2. Chọn biểu tượng **Boards Manager** ở thanh bên.
3. Nhập từ khóa `Arduino AVR Boards`.
4. Tìm gói **Arduino AVR Boards by Arduino**.
5. Nhấn Install nếu gói chưa được cài.
6. Chờ quá trình cài đặt hoàn tất.

Nếu gói đã được cài đặt, có thể tiếp tục sử dụng mà không cần cài lại.

### 7.3. Chọn loại bo mạch

Trong Arduino IDE, mở:

**Tools → Board → Arduino AVR Boards → Arduino Nano**

Sau khi lựa chọn, Arduino IDE sẽ sử dụng cấu hình tương ứng với Nano classic.

**Lưu ý:** Không chọn Arduino Nano Every hoặc Arduino Nano ESP32 vì đây là những bo mạch khác với Nano ATmega328P đang sử dụng trong tài liệu.

## 8. Cấu hình Processor và cổng COM

### 8.1. Chọn Processor

Sau khi chọn Arduino Nano, mở:

**Tools → Processor**

Chọn:

**ATmega328P**

Đây là cấu hình được sử dụng cho Arduino Nano trong bộ xe robot.

Một số bo Arduino Nano cũ hoặc bo tương thích có thể sử dụng bootloader cũ.

Nếu chọn đúng board, đúng cổng COM và kết nối USB bình thường nhưng quá trình nạp vẫn thất bại, có thể thử:

**ATmega328P (Old Bootloader)**

Bootloader là một chương trình nhỏ trong vi điều khiển, cho phép nhận và nạp chương trình mới thông qua giao tiếp phù hợp.

Việc sử dụng CH340 không có nghĩa chắc chắn phải chọn Old Bootloader. Hai yếu tố này độc lập với nhau.

### 8.2. Chọn cổng COM

Mở:

**Tools → Port**

Chọn cổng COM đã xác định trong Device Manager.

Ví dụ:

```text
COM4
```

Đây chỉ là ví dụ. Trên máy tính của bạn, số COM có thể khác.

### 8.3. Kiểm tra cấu hình trước khi nạp

| Thông số | Giá trị cần chọn |
|---|---|
| Board | Arduino Nano |
| Board package | Arduino AVR Boards |
| Processor | ATmega328P |
| Port | Cổng COM thực tế của Nano |
| Kết nối | USB dữ liệu |

Nếu sử dụng bo có bootloader cũ, lựa chọn Processor có thể cần chuyển sang ATmega328P (Old Bootloader).

**Kết quả mong đợi:** Arduino IDE đã được cấu hình đúng để biên dịch và nạp chương trình cho Nano.

## 9. Tìm hiểu cấu trúc chương trình Arduino

Trước khi nạp chương trình đầu tiên, chúng ta cần làm quen với cấu trúc cơ bản của một chương trình Arduino.

Chương trình Arduino thường có hai hàm chính:

```cpp
void setup() {

}

void loop() {

}
```

### 9.1. Hàm setup()

Hàm `setup()` được thực hiện một lần khi Arduino bắt đầu chạy chương trình, chẳng hạn sau khi cấp nguồn hoặc reset.

Hàm này thường được sử dụng để:

- Cấu hình chân vào/ra.
- Khởi tạo giao tiếp Serial.
- Khởi tạo cảm biến.
- Khởi tạo các module điều khiển.

Ví dụ:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}
```

Lệnh `pinMode()` cấu hình chân LED tích hợp làm đầu ra.

### 9.2. Hàm loop()

Hàm `loop()` được thực hiện lặp đi lặp lại trong quá trình Arduino hoạt động.

Ví dụ:

```cpp
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);

  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Chương trình bật LED, chờ một giây, tắt LED, chờ một giây và tiếp tục lặp lại.

Nhờ đó, đèn LED nhấp nháy liên tục.

## 10. Ví dụ 1: Nạp chương trình Blink

### 10.1. Chương trình Blink là gì?

Blink là chương trình mẫu cơ bản có sẵn trong Arduino IDE.

Chương trình sử dụng đèn LED tích hợp trên bo mạch để kiểm tra khả năng chạy mã.

Đối với Arduino Nano classic, đèn LED tích hợp thường được ký hiệu là **L** và kết nối với chân D13.

Chúng ta không cần lắp thêm LED bên ngoài để thực hiện bài này.

### 10.2. Mở chương trình Blink

Trong Arduino IDE, chọn:

**File → Examples → 01.Basics → Blink**

Arduino IDE sẽ mở chương trình Blink mẫu.

Có thể chọn **File → Save As** và lưu một bản với tên:

```text
NanoBlink
```

Ví dụ lưu trong thư mục:

```text
HocRobotNano
```

### 10.3. Chương trình Blink hoàn chỉnh

Bạn có thể sử dụng trực tiếp chương trình mẫu hoặc thay bằng mã sau:

```cpp
// ================= SETUP =================
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

// ================= LOOP =================
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);

  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

### 10.4. Giải thích chương trình

**Cấu hình chân LED**

```cpp
pinMode(LED_BUILTIN, OUTPUT);
```

Lệnh này cấu hình chân LED tích hợp làm chân xuất tín hiệu.

`LED_BUILTIN` là tên được Arduino định nghĩa cho chân LED tích hợp trên bo mạch.

Trên Arduino Nano classic, chân này tương ứng với D13.

**Bật LED**

```cpp
digitalWrite(LED_BUILTIN, HIGH);
```

Lệnh này đưa chân LED lên mức HIGH.

Với LED tích hợp của Nano classic, trạng thái này làm LED sáng.

**Chờ một giây**

```cpp
delay(1000);
```

Hàm `delay()` tạm dừng chương trình trong một khoảng thời gian tính bằng mili giây.

Trong đó:

- 1000 ms = 1 giây.
- 500 ms = 0,5 giây.
- 100 ms = 0,1 giây.

**Tắt LED**

```cpp
digitalWrite(LED_BUILTIN, LOW);
```

Lệnh này đưa chân LED xuống mức LOW và làm LED tắt.

Do các lệnh được đặt trong `loop()`, Arduino tiếp tục bật và tắt LED theo chu kỳ.

## 11. Biên dịch chương trình bằng Verify

### 11.1. Verify là gì?

Trước khi nạp chương trình vào Arduino, IDE cần biên dịch mã nguồn.

Biên dịch là quá trình chuyển chương trình đã viết thành dạng mã máy phù hợp với vi điều khiển.

Trong quá trình này, Arduino IDE cũng kiểm tra nhiều lỗi cú pháp, ví dụ:

- Thiếu dấu chấm phẩy.
- Sai tên hàm.
- Thiếu dấu ngoặc.
- Sử dụng biến chưa khai báo.
- Thiếu thư viện cần thiết.

### 11.2. Thực hiện Verify

Trong Arduino IDE:

1. Kiểm tra đã chọn Arduino Nano.
2. Kiểm tra Processor.
3. Nhấn nút **Verify** có biểu tượng dấu kiểm.
4. Chờ quá trình biên dịch hoàn tất.
5. Quan sát khu vực Output.

Nếu chương trình hợp lệ, IDE sẽ thông báo biên dịch thành công.

Một số thông tin về dung lượng chương trình và bộ nhớ có thể được hiển thị.

### 11.3. Phân biệt Verify và Upload

| Chức năng | Verify | Upload |
|---|---|---|
| Kiểm tra cú pháp và biên dịch | Có | Có |
| Tạo mã máy | Có | Có |
| Gửi chương trình vào Nano | Không | Có |
| Yêu cầu kết nối Nano để nạp | Không | Có |
| Làm Nano chạy chương trình mới | Không | Có, khi nạp thành công |

Như vậy, Verify thành công chưa có nghĩa chương trình đã được nạp vào Arduino.

## 12. Nạp chương trình vào Arduino Nano

### 12.1. Thực hiện Upload

Sau khi Verify thành công:

1. Kết nối Arduino Nano với máy tính.
2. Kiểm tra Board, Processor và Port.
3. Nhấn nút **Upload** có biểu tượng mũi tên.
4. Chờ Arduino IDE biên dịch và truyền chương trình.
5. Quan sát thông báo kết quả.

Trong quá trình nạp, không nên rút cáp USB hoặc ngắt kết nối bo mạch.

### 12.2. Kết quả mong đợi

Khi Upload thành công:

- Arduino IDE thông báo hoàn tất quá trình nạp.
- Arduino Nano bắt đầu chạy chương trình mới.
- Đèn LED L sáng khoảng một giây.
- Đèn LED L tắt khoảng một giây.
- Quá trình sáng/tắt tiếp tục lặp lại.

Đèn nguồn của Nano có thể vẫn sáng liên tục. Cần quan sát đúng đèn **L** để đánh giá kết quả chương trình Blink.

### 12.3. Arduino có cần kết nối máy tính liên tục không?

Sau khi nạp thành công, chương trình được lưu trong bộ nhớ chương trình của vi điều khiển.

Khi Arduino được cấp nguồn trở lại, chương trình sẽ tự chạy.

Vì vậy, sau khi nạp xong, Arduino Nano không cần tiếp tục kết nối với máy tính để thực hiện chương trình Blink.

Tuy nhiên, Arduino vẫn cần được cấp nguồn điện phù hợp để hoạt động.

## 13. Ví dụ 2: Thay đổi tốc độ nhấp nháy của LED

Ở ví dụ trước, LED sáng một giây và tắt một giây.

Bây giờ chúng ta sẽ thay đổi thời gian để LED nhấp nháy nhanh hơn.

### 13.1. Chương trình mẫu

Thay toàn bộ chương trình bằng:

```cpp
// ================= SETUP =================
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

// ================= LOOP =================
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(300);

  digitalWrite(LED_BUILTIN, LOW);
  delay(300);
}
```

### 13.2. Nạp lại chương trình

Thực hiện:

1. Nhấn Verify.
2. Chờ biên dịch thành công.
3. Nhấn Upload.
4. Quan sát LED L trên Nano.

### 13.3. So sánh kết quả

| Chương trình | Thời gian sáng | Thời gian tắt |
|---|---|---|
| Blink ban đầu | 1000 ms | 1000 ms |
| Blink đã sửa | 300 ms | 300 ms |

Sau khi sửa, LED nhấp nháy nhanh hơn.

**Kết quả mong đợi:** Nhịp nhấp nháy thay đổi rõ rệt sau khi nạp lại chương trình.

Điều này xác nhận rằng:

- Arduino IDE đã biên dịch chương trình mới.
- Máy tính đã truyền chương trình đến đúng Nano.
- Nano đang thực thi chương trình vừa nạp.

## 14. Một số lỗi thường gặp

### 14.1. Không xuất hiện cổng COM

**Hiện tượng:** Arduino IDE không hiển thị cổng kết nối phù hợp.

Nguyên nhân có thể gồm:

- Cáp USB chỉ hỗ trợ sạc, không truyền dữ liệu.
- Cáp hoặc cổng USB bị lỗi.
- Windows thiếu driver.
- Chip giao tiếp USB trên bo mạch gặp sự cố.

**Cách xử lý:**

1. Thử cáp USB dữ liệu khác.
2. Thử cổng USB khác trên máy tính.
3. Kiểm tra Device Manager.
4. Xác định chip giao tiếp USB.
5. Cài driver phù hợp nếu cần.

### 14.2. Lỗi không mở được cổng COM

Một thông báo có thể gặp:

```text
avrdude: ser_open(): can't open device
```

Nguyên nhân thường gặp:

- Chọn sai cổng COM.
- Cổng đang được chương trình khác sử dụng.
- Thiết bị bị ngắt kết nối.
- Driver hoặc kết nối USB gặp vấn đề.

**Cách xử lý:**

- Kiểm tra lại Tools → Port.
- Đóng Serial Monitor hoặc phần mềm khác đang chiếm cổng nếu cần.
- Rút và cắm lại Arduino.
- Thử Upload lại.

### 14.3. Lỗi không giao tiếp được với bootloader

Một thông báo có thể gặp:

```text
avrdude: stk500_recv(): programmer is not responding
```

Nguyên nhân có thể gồm:

- Chọn sai Board.
- Chọn sai Processor.
- Chọn sai cổng COM.
- Bootloader không phù hợp với cấu hình.
- Có thiết bị ngoại vi gây xung đột trên D0/D1.
- Kết nối USB không ổn định.

**Cách xử lý:**

1. Kiểm tra Board là Arduino Nano.
2. Kiểm tra Port.
3. Thử ATmega328P.
4. Nếu vẫn lỗi, thử ATmega328P (Old Bootloader).
5. Ngắt thiết bị ngoại vi khỏi D0/D1.
6. Thử lại cáp USB.

Chỉ cân nhắc các bước xử lý bootloader chuyên sâu sau khi đã loại trừ những nguyên nhân cơ bản.

### 14.4. Verify thành công nhưng LED không nhấp nháy

Kiểm tra:

- Đã nhấn Upload hay mới chỉ Verify?
- Upload có thực sự thành công?
- Có đang quan sát đúng LED L?
- Đã chọn đúng bo mạch và cổng COM?
- Chương trình có chứa các lệnh HIGH, LOW và delay trong `loop()` không?

Nếu cần, thay toàn bộ mã bằng chương trình Blink ở mục 10 rồi nạp lại.

### 14.5. LED nhấp nháy nhưng không đổi khi sửa chương trình

Nguyên nhân có thể là:

- Chưa Upload lại.
- Upload thất bại.
- Đang kết nối với bo mạch khác.
- Chương trình chưa được lưu hoặc chưa sửa đúng hai giá trị delay.

Cách kiểm tra:

1. Đổi cả hai giá trị `delay(1000)` thành `delay(300)`.
2. Nhấn Verify.
3. Nhấn Upload.
4. Quan sát lại LED L.

## 15. Bài tập thực hành

**Bài tập 1: Thay đổi thời gian nhấp nháy**

Sửa chương trình Blink để:

- LED sáng 500 ms.
- LED tắt 500 ms.

Nạp chương trình và quan sát kết quả.

**Bài tập 2: LED sáng và tắt không đều**

Viết chương trình để:

- LED sáng 100 ms.
- LED tắt 900 ms.

Quan sát sự khác biệt so với chương trình Blink ban đầu.

**Bài tập 3: LED nhấp nháy nhanh**

Sửa chương trình để LED sáng 100 ms và tắt 100 ms.

So sánh tốc độ nhấp nháy với các bài tập trước.

**Bài tập 4: Tìm hiểu Verify và Upload**

Trả lời các câu hỏi:

1. Verify có nạp chương trình vào Arduino không?
2. Upload có thực hiện biên dịch không?
3. Vì sao cần chọn đúng Board và Processor?
4. Cổng COM có chức năng gì?
5. Sau khi nạp thành công, Arduino có thể chạy mà không kết nối với máy tính không?

## 16. Tổng kết

Qua bài học này, chúng ta đã tìm hiểu và thực hành:

- Cách tải và cài đặt Arduino IDE.
- Cách kết nối Arduino Nano với máy tính.
- Cách xác định cổng COM.
- Cách cài đặt gói Arduino AVR Boards.
- Cách lựa chọn Arduino Nano và Processor ATmega328P.
- Cách sử dụng Verify để biên dịch chương trình.
- Cách sử dụng Upload để nạp chương trình.
- Cách điều khiển LED tích hợp bằng chương trình Blink.
- Cách thay đổi thời gian nhấp nháy và nạp lại chương trình.
- Cách kiểm tra và xử lý những lỗi cơ bản.

Sau khi hoàn thành, bạn cần đạt được ba kết quả:

1. Máy tính nhận diện được Arduino Nano.
2. Arduino IDE nạp chương trình thành công.
3. Đèn LED L thay đổi nhịp nhấp nháy theo chương trình đã sửa.

Đây là bước chuẩn bị quan trọng trước khi chuyển sang lập trình điều khiển servo, động cơ DC và đọc dữ liệu từ các cảm biến của xe robot.

---

[Bài tiếp: Viết chương trình Arduino đầu tiên](bai-giang/02-lap-trinh.md) · [Cài đặt thư viện](06-cai-thu-vien.md) · [Xử lý lỗi](07-chay-thu-va-xu-ly-loi.md) · [Lộ trình học](index.md)