import os
import re

blog_dir = r'D:\TyagiHubBlog'

html_files = []
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # 1. Remove the specific index.html text
    if 'index.html' in filepath:
        new_content = re.sub(r'<h2[^>]*>Our Complete Technical Library \(24 Guides\)</h2>', '', new_content)
        new_content = re.sub(r'<p[^>]*>Browse our massive collection of in-depth guides covering everything from hardware basics to advanced AI algorithms.</p>', '', new_content)
    
    # 2. Fix terms.html mentioning AdSense
    if 'terms.html' in filepath:
        new_content = new_content.replace('violates our AdSense compliance policies', 'violates our Terms of Service')
        new_content = new_content.replace('bypass our AdSense implementations, or ', '')
        
    # 3. Remove ALL HTML comments (<!-- ... -->)
    # Be careful not to remove the doctype or conditional IE comments (though there shouldn't be any here)
    # Using a non-greedy match for anything between <!-- and -->
    new_content = re.sub(r'<!--[\s\S]*?-->', '', new_content)
    
    # 4. Remove empty lines left by deleted comments (optional but makes it cleaner)
    # We will just write it out
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {os.path.basename(filepath)}")

print("Deep scan and cleanup complete.")
