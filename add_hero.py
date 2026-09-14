import re

files = [
    (r'D:\tyagihubblog\what-is-a-password-manager.html', 'password-manager-banner.webp'),
    (r'D:\tyagihubblog\what-is-artificial-intelligence.html', 'ai-explained.webp'),
    (r'D:\tyagihubblog\how-machine-learning-works.html', 'ml-banner.webp')
]

for filepath, img_name in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # check if already has hero image
    if f'src="assets/images/{img_name}" class="article-hero"' not in content:
        img_tag = f'\n        <img src="assets/images/{img_name}" class="article-hero" alt="Hero Image" style="width: 100%; height: auto; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">\n'
        content = content.replace('<div class="blog-content">', '<div class="blog-content">' + img_tag)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added hero image to {filepath}")
