# Bài 8. Thực hành tổng hợp và xử lý lỗi

Ở các bài trước, chúng ta đã thực hiện riêng từng thao tác: mở ứng dụng, chuyển thư mục, sửa tệp và chạy lệnh. Khi làm việc với robot, những thao tác này thường xuất hiện trong cùng một quy trình.

Bài cuối sẽ kết hợp chúng thành một nhiệm vụ nhỏ: tạo hồ sơ thực hành của máy Ubuntu. Từ kết quả đó, chúng ta cũng học cách mô tả một lỗi để có thể kiểm tra hoặc nhờ hỗ trợ rõ ràng hơn.

**Mục tiêu:** tự thực hiện một công việc nhỏ từ đầu đến cuối, sau đó biết cách cung cấp thông tin khi gặp lỗi.

**Chuẩn bị:** đã học bài 3–6. Phần kiểm tra robot là tùy chọn nếu chưa có robot bên cạnh.

## 1. Nhiệm vụ thực hành

Chúng ta sẽ tạo một thư mục riêng, ghi nhận cấu hình Ubuntu vào tệp rồi tìm lại tệp bằng cả Terminal và Files. Cách làm này giống việc lưu thông tin một lần thử robot để đối chiếu về sau. Toàn bộ thao tác thực hiện trong **Ubuntu**.

<!-- tutorial-figure:kiem-tra-tung-lop -->
<figure class="tutorial-figure" markdown>

[![Ba lớp kiểm tra: mạng, môi trường ROS 2, dữ liệu và hiển thị.](../assets/illustrations/kiem-tra-tung-lop.svg)](../assets/illustrations/kiem-tra-tung-lop.svg)

<figcaption>Kiểm tra từ kết nối mạng tới môi trường và dữ liệu. Ghi lại lệnh đã chạy cùng thông báo lỗi ở lớp gặp vấn đề. Nhấp hình để xem lớn.</figcaption>
</figure>
<!-- /tutorial-figure:kiem-tra-tung-lop -->

### Bước 1. Tạo thư mục bài tổng hợp

```bash
mkdir -p ~/hoc_ubuntu/tong_hop
```

```bash
cd ~/hoc_ubuntu/tong_hop
```

```bash
pwd
```

**Kết quả cần thấy:** đường dẫn kết thúc bằng `/hoc_ubuntu/tong_hop`.

### Bước 2. Ghi nhận phiên bản Ubuntu

Trước khi ghi kết quả, hãy đọc thông tin từ máy đang sử dụng. Nhờ đó, hồ sơ phản ánh môi trường thực tế thay vì chép nguyên phiên bản trong ví dụ.

```bash
cat /etc/os-release
```

Tìm dòng `PRETTY_NAME` hoặc `VERSION_ID`. Môi trường theo bộ tài liệu này cần là Ubuntu **22.04**. Lệnh trên chỉ đọc thông tin hệ điều hành.

Tiếp tục:

```bash
whoami
```

Ghi nhớ tên tài khoản mà lệnh trả về.

### Bước 3. Tạo tệp kết quả

```bash
nano ket_qua.txt
```

Nhập mẫu sau và thay nội dung theo máy của bạn:

```text
Ten tai khoan: ghi ten vua thay
Phien ban Ubuntu: ghi phien ban vua thay
Dang dung: may ao VMware hoac Ubuntu truc tiep
Thu muc thuc hanh: ghi ket qua lenh pwd
Toi da biet dung Ctrl+C de dung lenh ping.
```

Lưu bằng **Ctrl + O**, **Enter**, rồi thoát bằng **Ctrl + X**. Kiểm tra:

```bash
cat ket_qua.txt
```

**Kết quả cần thấy:** các thông tin bạn vừa ghi, không còn nguyên phần yêu cầu “ghi tên vừa thấy”.

### Bước 4. Tìm lại tệp bằng giao diện

Mở **Files → Home → hoc_ubuntu → tong_hop**. Bạn cần thấy `ket_qua.txt`.

Đây là tệp thật trên Ubuntu. Khi khởi động lại máy ảo bình thường, tệp vẫn còn, trừ khi bạn chủ động xóa hoặc khôi phục máy ảo về trạng thái cũ.

