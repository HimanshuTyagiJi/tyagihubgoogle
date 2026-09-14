import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # 1. Revert Header Logo to Green Text
    header = soup.find('header', class_='main-header')
    if header:
        logo_div = header.find('div', class_='logo')
        if logo_div:
            a_tag = logo_div.find('a')
            if a_tag:
                a_tag.clear()
                # Remove inline flex styles added earlier
                if 'style' in a_tag.attrs:
                    del a_tag['style']
                
                # Re-add text logo but in pure green
                span = soup.new_tag('span')
                span['class'] = "logo-text"
                span['style'] = "color: #16a34a;" # Techy green
                span['title'] = "TyagiHub"
                span.string = "TyagiHub"
                
                a_tag.append(span)
                changed = True
                
    # 2. Revert Footer Logo to Text
    footer = soup.find('footer', class_='main-footer')
    if footer:
        brand_col = footer.find('div', class_='brand-col')
        if brand_col:
            # We look for the first footer-title which is the brand name
            footer_title = brand_col.find('div', class_='footer-title')
            if footer_title:
                footer_title.clear()
                if 'style' in footer_title.attrs:
                    # Remove the flex style we added
                    footer_title['style'] = "color: #fff; font-size: 1.5rem; margin-bottom: 15px; font-weight: bold;"
                
                span = soup.new_tag('span')
                span['style'] = "color: #16a34a;"
                span['title'] = "TyagiHub"
                span.string = "TyagiHub"
                
                footer_title.append(span)
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Reverted logo back to text and made it green!")
