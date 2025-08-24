import os
import re
from pathlib import Path

def fix_js_paths():
    """Fix all JavaScript paths in HTML files after folder reorganization"""
    
    # Update main-pages folder (need to go up one level to access JavaScript)
    main_pages_dir = "main-pages"
    blog_posts_dir = "blog-posts"
    
    print("🔄 Fixing JavaScript paths in main pages...")
    
    # Fix main pages - JavaScript should be "../JavaScript/script.js"
    main_pages_files = [f for f in os.listdir(main_pages_dir) if f.endswith('.html')]
    
    for html_file in main_pages_files:
        file_path = os.path.join(main_pages_dir, html_file)
        print(f"Processing: {html_file}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix JavaScript paths: src="JavaScript/script.js" -> src="../JavaScript/script.js"
            content = re.sub(
                r'src="JavaScript/([^"]*\.js)"',
                r'src="../JavaScript/\1"',
                content
            )
            
            # Fix JavaScript paths: src='JavaScript/script.js' -> src='../JavaScript/script.js'
            content = re.sub(
                r"src='JavaScript/([^']*\.js)'",
                r"src='../JavaScript/\1'",
                content
            )
            
            # Fix CSS paths: href="styles.css" -> href="../styles.css"
            content = re.sub(
                r'href="styles\.css"',
                r'href="../styles.css"',
                content
            )
            
            # Fix CSS paths: href='styles.css' -> href='../styles.css'
            content = re.sub(
                r"href='styles\.css'",
                r"href='../styles.css'",
                content
            )
            
            # Fix responsive CSS paths: href="responsive_fixes.css" -> href="../responsive_fixes.css"
            content = re.sub(
                r'href="responsive_fixes\.css"',
                r'href="../responsive_fixes.css"',
                content
            )
            
            # Fix responsive CSS paths: href='responsive_fixes.css' -> href='../responsive_fixes.css'
            content = re.sub(
                r"href='responsive_fixes\.css'",
                r"href='../responsive_fixes.css'",
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
    
    print("\n🔄 Fixing JavaScript paths in blog posts...")
    
    # Fix blog posts - JavaScript should be "../JavaScript/script.js"
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
            
            # Fix JavaScript paths: src="JavaScript/script.js" -> src="../JavaScript/script.js"
            content = re.sub(
                r'src="JavaScript/([^"]*\.js)"',
                r'src="../JavaScript/\1"',
                content
            )
            
            # Fix JavaScript paths: src='JavaScript/script.js' -> src='../JavaScript/script.js'
            content = re.sub(
                r"src='JavaScript/([^']*\.js)'",
                r"src='../JavaScript/\1'",
                content
            )
            
            # Fix CSS paths: href="styles.css" -> href="../styles.css"
            content = re.sub(
                r'href="styles\.css"',
                r'href="../styles.css"',
                content
            )
            
            # Fix CSS paths: href='styles.css' -> href='../styles.css'
            content = re.sub(
                r"href='styles\.css'",
                r"href='../styles.css'",
                content
            )
            
            # Fix responsive CSS paths: href="responsive_fixes.css" -> href="../responsive_fixes.css"
            content = re.sub(
                r'href="responsive_fixes\.css"',
                r'href="../responsive_fixes.css"',
                content
            )
            
            # Fix responsive CSS paths: href='responsive_fixes.css' -> href='../responsive_fixes.css'
            content = re.sub(
                r"href='responsive_fixes\.css'",
                r"href='../responsive_fixes.css'",
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
    
    print(f"\n✅ JavaScript and CSS path fix completed!")
    print(f"📁 Main pages: {len(main_pages_files)} files")
    print(f"📝 Blog posts: {len(blog_posts_files)} files")
    print(f"🔧 All JavaScript and CSS paths updated to work with new folder structure")

if __name__ == "__main__":
    fix_js_paths()