### Bước 5. Đọc tệp từ vị trí khác

Tệp đã lưu có thể được đọc từ một thư mục khác nếu chúng ta cung cấp đúng đường dẫn. Hãy đưa Terminal về Home rồi tìm lại tệp bằng địa chỉ của nó:

```bash
cd ~
```

```bash
cat ~/hoc_ubuntu/tong_hop/ket_qua.txt
```

Nếu đọc được đúng nội dung, bạn đã hiểu cách dùng đường dẫn mà không phụ thuộc thư mục hiện tại.

## 2. Kiểm tra thêm nếu đã có môi trường robot

Nếu máy đã có ROS 2 và bạn có robot để thử kết nối, chúng ta có thể bổ sung thông tin môi trường vào lần kiểm tra. Nếu chưa có, bạn vẫn có thể hoàn thành phần thực hành tệp ở trên và quay lại phần này sau. Trước tiên, chạy:

```bash
printenv ROS_DISTRO
```

Nếu chưa hiện `humble`, quay lại phần môi trường ở [bài 6](06-cai-va-chay-phan-mem.md). Tiếp theo:

```bash
ros2 --help
```

Bạn cần thấy phần trợ giúp. Nếu robot đã bật và kết nối đúng mạng:

```bash
ip -br -4 addr
```

```bash
ping -c 4 192.168.4.1
```

Địa chỉ trên chỉ dùng khi robot vẫn sử dụng cấu hình mặc định. Kết quả IP và ping được đọc theo [bài 7](07-ket-noi-robot.md).

Những phép thử trên kiểm tra công cụ ROS 2 và kết nối mạng cơ bản. Để có dữ liệu cảm biến, chúng ta còn cần chạy chương trình khởi động hệ thống, thường gọi là **bringup**, theo tài liệu robot. Nếu bước đó chưa được thực hiện, việc chưa thấy topic robot chưa đủ để kết luận phần cứng có lỗi.

## 3. Gặp lỗi thì kiểm tra theo thứ tự nào?

Giả sử lệnh đọc tệp báo không tìm thấy đường dẫn. Cài lại phần mềm sẽ không giải quyết được việc Terminal đang đứng sai thư mục. Vì vậy, trước khi thay đổi cấu hình, chúng ta cần xác định bước đang lỗi thuộc phần thao tác, tệp, phần mềm hay mạng.

```mermaid
flowchart TD
    A["Một bước không chạy được"] --> B{"Đang nhập trong Terminal Ubuntu?"}
    B -->|"Không"| C["Mở đúng Terminal"]
    B -->|"Có"| D{"Lỗi tên lệnh hoặc đường dẫn?"}
    D -->|"Có"| E["Kiểm tra lệnh, pwd và ls"]
    D -->|"Không"| F{"Bước này cần kết nối mạng?"}
    F -->|"Có"| G["Kiểm tra Wi-Fi, IP và kết nối đích"]
    F -->|"Không hoặc vẫn lỗi"| H["Lưu nguyên thông báo để kiểm tra"]
    G --> H
```

Sơ đồ trên bắt đầu từ những thông tin có thể kiểm tra ngay trong cửa sổ đang dùng. Khi đã xác định được phần gặp vấn đề, chúng ta mới chọn thao tác sửa tương ứng và thử lại từng thay đổi.

## 4. Bảng tra lỗi nhanh

