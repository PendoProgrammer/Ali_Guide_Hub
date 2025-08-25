import os
import re
from pathlib import Path


def fix_html(text: str) -> str:
    original = text
    # Fix cases like:  / decoding="async"
    text = re.sub(r"\s*/\s*decoding=\"async\"", " decoding=\"async\"", text)
    # Ensure loading then decoding order is fine; no leading slash before decoding
    text = re.sub(r"loading=\"lazy\"\s*decoding=\"async\"", "loading=\"lazy\" decoding=\"async\"", text)
    # Fix cases like: alt="..."  / decoding -> add attribute before closing angle
    text = re.sub(r"(alt=\"[^\"]*\"[^>]*?)>\s*\n?\s*", lambda m: m.group(1) + ">", text)
    # Remove accidental double closing symbols like </section>>
    text = text.replace("</section>>", "</section>")
    return text if text != original else original


def process_file(path: Path) -> bool:
    src = path.read_text(encoding='utf-8')
    fixed = fix_html(src)
    if fixed != src:
        path.write_text(fixed, encoding='utf-8')
        print('Fixed:', path)
        return True
    return False


def main():
    root = Path(__file__).parent
    changed = 0
    for r, _, files in os.walk(root):
        for f in files:
            if not f.lower().endswith('.html'):
                continue
            if process_file(Path(r) / f):
                changed += 1
    print(f"Done. Files updated: {changed}")


if __name__ == '__main__':
    main()


