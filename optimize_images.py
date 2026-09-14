import os
import glob
import re

directory = r'D:\tyagihubblog'
html_files = glob.glob(os.path.join(directory, '*.html'))

count = 0
img_modified = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all img tags
    def add_lazy(match):
        global img_modified
        img_tag = match.group(0)
        if 'loading="lazy"' not in img_tag:
            img_modified += 1
            # insert loading="lazy" after <img 
            return img_tag.replace('<img ', '<img loading="lazy" ')
        return img_tag

    new_content = re.sub(r'<img [^>]+>', add_lazy, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Modified {count} files, updated {img_modified} image tags with loading='lazy'.")
