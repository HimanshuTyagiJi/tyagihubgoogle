import os

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Exact block to move
    nav_actions_block = '''<div class="nav-actions">
                    
                <div class="search-container" style="position: relative; margin-right: 15px;">
                    <input type="text" id="searchInput" placeholder="Search guides..." autocomplete="off" style="padding: 8px 16px; border-radius: 20px; border: 1px solid var(--border-color); background: var(--bg-alt); color: var(--text-main); outline: none; width: 220px; font-family: inherit; font-size: 0.95rem; transition: border-color 0.3s;">
                    <div id="searchResults" style="display: none; position: absolute; top: 100%; right: 0; width: 320px; background: var(--bg-main); border: 1px solid var(--border-color); border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); z-index: 9999; max-height: 400px; overflow-y: auto; margin-top: 10px;"></div>
                </div>

                </div>'''
    
    if nav_actions_block in content:
        # Remove from inside nav
        content = content.replace(nav_actions_block, '')
        
        # Insert before button
        content = content.replace('<button class="mobile-menu-btn"', nav_actions_block + '\n            <button class="mobile-menu-btn"')
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
