import os
import re

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

# Find all consecutive duplicate image srcs or any images duplicated in the same file that might be the banner.
for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # find all img srcs
    srcs = re.findall(r'<img[^>]*src="([^"]+)"', content)
    
    # we want to find if the same banner image is used twice
    # banner images are in assets/images/ and end with .webp, excluding himanshu-tyagi-author
    banners = [src for src in srcs if src.endswith('.webp') and 'author' not in src]
    
    if len(banners) != len(set(banners)):
        # print the duplicates
        from collections import Counter
        counts = Counter(banners)
        dups = [item for item, count in counts.items() if count > 1]
        if dups:
            print(f"{f} has duplicates: {dups}")
