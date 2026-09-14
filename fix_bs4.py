import os
from bs4 import BeautifulSoup

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. Build dictionary
page_meta = {}
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    title_tag = soup.find('title')
    title = title_tag.text.split('|')[0].strip() if title_tag else f.replace('.html', '').replace('-', ' ').title()
    
    og_img = soup.find('meta', property='og:image')
    # get just the filename
    if og_img and og_img.get('content'):
        banner_img = og_img.get('content').split('/')[-1]
    else:
        banner_img = 'default.jpg'
        
    page_meta[f] = {'banner': banner_img, 'title': title}


# 2. Fix the issues
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        html = file.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    
    # We look for all <img> tags
    for img in soup.find_all('img'):
        # Check if this image is inside a link to another article
        parent_a = img.find_parent('a')
        is_sidebar_or_related = False
        target_file = None
        
        if parent_a and parent_a.get('href') and parent_a.get('href').endswith('.html'):
            is_sidebar_or_related = True
            target_file = parent_a.get('href').split('/')[-1]
            
        # Or check if it's inside <div class="popular-post-item"> (sometimes the link is adjacent, not wrapping)
        if not is_sidebar_or_related:
            popular_div = img.find_parent('div', class_='popular-post-item')
            if popular_div:
                a_tag = popular_div.find('a')
                if a_tag and a_tag.get('href') and a_tag.get('href').endswith('.html'):
                    is_sidebar_or_related = True
                    target_file = a_tag.get('href').split('/')[-1]
        
        if is_sidebar_or_related and target_file in page_meta:
            # FIX 1: Set correct src
            correct_src = f"assets/images/{page_meta[target_file]['banner']}"
            if img.get('src') != correct_src:
                img['src'] = correct_src
                changed = True
            
            # FIX 2: Set correct alt
            correct_alt = page_meta[target_file]['title']
            if img.get('alt') != correct_alt:
                img['alt'] = correct_alt
                changed = True
                
            # FIX 3: Remove article-banner class from sidebar/thumbnails
            classes = img.get('class', [])
            if 'article-banner' in classes:
                classes.remove('article-banner')
                img['class'] = classes
                if not classes:
                    del img['class']
                # also explicitly set width/height for thumbnails so they don't break
                img['style'] = "width:100%; height:auto; object-fit:cover; border-radius:8px;"
                changed = True
                
        else:
            # This is likely the MAIN hero banner (or author img)
            if 'article-banner' in img.get('class', []):
                correct_alt = page_meta[f]['title']
                if img.get('alt') == 'Banner' or not img.get('alt'):
                    img['alt'] = f"{correct_alt} Banner"
                    changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Fixed sidebar images & alt texts in {f}")
