# Cài môi trường Python trên Windows

Chỉ thực hiện phần này khi muốn chạy nhận diện vật thể bằng YOLO trên PC hoặc Laptop.

> **Quan trọng:** Hãy cài Python, thư viện và tải model khi máy tính đang kết nối Internet. Sau khi chuẩn bị xong mới chuyển sang Wi-Fi `ESP32-Car-01`, vì Wi-Fi của robot không cung cấp Internet.

## 1. Cài Python

1. Truy cập [trang tải Python cho Windows](https://www.python.org/downloads/windows/).
2. Tải Python 64 bit. Khuyến nghị dùng Python 3.11 cho bộ chương trình này.
3. Mở tệp cài đặt.
4. Đánh dấu **Add python.exe to PATH**.
5. Chọn **Install Now**.

Mở Command Prompt và kiểm tra:

```bat
py --version
```

Nếu lệnh hiển thị phiên bản Python, quá trình cài đặt đã thành công.

## 2. Tạo môi trường riêng

Giả sử thư mục chương trình có tên `ESP32_Camera_YOLO`, mở thư mục đó trong File Explorer, nhấp vào thanh địa chỉ, gõ `cmd` rồi nhấn Enter.

Chạy:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

Khi môi trường hoạt động, đầu dòng lệnh sẽ xuất hiện `(.venv)`.

## 3. Cài thư viện

Chạy lần lượt:

```bat
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python numpy requests pillow websocket-client
```

Quá trình cài `ultralytics` và PyTorch có thể mất nhiều thời gian. Không đóng cửa sổ Command Prompt khi đang cài.

## 4. Kiểm tra

Chạy:

```bat
python -c "import cv2, requests, PIL, websocket, ultralytics; print('OK')"
```

Nếu hiện `OK`, các thư viện chính đã sẵn sàng.

Mỗi lần mở Command Prompt mới để chạy chương trình, cần vào đúng thư mục và kích hoạt lại môi trường bằng:

```bat
.venv\Scripts\activate.bat
```
