import os
import base64
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
css_file = os.path.join(blog_dir, 'assets', 'css', 'style.css')
js_file = os.path.join(blog_dir, 'assets', 'js', 'main.js')

# 1. Base64 SVG Logo
svg_raw = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 50" width="220" height="50">
  <text x="0" y="38" font-family="Arial, Helvetica, sans-serif" font-size="38" font-weight="800" fill="#16a34a" letter-spacing="-1">TyagiHub</text>
</svg>"""
b64_svg = base64.b64encode(svg_raw.encode('utf-8')).decode('utf-8')
img_src = f"data:image/svg+xml;base64,{b64_svg}"

# 2. Update CSS
new_css = """
/* Mobile TOC FAB */
.toc-fab {
    display: none;
    position: fixed; bottom: 25px; right: 25px;
    background: #16a34a; color: #fff;
    padding: 14px 24px; border-radius: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    z-index: 9000; border: none; font-weight: bold; font-size: 1.1rem; cursor: pointer;
}
@media (max-width: 900px) {
    .col-toc { display: none !important; }
    .toc-fab { display: block; }
}

/* Modal for TOC */
.toc-modal {
    display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(0,0,0,0.7); z-index: 10000;
    align-items: center; justify-content: center;
}
.toc-modal.active { display: flex; animation: fadeIn 0.2s ease; }

.toc-modal-content {
    background: var(--bg-main); width: 90%; max-width: 400px;
    border-radius: 12px; padding: 25px; position: relative;
    max-height: 80vh; overflow-y: auto; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
.toc-modal-close {
    position: absolute; top: 15px; right: 20px; background: none; border: none;
    font-size: 2rem; color: var(--text-main); cursor: pointer; line-height: 1;
}
.toc-modal-content ul { list-style: none; padding: 0; margin: 0; }
.toc-modal-content ul li { margin-bottom: 15px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; }
.toc-modal-content ul li:last-child { border-bottom: none; }
.toc-modal-content ul li a { color: var(--text-main); text-decoration: none; font-weight: 500; display: block; }
.toc-modal-content ul li a:hover { color: var(--primary-color); }
"""
with open(css_file, 'a', encoding='utf-8') as f:
    f.write(new_css)

# 3. Update JS
new_js = """
// TOC FAB Logic
document.addEventListener('DOMContentLoaded', () => {
    const fab = document.getElementById('tocFab');
    const modal = document.getElementById('tocModal');
    const closeBtn = document.getElementById('tocModalClose');
    
    if(fab && modal && closeBtn) {
        fab.addEventListener('click', () => {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
        
        const closeModal = () => {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        };
        
        closeBtn.addEventListener('click', closeModal);
        modal.addEventListener('click', (e) => {
            if(e.target === modal) closeModal();
        });
        
        modal.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', closeModal);
        });
    }
});
"""
with open(js_file, 'a', encoding='utf-8') as f:
    f.write(new_js)

# 4. Process HTML Files
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # --- Fix Logo ---
    logos = soup.find_all('img', class_='header-logo-img')
    for logo in logos:
        logo['src'] = img_src
        logo['style'] = "object-fit: contain; height: 45px;" # Slightly bigger
        changed = True
    
    # Same for footer logo if it doesn't have the class but is the same image
    for img in soup.find_all('img'):
        if img.get('src') == 'assets/images/header_logo.svg':
            img['src'] = img_src
            changed = True
            
    # --- Fix Mobile TOC ---
    toc = soup.find('aside', class_='col-toc')
    if toc:
        ul = toc.find('ul')
        if ul:
            # Check if modal already exists to prevent duplicates
            if not soup.find('div', id='tocModal'):
                # Build HTML block
                fab_html = '<button id="tocFab" class="toc-fab">Chapters</button>'
                modal_html = f'''
                <div id="tocModal" class="toc-modal">
                    <div class="toc-modal-content">
                        <button id="tocModalClose" class="toc-modal-close" aria-label="Close Chapters">&times;</button>
                        <h3 style="margin-top:0; color:var(--text-main); font-size:1.5rem; margin-bottom:20px; border-bottom: 2px solid var(--primary-color); padding-bottom: 10px;">Chapters</h3>
                        {str(ul)}
                    </div>
                </div>
                '''
                body = soup.find('body')
                if body:
                    body.append(BeautifulSoup(fab_html, 'html.parser'))
                    body.append(BeautifulSoup(modal_html, 'html.parser'))
                    changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("Fixed logo with base64 embedded SVG and created mobile TOC FAB!")
