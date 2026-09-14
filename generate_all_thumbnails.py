import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont
import random

blog_dir = r'D:\TyagiHubBlog'
img_dir = os.path.join(blog_dir, 'assets', 'images')

# Download 6 real tech stock photos
urls = [
    'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80', # Laptop
    'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80', # Servers
    'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80', # Matrix
    'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80', # Data
    'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80', # Circuit
    'https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80'  # Network
]
bases = []
for i, url in enumerate(urls):
    fname = f'base_{i}.jpg'
    urllib.request.urlretrieve(url, fname)
    # prep base image
    img = Image.open(fname).convert('RGBA')
    w, h = img.size
    aspect = 800 / 450
    if w/h > aspect:
        new_w = int(h * aspect)
        left = (w - new_w) / 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / aspect)
        top = (h - new_h) / 2
        img = img.crop((0, top, w, top + new_h))
    bases.append(img.resize((800, 450)))

font_path = 'C:/Windows/Fonts/segoeuib.ttf'
try:
    font_lg = ImageFont.truetype(font_path, 60)
    font_md = ImageFont.truetype(font_path, 50)
except:
    font_lg = ImageFont.load_default()
    font_md = ImageFont.load_default()

webp_files = [f for f in os.listdir(img_dir) if f.endswith('.webp')]

styles = ['left_gradient', 'center_box', 'split_solid', 'bottom_bar', 'top_left_badge']
colors = [(30,58,138), (185,28,28), (4,120,87), (180,83,9), (109,40,217), (15,23,42)] # Blue, Red, Green, Amber, Purple, Slate

for idx, file in enumerate(webp_files):
    # Determine title from filename
    name = file.replace('-banner', '').replace('.webp', '').replace('-', ' ').upper()
    if len(name) > 18:
        words = name.split()
        if len(words) > 2:
            title_lines = [" ".join(words[:2]), " ".join(words[2:])]
        else:
            title_lines = [name]
    else:
        title_lines = [name]

    base_img = bases[idx % len(bases)].copy()
    style = styles[idx % len(styles)]
    color = colors[idx % len(colors)]
    
    overlay = Image.new('RGBA', (800, 450), (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    
    if style == 'left_gradient':
        draw.rectangle([0, 0, 450, 450], fill=(color[0], color[1], color[2], 220))
        draw.rectangle([450, 0, 800, 450], fill=(color[0], color[1], color[2], 80))
        y = 130
        for line in title_lines:
            draw.text((40, y), line, font=font_lg, fill='white')
            y += 75
            
    elif style == 'center_box':
        draw.rectangle([0, 0, 800, 450], fill=(0, 0, 0, 100))
        box_w, box_h = 600, 200
        draw.rectangle([100, 125, 700, 325], fill=(color[0], color[1], color[2], 230))
        y = 150
        for line in title_lines:
            draw.text((120, y), line, font=font_md, fill='white')
            y += 65
            
    elif style == 'split_solid':
        draw.rectangle([0, 0, 350, 450], fill=(color[0], color[1], color[2], 255))
        y = 130
        for line in title_lines:
            draw.text((30, y), line, font=font_md, fill='white')
            y += 65
            
    elif style == 'bottom_bar':
        draw.rectangle([0, 320, 800, 450], fill=(color[0], color[1], color[2], 255))
        title = " ".join(title_lines)
        draw.text((30, 350), title, font=font_md, fill='white')
        
    elif style == 'top_left_badge':
        draw.rectangle([0, 0, 800, 450], fill=(0, 0, 0, 150))
        draw.rectangle([40, 40, 40+10, 240], fill=(color[0], color[1], color[2], 255))
        y = 50
        for line in title_lines:
            draw.text((70, y), line, font=font_lg, fill='white')
            y += 75

    out = Image.alpha_composite(base_img, overlay).convert('RGB')
    out.save(os.path.join(img_dir, file), 'WEBP', quality=90)
    print(f"Generated {file} with style {style}")
