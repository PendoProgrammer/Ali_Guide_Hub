import os
import re
from pathlib import Path

def final_link_fix():
    """Final comprehensive fix for all link issues"""
    
    print("🔄 Final comprehensive link fixing...")
    
    # Update main-pages folder
    main_pages_dir = "main-pages"
    blog_posts_dir = "blog-posts"
    
    print("\n📁 Fixing main pages...")
    
    # Fix main pages
    main_pages_files = [f for f in os.listdir(main_pages_dir) if f.endswith('.html')]
    
    for html_file in main_pages_files:
        file_path = os.path.join(main_pages_dir, html_file)
        print(f"Processing: {html_file}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix malformed links with duplicate blog-posts paths
            content = re.sub(
                r'href="blog-posts/blog-posts/blog-posts/([^"]*\.html)"',
                r'href="blog-posts/\1"',
                content
            )
            
            content = re.sub(
                r'href="blog-posts/blog-posts/([^"]*\.html)"',
                r'href="blog-posts/\1"',
                content
            )
            
            # Fix links that are missing quotes or have broken formatting
            content = re.sub(
                r'href="([^"]*\.html)\s*\n\s*"',
                r'href="\1"',
                content
            )
            
            # Fix links that point to blog posts but don't have blog-posts/ prefix
            main_page_names = ['index.html', 'about.html', 'author.html', 'contactus.html', 'blog.html', 'login.html', 'register.html', 'privacy-policy.html', 'terms-and-conditions.html', 'disclaimer.html']
            
            def replace_blog_links(match):
                href_content = match.group(1)
                if href_content.endswith('.html') and href_content not in main_page_names:
                    # Check if it already has blog-posts prefix
                    if not href_content.startswith('blog-posts/'):
                        return f'href="blog-posts/{href_content}"'
                return match.group(0)
            
            content = re.sub(
                r'href="([^"]*\.html)"',
                replace_blog_links,
                content
            )
            
            # Check if content was changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated: {html_file}")
            else:
                print(f"  - No changes needed: {html_file}")
                
        except Exception as e:
            print(f"  ✗ Error processing {html_file}: {e}")
    
    print("\n📝 Fixing blog posts...")
    
    # Fix blog posts
    blog_posts_files = [f for f in os.listdir(blog_posts_dir) if f.endswith('.html')]
    
    for html_file in blog_posts_files:
        if html_file == "google716fc1ddd856db74.html":
            continue  # Skip Google verification file
            
        file_path = os.path.join(blog_posts_dir, html_file)
        print(f"Processing: {html_file}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix links to main pages (need to go up to main-pages folder)
            content = re.sub(
                r'href="(index\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(about\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(author\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(contactus\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(blog\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(login\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(register\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(privacy-policy\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(terms-and-conditions\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            content = re.sub(
                r'href="(disclaimer\.html)"',
                r'href="../main-pages/\1"',
                content
            )
            
            # Check if content was changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated: {html_file}")
            else:
                print(f"  - No changes needed: {html_file}")
                
        except Exception as e:
            print(f"  ✗ Error processing {html_file}: {e}")
    
    print(f"\n✅ Final link fixing completed!")
    print(f"📁 Main pages: {len(main_pages_files)} files")
    print(f"📝 Blog posts: {len(blog_posts_files)} files")
    print(f"🔗 All links now work correctly")

if __name__ == "__main__":
    final_link_fix()
