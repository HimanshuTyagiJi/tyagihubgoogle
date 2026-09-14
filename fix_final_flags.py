import os
import re
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'

# 1. Fix categories.html
cat_path = os.path.join(blog_dir, 'categories.html')
with open(cat_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

grids = soup.find_all('div', class_='grid-container')

if len(grids) >= 4:
    # Grid 1: AI (Remove 2fa)
    grid_ai = grids[0]
    for a in grid_ai.find_all('a', href='two-factor-authentication-explained.html'):
        a.decompose()
        
    # Grid 4: Future Tech (Remove frontend vs backend)
    grid_future = grids[3]
    for a in grid_future.find_all('a', href='frontend-vs-backend-development.html'):
        a.decompose()

with open(cat_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Fixed categories.html duplicates")

# 2. Fix style.css (Remove .ad-space)
css_path = os.path.join(blog_dir, 'assets', 'css', 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# .ad-space { ... } ends with }
# We can use regex to remove it
new_css = re.sub(r'\.ad-space\s*\{[^}]*\}\s*', '', css_content)

if new_css != css_content:
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("Removed .ad-space from style.css")
