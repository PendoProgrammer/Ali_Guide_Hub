import os
import re
from pathlib import Path


IMAGES_DIR = "images"


def compute_relative_prefix(from_path: Path, project_root: Path) -> str:
    try:
        relative = from_path.parent.relative_to(project_root)
    except ValueError:
        return ""
    depth = len(list(relative.parts))
    if depth == 0:
        return ""
    return "../" * depth


def replacer_factory(prefix: str):
    # Replace src="/images/..." or src='/images/...'
    # Also fix inline styles url('/images/...') and url(/images/...)
    img_src_pattern = re.compile(r"(src\s*=\s*[\"'])/images/([^\"']+)([\"'])")
    url_pattern = re.compile(r"(url\(\s*[\"']?)/images/([^\)\"']+)([\"']?\s*\))")

    def _repl(content: str) -> str:
        content = img_src_pattern.sub(rf"\1{prefix}{IMAGES_DIR}/\2\3", content)
        content = url_pattern.sub(rf"\1{prefix}{IMAGES_DIR}/\2\3", content)
        return content

    return _repl


def process_file(html_path: Path, project_root: Path) -> bool:
    text = html_path.read_text(encoding="utf-8")
    prefix = compute_relative_prefix(html_path, project_root)
    replacer = replacer_factory(prefix)
    new_text = replacer(text)
    if new_text != text:
        html_path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    project_root = Path(__file__).parent

    updated = 0
    scanned = 0
    for root, _, files in os.walk(project_root):
        for name in files:
            if not name.lower().endswith(".html"):
                continue
            html_path = Path(root) / name
            scanned += 1
            if process_file(html_path, project_root):
                print(f"Updated: {html_path.relative_to(project_root)}")
                updated += 1

    print(f"\n✅ Done. Scanned: {scanned} HTML files, Updated: {updated} files")


if __name__ == "__main__":
    main()


