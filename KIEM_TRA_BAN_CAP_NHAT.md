# Kiểm tra bản cập nhật

- Build `mkdocs build --strict`: thành công với Material 9.6.20.
- Kiểm tra đường dẫn nội bộ và tài nguyên của 69 trang HTML: không có tệp đích bị thiếu.
- Năm gói tài liệu ZIP: kiểm tra giải nén thành công.
- Chromium, màn hình 1440 × 1000: bốn mục header; dropdown không bị che/cắt; chọn robot mở đúng trang; sidebar chỉ chứa sản phẩm đang chọn.
- Kiểm tra Escape, bấm ngoài, Enter, phím mũi tên và focus: thành công.
- Kiểm tra accordion: nhóm mới mở thì nhóm cùng cấp trước đó đóng, URL không đổi.
- Kiểm tra tải thực tế: nút Camera tải đúng `robovis-esp32-camera-docs.zip`.
- Chromium, màn hình 390 × 844: menu nhóm Sản phẩm, mở bài Camera và không tràn chiều ngang.
- Không ghi nhận lỗi JavaScript trong các luồng kiểm tra trên.

Kiểm tra trình duyệt tập trung vào giao diện cục bộ; tài nguyên ngoài như phông web và Mermaid CDN không được tải trong phép thử này. Không kiểm tra firmware, máy ảo hoặc vận hành robot thật. Chưa triển khai website.
