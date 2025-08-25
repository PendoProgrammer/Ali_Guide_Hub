import os
from pathlib import Path


def process_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    new_text = text.replace('src="../images/', 'src="../../images/')\
                   .replace("href=\"../images/", "href=\"../../images/")\
                   .replace("url('../images/", "url('../../images/")\
                   .replace('url("../images/', 'url("../../images/')
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print('Updated:', path)
        return True
    return False


def main():
    root = Path(__file__).parent / 'main-pages' / 'blog-posts'
    updated = 0
    for f in root.glob('*.html'):
        if process_file(f):
            updated += 1
    print(f"Done. Updated {updated} blog post files.")


if __name__ == '__main__':
    main()


