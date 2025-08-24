import os
import re
from pathlib import Path

def fix_all_image_issues():
    """Fix all image naming mismatches and external image references"""
    
    print("🔄 Fixing all image issues comprehensively...")
    
    # Get list of available images
    images_dir = "images"
    available_images = [f.lower() for f in os.listdir(images_dir) if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg'))]
    
    print(f"📁 Found {len(available_images)} available images")
    
    # Image name mappings (what's referenced vs what actually exists)
    image_mappings = {
        'top_high_incom_skill.webp': 'tophighincomskill.webp',
        'hidden_incom_streams.webp': 'hidden incom streams.webp'
    }
    
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
            
            # Fix external image references (remove the /images/ prefix from external URLs)
            content = re.sub(
                r'src="/images/https://([^"]*)"',
                r'src="https://\1"',
                content
            )
            
            # Check if content was changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated external images: {html_file}")
            else:
                print(f"  - No external image changes needed: {html_file}")
                
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
            
            # Fix image name mismatches
            for wrong_name, correct_name in image_mappings.items():
                content = re.sub(
                    rf'src="/images/{re.escape(wrong_name)}"',
                    rf'src="/images/{correct_name}"',
                    content
                )
            
            # Check if content was changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated image names: {html_file}")
            else:
                print(f"  - No image name changes needed: {html_file}")
                
        except Exception as e:
            print(f"  ✗ Error processing {html_file}: {e}")
    
    print(f"\n✅ All image issues fixed!")
    print(f"📁 Main pages: {len(main_pages_files)} files")
    print(f"📝 Blog posts: {len(blog_posts_files)} files")
    print(f"🖼️ Image name mismatches corrected")
    print(f"🌐 External image references fixed")

def verify_fixes():
    """Verify that all image issues have been resolved"""
    
    print("\n🔍 Verifying all fixes...")
    
    # Get list of available images
    images_dir = "images"
    available_images = [f.lower() for f in os.listdir(images_dir) if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg'))]
    
    # Check main pages
    main_pages_dir = "main-pages"
    main_pages_files = [f for f in os.listdir(main_pages_dir) if f.endswith('.html')]
    
    missing_images = []
    external_images = []
    
    for html_file in main_pages_files:
        file_path = os.path.join(main_pages_dir, html_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all image references
            image_matches = re.findall(r'src="([^"]*)"', content)
            
            for image_src in image_matches:
                if image_src.startswith('/images/'):
                    image_name = image_src.replace('/images/', '')
                    if image_name.lower() not in available_images:
                        missing_images.append(f"{html_file}: {image_name}")
                elif image_src.startswith('http'):
                    external_images.append(f"{html_file}: {image_src}")
                    
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
            image_matches = re.findall(r'src="([^"]*)"', content)
            
            for image_src in image_matches:
                if image_src.startswith('/images/'):
                    image_name = image_src.replace('/images/', '')
                    if image_name.lower() not in available_images:
                        missing_images.append(f"{html_file}: {image_name}")
                elif image_src.startswith('http'):
                    external_images.append(f"{html_file}: {image_src}")
                    
        except Exception as e:
            print(f"  ✗ Error checking {html_file}: {e}")
    
    print(f"\n📊 Verification Results:")
    
    if missing_images:
        print(f"❌ Found {len(missing_images)} missing images:")
        for missing in missing_images[:10]:  # Show first 10
            print(f"  - {missing}")
        if len(missing_images) > 10:
            print(f"  ... and {len(missing_images) - 10} more")
    else:
        print(f"✅ All local images are available!")
    
    if external_images:
        print(f"🌐 Found {len(external_images)} external images (these are OK):")
        for external in external_images[:5]:  # Show first 5
            print(f"  - {external}")
        if len(external_images) > 5:
            print(f"  ... and {len(external_images) - 5} more")
    
    return len(missing_images) == 0

if __name__ == "__main__":
    fix_all_image_issues()
    verify_fixes()
