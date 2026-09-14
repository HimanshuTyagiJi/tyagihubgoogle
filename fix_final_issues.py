import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. Update CSS for Topics FAB
css_file = os.path.join(blog_dir, 'assets', 'css', 'style.css')
fab_css = """
/* --- Mobile Topics FAB --- */
.topics-fab {
    display: none;
    position: fixed; bottom: 20px; right: 20px;
    background: #16a34a; color: #fff;
    padding: 12px 24px; border-radius: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    z-index: 9000; border: none; font-weight: bold; font-size: 1.1rem; cursor: pointer;
}
@media (max-width: 900px) {
    .sidebar-col { display: none !important; }
    .topics-fab { display: block; }
}

.topics-modal {
    display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(0,0,0,0.7); z-index: 10000;
    align-items: center; justify-content: center;
}
.topics-modal.active { display: flex; animation: fadeIn 0.2s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.topics-modal-content {
    background: var(--bg-main); width: 90%; max-width: 400px;
    border-radius: 12px; padding: 25px; position: relative;
    max-height: 80vh; overflow-y: auto; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
.topics-modal-close {
    position: absolute; top: 15px; right: 20px; background: none; border: none;
    font-size: 2rem; color: var(--text-main); cursor: pointer; line-height: 1;
}
.topics-modal-content ul { list-style: none; padding: 0; margin: 0; }
.topics-modal-content ul li { margin-bottom: 15px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; }
.topics-modal-content ul li:last-child { border-bottom: none; }
.topics-modal-content ul li a { color: var(--text-main); text-decoration: none; font-weight: 500; display: block; font-size: 1.1rem; }
.topics-modal-content ul li a:hover { color: var(--primary-color); }
"""
with open(css_file, 'a', encoding='utf-8') as f:
    f.write(fab_css)

# 2. Update JS for Topics FAB
js_file = os.path.join(blog_dir, 'assets', 'js', 'main.js')
fab_js = """
// --- Topics FAB Logic ---
document.addEventListener('DOMContentLoaded', () => {
    const fab = document.getElementById('topicsFab');
    const modal = document.getElementById('topicsModal');
    const closeBtn = document.getElementById('topicsModalClose');
    
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
    f.write(fab_js)


for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # --- 1. Fix Logo (Icon + Text) ---
    header_a = soup.select_one('.logo a')
    if header_a:
        header_a.clear()
        header_a['style'] = "display: flex; align-items: center; gap: 12px; text-decoration: none;"
        
        img = soup.new_tag('img')
        img['src'] = "assets/images/logo.png" # The geometric TH icon
        img['alt'] = "TyagiHub Icon"
        img['style'] = "height: 40px; width: 40px; border-radius: 8px; object-fit: cover;"
        
        span = soup.new_tag('span')
        span['style'] = "color: #16a34a; font-size: 1.8rem; font-weight: 800; letter-spacing: -0.5px;"
        span['title'] = "TyagiHub"
        span.string = "TyagiHub"
        
        header_a.append(img)
        header_a.append(span)
        changed = True

    # Same for footer
    footer_title = soup.select_one('footer .footer-title')
    if footer_title:
        footer_title.clear()
        footer_title['style'] = "display: flex; align-items: center; gap: 10px; margin-bottom: 15px;"
        
        img_f = soup.new_tag('img')
        img_f['src'] = "assets/images/logo.png"
        img_f['alt'] = "TyagiHub Footer Icon"
        img_f['style'] = "height: 35px; width: 35px; border-radius: 6px; object-fit: cover;"
        
        span_f = soup.new_tag('span')
        span_f['style'] = "color: #16a34a; font-size: 1.5rem; font-weight: bold;"
        span_f.string = "TyagiHub"
        
        footer_title.append(img_f)
        footer_title.append(span_f)
        changed = True
        
    # --- 2. Mobile Topics Modal ---
    # Find the Topics ul inside sidebar
    topics_ul = None
    sidebars = soup.find_all('div', class_='sidebar-widget')
    for widget in sidebars:
        title = widget.find('div', class_='sidebar-title')
        if title and 'Topics' in title.get_text(strip=True):
            topics_ul = widget.find('ul')
            break
            
    if topics_ul and not soup.find('div', id='topicsModal'):
        fab_html = '<button id="topicsFab" class="topics-fab">Topics</button>'
        modal_html = f'''
        <div id="topicsModal" class="topics-modal">
            <div class="topics-modal-content">
                <button id="topicsModalClose" class="topics-modal-close" aria-label="Close Topics">&times;</button>
                <h3 style="margin-top:0; color:var(--text-main); font-size:1.5rem; margin-bottom:20px; border-bottom: 2px solid var(--primary-color); padding-bottom: 10px;">Topics</h3>
                {str(topics_ul)}
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

print("Applied graphical logo and Mobile Topics Modal to all HTML files.")
