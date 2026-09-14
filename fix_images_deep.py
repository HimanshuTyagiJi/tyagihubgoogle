import os
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# 1. Build dictionary mapping html_filename -> (banner_image, title)
page_meta = {}
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1).split('|')[0].strip() if title_match else f.replace('.html', '').replace('-', ' ').title()
    
    # Extract Banner Image
    img_match = re.search(r'<meta property="og:image" content="https://tyagihub.in/assets/images/([^"]+)">', content)
    banner_img = img_match.group(1) if img_match else 'default.jpg'
    
    page_meta[f] = {'banner': banner_img, 'title': title}


# 2. Iterate and fix all files
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    orig = content
    
    # A. Fix the main hero banner alt text
    # We look for the img just before </header> or the one that actually IS the main banner
    # Actually, let's just find the first `<img ... class="article-banner"` in the file (which should be the main one)
    # But wait, we are removing class="article-banner" from the others, so we can do that first.
    
    # B. Fix all links containing an image
    def fix_link_image(match):
        a_tag_content = match.group(0)
        href_match = re.search(r'href=["\']([^"\']+\.html)["\']', a_tag_content)
        if href_match:
            dest_html = href_match.group(1)
            dest_html = dest_html.split('/')[-1] # just in case
            
            if dest_html in page_meta:
                correct_img = page_meta[dest_html]['banner']
                correct_title = page_meta[dest_html]['title']
                
                # Replace src
                a_tag_content = re.sub(r'src=["\'][^"\']+["\']', f'src="assets/images/{correct_img}"', a_tag_content)
                # Replace alt
                a_tag_content = re.sub(r'alt=["\'][^"\']*["\']', f'alt="{correct_title}"', a_tag_content)
                # Remove class="article-banner" if present
                a_tag_content = re.sub(r'class=["\']article-banner["\']', '', a_tag_content)
                
        return a_tag_content

    # This regex finds <a ...> ... <img ...> ... </a>
    # We use a cautious approach: find <a> tags that contain an <img>
    content = re.sub(r'<a\s+[^>]*href=["\'][^"\']+\.html["\'][^>]*>[\s\S]*?<img[\s\S]*?</a>', fix_link_image, content)
    
    # Wait, the popular-post-item structure is sometimes:
    # <div class="popular-post-item"> <img ...> <div> <a href="...">...</a> </div> </div>
    # The image is NOT inside the <a> tag!
    # Let's write a specific fixer for popular-post-item
    def fix_popular_post(match):
        block = match.group(0)
        href_match = re.search(r'href=["\']([^"\']+\.html)["\']', block)
        if href_match:
            dest_html = href_match.group(1).split('/')[-1]
            if dest_html in page_meta:
                correct_img = page_meta[dest_html]['banner']
                correct_title = page_meta[dest_html]['title']
                block = re.sub(r'src=["\'][^"\']+["\']', f'src="assets/images/{correct_img}"', block)
                block = re.sub(r'alt=["\'][^"\']*["\']', f'alt="{correct_title}"', block)
                block = re.sub(r'class=["\']article-banner["\']', '', block)
        return block

    content = re.sub(r'<div class="popular-post-item">[\s\S]*?</div>\s*</div>', fix_popular_post, content)

    # Now, fix the MAIN hero banner's alt text
    # It's the only one left with class="article-banner" (if it had it)
    my_title = page_meta[f]['title']
    content = re.sub(r'(<img[^>]*class=["\']article-banner["\'][^>]*)alt=["\']Banner["\']', r'\1alt="' + my_title + '"', content)
    content = re.sub(r'(<img[^>]*class=["\']article-banner["\'][^>]*)alt=["\']["\']', r'\1alt="' + my_title + '"', content)

    if orig != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed images and alt texts in {f}")

