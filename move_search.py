import os

blog_dir = r'D:\TyagiHubBlog'
html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(blog_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Locate <div class="nav-actions">
    nav_actions_start = content.find('<div class="nav-actions">')
    
    # Locate the end of the <div class="nav-actions"> by finding </nav>
    nav_end = content.find('</nav>', nav_actions_start)
    
    if nav_actions_start != -1 and nav_end != -1:
        # Extract the entire nav-actions block
        # Actually it's just before </nav>
        
        # Let's find the closing </div> of nav-actions. 
        # It's right before </nav> in our structure (with maybe some whitespace).
        nav_actions_block = content[nav_actions_start:nav_end]
        
        # Remove it from the current position
        content = content[:nav_actions_start] + content[nav_end:]
        
        # Insert it before <button class="mobile-menu-btn"
        btn_index = content.find('<button class="mobile-menu-btn"')
        if btn_index != -1:
            content = content[:btn_index] + nav_actions_block + '\n            ' + content[btn_index:]
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)

print("Moved nav-actions outside of main-nav for mobile visibility.")
