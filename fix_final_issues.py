import os
import re
from PIL import Image

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. Resize the large author image
img_path = os.path.join(blog_dir, 'assets', 'images', 'himanshu-tyagi-author.jpg')
if os.path.exists(img_path):
    try:
        with Image.open(img_path) as img:
            # Resize to max 300x300, maintaining aspect ratio
            img.thumbnail((300, 300))
            img.save(img_path, optimize=True, quality=80)
        print("Successfully resized himanshu-tyagi-author.jpg")
    except Exception as e:
        print(f"Failed to resize image: {e}")

# 2. Add Meta Descriptions and 3. Fix #10B981 color contrast
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # Check for meta description
    if '<meta name="description"' not in content:
        # Create a generic description based on the title
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            title = title_match.group(1).replace('TyagiHub', '').replace('|', '').strip()
            desc = f"Learn more about {title} on TyagiHub. Your ultimate digital destination for premium tech insights and educational resources."
            meta_tag = f'\n    <meta name="description" content="{desc}">\n'
            # Insert after <head> or <title>
            content = content.replace('</title>', f'</title>{meta_tag}')
            modified = True
            
    # Check for contrast issue (#10B981)
    if '#10B981' in content:
        content = content.replace('#10B981', '#047857')
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

print("Done with all updates.")
