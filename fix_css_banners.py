import os
import re

blog_dir = r'D:\TyagiHubBlog'

for f in os.listdir(blog_dir):
    if not f.endswith('.html'): 
        continue
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    orig = content
    
    img_match = re.search(r'assets/images/([^"\']+\.webp)', content)
    if img_match:
        img_name = img_match.group(1)
        
        content = re.sub(r'<div class="pure-css-banner">[\s\S]*?</div>\s*(?=</header>)', 
                         f'<img loading="lazy" src="assets/images/{img_name}" alt="Banner" class="article-banner" width="800" height="450">\n                ', content)
        
        content = re.sub(r'<div class="health-banner">[\s\S]*?</div>\s*(?=</header>)', 
                         f'<img loading="lazy" src="assets/images/{img_name}" alt="Banner" class="article-banner" width="800" height="450">\n                ', content)
                         
        content = re.sub(r'<div class="automation-banner">[\s\S]*?</div>\s*(?=</header>)', 
                         f'<img loading="lazy" src="assets/images/{img_name}" alt="Banner" class="article-banner" width="800" height="450">\n                ', content)
                         
    if orig != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Fixed CSS banner in {f}')
