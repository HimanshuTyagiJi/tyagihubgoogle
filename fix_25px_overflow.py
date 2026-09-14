import os
import re

blog_dir = r'D:\TyagiHubBlog'
css_file = os.path.join(blog_dir, 'assets', 'css', 'style.css')

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

new_table_css = """
/* --- Table & Overflow Global Fix --- */
.layout-wrapper {
    max-width: 100% !important;
    box-sizing: border-box !important;
}
.blog-container.main-col {
    min-width: 0 !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}
.table-responsive-wrapper {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important; /* Forces it to respect parent padding, unlike 100vw */
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    margin: 30px 0 !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 8px !important;
    box-sizing: border-box !important;
}
.blog-content table {
    display: table !important;
    width: 100% !important;
    min-width: 600px !important; /* Table scrolls inside wrapper */
    margin: 0 !important; 
    border-collapse: collapse !important;
}
.blog-content th, .blog-content td {
    white-space: normal !important;
    word-break: normal !important;
}

pre, code {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}
pre {
    overflow-x: auto !important;
}
/* --------------------------------- */
"""

# Replace the previous block
css_content = re.sub(r'/\* --- Table & Overflow Global Fix --- \*/.*?(?=\/\* --------------------------------- \*/)\/\* --------------------------------- \*/', '', css_content, flags=re.DOTALL)
css_content += "\n" + new_table_css

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS updated to completely eliminate 25px overflow bug.")
