import glob
from bs4 import BeautifulSoup
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        headings = [int(h.name[1]) for h in soup.find_all(re.compile('^h[1-6]$'))]
        if not headings: continue
        if headings[0] != 1:
            print(f"{file}: First heading is not H1 (is H{headings[0]})")
        
        # check if there are multiple H1
        if headings.count(1) > 1:
            print(f"{file}: Multiple H1 tags found")
            
        # check skips
        prev = headings[0]
        for h in headings[1:]:
            if h - prev > 1:
                print(f"{file}: Skipped heading level from H{prev} to H{h}")
            prev = h
