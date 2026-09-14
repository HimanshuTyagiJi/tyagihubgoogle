import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # New Links
    new_links_desktop = [
        ('Privacy', 'privacy-policy.html'),
        ('Terms', 'terms.html'),
        ('Disclaimer', 'disclaimer.html')
    ]
    
    new_links_mobile = [
        ('Privacy Policy', 'privacy-policy.html'),
        ('Terms of Service', 'terms.html'),
        ('Disclaimer', 'disclaimer.html')
    ]
    
    # 1. Update Desktop Nav
    desktop_nav = soup.find('nav', class_='desktop-nav')
    if desktop_nav:
        ul = desktop_nav.find('ul')
        if ul:
            # Check if Privacy is already there to prevent duplicates
            has_privacy = False
            for a in ul.find_all('a'):
                if 'privacy' in a.get('href', '').lower():
                    has_privacy = True
                    break
            
            if not has_privacy:
                # To prevent overflow, we can add a small CSS tweak to the desktop-nav ul if we want,
                # but adding li is enough for now.
                ul['style'] = "list-style: none; display: flex; gap: 15px; margin: 0; padding: 0;" # Reduced gap to 15px
                
                for text, href in new_links_desktop:
                    li = soup.new_tag('li')
                    a = soup.new_tag('a', href=href)
                    a.string = text
                    li.append(a)
                    ul.append(li)
                changed = True

    # 2. Update Mobile Side Menu
    side_menu = soup.find('div', id='mobileSideMenu')
    if side_menu:
        ul = side_menu.find('ul')
        if ul:
            has_privacy = False
            for a in ul.find_all('a'):
                if 'privacy' in a.get('href', '').lower():
                    has_privacy = True
                    break
            
            if not has_privacy:
                for text, href in new_links_mobile:
                    li = soup.new_tag('li')
                    a = soup.new_tag('a', href=href)
                    a.string = text
                    # We need to maintain the existing classes/styles if any, but in my previous script they were handled by CSS.
                    li.append(a)
                    ul.append(li)
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Added legal links to both Desktop and Mobile navigation menus.")
