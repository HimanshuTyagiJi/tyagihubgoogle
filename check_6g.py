import os
import re

blog_dir = r'D:\TyagiHubBlog'
filepath = os.path.join(blog_dir, 'what-is-6g-technology.html')
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+>', html)
for img in imgs:
    src_match = re.search(r'src=["\']([^"\']+)["\']', img)
    cls_match = re.search(r'class=["\']([^"\']+)["\']', img)
    src = src_match.group(1) if src_match else 'None'
    cls = cls_match.group(1) if cls_match else 'None'
    print(f'SRC: {src} | CLASS: {cls}')
