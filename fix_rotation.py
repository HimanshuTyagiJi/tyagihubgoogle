from PIL import Image, ExifTags
import os

img_path = r'D:\tyagihubblog\assets\images\himanshu-tyagi-author.jpg'
try:
    image = Image.open(img_path)
    # Check EXIF and rotate if necessary
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
            
    exif = image._getexif()
    if exif is not None:
        if orientation in exif:
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
                
    # Remove EXIF by creating new image without it, and ensure it's saved upright
    image.save(img_path, 'JPEG', quality=95)
    print("Fixed rotation and saved.")
except Exception as e:
    print(f"Error: {e}")
