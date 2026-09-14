import os
import re

blog_dir = r'D:\TyagiHubBlog'

for f in os.listdir(blog_dir):
    if not f.endswith('.html'):
        continue
        
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    def replace_empty_alt(match):
        card_html = match.group(0)
        h_match = re.search(r'<h[234][^>]*>(.*?)</h[234]>', card_html)
        if h_match:
            title = h_match.group(1).strip()
            title = re.sub(r'<[^>]+>', '', title)
            new_card = re.sub(r'alt=""', f'alt="{title}"', card_html)
            return new_card
        return card_html

    # In categories.html, the a tag has class="card-link"
    new_content = re.sub(r'(<a\s+[^>]*class="(?:article-card|card-link)"[^>]*>[\s\S]*?</a>)', replace_empty_alt, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed empty alt tags in {f}")
