import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    
match = re.search(r'<article class="post-card">.*?</article>', text, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("No post-card found")
