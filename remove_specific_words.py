import os

directory = r'D:\TyagiHubBlog'

def specific_replace(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

replacements_list = {
    'about.html': [('300-word "tech news" blogs', 'short "tech news" blogs')],
    'contact.html': [('new 2,000-word tech guide', 'new comprehensive tech guide')],
    'what-is-6g-technology.html': [('exhaustive 3000-word educational guide', 'exhaustive educational guide')]
}

for filename, replacements in replacements_list.items():
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        specific_replace(filepath, replacements)

print("Fixed specific leftover instances.")
