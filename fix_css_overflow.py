import os
import re

blog_dir = r'D:\TyagiHubBlog'
css_file = os.path.join(blog_dir, 'assets', 'css', 'style.css')

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# 1. Force fix the Table CSS
new_table_css = """
/* --- Table & Overflow Global Fix --- */
.table-responsive-wrapper {
    display: block;
    width: 100%;
    max-width: 100vw;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin: 30px 0;
    border: 1px solid var(--border-color);
    border-radius: 8px;
}
.blog-content table {
    display: table !important;
    width: 100% !important;
    min-width: 600px; /* Forces scrolling on mobile */
    margin: 0; 
    border-collapse: collapse;
}
.blog-content th, .blog-content td {
    white-space: normal !important;
    word-break: normal !important;
}

pre, code {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100%;
}
pre {
    overflow-x: auto;
}
/* --------------------------------- */
"""

# Remove the old buggy block
css_content = re.sub(r'/\* --- Table Overflow Fix --- \*/.*?(?=\/\* --- Header Layout Updates)', '', css_content, flags=re.DOTALL)

# Also remove my new block if it got half-added
css_content = re.sub(r'/\* --- Table & Overflow Global Fix --- \*/.*?(?=\/\* --------------------------------- \*/)\/\* --------------------------------- \*/', '', css_content, flags=re.DOTALL)

css_content += "\n" + new_table_css

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Fixed CSS for tables and code blocks to prevent mobile overflow!")
