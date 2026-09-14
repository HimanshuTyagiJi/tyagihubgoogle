import os
from bs4 import BeautifulSoup
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    changed = False
    
    # 1. REMOVE "Popular Guides" from Sidebar (Fix duplicate content red flag)
    # Search for all sidebar widgets
    for widget in soup.find_all('div', class_='sidebar-widget'):
        # If it has a heading that says "Popular Guides" or contains popular-post-item
        if widget.find(string=re.compile(r'Popular Guides', re.I)) or widget.find('div', class_='popular-post-item'):
            widget.decompose()
            changed = True
            
    # 2. FIX HEADING HIERARCHY
    
    # A. Footer Headings: h3 -> div.footer-title
    for col in soup.find_all('div', class_='footer-col'):
        for h3 in col.find_all('h3'):
            h3.name = 'div'
            h3['class'] = h3.get('class', []) + ['footer-title']
            # Inline style to preserve look just in case CSS doesn't apply
            h3['style'] = "color: #fff; font-size: 1.5rem; margin-bottom: 15px; font-weight: bold;"
            changed = True
            
    # B. Sidebar Headings: h3 -> div.sidebar-title
    for widget in soup.find_all('div', class_='sidebar-widget'):
        for h3 in widget.find_all('h3'):
            h3.name = 'div'
            h3['class'] = h3.get('class', []) + ['sidebar-title']
            h3['style'] = "margin-top: 0; margin-bottom: 20px; font-size: 1.25rem; color: var(--text-main); border-bottom: 2px solid var(--primary-color); padding-bottom: 8px; font-weight: bold;"
            changed = True
            
    # C. Article Bottom ("More from TyagiHub")
    bottom_section = soup.find('div', class_='bottom-related-section')
    if bottom_section:
        # Change the h3 header to h2
        more_heading = bottom_section.find('h3')
        if more_heading:
            more_heading.name = 'h2'
            changed = True
        
        # Change the h4 article titles to div.related-post-title
        for h4 in bottom_section.find_all('h4'):
            h4.name = 'div'
            h4['class'] = h4.get('class', []) + ['related-post-title']
            h4['style'] = "color:var(--text-main); font-size:1.1rem; margin:12px 0 0 0; line-height:1.4; font-weight:bold;"
            changed = True

    # D. Index/Categories Cards
    # These often use h3 or h4 inside rich-card-content or card-content
    for card_content in soup.find_all(['div'], class_=['card-content', 'rich-card-content']):
        for heading in card_content.find_all(['h3', 'h4']):
            heading.name = 'div'
            heading['class'] = heading.get('class', []) + ['card-title']
            heading['style'] = "margin: 0 0 15px 0; color: var(--text-main); font-size: 1.15rem; line-height: 1.5; font-weight: bold;"
            changed = True
            
    # E. index.html specific: Any stray h3 for cards that are NOT in .card-content?
    # In index.html, the cards are just <a><img><h3>...
    if f == 'index.html':
        grid = soup.find('div', class_='grid-container')
        if grid:
            for h3 in grid.find_all('h3'):
                h3.name = 'div'
                h3['class'] = h3.get('class', []) + ['card-title']
                h3['style'] = "margin: 0; font-size: 1.15rem; color: var(--text-main); line-height: 1.4; font-weight: bold;"
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
            
print("Fixed hierarchy and duplicate content!")
