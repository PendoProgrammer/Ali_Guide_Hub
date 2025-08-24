import os
import re
from pathlib import Path

def fix_image_issues():
    """Fix all image path issues to ensure images display correctly"""
    
    print("🔄 Fixing all image path issues...")
    
    # Get list of available images
    images_dir = "images"
    available_images = [f.lower() for f in os.listdir(images_dir) if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg'))]
    
    print(f"📁 Found {len(available_images)} available images")
    
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
            
            # Fix image paths to use absolute paths from root
            content = re.sub(
                r'src="../images/([^"]*)"',
                r'src="/images/\1"',
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
            
            # Fix image paths to use absolute paths from root
            content = re.sub(
                r'src="../images/([^"]*)"',
                r'src="/images/\1"',
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
    
    print(f"\n✅ Image path fixing completed!")
    print(f"📁 Main pages: {len(main_pages_files)} files")
    print(f"📝 Blog posts: {len(blog_posts_files)} files")
    print(f"🖼️ All images now use absolute paths from root")

def check_missing_images():
    """Check for any missing images and report them"""
    
    print("\n🔍 Checking for missing images...")
    
    # Get list of available images
    images_dir = "images"
    available_images = [f.lower() for f in os.listdir(images_dir) if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg'))]
    
    # Check main pages
    main_pages_dir = "main-pages"
    main_pages_files = [f for f in os.listdir(main_pages_dir) if f.endswith('.html')]
    
    missing_images = []
    
    for html_file in main_pages_files:
        file_path = os.path.join(main_pages_dir, html_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all image references
            image_matches = re.findall(r'src="/images/([^"]*)"', content)
            
            for image_name in image_matches:
                if image_name.lower() not in available_images:
                    missing_images.append(f"{html_file}: {image_name}")
                    
        except Exception as e:
            print(f"  ✗ Error checking {html_file}: {e}")
    
    # Check blog posts
    blog_posts_dir = "blog-posts"
    blog_posts_files = [f for f in os.listdir(blog_posts_dir) if f.endswith('.html')]
    
    for html_file in blog_posts_files:
        if html_file == "google716fc1ddd856db74.html":
            continue
            
        file_path = os.path.join(blog_posts_dir, html_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all image references
            image_matches = re.findall(r'src="/images/([^"]*)"', content)
            
            for image_name in image_matches:
                if image_name.lower() not in available_images:
                    missing_images.append(f"{html_file}: {image_name}")
                    
        except Exception as e:
            print(f"  ✗ Error checking {html_file}: {e}")
    
    if missing_images:
        print(f"\n❌ Found {len(missing_images)} missing images:")
        for missing in missing_images:
            print(f"  - {missing}")
    else:
        print(f"\n✅ All images are available!")
    
    return missing_images

if __name__ == "__main__":
    fix_image_issues()
    check_missing_images()
