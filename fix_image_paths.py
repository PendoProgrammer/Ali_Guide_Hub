import os
import re
from pathlib import Path

def fix_image_paths():
    """Fix all image paths in HTML files after folder reorganization"""
    
    # Update main-pages folder (need to go up one level to access images)
    main_pages_dir = "main-pages"
    blog_posts_dir = "blog-posts"
    
    print("🔄 Fixing image paths in main pages...")
    
    # Fix main pages - images should be "../images/image.webp"
    main_pages_files = [f for f in os.listdir(main_pages_dir) if f.endswith('.html')]
    
    for html_file in main_pages_files:
        file_path = os.path.join(main_pages_dir, html_file)
        print(f"Processing: {html_file}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix image paths: src="images/image.webp" -> src="../images/image.webp"
            content = re.sub(
                r'src="images/([^"]*\.(webp|png|jpg|jpeg))"',
                r'src="../images/\1"',
                content
            )
            
            # Fix image paths: src='images/image.webp' -> src='../images/image.webp'
            content = re.sub(
                r"src='images/([^']*\.(webp|png|jpg|jpeg))'",
                r"src='../images/\1'",
                content
            )
            
            # Fix href to images: href="images/image.webp" -> href="../images/image.webp"
            content = re.sub(
                r'href="images/([^"]*\.(webp|png|jpg|jpeg))"',
                r'href="../images/\1"',
                content
            )
            
            # Fix href to images: href='images/image.webp' -> href='../images/image.webp'
            content = re.sub(
                r"href='images/([^']*\.(webp|png|jpg|jpeg))'",
                r"href='../images/\1'",
                content
            )
            
            # Fix data-src: data-src="images/image.webp" -> data-src="../images/image.webp"
            content = re.sub(
                r'data-src="images/([^"]*\.(webp|png|jpg|jpeg))"',
                r'data-src="../images/\1"',
                content
            )
            
            # Fix data-src: data-src='images/image.webp' -> data-src='../images/image.webp'
            content = re.sub(
                r"data-src='images/([^']*\.(webp|png|jpg|jpeg))'",
                r"data-src='../images/\1'",
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
    
    print("\n🔄 Fixing image paths in blog posts...")
    
    # Fix blog posts - images should be "../images/image.webp"
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
            
            # Fix image paths: src="images/image.webp" -> src="../images/image.webp"
            content = re.sub(
                r'src="images/([^"]*\.(webp|png|jpg|jpeg))"',
                r'src="../images/\1"',
                content
            )
            
            # Fix image paths: src='images/image.webp' -> src='../images/image.webp'
            content = re.sub(
                r"src='images/([^']*\.(webp|png|jpg|jpeg))'",
                r"src='../images/\1'",
                content
            )
            
            # Fix href to images: href="images/image.webp" -> href="../images/image.webp"
            content = re.sub(
                r'href="images/([^"]*\.(webp|png|jpg|jpeg))"',
                r'href="../images/\1"',
                content
            )
            
            # Fix href to images: href='images/image.webp' -> href='../images/image.webp'
            content = re.sub(
                r"href='images/([^']*\.(webp|png|jpg|jpeg))'",
                r"href='../images/\1'",
                content
            )
            
            # Fix data-src: data-src="images/image.webp" -> data-src="../images/image.webp"
            content = re.sub(
                r'data-src="images/([^"]*\.(webp|png|jpg|jpeg))"',
                r'data-src="../images/\1"',
                content
            )
            
            # Fix data-src: data-src='images/image.webp' -> data-src='../images/image.webp'
            content = re.sub(
                r"data-src='images/([^']*\.(webp|png|jpg|jpeg))'",
                r"data-src='../images/\1'",
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
    
    print(f"\n✅ Image path fix completed!")
    print(f"📁 Main pages: {len(main_pages_files)} files")
    print(f"📝 Blog posts: {len(blog_posts_files)} files")
    print(f"🖼️ All image paths updated to work with new folder structure")

if __name__ == "__main__":
    fix_image_paths()
