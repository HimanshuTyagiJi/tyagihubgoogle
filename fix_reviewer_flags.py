import os
import re

blog_dir = r'D:\TyagiHubBlog'

html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    original_content = content
    
    # 1. Remove the author image from the top <div class="blog-meta"> to fix duplication
    # We find the blog-meta div, and remove any <img> tag directly inside it.
    def remove_author_img(match):
        meta_html = match.group(0)
        # Remove the author image tag
        clean_meta = re.sub(r'<img[^>]*himanshu-tyagi-author\.jpg[^>]*>\s*', '', meta_html)
        return clean_meta
    
    content = re.sub(r'<div class="blog-meta">[\s\S]*?(?=</div>\s*</div>|</div>\s*<img|</div>\s*<!--)', remove_author_img, content)
    # A safer regex for removing author image from blog-meta:
    content = re.sub(r'(<div class="blog-meta"[^>]*>\s*)<img[^>]*himanshu-tyagi-author\.jpg[^>]*>\s*', r'\1', content)

    # 2. Check if the page is missing the hero image (article-banner)
    # We only care about actual article pages, which have <article class="blog-container">
    if '<article ' in content or 'class="blog-container"' in content:
        if 'class="article-banner"' not in content:
            # It's missing the banner! Let's find the banner filename from the meta tags
            img_match = re.search(r'assets/images/([^"\']+\.webp)', content)
            if img_match:
                img_name = img_match.group(1)
                
                # Remove custom CSS banners
                content = re.sub(r'<div class="pure-css-banner">[\s\S]*?</div>\s*</header>', '</header>', content)
                content = re.sub(r'<div class="health-banner">[\s\S]*?</div>\s*</header>', '</header>', content)
                content = re.sub(r'<div class="automation-banner">[\s\S]*?</div>\s*</header>', '</header>', content)
                
                # Inject the standard image banner before </header>
                img_tag = f'\n                <img loading="lazy" src="assets/images/{img_name}" alt="Banner" class="article-banner" width="800" height="450">\n            </header>'
                content = content.replace('</header>', img_tag, 1)
                print(f"Added standard banner '{img_name}' to {f}")
                
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed duplicate author and/or banners in {f}")
