import os
from PIL import Image, ImageDraw, ImageFont

blog_dir = r'D:\TyagiHubBlog'
img_dir = os.path.join(blog_dir, 'assets', 'images')

# We already have base_0.jpg to base_5.jpg downloaded from previous script.
bases = []
for i in range(6):
    fname = os.path.join(blog_dir, f'base_{i}.jpg')
    if os.path.exists(fname):
        img = Image.open(fname).convert('RGBA')
        bases.append(img.resize((800, 450)))
    else:
        # Fallback just in case
        bases.append(Image.new('RGBA', (800, 450), color=(50,50,50,255)))

font_path = 'C:/Windows/Fonts/segoeuib.ttf'
try:
    font_xl = ImageFont.truetype(font_path, 65)
    font_lg = ImageFont.truetype(font_path, 55)
    font_md = ImageFont.truetype(font_path, 45)
except:
    font_xl = ImageFont.load_default()
    font_lg = ImageFont.load_default()
    font_md = ImageFont.load_default()

webp_files = [f for f in os.listdir(img_dir) if f.endswith('.webp')]

# News channel colors (Solid, no transparency)
# Red, Dark Blue, Deep Yellow, Emerald Green, Maroon
colors = [(220, 38, 38, 255), (30, 58, 138, 255), (217, 119, 6, 255), (4, 120, 87, 255), (153, 27, 27, 255)] 

styles = ['news_bottom', 'news_left', 'news_split_ribbon', 'news_breaking_box']

for idx, file in enumerate(webp_files):
    name = file.replace('-banner', '').replace('.webp', '').replace('-', ' ').upper()
    if len(name) > 20:
        words = name.split()
        if len(words) >= 3:
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
    
    if style == 'news_bottom':
        # Solid bar at the bottom like a news ticker
        draw.rectangle([0, 310, 800, 450], fill=color)
        draw.rectangle([0, 310, 800, 320], fill=(250, 204, 21, 255)) # Yellow accent line
        
        y = 330
        for line in title_lines:
            draw.text((30, y), line, font=font_md, fill='white')
            y += 50
            
    elif style == 'news_left':
        # Solid block on the left (very common in news panels)
        draw.rectangle([0, 0, 400, 450], fill=color)
        draw.rectangle([390, 0, 400, 450], fill=(255, 255, 255, 255)) # White separator
        
        y = 120
        for line in title_lines:
            draw.text((30, y), line, font=font_lg, fill='white')
            y += 70
            
    elif style == 'news_split_ribbon':
        # Two solid overlapping ribbons at bottom left
        draw.rectangle([0, 250, 500, 340], fill=color)
        draw.rectangle([0, 340, 650, 430], fill=(30, 41, 59, 255)) # Dark slate ribbon
        
        if len(title_lines) >= 1:
            draw.text((30, 265), title_lines[0], font=font_lg, fill='white')
        if len(title_lines) >= 2:
            draw.text((30, 355), title_lines[1], font=font_lg, fill='white')
        elif len(title_lines) == 1:
             draw.text((30, 355), "EXPLAINED", font=font_lg, fill='white')
             
    elif style == 'news_breaking_box':
        # Solid box taking up bottom left corner
        box_w = 550
        box_h = 180
        draw.rectangle([0, 450-box_h, box_w, 450], fill=color)
        # Red "Breaking" top badge
        draw.rectangle([0, 450-box_h-40, 200, 450-box_h], fill=(220, 38, 38, 255))
        draw.text((15, 450-box_h-35), "TECH NEWS", font=ImageFont.truetype(font_path, 25), fill='white')
        
        y = 450 - box_h + 15
        for line in title_lines:
            draw.text((30, y), line, font=font_lg, fill='white')
            y += 65

    out = Image.alpha_composite(base_img, overlay).convert('RGB')
    out.save(os.path.join(img_dir, file), 'WEBP', quality=90)
    print(f"Generated {file} with style {style}")
