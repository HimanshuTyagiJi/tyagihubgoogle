import os
import re

directory = r'D:\TyagiHubBlog'

def replace_patterns(content):
    # Meta description replacements
    content = re.sub(r'(A\s+)?massive,?\s+\d+(,\d+)?\+?-?word\s+(deep dive|guide)', r'A comprehensive \3', content, flags=re.IGNORECASE)
    content = re.sub(r'comprehensive\s+\d+(,\d+)?\+?-?word\s+guide', 'comprehensive guide', content, flags=re.IGNORECASE)
    
    # JSON-LD Schema replacements (remove wordCount entirely)
    content = re.sub(r'\s*"wordCount":\s*"\d+",?', '', content)
    
    # Specific file textual replacements
    content = content.replace('frequently exceed 2,000 words', 'are incredibly detailed and exhaustive')
    content = content.replace('superficial 300-word summaries', 'superficial short summaries')
    content = content.replace('complex 3,000-word tutorial', 'complex, long-form tutorial')
    
    return content

processed = 0
modified = 0

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
            
        new_content = replace_patterns(original_content)
        
        if original_content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1
        processed += 1

print(f"Processed {processed} files, updated {modified} files successfully.")
