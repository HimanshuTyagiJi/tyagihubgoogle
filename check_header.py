import os
with open('ai-impact-on-healthcare.html', 'r', encoding='utf-8') as f:
    text = f.read()
    start = text.find('<header class="blog-header">')
    end = text.find('</header>')
    print(text[start:end+10])
