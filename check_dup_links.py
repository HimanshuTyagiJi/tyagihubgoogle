import glob
from bs4 import BeautifulSoup
from collections import Counter

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
        counts = Counter(links)
        dups = {k: v for k, v in counts.items() if v > 1 and not k.startswith('#') and k != 'index.html' and k != 'categories.html' and k != 'about.html' and k != 'contact.html' and k != 'privacy-policy.html' and k != 'terms.html' and k != 'disclaimer.html' and k != 'author.html'}
        if dups:
            print(f"{file} has duplicate links: {dups}")
