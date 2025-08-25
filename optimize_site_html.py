import os
import re
from pathlib import Path


CANONICAL = '<link rel="canonical" href="https://guidehubz.com/" />'


def ensure_canonical(head_html: str) -> str:
    if 'rel="canonical"' in head_html:
        return head_html
    # Insert canonical after opening <head>
    return head_html.replace('<head>', '<head>' + "\n" + CANONICAL, 1)


def add_img_dimensions(html: str) -> str:
    # Add decoding and loading attributes if missing; keep existing values
    def repl(match: re.Match) -> str:
        tag = match.group(0)
        if 'decoding=' not in tag:
            tag = tag[:-1] + ' decoding="async">'
        if 'loading=' not in tag:
            tag = tag[:-1] + ' loading="lazy">'
        return tag

    return re.sub(r'<img(?![^>]*decoding=)[^>]*>', repl, html)


def set_lcp_fetchpriority(html: str) -> str:
    # Promote the first post image or first img as LCP
    idx = html.find('<img')
    if idx == -1:
        return html
    end = html.find('>', idx)
    if end == -1:
        return html
    tag = html[idx:end+1]
    if 'fetchpriority=' in tag:
        return html
    new_tag = tag[:-1] + ' fetchpriority="high">'
    return html.replace(tag, new_tag, 1)


def add_preload_for_first_image(head_html: str, body_html: str, root_rel: str) -> str:
    # Find first image src to preload
    m = re.search(r'<img[^>]*\ssrc=[\"\']([^\"\']+)[\"\']', body_html)
    if not m:
        return head_html
    src = m.group(1)
    if 'http' in src:
        return head_html
    if 'rel="preload"' in head_html and src in head_html:
        return head_html
    preload = f'<link rel="preload" as="image" href="{src}">'
    return head_html.replace('<head>', '<head>' + "\n" + preload, 1)


def process_html(file_path: Path, project_root: Path) -> bool:
    text = file_path.read_text(encoding='utf-8')
    changed = False
    # Split head and rest
    parts = text.split('<head>')
    if len(parts) >= 2:
        head_and_after = parts[1]
        head_close_idx = head_and_after.find('</head>')
        if head_close_idx != -1:
            head_html = '<head>' + head_and_after[:head_close_idx+7]
            body_html = head_and_after[head_close_idx+7:]

            new_head = ensure_canonical(head_html)
            new_head = add_preload_for_first_image(new_head, body_html, '')
            if new_head != head_html:
                changed = True

            new_body = add_img_dimensions(body_html)
            new_body = set_lcp_fetchpriority(new_body)
            if new_body != body_html:
                changed = True

            if changed:
                new_text = parts[0] + new_head + new_body
                file_path.write_text(new_text, encoding='utf-8')
    return changed


def main():
    root = Path(__file__).parent
    updated = 0
    scanned = 0
    for r, _, files in os.walk(root):
        for f in files:
            if not f.lower().endswith('.html'):
                continue
            scanned += 1
            path = Path(r) / f
            if process_html(path, root):
                print('Updated:', path.relative_to(root))
                updated += 1
    print(f"\n✅ Optimization done. Scanned {scanned} files, Updated {updated} files")


if __name__ == '__main__':
    main()


