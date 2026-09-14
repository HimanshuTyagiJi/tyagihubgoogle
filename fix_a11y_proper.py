import os
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace author h4 with div
    content = content.replace('<h4 style="margin:0; color:var(--text-main); font-size:1.4rem;">', '<div style="margin:0; color:var(--text-main); font-size:1.4rem; font-weight:bold;">')
    
    # Replace the corresponding closing </h4>
    # Since we replaced the opening tag with a div, we find that div and replace the </h4> after it
    content = re.sub(r'(<div style="margin:0; color:var\(--text-main\); font-size:1.4rem; font-weight:bold;">.*?)(</h4>)', r'\1</div>', content, flags=re.DOTALL)
    
    # Footer h4 to h3
    content = content.replace('<h4>Legal Info</h4>', '<h3>Legal Info</h3>')
    content = content.replace('<h4>Company</h4>', '<h3>Company</h3>')
    
    # Redundant alt text in grids
    if f in ['index.html', 'categories.html']:
        content = re.sub(r'(<img[^>]*?assets/images/[^>]*?)(alt="[^"]*")([^>]*>)', r'\1alt=""\3', content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print('Done')
