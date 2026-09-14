import os
from bs4 import BeautifulSoup
import re

blog_dir = r'D:\TyagiHubBlog'
css_file = os.path.join(blog_dir, 'assets', 'css', 'style.css')
js_file = os.path.join(blog_dir, 'assets', 'js', 'main.js')

# 1. NEW CSS
new_css = """
/* --- MODERN RESPONSIVE HEADER --- */
.header-logo-img { height: 35px; width: auto; object-fit: contain; }
@media (max-width: 768px) {
    .header-logo-img { height: 28px; } /* Even smaller on mobile to ensure it fits perfectly */
}

.header-inner { display: flex; justify-content: space-between; align-items: center; height: 70px; position: relative; }

.header-actions-wrapper { display: flex; align-items: center; gap: 15px; }

.icon-btn { background: none; border: none; color: var(--text-main); cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 5px; outline: none; }
.icon-btn:hover { color: var(--primary-color); }

.desktop-nav { display: none; }
@media (min-width: 800px) {
    .desktop-nav { display: block; }
    .hamburger-btn { display: none !important; }
}
.desktop-nav ul { list-style: none; display: flex; gap: 20px; margin: 0; padding: 0; }
.desktop-nav ul li a { font-weight: 600; color: var(--text-light); transition: color 0.2s; text-decoration: none; }
.desktop-nav ul li a:hover { color: var(--primary-color); }

/* Search Bar Dropdown */
.search-dropdown-wrapper {
    display: none;
    position: absolute;
    top: 70px;
    left: 0;
    width: 100%;
    background: var(--bg-main);
    padding: 15px 20px;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    border-top: 1px solid var(--border-color);
    z-index: 999;
}
.search-dropdown-wrapper.active { display: block; animation: slideDown 0.3s ease; }
@keyframes slideDown { from { transform: translateY(-10px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

#searchInput {
    width: 100%; padding: 12px 20px; border-radius: 30px; border: 1px solid var(--border-color); background: var(--bg-alt); color: var(--text-main); font-size: 1rem; outline: none;
}

/* Slide-out Menu (Right to Left) */
.mobile-side-menu {
    position: fixed; top: 0; right: -300px; width: 280px; height: 100vh; background: var(--bg-main);
    box-shadow: -5px 0 15px rgba(0,0,0,0.1); z-index: 10000; transition: right 0.3s ease;
    display: flex; flex-direction: column; padding: 30px 20px;
}
.mobile-side-menu.active { right: 0; }

.close-menu-btn { align-self: flex-end; background: none; border: none; font-size: 2.5rem; color: var(--text-main); cursor: pointer; margin-bottom: 30px; line-height: 1; }

.mobile-side-menu ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 20px; }
.mobile-side-menu ul li a { font-size: 1.2rem; font-weight: 600; color: var(--text-main); text-decoration: none; display: block; padding-bottom: 10px; border-bottom: 1px solid var(--border-color); }

.menu-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.5); z-index: 9999; display: none; opacity: 0; transition: opacity 0.3s ease; }
.menu-overlay.active { display: block; opacity: 1; }
"""

with open(css_file, 'a', encoding='utf-8') as f:
    f.write(new_css)


# 2. NEW JS LOGIC
new_js = """
// --- MODERN RESPONSIVE UI LOGIC ---
document.addEventListener('DOMContentLoaded', () => {
    const searchToggleBtn = document.getElementById('searchToggleBtn');
    const searchWrapper = document.getElementById('searchDropdownWrapper');
    const sideMenu = document.getElementById('mobileSideMenu');
    const menuOverlay = document.getElementById('menuOverlay');
    
    // Using querySelectorAll to catch all menu buttons if there are multiple
    const menuButtons = document.querySelectorAll('.hamburger-btn');
    const closeMenuBtn = document.getElementById('closeMenuBtn');

    if(searchToggleBtn && searchWrapper) {
        searchToggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            searchWrapper.classList.toggle('active');
            if(searchWrapper.classList.contains('active')) {
                document.getElementById('searchInput').focus();
            }
        });
        
        document.addEventListener('click', (e) => {
            if(!searchWrapper.contains(e.target) && !searchToggleBtn.contains(e.target)) {
                searchWrapper.classList.remove('active');
            }
        });
        searchWrapper.addEventListener('click', (e) => e.stopPropagation());
    }

    function toggleMenu() {
        if(sideMenu && menuOverlay) {
            sideMenu.classList.toggle('active');
            menuOverlay.classList.toggle('active');
            document.body.style.overflow = sideMenu.classList.contains('active') ? 'hidden' : '';
        }
    }

    menuButtons.forEach(btn => btn.addEventListener('click', toggleMenu));
    if(closeMenuBtn) closeMenuBtn.addEventListener('click', toggleMenu);
    if(menuOverlay) menuOverlay.addEventListener('click', toggleMenu);
});
"""

with open(js_file, 'a', encoding='utf-8') as f:
    f.write(new_js)


# 3. HTML REPLACEMENT
new_header_html = """
<header class="main-header">
  <div class="container header-inner">
    
    <!-- Logo with Image -->
    <div class="logo">
      <a href="index.html" style="display: flex; align-items: center; text-decoration: none;">
        <img src="assets/images/header_logo.png" alt="TyagiHub Logo" title="TyagiHub" class="header-logo-img">
      </a>
    </div>
    
    <!-- Desktop Nav -->
    <nav class="desktop-nav">
       <ul>
         <li><a href="index.html">Home</a></li>
         <li><a href="categories.html">Categories</a></li>
         <li><a href="about.html">About</a></li>
         <li><a href="contact.html">Contact</a></li>
       </ul>
    </nav>
    
    <!-- Actions (Search & Hamburger) -->
    <div class="header-actions-wrapper">
      <button id="searchToggleBtn" class="icon-btn" aria-label="Toggle Search">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      </button>
      
      <button class="icon-btn hamburger-btn" aria-label="Open Menu">
        <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
      </button>
    </div>
    
  </div>
  
  <!-- Collapsible Search Bar (Frees up mobile header space) -->
  <div id="searchDropdownWrapper" class="search-dropdown-wrapper">
     <div style="position: relative; max-width: 600px; margin: 0 auto;">
         <input type="text" id="searchInput" placeholder="Search guides..." aria-label="Search TyagiHub" autocomplete="off">
         <div id="searchResults" style="display: none; position: absolute; top: 100%; left: 0; width: 100%; background: var(--bg-main); border: 1px solid var(--border-color); border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); z-index: 9999; max-height: 400px; overflow-y: auto; margin-top: 10px;"></div>
     </div>
  </div>
</header>

<!-- Slide-out Menu (Right to Left) -->
<div id="mobileSideMenu" class="mobile-side-menu">
   <button id="closeMenuBtn" class="close-menu-btn" aria-label="Close Menu">&times;</button>
   <ul>
     <li><a href="index.html">Home</a></li>
     <li><a href="categories.html">Categories</a></li>
     <li><a href="about.html">About</a></li>
     <li><a href="contact.html">Contact</a></li>
   </ul>
</div>
<div id="menuOverlay" class="menu-overlay"></div>
"""

new_header_soup = BeautifulSoup(new_header_html, 'html.parser')

html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    header = soup.find('header', class_='main-header')
    if header:
        header.replace_with(BeautifulSoup(new_header_html, 'html.parser'))
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Applied modern responsive mobile header to all HTML files.")
