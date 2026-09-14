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
                # Clear existing content
                a_tag.clear()
                
                # Make sure it has flex styles
                a_tag['style'] = "display: flex; align-items: center; text-decoration: none;"
                
                # Insert the new image
                img = soup.new_tag('img')
                img['src'] = "assets/images/header_logo.png"
                img['alt'] = "TyagiHub Logo"
                img['title'] = "TyagiHub"
                img['height'] = "40" # Fixed height, width will auto-scale
                img['style'] = "object-fit: contain;"
                
                a_tag.append(img)
                changed = True
                
    # 2. Update Footer Logo
    footer = soup.find('footer', class_='main-footer')
    if footer:
        brand_col = footer.find('div', class_='brand-col')
        if brand_col:
            footer_title = brand_col.find('div', class_='footer-title')
            if footer_title:
                footer_title.clear()
                
                img = soup.new_tag('img')
                img['src'] = "assets/images/header_logo.png"
                img['alt'] = "TyagiHub Logo"
                img['title'] = "TyagiHub"
                img['height'] = "35"
                img['style'] = "object-fit: contain;"
                
                footer_title.append(img)
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Replaced header and footer with the new green text logo image.")
