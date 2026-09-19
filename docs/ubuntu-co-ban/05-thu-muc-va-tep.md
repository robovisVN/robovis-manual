# Bài 5. Thư mục, đường dẫn và tệp

**Mục tiêu:** biết mình đang ở đâu, vào đúng thư mục và tạo được một tệp ghi chú bằng Terminal.

**Chuẩn bị:** đã làm được [bài Terminal](04-terminal.md). Các thao tác dưới đây dùng thư mục thực hành `hoc_ubuntu` trong Home.

## 1. Đường dẫn là địa chỉ của thư mục hoặc tệp

Ví dụ `/home/robovis/hoc_ubuntu` có nghĩa là thư mục `hoc_ubuntu` nằm trong Home của tài khoản `robovis`.

Tên tài khoản của bạn có thể khác. Để không phải thay tên người dùng trong từng lệnh, các bài dùng ký hiệu **`~`**, đại diện cho Home của tài khoản đang đăng nhập.

| Cách viết | Ý nghĩa |
| --- | --- |
| `~` | Home của bạn |
| `~/hoc_ubuntu` | Thư mục `hoc_ubuntu` trong Home |
| `/home/robovis/hoc_ubuntu` | Địa chỉ đầy đủ trong ví dụ tài khoản `robovis` |
| `.` | Thư mục hiện tại của Terminal |
| `..` | Thư mục cha, tức lên một cấp |

**Đường dẫn tuyệt đối** bắt đầu từ `/`. **Đường dẫn tương đối** được hiểu từ thư mục Terminal đang đứng. Bạn sẽ thấy khác biệt ngay ở bài tập tiếp theo.

## 2. Về Home và xem thư mục đang có

Chạy từng lệnh:

```bash
cd ~
```

`cd` dùng để chuyển thư mục làm việc của Terminal.

```bash
pwd
```

**Kết quả cần thấy:** đường dẫn Home, ví dụ `/home/robovis`.

```bash
ls
```

`ls` liệt kê tên tệp và thư mục tại vị trí hiện tại. Danh sách có thể gồm `Downloads`, `Documents`, `hoc_ubuntu` hoặc những tên khác trên máy bạn.

Mở một thư mục trong Files **không tự chuyển** vị trí của Terminal đã mở trước đó. Khi chưa chắc, chạy `pwd`.

## 3. Tạo thư mục thực hành và vào bên trong

```bash
mkdir -p ~/hoc_ubuntu/bai_05
```

Lệnh này tạo `bai_05` trong `hoc_ubuntu`. Tùy chọn `-p` giúp tạo cả thư mục cha nếu còn thiếu và không báo lỗi chỉ vì thư mục đã có.

```bash
cd ~/hoc_ubuntu/bai_05
```

```bash
pwd
```

**Kết quả cần thấy:** đường dẫn kết thúc bằng `/hoc_ubuntu/bai_05`.

Trong Files, bạn cũng có thể mở Home → `hoc_ubuntu` → `bai_05` để nhìn thấy cùng vị trí. Terminal và Files đang nhìn vào cùng dữ liệu, chỉ khác cách thao tác.

## 4. Tạo một tệp ghi chú

Chạy:

```bash
nano ghi_chu.txt
```

`nano` là trình sửa văn bản trong Terminal. `ghi_chu.txt` là tên tệp muốn sửa; nếu chưa có, nano sẽ mở nội dung trống để bạn tạo tệp.

Nhập hai dòng sau **vào màn hình nano**, không chạy chúng như lệnh:

```text
Toi dang hoc Ubuntu.
Toi biet mo Terminal va tim thu muc Home.
```

Để lưu và thoát:

1. Nhấn **Ctrl + O**. Trong nano, chữ `^O` ở dưới màn hình có nghĩa là Ctrl + O.
2. Nhấn **Enter** để xác nhận tên `ghi_chu.txt`.
3. Nhấn **Ctrl + X** để thoát.

