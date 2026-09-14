import os

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

updated_files = 0
target_string = '<button class="mobile-menu-btn" id="mobileMenuBtn">'
replacement_string = '<button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle mobile menu">'

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if target_string in content:
        content = content.replace(target_string, replacement_string)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        updated_files += 1

print(f"Fixed accessibility issue on {updated_files} HTML files.")
