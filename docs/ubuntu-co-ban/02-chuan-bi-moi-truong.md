# Bài 2. Chuẩn bị môi trường Ubuntu

**Mục tiêu:** mở được Ubuntu để thực hành các bài tiếp theo.

**Chuẩn bị:** máy tính và bộ máy ảo ROBOVIS nếu bạn đang dùng Windows.

## 1. Chọn đúng nhánh dành cho bạn

| Máy tính hiện tại | Việc cần làm |
| --- | --- |
| Windows, đã mở được máy ảo Ubuntu ROBOVIS | Kiểm tra phiên bản ở mục 4 |
| Windows, chưa có máy ảo | Thực hiện mục 2 và 3 |
| Đã cài Ubuntu trực tiếp | Bỏ qua VMware, thực hiện mục 4 |

Tài liệu robot hiện dùng **Ubuntu 22.04 và ROS 2 Humble**. Không chọn một phiên bản Ubuntu khác chỉ vì số phiên bản mới hơn: phần mềm robot cần đúng môi trường tương thích.

Bạn có thể gặp hướng dẫn dùng **WSL**, tức môi trường Linux tích hợp trong Windows. Series này đi theo máy ảo VMware đã dùng trong tài liệu ROBOVIS; chưa chuyển quy trình robot sang WSL.

## 2. Chuẩn bị trên Windows

### Bước 1. Kiểm tra máy tính

Đây là mức chuẩn bị trong hướng dẫn máy ảo ROBOVIS:

| Hạng mục | Tối thiểu | Nên có để sử dụng thoải mái hơn |
| --- | --- | --- |
| RAM của máy tính Windows | 8 GB | 16 GB |
| Dung lượng trống ở nơi lưu máy ảo | 30 GB | 50 GB hoặc hơn |
| Hệ điều hành của bộ hướng dẫn này | Windows 10/11 64-bit | Theo cấu hình máy đang sử dụng |

RAM trong bảng là RAM **toàn bộ máy tính**, không phải yêu cầu cấp toàn bộ số đó cho máy ảo. Giữ cấu hình máy ảo được cung cấp nếu chưa được hướng dẫn thay đổi.

### Bước 2. Tải đủ tệp khi còn Internet

Chuẩn bị hai thành phần từ bộ tài liệu được gửi cùng robot:

- Bộ cài **VMware Workstation**. Hướng dẫn gốc dùng bản **17.6.1**.
- Tệp **`robovis.zip`**, chứa máy ảo Ubuntu đã cài môi trường robot.

Nếu chưa có bộ tệp này, lấy từ ROBOVIS trước khi tiếp tục. Không dùng một máy ảo Ubuntu bất kỳ rồi coi đó là môi trường robot đã cài sẵn.

### Bước 3. Cài VMware

1. Mở bộ cài VMware trên Windows.
2. Đi qua các bước **Next**, đọc điều khoản và chọn chấp nhận nếu đồng ý.
3. Giữ vị trí cài mặc định nếu không có nhu cầu thay đổi.
4. Chọn **Install**, chờ hoàn tất rồi chọn **Finish**.
5. Khởi động lại Windows nếu bộ cài yêu cầu.

Màn hình kích hoạt hoặc điều khoản có thể khác giữa các bản VMware. Thực hiện theo bộ cài bạn được cung cấp; bài này không yêu cầu chọn một loại giấy phép cụ thể.

**Kết quả cần thấy:** mở được cửa sổ VMware và có lựa chọn **Open a Virtual Machine**.

## 3. Mở máy ảo Ubuntu

### Bước 1. Giải nén đầy đủ

Giải nén `robovis.zip` vào một thư mục dễ tìm, ví dụ `D:\ROBOVIS\Ubuntu` nếu máy có ổ D còn đủ dung lượng.