Nếu báo `nano: command not found`, xem phần cài `nano` ở [bài 6](06-cai-va-chay-phan-mem.md), rồi quay lại bước này. Bạn cũng có thể dùng ứng dụng **Text Editor**, nhập nội dung và dùng **Save As** lưu vào đúng `~/hoc_ubuntu/bai_05/ghi_chu.txt`.

## 5. Kiểm tra tệp vừa lưu

```bash
ls
```

Bạn cần thấy `ghi_chu.txt` trong danh sách. Để đọc nội dung:

```bash
cat ghi_chu.txt
```

**Kết quả cần thấy:** hai dòng vừa nhập. Lệnh `cat` ở đây chỉ đọc tệp văn bản, không mở chế độ chỉnh sửa.

Thử đi lên thư mục cha:

```bash
cd ..
```

Chạy `pwd`, bạn sẽ thấy vị trí kết thúc bằng `/hoc_ubuntu`. Từ đây, muốn đọc tệp cần ghi thêm thư mục con:

```bash
cat bai_05/ghi_chu.txt
```

Đó là đường dẫn **tương đối**. Nếu muốn đọc tệp từ vị trí bất kỳ, dùng đường dẫn bắt đầu từ Home:

```bash
cat ~/hoc_ubuntu/bai_05/ghi_chu.txt
```

## 6. Sao chép tệp trước khi sửa

Tạo bản sao bằng lệnh:

```bash
cp -i ~/hoc_ubuntu/bai_05/ghi_chu.txt ~/hoc_ubuntu/bai_05/ghi_chu_ban_sao.txt
```

`cp` nhận **nguồn trước, đích sau**. Tùy chọn `-i` hỏi lại nếu đích đã tồn tại; trong bài này, chọn `n` nếu không muốn ghi đè bản sao cũ.

Chạy:

```bash
ls ~/hoc_ubuntu/bai_05
```

**Kết quả cần thấy:** tệp gốc và tệp `ghi_chu_ban_sao.txt`. Bạn có thể mở bản sao bằng nano rồi sửa thử một câu để so sánh hai tệp.

## 7. Khi gặp đường dẫn trong tài liệu robot

| Ví dụ | Bạn cần hiểu gì? |
| --- | --- |
| `~/robot_ws` | Workspace của robot, nếu được cài theo cấu trúc này |
| `~/m_map.yaml` | Tệp mô tả bản đồ nằm trong Home |
| `~/m_map.pgm` | Tệp ảnh bản đồ tương ứng trong ví dụ |
| `~/.bashrc` | Tệp cấu hình của Bash; tên bắt đầu bằng dấu chấm nên thường bị ẩn |

Nhấn **Ctrl + H** trong Files để hiện hoặc ẩn tệp ẩn. Bài này chỉ giúp bạn nhận biết `.bashrc`; chưa cần sửa nó.

Tệp `.yaml` và `.pgm` của bản đồ có vai trò khác nhau. Khi sao lưu bản đồ, cần giữ các tệp liên quan cùng nhau theo bài quản lý bản đồ của robot.

## 8. Lỗi đường dẫn thường gặp

| Lỗi hoặc tình huống | Cách sửa |
| --- | --- |
| `No such file or directory` | Chạy `pwd` và `ls`; kiểm tra tên và vị trí |
| Gõ `Robot_ws` trong khi tên là `robot_ws` | Dùng đúng chữ hoa/thường |
| Thư mục có khoảng trắng | Đặt đường dẫn trong nháy kép, ví dụ `cd "$HOME/Thu muc hoc"` |
| Không thấy `ghi_chu.txt` ở nơi mong muốn | Xem có đang mở Home của Windows thay vì Ubuntu không |

**Mẹo:** nhấn **Tab** để Terminal hỗ trợ hoàn thành tên đường dẫn. Với tệp thực hành và bản đồ mới, đặt tên không dấu, dùng `_` thay khoảng trắng sẽ dễ thao tác hơn.

**Bạn đã hoàn thành bài này khi:** tạo, đọc và tìm lại được `ghi_chu.txt` từ một thư mục khác.

[← Bài 4](04-terminal.md) · [Bài 6: Cài phần mềm và chạy chương trình →](06-cai-va-chay-phan-mem.md)
