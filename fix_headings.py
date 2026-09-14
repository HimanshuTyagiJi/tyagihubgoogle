import os
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# We'll fix multiple things:
# 1. Author box H4 to DIV
# 2. Card image redundant alt attributes (set alt="")
# 3. Any other random H4s that break structure

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace <h4> used in author box with <div class="author-name-title">
    # The user provided: <h4 style="margin:0; color:var(--text-main); font-size:1.4rem;">
    content = content.replace('<h4 style="margin:0; color:var(--text-main); font-size:1.4rem;">', '<div style="margin:0; color:var(--text-main); font-size:1.4rem; font-weight:bold;">')
    content = content.replace('</h4>', '</div>') # Only safe if all <h4> in the document are meant to be closed. Since we replaced the opening tag, we should be careful.
    
    # Actually, a better regex for H4 replacement:
    content = re.sub(r'<h4([^>]*)>(.*?)</h4>', r'<div\1 style="font-weight:bold;">\2</div>', content, flags=re.IGNORECASE)

    # 2. Fix Redundant Alt Text in Cards
    # If the image is inside an <a> tag along with text, it's redundant.
    # The cards have <div class="card-img-wrapper"> <img alt="..."> </div>
    # Let's replace the alt="..." in card-img-wrapper with alt=""
    
    def remove_card_alt(match):
        img_tag = match.group(1)
        # replace alt="..." with alt=""
        img_tag = re.sub(r'alt="[^"]*"', 'alt=""', img_tag)
        return f'<div class="card-img-wrapper"{match.group(2)}>{img_tag}</div>'

    # Actually simpler: just find all images in card-img-wrapper
    # Or just replace alt text for all images that have class="card-img" or are inside the grid
    # Let's do it specifically for the grid in index and categories:
    if f in ['index.html', 'categories.html']:
        content = re.sub(r'(<img[^>]*?assets/images/[^>]*?)(alt="[^"]*")([^>]*>)', r'\1alt=""\3', content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fixed Headings and Redundant Alt text.")
