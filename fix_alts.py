import os
from bs4 import BeautifulSoup

def fix_alt_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    
    # Find all anchor tags (which are the article cards)
    links = soup.find_all('a', class_='article-card')
    for link in links:
        img = link.find('img')
        h4 = link.find('h4')
        if img and h4:
            alt_val = img.get('alt')
            # If alt is missing or empty
            if alt_val is None or alt_val.strip() == '':
                title_text = h4.get_text(strip=True)
                img['alt'] = f"Thumbnail for {title_text}"
                changed = True
                
    if changed:
        # Save back the HTML
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed alt tags in {os.path.basename(filepath)}")

# We will just apply this to all HTML files just in case
blog_dir = r'D:\TyagiHubBlog'
for f in os.listdir(blog_dir):
    if f.endswith('.html'):
        fix_alt_tags(os.path.join(blog_dir, f))
