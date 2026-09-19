# Tài liệu hướng dẫn Robovis

Project hoàn chỉnh cho `manual.robovis.vn`, dùng MkDocs Material. Đã có series Ubuntu cơ bản, menu sản phẩm dạng dropdown và trung tâm tải xuống.

## Điều hướng

**Trang chủ · Kiến thức nền · Sản phẩm ▾ · Tải xuống**

- **Kiến thức nền:** lộ trình và 8 bài Ubuntu cơ bản.
- **Sản phẩm:** Robot Arduino, Robot ESP32, Robot ESP32 Camera, Robot ESP32 LiDAR. Chọn sản phẩm mở bài đầu; sidebar máy tính chỉ hiển thị bài của sản phẩm được chọn.
- **Tải xuống:** năm gói tài liệu Markdown/hình minh họa có thể tải ngay và trạng thái mã nguồn/công cụ của từng sản phẩm.

Trên điện thoại, Sản phẩm là nhóm trong menu gốc của Material. Trên máy tính, bấm Sản phẩm để mở dropdown; bấm ngoài hoặc Escape để đóng. Enter, Tab và phím mũi tên dùng được trong dropdown.

## Chạy trên Windows PowerShell

Mở tại thư mục có `mkdocs.yml`:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/build_downloads.py
.\.venv\Scripts\python.exe -m mkdocs serve
```

Nếu `.venv` đã có, bỏ qua bước tạo môi trường. Không cần đổi Execution Policy với cách gọi Python trực tiếp này.

## Chạy trên Ubuntu

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_downloads.py
.venv/bin/python -m mkdocs serve
```

Nếu thiếu module venv, cài `python3-venv` rồi tạo lại môi trường. Mở địa chỉ server in ra, thường là `http://127.0.0.1:8000/`. Ctrl+C để dừng.

## Cập nhật vào repository đang có

Sao lưu chỉnh sửa chưa commit rồi chép nội dung gói vào project hiện tại, bao gồm **`overrides/`**, **`scripts/`**, **`docs/`**, **`mkdocs.yml`** và workflow **`.github/workflows/deploy.yml`**. Không chỉ chép các bài `.md`: dropdown cần template, CSS và JavaScript đi kèm.

Giữ `.git` và `.venv` hiện có trên máy. Gói bàn giao không chứa `.git`, `.venv` hoặc thư mục build `site/`. File `docs/CNAME` và `site_url` vẫn là tên miền hiện tại; không cần đổi DNS.

Xem lại thay đổi bằng `git diff`. Trong môi trường Python của project, chạy:

```bash
python scripts/build_downloads.py
python -m mkdocs build --strict
```

Sau khi kiểm tra bằng trình duyệt:

```bash
git status
git diff
git add mkdocs.yml docs overrides scripts .github/workflows/deploy.yml README.md CAP_NHAT_UBUNTU.md HUONG_DAN_THEM_TEP_TAI.md
git commit -m "Add product dropdown and downloads center"
git push
```

Chỉ commit những thay đổi đã xem lại. Workflow hiện có chạy khi push nhánh `main`, tạo lại năm gói tài liệu rồi dùng `mkdocs gh-deploy --force` để cập nhật nhánh `gh-pages`. Đợi GitHub Actions thành công rồi kiểm tra website.

## Duy trì trang tải xuống

Đọc `HUONG_DAN_THEM_TEP_TAI.md`. `scripts/build_downloads.py` chỉ đóng gói bài Markdown và hình hiện có; không tạo firmware hoặc chương trình robot. Chạy script sau khi sửa bài để gói tải phản ánh nội dung mới.

Mã nguồn robot, firmware, công cụ cấu hình và máy ảo chưa được đính kèm trong project nguồn. Trang tải ghi rõ trạng thái, không tạo nút giả. Có thể bổ sung tệp hoặc URL tải thật sau này mà không sửa dropdown.

## Các tệp giao diện

| Tệp | Vai trò |
| --- | --- |
| `overrides/partials/tabs.html` | Gom sản phẩm vào dropdown trên header |
| `overrides/partials/nav.html` | Đánh dấu trang sản phẩm để giới hạn sidebar máy tính |
| `overrides/main.html` | Đường dẫn Sản phẩm → robot → bài viết |
| `docs/javascripts/products-dropdown.js` | Đóng ngoài, Escape và thao tác phím mũi tên |
| `docs/javascripts/navigation-accordion.js` | Giữ một nhóm cùng cấp mở trong sidebar |
| `docs/stylesheets/extra.css` | Bộ nhận diện, dropdown và sidebar |

Phiên bản Material được giữ theo `requirements.txt`. Khi nâng phiên bản theme, kiểm tra lại các template override. Cấu hình Mermaid được giữ; việc hiển thị sơ đồ trên web cần trình duyệt tải được tài nguyên Mermaid.
