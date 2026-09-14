import os
from PIL import Image, ImageDraw, ImageFont

blog_dir = r'D:\TyagiHubBlog'
img_dir = os.path.join(blog_dir, 'assets', 'images')

banners = [
    {
        'file': 'password-manager-banner.webp',
        'title': 'PASSWORD MANAGER',
        'subtitle': 'Ultimate Security Guide',
        'bg': (30, 41, 59),       # Dark Slate
        'accent': (59, 130, 246)  # Blue
    },
    {
        'file': 'ai-explained.webp',
        'title': 'WHAT IS AI?',
        'subtitle': 'Artificial Intelligence Explained',
        'bg': (49, 46, 129),      # Dark Indigo
        'accent': (139, 92, 246)  # Purple
    },
    {
        'file': 'ml-banner.webp',
        'title': 'MACHINE LEARNING',
        'subtitle': 'How Computers Learn',
        'bg': (6, 78, 59),        # Dark Emerald
        'accent': (16, 185, 129)  # Green
    },
    {
        'file': 'cloud-computing.webp',
        'title': 'CLOUD COMPUTING',
        'subtitle': 'IaaS, PaaS, and SaaS',
        'bg': (124, 45, 18),      # Dark Orange
        'accent': (245, 158, 11)  # Amber
    }
]

font_title_path = 'C:/Windows/Fonts/segoeuib.ttf'
font_sub_path = 'C:/Windows/Fonts/segoeui.ttf'

for b in banners:
    width, height = 800, 450
    img = Image.new('RGB', (width, height), color=b['bg'])
    draw = ImageDraw.Draw(img)
    
    # Draw an angled Canva-style shape
    points = [(width*0.5, 0), (width, 0), (width, height), (width*0.3, height)]
    draw.polygon(points, fill=b['accent'])
    
    # Add a slight dark overlay to the right side to balance
    overlay = Image.new('RGBA', (width, height), (0,0,0,0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.polygon(points, fill=(0, 0, 0, 40))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype(font_title_path, 65)
        font_sub = ImageFont.truetype(font_sub_path, 35)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Draw Text
    title_x, title_y = 50, 150
    draw.text((title_x+3, title_y+3), b['title'], font=font_title, fill=(0, 0, 0)) # Shadow
    draw.text((title_x, title_y), b['title'], font=font_title, fill=(255, 255, 255))
    
    sub_y = title_y + 80
    draw.text((title_x+2, sub_y+2), b['subtitle'], font=font_sub, fill=(0, 0, 0))
    draw.text((title_x, sub_y), b['subtitle'], font=font_sub, fill=(240, 240, 240))
    
    # Save
    out_path = os.path.join(img_dir, b['file'])
    img.save(out_path, 'WEBP', quality=90)
    print(f"Generated {b['file']}")
