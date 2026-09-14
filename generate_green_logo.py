import os
from PIL import Image, ImageDraw, ImageFont

blog_dir = r'D:\TyagiHubBlog'
images_dir = os.path.join(blog_dir, 'assets', 'images')

# We will try to use Arial Bold, fallback to default if not found
try:
    font_large = ImageFont.truetype("arialbd.ttf", 100)
    font_icon = ImageFont.truetype("arialbd.ttf", 250)
except:
    # If standard Windows font fails, just load whatever default
    import PIL.ImageFont
    font_large = PIL.ImageFont.load_default()
    font_icon = PIL.ImageFont.load_default()

green_color = "#16a34a" # A nice professional green

# 1. Create header_logo.png (Horizontal with text "TyagiHub")
header_img = Image.new('RGBA', (600, 150), (255, 255, 255, 0)) # Transparent
draw_header = ImageDraw.Draw(header_img)

# Center the text "TyagiHub"
try:
    text_bbox = draw_header.textbbox((0, 0), "TyagiHub", font=font_large)
    w = text_bbox[2] - text_bbox[0]
    h = text_bbox[3] - text_bbox[1]
except:
    w, h = 300, 50

draw_header.text(((600 - w) / 2, (150 - h) / 2 - 20), "TyagiHub", fill=green_color, font=font_large)
header_logo_path = os.path.join(images_dir, 'header_logo.png')
header_img.save(header_logo_path, 'PNG')

# 2. Create favicon_base.png (Square with text "TH")
icon_img = Image.new('RGBA', (512, 512), green_color) # Green background
draw_icon = ImageDraw.Draw(icon_img)

try:
    text_bbox_ic = draw_icon.textbbox((0, 0), "TH", font=font_icon)
    w_ic = text_bbox_ic[2] - text_bbox_ic[0]
    h_ic = text_bbox_ic[3] - text_bbox_ic[1]
except:
    w_ic, h_ic = 200, 100

draw_icon.text(((512 - w_ic) / 2, (512 - h_ic) / 2 - 40), "TH", fill=(255, 255, 255), font=font_icon)
icon_logo_path = os.path.join(images_dir, 'favicon_base.png')
icon_img.save(icon_logo_path, 'PNG')

# 3. Generate favicons from favicon_base.png
# apple-touch-icon.png
icon_img.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(blog_dir, 'apple-touch-icon.png'))
# favicon-32x32.png
icon_img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(blog_dir, 'favicon-32x32.png'))
# favicon-16x16.png
icon_img.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(blog_dir, 'favicon-16x16.png'))
# favicon.ico
icon_img.save(os.path.join(blog_dir, 'favicon.ico'), format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64)])

print("Generated green text logos and favicons successfully.")
