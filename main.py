import os

# Specify folders to include
included_folders = ["folder1", "folder2", "folder3"]

# Function to generate folder tree structure as HTML
def generate_nav(folder, base_path=""):
    html = "<ul>\n"
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        relative_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            html += f'<li><strong>{item}/</strong>\n'
            html += generate_nav(item_path, relative_path)  # Recursive call for subfolders
            html += "</li>\n"
        elif item.endswith(".html"):  # Include only HTML files
            html += f'<li><a href="{relative_path}">{item}</a></li>\n'
    html += "</ul>\n"
    return html

# Function to add a navigation bar to an HTML file
def add_navbar_to_html(file_path, nav_html):
    with open(file_path, "r") as f:
        original_content = f.read()
    
    # Insert the navigation bar
    html_content = f"""
<html>
<head>
<title>Navigation</title>
<style>
  body {{
    display: flex;
    flex-direction: row;
    margin: 0;
    padding: 0;
  }}
  nav {{
    width: 250px;
    padding: 10px;
    background: #f4f4f4;
    border-right: 1px solid #ddd;
    height: 100vh;
    overflow-y: auto;
  }}
  main {{
    flex-grow: 1;
    padding: 20px;
  }}
  a {{
    text-decoration: none;
    color: #0073e6;
  }}
  a:hover {{
    text-decoration: underline;
  }}
</style>
</head>
<body>
<nav>
<h3>Navigation</h3>
{nav_html}
</nav>
<main>
{original_content}
</main>
</body>
</html>
"""
    with open(file_path, "w") as f:
        f.write(html_content)

# Generate the folder tree HTML
nav_html = generate_nav(".", "")

# Add the navigation bar to all HTML files
for folder in included_folders:
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                add_navbar_to_html(file_path, nav_html)
