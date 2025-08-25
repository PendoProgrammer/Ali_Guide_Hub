import os
from pathlib import Path


REPLACEMENTS = {
    "hidden_incom_streams.webp": "hidden incom streams.webp",
    "top_high_incom_skill.webp": "tophighincomskill.webp",
}


def replace_in_text(text: str) -> str:
    for wrong, correct in REPLACEMENTS.items():
        text = text.replace(f"/images/{wrong}", f"/images/{correct}")
        text = text.replace(f"images/{wrong}", f"images/{correct}")
        text = text.replace(f"../images/{wrong}", f"../images/{correct}")
    return text


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = replace_in_text(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"Updated: {path}")
        return True
    return False


def main():
    root = Path(__file__).parent
    changed = 0
    scanned = 0
    for r, _, files in os.walk(root):
        for f in files:
            if not f.lower().endswith(".html"):
                continue
            scanned += 1
            if process_file(Path(r) / f):
                changed += 1
    print(f"\nDone. Scanned {scanned} HTML files, changed {changed} files.")


if __name__ == "__main__":
    main()


