import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # Update Mobile Side Menu
    side_menu = soup.find('div', id='mobileSideMenu')
    if side_menu:
        # Check if we already have the mobile-menu-header
        if not side_menu.find('div', class_='mobile-menu-header'):
            # Find existing close button
            close_btn = side_menu.find('button', id='closeMenuBtn')
            if close_btn:
                # We will wrap the logo and the close button in a header div
                header_html = f'''
                <div class="mobile-menu-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1px solid var(--border-color); width: 100%;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <img src="assets/images/logo.png" alt="TyagiHub Icon" style="height: 32px; width: 32px; border-radius: 6px; object-fit: cover;">
                        <span style="color: #16a34a; font-size: 1.4rem; font-weight: 800; letter-spacing: -0.5px;">TyagiHub</span>
                    </div>
                    <button id="closeMenuBtn" class="close-menu-btn" aria-label="Close Menu" style="align-self: auto; margin-bottom: 0; font-size: 2.2rem; margin-top: -5px;">&times;</button>
                </div>
                '''
                
                # Replace the old close button with this new header
                close_btn.replace_with(BeautifulSoup(header_html, 'html.parser'))
                
                # Fix padding of the side menu if needed (already flex column)
                changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Added Logo to the Mobile Side Menu!")
