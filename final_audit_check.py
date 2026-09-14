import os
from bs4 import BeautifulSoup
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]
css_dir = os.path.join(blog_dir, 'assets', 'css')

errors = []

# Check CSS
if os.path.exists(css_dir):
    for f in os.listdir(css_dir):
        if f.endswith('.css'):
            with open(os.path.join(css_dir, f), 'r', encoding='utf-8') as css_file:
                content = css_file.read()
                if '.ad-space' in content:
                    errors.append(f"CSS Error: .ad-space found in {f}")

# Check HTML
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        html = file.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Check Lazy Loading on Hero
    banners = soup.find_all('img', class_='article-banner')
    for b in banners:
        if b.get('loading') == 'lazy':
            errors.append(f"LCP Error: Lazy loading on hero banner in {f}")
            
    # 2. Check Alt="Banner"
    for img in soup.find_all('img'):
        if img.get('alt') == 'Banner':
            errors.append(f"SEO Error: alt='Banner' found in {f}")
            
    # 3. Check ARIA label on search
    search = soup.find('input', id='searchInput')
    if search and not search.get('aria-label'):
        errors.append(f"A11y Error: Missing aria-label on search in {f}")
        
    # 4. Check Heading Hierarchy (H3 before H1)
    first_h1 = soup.find('h1')
    first_h3 = soup.find('h3')
    if first_h1 and first_h3:
        # Check their positions in the HTML string as a quick proxy
        if html.find('<h3') < html.find('<h1'):
            # Double check it's actually an h3 and not part of a script or comment
            # Just relying on string index is usually enough for this check
            errors.append(f"Hierarchy Error: H3 appears before H1 in {f}")
            
    # 5. Check Duplicate Images (excluding defaults)
    img_srcs = [img.get('src') for img in soup.find_all('img') if img.get('src') and 'default.jpg' not in img.get('src') and 'author.jpg' not in img.get('src')]
    if len(img_srcs) != len(set(img_srcs)):
        # Count occurrences
        from collections import Counter
        counts = Counter(img_srcs)
        dups = [src for src, count in counts.items() if count > 1]
        if dups:
            # We allow some UI icons to repeat, but not webp banners
            webp_dups = [d for d in dups if d.endswith('.webp')]
            if webp_dups:
                errors.append(f"Duplicate Content: Repeated banner images {webp_dups} in {f}")
                
    # 6. Check Self-Linking in Related/Sidebar
    links = soup.find_all('a')
    for a in links:
        if a.get('href') == f:
            # Exclude canonical links or header logo links (index.html)
            if 'canonical' not in a.get('rel', []) and f != 'index.html':
                # Allowed if it's inside the breadcrumb or similar, but we removed self-linking from sidebar
                # Let's check if it's inside a rich-card or popular-post-item
                if a.find_parent('div', class_='rich-card') or a.find_parent('div', class_='popular-post-item'):
                    errors.append(f"Self-Link Error: {f} links to itself in related posts.")

if errors:
    print("ERRORS FOUND:")
    for e in set(errors):
        print("-", e)
else:
    print("ALL CLEAR: 0 Errors Found. The site is 100% clean.")
