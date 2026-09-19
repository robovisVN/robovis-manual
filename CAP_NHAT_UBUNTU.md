# Nội dung bản cập nhật hoàn chỉnh

## Những phần đã tích hợp

- Giữ toàn bộ tài liệu sản phẩm và series Ubuntu cơ bản đã ghép.
- Header gồm Trang chủ, Kiến thức nền, Sản phẩm dạng dropdown và Tải xuống.
- Cấu trúc `nav` thực sự có nhóm Sản phẩm; menu điện thoại dùng nhóm này, không phải một dropdown chỉ có trên máy tính.
- Dropdown chọn robot mở bài đầu; trên máy tính sidebar chỉ hiển thị bài của robot đó.
- Có đường dẫn phân cấp trên các trang sản phẩm.
- Trung tâm tải xuống và năm trang theo robot/Ubuntu; năm tệp ZIP tài liệu tải được ngay.
- Các tệp robot chưa được cung cấp được ghi rõ trạng thái; không có URL tải giả.
- Giữ accordion, bài đang đọc, Mermaid và tên miền của project cũ.
- Workflow tái tạo gói tài liệu trước khi triển khai.

## Khi chép bản cập nhật

Chép cả thư mục `overrides`, `scripts`, `docs`, cấu hình `mkdocs.yml` và workflow trong `.github`. Giữ `.git` cùng môi trường `.venv` của repository hiện tại.

Các gói ZIP trong `docs/downloads/` chứa tài liệu Markdown và ảnh, không phải mã nguồn điều khiển robot. Thêm tệp thật theo `HUONG_DAN_THEM_TEP_TAI.md` khi có bộ mã nguồn hoặc firmware được xác nhận.

Bản cập nhật chưa tự push GitHub hoặc triển khai website.
