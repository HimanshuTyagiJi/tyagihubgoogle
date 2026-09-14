import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. Fix ARIA labels and lazy loading across all files
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # Fix Input ARIA label
    search_inputs = soup.find_all('input', id='searchInput')
    for inp in search_inputs:
        if not inp.get('aria-label'):
            inp['aria-label'] = "Search TyagiHub"
            changed = True
            
    # Fix Hero Image loading="lazy" -> loading="eager"
    banners = soup.find_all('img', class_='article-banner')
    for banner in banners:
        if banner.get('loading') == 'lazy':
            banner['loading'] = 'eager'
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

# 2. Fix H1 tags in categories.html
cat_path = os.path.join(blog_dir, 'categories.html')
with open(cat_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

changed = False

# Change h1.cat-title to h2.cat-title
for h1 in soup.find_all('h1', class_='cat-title'):
    h1.name = 'h2'
    changed = True

# Add a single main H1 if there isn't one
if changed and not soup.find('h1'):
    # Find the wrapper where we can insert the main H1
    layout = soup.find('div', class_='layout-wrapper')
    if layout:
        # Create a new H1
        new_h1 = soup.new_tag('h1')
        new_h1.string = "Explore Our Technical Library"
        new_h1['style'] = "text-align: center; color: var(--text-main); margin-top: 20px; font-size: 2.2rem;"
        layout.insert(0, new_h1)

if changed:
    with open(cat_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
        
print("Fixed ARIA labels, lazy loading, and H1 tags")
