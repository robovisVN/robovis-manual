#!/usr/bin/env python3
"""Package existing documentation only; never invent robot source/firmware files."""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from zipfile import ZipFile, ZIP_DEFLATED
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE_URL = "https://manual.robovis.vn/"
PACKAGES = [
    ("robot-arduino", "Robot Arduino", "robovis-arduino-docs.zip", "01-gioi-thieu.md"),
    ("robot-esp32", "Robot ESP32", "robovis-esp32-docs.zip", "index.md"),
    ("robot-esp32-camera", "Robot ESP32 Camera", "robovis-esp32-camera-docs.zip", "01-bat-dau/01-tong-quan.md"),
    ("robot-esp32-lidar", "Robot ESP32 LiDAR", "robovis-esp32-lidar-docs.zip", "index.md"),
    ("ubuntu-co-ban", "Ubuntu cơ bản", "robovis-ubuntu-docs.zip", "index.md"),
]


def portable_markdown(text, document, product):
    """Keep bundled relative links, route links outside this package to the website."""
    def replace(match):
        dest = match.group(2)
        parsed = urlsplit(dest)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(document.parent.relative_to(DOCS).as_posix(), parsed.path))
        if target == product or target.startswith(product + "/"):
            return match.group(0)
        if target.endswith("/index.md"):
            target = target[:-8]
        elif target.endswith(".md"):
            target = target[:-3] + "/"
        online = urlsplit(BASE_URL + target)
        return match.group(1) + urlunsplit((online.scheme, online.netloc, online.path, parsed.query, parsed.fragment)) + match.group(3)
    return re.sub(r"(\]\()([^\s)]+)(\))", replace, text)


def main():
    output = DOCS / "downloads"
    output.mkdir(exist_ok=True)
    for product, title, filename, start in PACKAGES:
        folder = DOCS / product
        if not (folder / start).is_file():
            raise FileNotFoundError(folder / start)
        files = sorted(p for p in folder.rglob("*") if p.is_file())
        # Two old index pages are placeholders; the real first lessons are above.
        if product in {"robot-arduino", "robot-esp32-camera"}:
            files = [p for p in files if p != folder / "index.md"]
        intro = (
            f"# Bộ tài liệu {title}\n\n"
            f"Bắt đầu: [{title}]({product}/{start}).\n\n"
            "Gói này chứa các bài Markdown và hình minh họa hiện có. "
            "Không bao gồm bộ mã nguồn điều khiển, firmware hoặc máy ảo robot.\n\n"
            "Mở bằng trình xem Markdown. Sơ đồ cần hỗ trợ Mermaid. "
            "Liên kết ra ngoài bộ tài liệu dẫn tới website và cần Internet.\n\n"
            f"Tài liệu trực tuyến: {BASE_URL}{product}/{start[:-8] if start.endswith('index.md') else start[:-3] + '/'}\n"
        )
        with ZipFile(output / filename, "w", ZIP_DEFLATED) as archive:
            archive.writestr("DOC_TRUOC.md", intro)
            for path in files:
                data = path.read_bytes()
                if path.suffix == ".md":
                    data = portable_markdown(data.decode("utf-8"), path, product).encode("utf-8")
                archive.writestr(path.relative_to(DOCS).as_posix(), data)
        with ZipFile(output / filename) as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"Archive validation failed: {filename}")
        print(f"{filename}: {len(files)} source files")


if __name__ == "__main__":
    main()