| Bạn thấy gì? | Có thể do đâu? | Làm gì tiếp? |
| --- | --- | --- |
| `command not found` | Gõ sai hoặc công cụ chưa được cài/nạp môi trường | Kiểm tra tên lệnh; xem bài 6 |
| `No such file or directory` | Sai vị trí hoặc tệp chưa có | Dùng `pwd`, `ls`; xem bài 5 |
| `Permission denied` | Không đủ quyền với tệp hoặc thiết bị | Ghi lại tệp/cổng bị lỗi; không tự thêm `sudo` vào lệnh ROS 2 |
| Nhập mật khẩu mà không thấy ký tự | Terminal đang ẩn mật khẩu | Gõ đủ mật khẩu rồi Enter |
| Terminal chưa trả dấu nhắc | Chương trình còn chạy hoặc chờ nhập | Đọc dòng cuối; giữ mở hoặc Ctrl + C tùy mục đích |
| Dấu `>` xuất hiện sau lệnh vừa gõ | Có thể thiếu dấu nháy hoặc cấu trúc lệnh chưa đóng | Ctrl + C rồi nhập lại lệnh đầy đủ |
| Robot Wi-Fi báo No Internet | Mạng robot chỉ dùng nội bộ | Giữ kết nối, thử ping robot |
| Windows có Internet, Ubuntu không có | Cấu hình card ảo/IP khác Windows | Xem lại Bridged và IPv4 trong Ubuntu |
| Tải tệp xong nhưng không tìm thấy | Tải ở hệ điều hành khác hoặc thư mục khác | Xác định trình duyệt Windows hay Ubuntu |
| `Package ... not found` trong ROS 2 | Chưa nạp workspace hoặc chưa có gói | Kiểm tra đúng môi trường và workspace của sản phẩm |

## 5. Gửi thông tin lỗi thế nào để dễ hỗ trợ?

Để người hỗ trợ hiểu cùng một tình huống, chúng ta cần cho biết đã làm bước nào, mong đợi điều gì và thực tế nhận được gì. Một ảnh chỉ có dòng “Error” thường chưa chứa đủ thông tin này. Hãy giữ cả lệnh đã chạy và đoạn thông báo liên quan trước, sau lỗi.

Bạn có thể dùng mẫu sau:

```text
Tôi đang làm bài: ...
Bước bị lỗi: ...
Tôi dùng Ubuntu trực tiếp / VMware: ...
Phiên bản Ubuntu: ...
Lệnh đã chạy: ...
Kết quả tôi mong đợi: ...
Thông báo thực tế: ...
Nếu lỗi mạng: Wi-Fi đang kết nối, IP Ubuntu, kết quả ping.
```

Trong Terminal, bôi chọn nội dung rồi **Ctrl + Shift + C** để sao chép. Hoặc chụp cửa sổ có cả câu lệnh và thông báo. Không cần gửi mật khẩu Wi-Fi cá nhân hay mật khẩu tài khoản.

## 6. Bạn đã sẵn sàng học phần robot chưa?

Nếu mục tiêu là hiểu phần mềm trước khi vận hành robot, học tiếp [Robot và ROS 2 cơ bản](../kien-thuc-nen/robot-ros2/index.md): bài truyền nhận mẫu không cần robot. Nếu muốn sử dụng robot ngay, làm theo các bước sản phẩm bên dưới.

Để sử dụng robot, chuyển sang khu vực [ESP32 LiDAR](../robot-esp32-lidar/index.md) trên website. Làm bài [Khởi động và kiểm tra dữ liệu](../robot-esp32-lidar/03-van-hanh/02-khoi-dong-va-kiem-tra.md) trước, sau đó mới [Chạy thử lần đầu](../robot-esp32-lidar/03-van-hanh/01-chay-thu-lan-dau.md).

Nếu Ubuntu của bạn chưa có ROS 2 và workspace, hoàn thành các bài [Cài ROS 2](../robot-esp32-lidar/02-chuan-bi/01-yeu-cau-va-cai-ros2.md) và [Cài workspace](../robot-esp32-lidar/02-chuan-bi/02-cai-dat-workspace.md) của sản phẩm trước bước khởi động.

## Tài liệu đọc thêm

Sau khi hoàn thành bài thực hành, bạn có thể học thêm các thao tác Terminal qua [hướng dẫn dòng lệnh cho người mới của Ubuntu](https://ubuntu.com/tutorials/command-line-for-beginners).

## Tổng kết

Kết quả của nhóm bài Ubuntu là khả năng tự thực hiện và kiểm tra một chuỗi thao tác trên máy tính: mở đúng môi trường, tạo và tìm lại tệp, chạy chương trình, đọc thông báo và kiểm tra mạng khi cần. Với nền tảng này, chúng ta có thể chuyển sang tìm hiểu cách các chương trình robot trao đổi dữ liệu trong ROS 2.

[← Bài 7](07-ket-noi-robot.md) · [Quay lại lộ trình Ubuntu cơ bản](index.md)
