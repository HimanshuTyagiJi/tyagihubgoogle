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
                a_tag.clear()
                
                # Make sure it has flex styles
                a_tag['style'] = "display: flex; align-items: center; text-decoration: none; gap: 12px;"
                
                # Insert the graphical Image Logo
                img = soup.new_tag('img')
                img['src'] = "assets/images/logo.png"
                img['alt'] = "TyagiHub Icon"
                img['class'] = "header-logo-icon"
                img['style'] = "height: 40px; width: 40px; border-radius: 8px; object-fit: cover;"
                
                # Insert the Green Text
                span = soup.new_tag('span')
                span['class'] = "logo-text"
                span['style'] = "color: #16a34a; font-size: 1.8rem; font-weight: 800; letter-spacing: -0.5px;"
                span['title'] = "TyagiHub"
                span.string = "TyagiHub"
                
                a_tag.append(img)
                a_tag.append(span)
                changed = True
                
    # 2. Update Footer Logo
    footer = soup.find('footer', class_='main-footer')
    if footer:
        brand_col = footer.find('div', class_='brand-col')
        if brand_col:
            footer_title = brand_col.find('div', class_='footer-title')
            if footer_title:
                footer_title.clear()
                footer_title['style'] = "display: flex; align-items: center; gap: 10px; margin-bottom: 15px;"
                
                img = soup.new_tag('img')
                img['src'] = "assets/images/logo.png"
                img['alt'] = "TyagiHub Footer Icon"
                img['style'] = "height: 35px; width: 35px; border-radius: 6px; object-fit: cover;"
                
                span = soup.new_tag('span')
                span['style'] = "color: #16a34a; font-size: 1.5rem; font-weight: bold;"
                span.string = "TyagiHub"
                
                footer_title.append(img)
                footer_title.append(span)
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Restored graphical logo next to green text in header and footer.")
