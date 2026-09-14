import os
from bs4 import BeautifulSoup
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. First, let's identify the banner for each page via og:image
page_meta = {}
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    og_img = soup.find('meta', property='og:image')
    banner_img = og_img.get('content').split('/')[-1] if og_img and og_img.get('content') else 'default.jpg'
    page_meta[f] = banner_img

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        html = file.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    
    # ISSUE 1: Self-linking in sidebar/related
    # Check all <a> tags. If href == f (this file), remove its container
    for a_tag in soup.find_all('a', href=f):
        # We don't want to remove navigation links, only sidebar/related posts.
        # Related posts are usually an <a> tag directly inside a grid.
        # Popular posts are inside <div class="popular-post-item">
        
        # Check if it's a popular post item
        pop_item = a_tag.find_parent('div', class_='popular-post-item')
        if pop_item:
            pop_item.decompose()
            changed = True
            continue
            
        # Check if it's a related post (a tag with an img inside, inside a grid)
        # Often looks like: <a href="thisfile.html" style="text-decoration:none;"><img...><h4...></a>
        if a_tag.find('h4'):
            a_tag.decompose()
            changed = True
            continue
            
        # Check if it's an article-card in categories/index (we shouldn't remove those usually, 
        # but if it's somehow self linking in a sidebar, yes). Let's be safe.
        if 'article-card' in a_tag.get('class', []):
            # Do not remove from index.html or categories.html
            if f not in ['index.html', 'categories.html']:
                a_tag.decompose()
                changed = True

    # ISSUE 2: Repeated Hero Image in Content
    banner = page_meta[f]
    banner_src = f"assets/images/{banner}"
    banner_count = 0
    for img in soup.find_all('img'):
        if img.get('src') == banner_src:
            banner_count += 1
            if banner_count > 1:
                # This is a duplicate banner! Remove it.
                img.decompose()
                changed = True
                
    # ISSUE 3: Missing Width/Height on Author Image
    for img in soup.find_all('img', src=re.compile(r'himanshu-tyagi-author\.jpg')):
        if not img.get('width'):
            img['width'] = "90"
            changed = True
        if not img.get('height'):
            img['height'] = "90"
            changed = True
            
    if changed:
        # Use str(soup) but let's ensure we don't mess up html structure too much
        # bs4 sometimes adds closing tags or changes formatting, but it's safe for HTML5
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Fixed zero-risk issues in {f}")

