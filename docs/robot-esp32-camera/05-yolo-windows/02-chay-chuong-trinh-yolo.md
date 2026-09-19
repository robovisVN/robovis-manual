# Chuẩn bị và chạy chương trình YOLO

## 1. Kiểm tra thư mục chương trình

Thư mục nên có cấu trúc tương tự:

```text
ESP32_Camera_YOLO/
├── esp32_yolo_gui.py
├── models/
│   └── yolov8n.pt
└── .venv/
```

Tên tệp Python có thể khác tùy theo gói do ROBOVIS cung cấp. Khi chạy lệnh, thay `esp32_yolo_gui.py` bằng tên thực tế.

Giữ thư mục `models` ở cùng cấp với tệp Python. Model `yolov8n.pt` là lựa chọn nhẹ và phù hợp để chạy thử trên máy tính không có GPU rời.

## 2. Kết nối với robot

1. Bật nguồn robot và chờ khoảng 10 giây.
2. Kết nối Windows với Wi-Fi `ESP32-Car-01`.
3. Nhập mật khẩu `abcd1234`.
4. Chấp nhận giữ kết nối dù Windows báo không có Internet.
5. Mở trình duyệt và kiểm tra `http://192.168.4.1:82` hoạt động.

Chỉ tiếp tục khi giao diện web và hình ảnh camera đã mở được.

## 3. Chạy chương trình

Mở Command Prompt tại thư mục chương trình rồi chạy:

```bat
.venv\Scripts\activate.bat
python esp32_yolo_gui.py
```

Nếu chương trình được cung cấp dưới dạng `.exe`, có thể mở trực tiếp tệp `.exe` và bỏ qua lệnh Python. Tuy nhiên, vẫn phải kết nối máy tính với Wi-Fi của robot.

## 4. Nhập đúng địa chỉ kết nối

Trong phần mềm, sử dụng:

```text
ESP32 IP:       192.168.4.1:81
Path:           /stream
Stream URL:     http://192.168.4.1:81/stream
WebSocket URL:  ws://192.168.4.1:82/ws
```

Đây cũng là các giá trị mặc định trong chương trình Python được cung cấp. Không xóa `:82` khỏi WebSocket URL.

## 5. Trình tự khởi động

1. Chọn model `models/yolov8n.pt`.
2. Giữ `Conf = 0.5`.
3. Giữ `Input size = 320`.
4. Nhấn **Reload model** nếu vừa đổi model.
5. Nhấn **Connect WS** để kết nối điều khiển robot.
6. Nhấn **Start** để mở camera và chạy nhận diện.

Khi hình ảnh xuất hiện cùng các khung nhận diện, chương trình đã hoạt động.
