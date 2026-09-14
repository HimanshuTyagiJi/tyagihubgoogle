import os

blog_dir = r'D:\TyagiHubBlog'
cat_path = os.path.join(blog_dir, 'categories.html')

with open(cat_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove 2FA from AI category
block_2fa = '''        <a href="two-factor-authentication-explained.html" class="card-link">
            <div class="rich-card">
                <img loading="lazy" src="assets/images/2fa-banner.webp" alt="Two-Factor Authentication (2FA) Explained: A Security Must-Have" width="800" height="450">
                <div class="rich-card-content">
                    <h4>Two-Factor Authentication (2FA) Explained: A Security Must-Have</h4>
                    <span class="read-more">Read Full Guide →</span>
                </div>
            </div>
        </a>'''
        
if block_2fa in html:
    # It appears twice. We want to remove the first occurrence.
    html = html.replace(block_2fa + '\n', '', 1)

# 2. Remove Frontend vs Backend from Future Tech category
block_frontend = '''        <a href="frontend-vs-backend-development.html" class="card-link">
            <div class="rich-card">
                <img loading="lazy" src="assets/images/frontend-vs-backend.webp" alt="The Difference Between Frontend and Backend Web Development" width="800" height="450">
                <div class="rich-card-content">
                    <h4>The Difference Between Frontend and Backend Web Development</h4>
                    <span class="read-more">Read Full Guide →</span>
                </div>
            </div>
        </a>'''

# This block also appears twice. We want to remove the SECOND occurrence.
# Actually, the Future Tech section has this as its ONLY item.
parts = html.split('<h1 class="cat-title">Future Tech & Networks</h1>')
if len(parts) == 2:
    future_tech_section = parts[1]
    if block_frontend in future_tech_section:
        future_tech_section = future_tech_section.replace(block_frontend, '')
        
        # Now add the missing Future Tech articles!
        missing_articles = '''
        <a href="what-is-6g-technology.html" class="card-link">
            <div class="rich-card">
                <img loading="lazy" src="assets/images/6g-banner.webp" alt="What is 6G Technology? The Complete 2026 Educational Guide" width="800" height="450">
                <div class="rich-card-content">
                    <h4>What is 6G Technology? The Complete 2026 Educational Guide</h4>
                    <span class="read-more">Read Full Guide →</span>
                </div>
            </div>
        </a>
        <a href="what-is-edge-computing.html" class="card-link">
            <div class="rich-card">
                <img loading="lazy" src="assets/images/edge-computing-banner.webp" alt="The Ultimate Guide to Edge Computing in 2026" width="800" height="450">
                <div class="rich-card-content">
                    <h4>The Ultimate Guide to Edge Computing in 2026</h4>
                    <span class="read-more">Read Full Guide →</span>
                </div>
            </div>
        </a>
        <a href="what-is-quantum-computing.html" class="card-link">
            <div class="rich-card">
                <img loading="lazy" src="assets/images/quantum-banner.webp" alt="What is Quantum Computing? The Ultimate 2026 Educational Guide" width="800" height="450">
                <div class="rich-card-content">
                    <h4>What is Quantum Computing? The Ultimate 2026 Educational Guide</h4>
                    <span class="read-more">Read Full Guide →</span>
                </div>
            </div>
        </a>
        <a href="what-is-web3-explained.html" class="card-link">
            <div class="rich-card">
                <img loading="lazy" src="assets/images/web3-banner.webp" alt="Web 3.0 Explained: The Decentralized Internet" width="800" height="450">
                <div class="rich-card-content">
                    <h4>Web 3.0 Explained: The Decentralized Internet</h4>
                    <span class="read-more">Read Full Guide →</span>
                </div>
            </div>
        </a>
        '''
        
        # Insert them into the grid-container in future tech section
        future_tech_section = future_tech_section.replace('<div class="grid-container">', '<div class="grid-container">\n' + missing_articles)
        
        html = parts[0] + '<h1 class="cat-title">Future Tech & Networks</h1>' + future_tech_section

with open(cat_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Manually fixed categories.html")
