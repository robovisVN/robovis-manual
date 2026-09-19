# Bài 6. Cài phần mềm và chạy chương trình

**Mục tiêu:** phân biệt cài phần mềm, mở phần mềm và chuẩn bị môi trường; biết dùng `sudo` khi hướng dẫn yêu cầu.

**Chuẩn bị:** đã biết Terminal và đường dẫn. Phần cài công cụ cần Ubuntu có Internet; phần chạy chương trình mẫu không cần robot.

## 1. Cài và chạy là hai việc khác nhau

Cài phần mềm là đưa chương trình cùng các thành phần cần thiết vào máy. Chạy phần mềm là mở chương trình đã có để làm việc.

| Ví dụ | Đang làm gì? | Khi nào thực hiện? |
| --- | --- | --- |
| `sudo apt install nano` | Cài công cụ sửa văn bản nano | Khi công cụ chưa có hoặc cần cập nhật |
| `nano ghi_chu.txt` | Mở nano để sửa tệp | Mỗi lần cần sửa tệp |
| `source /opt/ros/humble/setup.bash` | Nạp thiết lập ROS 2 cho Terminal hiện tại | Khi Terminal chưa có môi trường ROS 2 |
| `ros2 topic list` | Chạy công cụ xem tên các kênh dữ liệu ROS 2 | Khi muốn kiểm tra hệ thống |

Tắt máy rồi mở lại không có nghĩa phải cài lại toàn bộ phần mềm. Một số chương trình và thiết lập môi trường cần được khởi chạy hoặc nạp lại.

## 2. `sudo` và mật khẩu

`sudo` cho phép chạy một lệnh với quyền quản trị khi tài khoản của bạn được cấp quyền. Công việc như cài phần mềm thường cần quyền này.

Khi lệnh hỏi mật khẩu, Terminal có thể hiện:

```text
[sudo] password for robovis:
```

Nhập mật khẩu Ubuntu của tài khoản, rồi nhấn **Enter**. **Màn hình không hiện chữ hoặc dấu sao khi gõ mật khẩu là bình thường.**

Nếu mật khẩu sai, đọc thông báo rồi nhập lại. Không tự thêm `sudo` vào mọi lệnh để chữa lỗi. Các ví dụ đọc tệp, chạy chương trình Python và kiểm tra ROS 2 trong bài này không cần `sudo`.

## 3. Kiểm tra công cụ trước khi cài

Chạy từng lệnh:

```bash
nano --version
```

```bash
python3 --version
```

**Kết quả cần thấy:** thông tin phiên bản. Nếu các công cụ đã có, chuyển sang mục 5. Nếu máy báo `command not found`, đọc mục 4 để cài công cụ còn thiếu.

## 4. Cài công cụ còn thiếu bằng `apt`

`apt` là công cụ lấy và cài các gói phần mềm từ nguồn đã cấu hình trong Ubuntu.

### Bước 1. Kết nối Internet

Nếu đang nối Wi-Fi robot, hãy chuyển về mạng có Internet. Với máy ảo, không chỉ Windows mà **Ubuntu cũng phải truy cập Internet được**. Thử mở một trang web trong trình duyệt Ubuntu.

### Bước 2. Cập nhật danh sách gói

```bash
sudo apt update
```

Lệnh này tải lại danh sách gói có sẵn. Nó không có nghĩa là nâng cấp phiên bản Ubuntu. Chờ dấu nhắc quay lại và kiểm tra có lỗi tải dữ liệu không trước khi tiếp tục.

### Bước 3. Cài đúng công cụ cần dùng

Nếu thiếu nano:

```bash
sudo apt install nano
```

Nếu thiếu Python 3:

```bash
sudo apt install python3
```

Nếu bài Terminal hoặc kiểm tra mạng báo thiếu `ping`:

```bash
sudo apt install iputils-ping
```

Khi có câu hỏi **Do you want to continue? [Y/n]**, đọc danh sách thay đổi. Nếu đúng phần mềm cần cài, nhập `y` rồi nhấn **Enter**. Sau khi hoàn tất, chạy lại lệnh kiểm tra phiên bản hoặc thử `ping -c 2 127.0.0.1`.

