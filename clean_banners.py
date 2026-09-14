import os
import re

blog_dir = r'D:\TyagiHubBlog'
for f in ['ai-impact-on-healthcare.html', 'automation-to-boost-productivity.html']:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's cleanly remove <div class="health-banner">...</div> and <div class="automation-banner">...</div>
    # by just matching until </header>
    content = re.sub(r'<div class="health-banner">[\s\S]*?(?=<img loading="lazy" src="assets/images/ai-healthcare-banner.webp")', '', content)
    content = re.sub(r'<div class="automation-banner">[\s\S]*?(?=<img loading="lazy" src="assets/images/automation-banner.webp")', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Cleaned up broken banner divs in {f}")