Giữ toàn bộ tệp đã giải nén cùng nhau. Tệp **`.vmx`** là cấu hình máy ảo; tệp **`.vmdk`** chứa dữ liệu ổ đĩa máy ảo. Không chỉ chép riêng tệp `.vmx` sang chỗ khác.

### Bước 2. Chọn tệp máy ảo

1. Mở VMware → **Open a Virtual Machine**.
2. Vào thư mục đã giải nén.
3. Chọn tệp có đuôi **`.vmx`**, tên hiển thị có thể là **Ubuntu 64-bit**.
4. Chọn **Open**.

Nếu Windows đang ẩn đuôi tệp, tìm mục có loại tệp **VMware virtual machine configuration**.

### Bước 3. Kiểm tra mạng và bật máy

Khi máy ảo còn tắt, vào **Edit virtual machine settings → Network Adapter**. Với cấu hình robot trong bộ tài liệu này, chọn **Bridged**, đồng thời bật **Connect at power on**.

Chọn **Power on this virtual machine**. Nếu VMware hỏi máy ảo đã được di chuyển hay sao chép, chọn **I copied it** cho bản sao bạn vừa nhận.

Nếu báo lỗi không hỗ trợ ảo hóa hoặc không thể khởi động, chụp nguyên thông báo lỗi. Đừng tiếp tục thay đổi hàng loạt tùy chọn của Windows hoặc BIOS theo một lỗi chưa xác định.

### Bước 4. Đăng nhập Ubuntu

Chọn tài khoản có sẵn trong máy ảo. Với **bản máy ảo ROBOVIS mô tả trong tài liệu gốc**, mật khẩu ban đầu là **`1`**, nếu chưa được đổi. Máy Ubuntu tự cài sử dụng mật khẩu của người cài máy, không mặc định là `1`.

Nhấp vào bên trong màn hình Ubuntu để nhập bàn phím. Khi cần trả chuột và bàn phím về Windows, nhấn **Ctrl + Alt** trong VMware.

**Kết quả cần thấy:** màn hình làm việc Ubuntu với thanh ứng dụng và menu hệ thống. Bạn không còn ở màn hình đăng nhập hoặc màn hình Home của VMware.

## 4. Kiểm tra Ubuntu đang dùng

Thực hiện **bên trong Ubuntu**:

1. Mở **Settings**.
2. Tìm mục **About**.
3. Xem dòng **OS Name**.

Với môi trường của series, dòng này cần thể hiện **Ubuntu 22.04 LTS** hoặc một bản cập nhật **22.04.x LTS**.

Nếu bạn tự cài Ubuntu, việc mở được desktop **chưa có nghĩa** đã có ROS 2 và phần mềm robot. Bạn vẫn học được bài 3–5. Bài 6 sẽ chỉ cách kiểm tra phần mềm trước khi sử dụng.

## 5. Những tình huống dễ nhầm

| Hiện tượng | Cách xử lý |
| --- | --- |
| Chỉ thấy danh sách tệp trong ZIP | Giải nén hết rồi mở `.vmx` bằng VMware |
| Chuột nằm trong Ubuntu, khó chuyển sang Windows | Nhấn **Ctrl + Alt** |
| Ubuntu hiển thị nhỏ trong cửa sổ | Thử phóng to cửa sổ VMware; xem tiếp phần màn hình ở bài 3 |
| Chưa có Internet trong Ubuntu | Chưa cần kết nối robot; kiểm tra mạng Windows và card mạng VMware ở bài 7 |
| Đã có Ubuntu nhưng không có phần mềm robot | Hoàn thành phần chuẩn bị ROS 2/workspace của tài liệu sản phẩm sau series này |

**Bạn đã hoàn thành bài này khi:** đăng nhập được Ubuntu và biết mình dùng máy ảo hay cài trực tiếp.

[← Bài 1](01-ubuntu-la-gi.md) · [Bài 3: Làm quen với giao diện →](03-giao-dien-ubuntu.md)
