import os
from PIL import Image, ImageDraw, ImageFont

# Ensure directory exists
out_dir = r"D:\TyagiHubBlog\assets\images"
os.makedirs(out_dir, exist_ok=True)

try:
    # Try to load a Windows standard font
    font_large = ImageFont.truetype("segoeuib.ttf", 80)
    font_medium = ImageFont.truetype("segoeuib.ttf", 60)
except:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()

# 1. Create logo.png (512x512)
img_logo = Image.new('RGB', (512, 512), color=(15, 23, 42)) # Dark blue-grey (var(--bg-main))
draw_logo = ImageDraw.Draw(img_logo)
# Draw text "TH" or "TyagiHub"
# We will just center "TyagiHub"
text_logo = "Tyagi\nHub"
bbox = draw_logo.textbbox((0, 0), text_logo, font=font_large)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
draw_logo.text(((512-w)/2, (512-h)/2 - 20), text_logo, fill=(16, 185, 129), font=font_large, align="center") # Green highlight
img_logo.save(os.path.join(out_dir, "logo.png"))

# 2. Create default.jpg (1200x630) for OG/Twitter
img_def = Image.new('RGB', (1200, 630), color=(15, 23, 42))
draw_def = ImageDraw.Draw(img_def)
text_def = "TyagiHub\nTechnical Library"
bbox2 = draw_def.textbbox((0, 0), text_def, font=font_large)
w2 = bbox2[2] - bbox2[0]
h2 = bbox2[3] - bbox2[1]
draw_def.text(((1200-w2)/2, (630-h2)/2), text_def, fill=(255, 255, 255), font=font_large, align="center")
# Highlight word Hub
# (simple version: just let it be white, or draw a green accent line)
draw_def.line([(1200-w2)/2, (630+h2)/2 + 20, (1200+w2)/2, (630+h2)/2 + 20], fill=(16, 185, 129), width=8)

img_def.save(os.path.join(out_dir, "default.jpg"), quality=90)

print("Created logo.png and default.jpg successfully!")
