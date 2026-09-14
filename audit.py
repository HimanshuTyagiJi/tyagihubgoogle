import os
import glob
from bs4 import BeautifulSoup

def scan_directory():
    html_files = glob.glob('*.html')
    broken_links = []
    missing_alts = []
    missing_arias = []
    adsense_flags = []
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Check broken links
            for a in soup.find_all('a'):
                href = a.get('href')
                if not href or href == '#' or href == '':
                    broken_links.append((file, a.text.strip() or 'No Text'))
                    
            # Check missing alts
            for img in soup.find_all('img'):
                alt = img.get('alt')
                if alt is None or alt.strip() == '':
                    missing_alts.append((file, img.get('src')))
                    
            # Check missing arias on buttons/inputs without text
            for btn in soup.find_all('button'):
                if not btn.get('aria-label') and not btn.text.strip():
                    missing_arias.append((file, 'button'))
            for inp in soup.find_all('input'):
                if not inp.get('aria-label') and not inp.get('title') and inp.get('type') not in ['submit', 'hidden']:
                    missing_arias.append((file, 'input ' + str(inp.get('type'))))

            # AdSense flags (meta tags for adsense without being in a proper setup, or spammy keyword stuffing)
            for meta in soup.find_all('meta'):
                if meta.get('name') == 'google-adsense-account':
                    adsense_flags.append((file, 'AdSense Meta Tag'))
                    
    print('--- Broken Links ---')
    if broken_links:
        for b in broken_links[:10]: print(b)
        if len(broken_links) > 10: print('...and more')
    else: print('None')
        
    print('\n--- Missing Alts ---')
    if missing_alts:
        for m in missing_alts[:10]: print(m)
        if len(missing_alts) > 10: print('...and more')
    else: print('None')
        
    print('\n--- Missing Arias ---')
    if missing_arias:
        for m in missing_arias[:10]: print(m)
        if len(missing_arias) > 10: print('...and more')
    else: print('None')

    print('\n--- AdSense Flags ---')
    if adsense_flags:
        print(f"Found AdSense tags in {len(adsense_flags)} files.")

scan_directory()
