# Bổ sung mã nguồn, firmware và tài liệu tải

Trang người dùng nằm trong `docs/tai-xuong/`. Có một trang tổng và một trang cho từng sản phẩm. Tệp tải thực tế nằm trong `docs/downloads/`.

## 1. Năm gói tài liệu có sẵn

Chạy `python scripts/build_downloads.py` bằng môi trường Python của project để đóng gói lại bài viết và hình hiện có. Script chỉ ghi đè năm tệp `robovis-*-docs.zip`, không xóa các tệp tải khác.

Nếu phát hành tài liệu mới, cập nhật ngày và bản tài liệu trong bảng tại `docs/tai-xuong/index.md` và các trang con. Workflow GitHub đã tự chạy script trước khi triển khai.

## 2. Thêm tệp thực tế

Ví dụ bạn đã có gói mã nguồn Camera được kiểm tra:

1. Đặt tệp đó trong `docs/downloads/esp32-camera/`, dùng tên có phiên bản, không dấu và không có khoảng trắng.
2. Mở `docs/tai-xuong/robot-esp32-camera.md`.
3. Thay dòng trạng thái chưa có tệp bằng thông tin và đường dẫn thật. Ghi đúng loại chương trình: Camera + motor dùng với YOLO, hay bản kiểm tra toàn bộ cảm biến.
4. Thêm sản phẩm áp dụng, phiên bản thực, ngày phát hành và ghi chú tương thích từ bộ bàn giao. Không lấy ngày cập nhật tài liệu làm phiên bản firmware.
5. Thêm liên kết từ bài hướng dẫn cần sử dụng tệp đó tới trang tải tương ứng.

Cú pháp mẫu sau chỉ minh họa cấu trúc; thay tên và thông tin bằng tệp thật trước khi đưa vào bài:

```markdown
[Tải mã nguồn](../downloads/esp32-camera/TEN_TEP_THAT.zip){ .md-button .md-button--primary download="TEN_TEP_THAT.zip" }
```

Với tệp lớn như máy ảo, có thể dùng đường dẫn Drive hoặc kho phát hành đã được chia sẻ phù hợp thay vì đưa tệp lớn vào repository. Gắn URL thật vào nút tải, không dùng thuộc tính `download` để ép tải một trang chia sẻ bên ngoài. Kiểm tra khả năng truy cập của người nhận.

## 3. Kiểm tra

- Tên tệp trong bài phải khớp cả chữ hoa/thường với tệp thực tế.
- Nút tải phải tải đúng tệp, không dẫn tới thư mục thiếu quyền.
- Giải nén được và đọc được nội dung.
- Chỉ rõ firmware/mã nguồn tương thích model nào.
- Chạy build và kiểm tra lại các nút tải trước khi push.

Không sửa `overrides/` hoặc JavaScript chỉ để thêm một tệp tải.
