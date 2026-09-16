import os
import re

target_files = [
    'privacy-policy.html', 
    'terms.html', 
    'disclaimer.html', 
    'contact.html', 
    'about.html',
    'categories.html',
    'author.html'
]

directory = r'D:\TyagiHubBlog'

adsense_meta_pattern = re.compile(r'<meta content="ca-pub-[0-9]+" name="google-adsense-account"\s*/?>', re.IGNORECASE)
adsense_script_pattern = re.compile(r'<script[^>]*src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js[^>]*>\s*</script>', re.IGNORECASE)

for filename in target_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = adsense_meta_pattern.sub('', content)
        new_content = adsense_script_pattern.sub('', new_content)
        
        # Remove empty lines that might have been left
        new_content = re.sub(r'\n\s*\n', '\n', new_content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed AdSense code from {filename}")
        else:
            print(f"No AdSense code found in {filename}")
