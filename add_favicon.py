import os
from PIL import Image
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
images_dir = os.path.join(blog_dir, 'assets', 'images')
logo_path = os.path.join(images_dir, 'logo.png')

# 1. Generate Favicon Files
if os.path.exists(logo_path):
    img = Image.open(logo_path).convert('RGBA')
    
    # apple-touch-icon.png
    img.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(blog_dir, 'apple-touch-icon.png'))
    
    # favicon-32x32.png
    img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(blog_dir, 'favicon-32x32.png'))
    
    # favicon-16x16.png
    img.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(blog_dir, 'favicon-16x16.png'))
    
    # favicon.ico (multi-size)
    img.save(
        os.path.join(blog_dir, 'favicon.ico'),
        format='ICO',
        sizes=[(16,16), (32,32), (48,48), (64,64)]
    )
    print("Generated favicon image files.")
else:
    print(f"ERROR: {logo_path} not found.")

# 2. Inject into all HTML files
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

favicon_html = """
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
"""
favicon_soup = BeautifulSoup(favicon_html, 'html.parser')

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    head = soup.find('head')
    if head:
        # Check if already has favicon
        if not head.find('link', rel=lambda r: r and 'icon' in r):
            # Insert the links right before the closing </head>
            head.append(BeautifulSoup(favicon_html, 'html.parser'))
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))
            print(f"Added favicon tags to {f}")
