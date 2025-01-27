import os

# Specify folders to include
included_folders = ["folder1", "folder2"]

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
        else:
            html += f'<li><a href="{relative_path}">{item}</a></li>\n'
    html += "</ul>\n"
    return html

# Function to generate index.html for a folder
def generate_folder_html(folder, base_path=""):
    files = os.listdir(folder)
    nav_html = generate_nav(".", "")  # Full tree from root
    html_content = f"""
<html>
<head>
<title>{folder}</title>
<style>
  body {{
    display: flex;
  }}
  nav {{
    width: 250px;
    padding: 10px;
    background: #f4f4f4;
    border-right: 1px solid #ddd;
  }}
  main {{
    flex-grow: 1;
    padding: 10px;
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
<h3>Folder Tree</h3>
{nav_html}
</nav>
<main>
<h1>{folder}</h1>
<ul>
"""
    for file in files:
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):  # Only include files
            relative_path = os.path.join(base_path, file)
            html_content += f'<li><a href="{relative_path}">{file}</a></li>\n'
    html_content += """
</ul>
</main>
</body>
</html>
"""
    # Write the index.html for the folder
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html_content)

# Generate root index.html
def generate_root_html(folders):
    nav_html = generate_nav(".", "")  # Full tree from root
    html_content = f"""
<html>
<head>
<title>Root Directory</title>
<style>
  body {{
    display: flex;
  }}
  nav {{
    width: 250px;
    padding: 10px;
    background: #f4f4f4;
    border-right: 1px solid #ddd;
  }}
  main {{
    flex-grow: 1;
    padding: 10px;
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
<h3>Folder Tree</h3>
{nav_html}
</nav>
<main>
<h1>Welcome</h1>
<ul>
"""
    for folder in folders:
        if os.path.exists(folder):
            html_content += f'<li><a href="{folder}/index.html">{folder}</a></li>\n'
    html_content += """
</ul>
</main>
</body>
</html>
"""
    # Write the root index.html
    with open("index.html", "w") as f:
        f.write(html_content)

# Generate index.html for each folder
for folder in included_folders:
    if os.path.exists(folder):
        generate_folder_html(folder)
    else:
        print(f"Folder {folder} does not exist.")

# Generate the root index.html
generate_root_html(included_folders)
