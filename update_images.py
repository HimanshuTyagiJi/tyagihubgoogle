from PIL import Image
import os

images = {
    r'C:\Users\himan\.gemini\antigravity\brain\088e9058-764d-4230-b977-229097173098\password_manager_1789374469298.jpg': r'D:\tyagihubblog\assets\images\password-manager-banner.webp',
    r'C:\Users\himan\.gemini\antigravity\brain\088e9058-764d-4230-b977-229097173098\ai_explained_1789374496427.jpg': r'D:\tyagihubblog\assets\images\ai-explained.webp',
    r'C:\Users\himan\.gemini\antigravity\brain\088e9058-764d-4230-b977-229097173098\ml_banner_1789374518600.jpg': r'D:\tyagihubblog\assets\images\ml-banner.webp'
}

for src, dest in images.items():
    if os.path.exists(src):
        img = Image.open(src)
        # Resize to 800x450
        img = img.resize((800, 450), Image.LANCZOS)
        # Save as optimized webp
        img.save(dest, 'WEBP', quality=80)
        print(f"Updated {dest}")
    else:
        print(f"Source not found: {src}")
