import os
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

updated_files = 0
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to add width and height to article images.
    # We know the card-img-wrapper has an image.
    # Let's replace <img src="assets/images/...webp" alt="..." style="..."> 
    # with <img src="..." alt="..." width="800" height="450" style="...">
    
    def add_dimensions(match):
        img_tag = match.group(0)
        # Skip if already has width or if it's the logo or author
        if 'width=' in img_tag and not 'style="width' in img_tag: 
            # It already has a width attribute
            return img_tag
        if 'logo' in img_tag or 'author' in img_tag:
            return img_tag
            
        # Add dimensions before style
        if 'style=' in img_tag:
            return img_tag.replace('style=', 'width="800" height="450" style=')
        else:
            return img_tag.replace('>', ' width="800" height="450">')

    new_content = re.sub(r'<img\s+[^>]+>', add_dimensions, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        updated_files += 1

print(f"Added image dimensions to {updated_files} HTML files to fix CLS.")
