# Bài 3. Làm quen với giao diện Ubuntu

**Mục tiêu:** mở ứng dụng, tìm thư mục Home, chuyển cửa sổ và tắt Ubuntu đúng cách.

**Chuẩn bị:** đã đăng nhập Ubuntu theo [bài 2](02-chuan-bi-moi-truong.md). Chưa cần bật robot.

## 1. Nhận biết các khu vực trên màn hình

Trên Ubuntu Desktop 22.04 mặc định, bạn thường thấy:

| Khu vực | Vị trí thường gặp | Dùng để làm gì? |
| --- | --- | --- |
| **Activities** | Góc trên bên trái | Tìm ứng dụng và xem cửa sổ đang mở |
| Thanh ứng dụng, còn gọi là Dock | Mép trái | Mở nhanh Files, trình duyệt và ứng dụng đã ghim |
| Ngày, giờ | Thanh trên cùng | Xem lịch và thông báo |
| Menu hệ thống | Góc trên bên phải | Mạng, âm thanh, Settings và tắt máy |
| **Show Applications** | Nút hình các chấm trên Dock | Xem danh sách ứng dụng |

Vị trí có thể khác nếu máy đã được tùy chỉnh. Khi không thấy biểu tượng, dùng chức năng tìm tên ứng dụng ở bước tiếp theo.

## 2. Mở một ứng dụng bằng tên

1. Nhấp **Activities**.
2. Gõ `Files`.
3. Nhấp ứng dụng **Files** trong kết quả.

**Kết quả cần thấy:** một cửa sổ quản lý tệp mở ra. Bạn có thể thấy Home, Downloads, Documents và các thư mục khác.

Lặp lại với từ `Settings` để mở cài đặt. Cách tìm bằng tên giúp bạn không phải nhớ vị trí từng biểu tượng.

!!! tip "Phím Super là phím nào?"
    Trên nhiều bàn phím máy tính, **Super** chính là phím có logo Windows. Nhấn phím này trong Ubuntu thường mở màn hình Activities. Nếu đang dùng máy ảo và Windows nhận phím thay vì Ubuntu, hãy nhấp Activities bằng chuột.

## 3. Tìm thư mục Home và Downloads

Trong Files, chọn **Home** ở thanh bên trái. Home là thư mục riêng của tài khoản đang đăng nhập.

Mở thư mục **Downloads** nếu có. Đây thường là nơi chứa tệp tải bằng trình duyệt **bên trong Ubuntu**. Với giao diện ngôn ngữ khác, tên hiển thị có thể được dịch.

Nếu bạn đã tải `robovis.zip` bằng Windows, tệp đó nằm trong Windows. Không thấy nó ở Downloads của Ubuntu là điều bình thường.

### Thử tạo một thư mục bằng chuột

1. Quay lại **Home**.
2. Nhấp chuột phải vùng trống → **New Folder**. Bạn cũng có thể dùng **Ctrl + Shift + N**.
3. Đặt tên `hoc_ubuntu` rồi chọn **Create**.
4. Nhấp đúp để mở thư mục vừa tạo.

Nếu đã có `hoc_ubuntu`, mở thư mục đó, không cần tạo thêm. Các bài sau dùng chính thư mục này để thực hành.

**Kết quả cần thấy:** Files đang mở thư mục `hoc_ubuntu` trong Home. Chưa có tệp bên trong cũng đúng.

## 4. Chuyển giữa các cửa sổ

Giữ Files mở, sau đó mở Settings.

- Dùng **Alt + Tab** để chuyển qua lại giữa các ứng dụng.
- Dùng **Activities** để xem và chọn các cửa sổ đang mở.
- Nhấp biểu tượng ứng dụng trên Dock để quay lại ứng dụng đó.

**Thu nhỏ** cửa sổ và **đóng** ứng dụng là hai thao tác khác nhau. Sau này, Terminal chạy phần mềm robot cần được giữ mở; bạn có thể chuyển sang cửa sổ khác mà không đóng nó.

Các phím thao tác chung được mô tả thêm trong [hướng dẫn phím tắt Ubuntu](https://help.ubuntu.com/stable/ubuntu-help/shell-keyboard-shortcuts.html.en).

## 5. Chỉnh màn hình cho dễ đọc

1. Mở **Settings → Displays**.
2. Xem độ phân giải hiện tại ở **Resolution**.
3. Chọn độ phân giải phù hợp với màn hình, nếu có lựa chọn.
4. Nhấn **Apply**, rồi xác nhận giữ thay đổi nếu màn hình hiển thị tốt.

Với máy ảo, trước tiên thử phóng to cửa sổ VMware hoặc dùng **View → Full Screen**. Khả năng tự khớp kích thước phụ thuộc công cụ hỗ trợ đã cài trong máy ảo.

Nếu chỉ có ít lựa chọn độ phân giải, ghi nhận hiện tượng và tiếp tục bài học nếu vẫn đọc được. Không cần cài thêm trình điều khiển đồ họa để thực hành các thao tác cơ bản.

## 6. Xem kết nối mạng

Nhấp menu hệ thống góc trên bên phải để xem trạng thái kết nối.

- **Ubuntu cài trực tiếp:** thường có mục Wi-Fi nếu máy có card Wi-Fi được nhận.
- **Ubuntu trong VMware:** thường hiện **Wired**, dù máy Windows kết nối bằng Wi-Fi. Đây là card mạng ảo của Ubuntu.

Vì vậy, không thấy danh sách Wi-Fi trong máy ảo chưa phải là lỗi. [Bài 7](07-ket-noi-robot.md) sẽ hướng dẫn kiểm tra đường kết nối này.

## 7. Tắt Ubuntu sau khi học

Lưu các tệp đang sửa. Trong Ubuntu, mở menu hệ thống → **Power Off / Log Out → Power Off**, rồi xác nhận.

Nếu dùng máy ảo, đợi Ubuntu tắt xong mới đóng VMware. Không dùng nút tắt cưỡng bức máy ảo như thao tác kết thúc thông thường.

## Tự thực hành

Thử làm lại mà không nhìn từng bước:

- Mở Files và vào `hoc_ubuntu`.
- Mở Settings và xem About.
- Chuyển trở lại Files.
- Xác định Ubuntu đang dùng Wi-Fi trực tiếp hay card Wired của máy ảo.

**Bạn đã hoàn thành bài này khi:** tự mở được Files, Settings và tìm được thư mục thực hành.

[← Bài 2](02-chuan-bi-moi-truong.md) · [Bài 4: Làm quen với Terminal →](04-terminal.md)
