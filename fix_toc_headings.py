import os
from bs4 import BeautifulSoup
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # Target <aside class="col-toc">
    for aside in soup.find_all('aside', class_='col-toc'):
        # Target the h3 heading inside it
        for h3 in aside.find_all('h3'):
            h3.name = 'div'
            h3['class'] = h3.get('class', []) + ['sidebar-heading']
            # Replicating original h3 styling for sidebar
            h3['style'] = "margin-top: 0; margin-bottom: 20px; font-size: 1.25rem; color: var(--text-main); border-bottom: 2px solid var(--primary-color); padding-bottom: 8px; font-weight: bold;"
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
            
print("Fixed TOC sidebar headings!")
