import os
import re

directory = r'D:\TyagiHubBlog'

def replace_patterns(content):
    # Regex to catch "2000+ word", "2,000-word", "3000 words", etc.
    # We replace it with nothing or 'comprehensive' depending on context
    
    # "A deep, 2000+ word educational dive" -> "A deep, comprehensive educational dive"
    content = re.sub(r'2000\+ word', 'comprehensive', content, flags=re.IGNORECASE)
    content = re.sub(r'3000\+ word', 'comprehensive', content, flags=re.IGNORECASE)
    content = re.sub(r'\d{1,4}[,+]*[- ]word', 'comprehensive', content, flags=re.IGNORECASE)
    
    # Specific meta cleanups
    content = content.replace('massive, comprehensive deep dive', 'comprehensive deep dive')
    content = content.replace('massive comprehensive deep dive', 'comprehensive deep dive')
    content = content.replace('massive, comprehensive educational dive', 'comprehensive educational dive')
    content = content.replace('massive comprehensive educational dive', 'comprehensive educational dive')
    content = content.replace('over the next comprehensives', 'throughout this guide')
    
    return content

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
            
        new_content = replace_patterns(original_content)
        
        if original_content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Fixed all remaining word counts.")
