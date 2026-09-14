import os
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

fixed = 0
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Use regex to find and remove any <img> tag with class="article-hero"
    # Also remove any trailing whitespace or newlines directly following it to keep HTML clean
    new_content = re.sub(r'[ \t]*<img[^>]*class="article-hero"[^>]*>\n?', '', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        fixed += 1
        print(f"Removed duplicate hero image from {f}")

print(f"Total files fixed: {fixed}")