Nếu báo đang có tiến trình khác giữ khóa `apt`, chờ trình cài/cập nhật đó hoàn tất. Không xóa tệp khóa để ép hai trình cài chạy cùng lúc.

## 5. Chạy một chương trình Python nhỏ

Đây là bài tập hiểu cách **chạy tệp chương trình**. Bạn không cần học Python trước và chương trình không điều khiển robot.

Tạo thư mục:

```bash
mkdir -p ~/hoc_ubuntu/bai_06
```

Mở tệp mới:

```bash
nano ~/hoc_ubuntu/bai_06/xin_chao.py
```

Nhập đúng dòng dưới đây vào nano:

```python
print("Xin chao! Toi da chay duoc chuong trinh tren Ubuntu.")
```

Lưu bằng **Ctrl + O**, **Enter**, rồi thoát bằng **Ctrl + X**. Chạy:

```bash
python3 ~/hoc_ubuntu/bai_06/xin_chao.py
```

**Kết quả cần thấy:**

```text
Xin chao! Toi da chay duoc chuong trinh tren Ubuntu.
```

Ở đây, `python3` là chương trình đọc và thực thi tệp `xin_chao.py`. Bạn không cần dùng `sudo` hoặc đổi quyền tệp khi chạy theo cách này.

## 6. Hiểu bước `source` trong tài liệu ROS 2

Phần này dành cho máy **đã cài ROS 2 Humble**, chẳng hạn máy ảo ROBOVIS. Máy Ubuntu mới cài có thể chưa có ROS 2; khi đó hoàn thành phần cài môi trường trong tài liệu robot trước.

Kiểm tra trong Terminal hiện tại:

```bash
printenv ROS_DISTRO
```

**Kết quả mong đợi với môi trường này:** `humble`. Nếu không in gì, biến môi trường chưa được đặt trong Terminal đó; chưa thể kết luận phần mềm không được cài.

Kiểm tra tệp thiết lập:

```bash
ls /opt/ros/humble/setup.bash
```

Nếu tệp tồn tại, nạp thiết lập:

```bash
source /opt/ros/humble/setup.bash
```

Chạy lại `printenv ROS_DISTRO`, rồi:

```bash
ros2 --help
```

**Kết quả cần thấy:** danh sách trợ giúp của công cụ `ros2`. Lệnh này không làm robot di chuyển.

`source` chỉ áp dụng thiết lập vào phiên Terminal hiện tại. Terminal mở mới cần được nạp thiết lập riêng, trừ khi cấu hình khởi động như `.bashrc` đã làm sẵn. Bản máy ảo ROBOVIS có thể đã chuẩn bị việc này.

### Workspace của robot là lớp riêng

ROS 2 chạy được chưa đảm bảo các gói riêng của robot đã được nạp. Với workspace theo cấu trúc `~/robot_ws`, kiểm tra:

```bash
ls ~/robot_ws/install/setup.bash
```

**Chỉ khi tệp này tồn tại**, chạy:

```bash
source ~/robot_ws/install/setup.bash
```

Nếu tệp không có, không tạo một tệp rỗng để cho hết lỗi. Workspace có thể nằm ở nơi khác hoặc chưa được chuẩn bị. Quay lại bài cài workspace của sản phẩm hoặc gửi thông báo lỗi để kiểm tra.

## 7. Nếu chưa chạy được

| Hiện tượng | Hướng kiểm tra |
| --- | --- |
| `Temporary failure resolving ...` khi dùng apt | Kiểm tra Internet và DNS của Ubuntu |
| `Unable to locate package ...` | Kiểm tra tên gói và kết quả `apt update` |
| Python báo không mở được tệp | Kiểm tra đường dẫn `xin_chao.py` |
| `ros2: command not found` | Kiểm tra nơi nhập lệnh, tệp thiết lập ROS 2 và lệnh `source` |
| `ROS_DISTRO` hiện tên khác `humble` | Kiểm tra môi trường theo tài liệu robot, chưa chạy lệnh cài chồng thêm phiên bản |

**Bạn đã hoàn thành bài này khi:** chạy được `xin_chao.py`, hiểu mật khẩu `sudo` và biết vì sao đôi khi cần `source`.

[← Bài 5](05-thu-muc-va-tep.md) · [Bài 7: Kết nối máy tính với robot →](07-ket-noi-robot.md)
