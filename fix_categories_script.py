import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
filepath = os.path.join(blog_dir, 'categories.html')

with open(filepath, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

body = soup.find('body')
if body:
    # Check if main.js is already there
    has_script = False
    for script in soup.find_all('script'):
        if script.get('src') == 'assets/js/main.js':
            has_script = True
            break
            
    if not has_script:
        script_tag = soup.new_tag('script', src="assets/js/main.js")
        body.append(script_tag)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print("Successfully injected main.js into categories.html")
    else:
        print("main.js already exists.")
else:
    print("Error: Could not find <body> tag in categories.html")
