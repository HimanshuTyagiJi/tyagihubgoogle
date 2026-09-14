import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # 1. Update Header Logo
    header = soup.find('header', class_='main-header')
    if header:
        logo_div = header.find('div', class_='logo')
        if logo_div:
            a_tag = logo_div.find('a')
            if a_tag:
                # Check if img is already there
                if not a_tag.find('img'):
                    # Change a_tag styles to flex
                    a_tag['style'] = "display: flex; align-items: center; gap: 10px; text-decoration: none;"
                    
                    # Create img tag
                    img = soup.new_tag('img')
                    img['src'] = "assets/images/logo.png"
                    img['alt'] = "TyagiHub Logo"
                    img['width'] = "40"
                    img['height'] = "40"
                    # Add a slight border radius so it looks like an app icon
                    img['style'] = "border-radius: 8px; object-fit: cover;"
                    
                    # Insert img at the beginning of a_tag
                    a_tag.insert(0, img)
                    changed = True
                    
    # 2. Update Footer Logo (Optional but nice)
    footer = soup.find('footer', class_='main-footer')
    if footer:
        brand_col = footer.find('div', class_='brand-col')
        if brand_col:
            footer_title = brand_col.find('div', class_='footer-title')
            if footer_title and not footer_title.find('img'):
                # Make it flex
                footer_title['style'] = footer_title.get('style', '') + " display: flex; align-items: center; gap: 10px;"
                
                img = soup.new_tag('img')
                img['src'] = "assets/images/logo.png"
                img['alt'] = "TyagiHub Footer Logo"
                img['width'] = "35"
                img['height'] = "35"
                img['style'] = "border-radius: 6px; object-fit: cover;"
                
                footer_title.insert(0, img)
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
            
print("Added logo image to header and footer in all HTML files.")
