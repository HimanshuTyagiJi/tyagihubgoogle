import os
import re
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. Update CSS for tables
css_file = os.path.join(blog_dir, 'assets', 'css', 'style.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the problematic table CSS with a better wrapper approach
if '/* --- Table Overflow Fix --- */' in css_content:
    css_content = re.sub(
        r'/\* --- Table Overflow Fix --- \*/.*?min-width: 150px;\s*\}',
        '''/* --- Table Overflow Fix --- */
.table-responsive-wrapper { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 30px 0; }
.blog-content table { display: table !important; width: 100% !important; min-width: 600px; margin: 0; white-space: normal; }''',
        css_content,
        flags=re.DOTALL
    )
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # --- 1. Remove duplicate tocFab / tocModal ---
    old_fab = soup.find('button', id='tocFab')
    if old_fab:
        old_fab.decompose()
        changed = True
        
    old_modal = soup.find('div', id='tocModal')
    if old_modal:
        old_modal.decompose()
        changed = True
        
    # --- 2. Wrap all tables in a responsive div ---
    tables = soup.find_all('table')
    for table in tables:
        # Check if already wrapped
        parent = table.parent
        if not (parent and parent.name == 'div' and 'table-responsive-wrapper' in parent.get('class', [])):
            wrapper = soup.new_tag('div')
            wrapper['class'] = 'table-responsive-wrapper'
            table.wrap(wrapper)
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Fixed duplicate TOC FABs and wrapped tables to prevent CSS breaking on mobile.")
