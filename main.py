import os

# Specify folders to include
included_folders = ["folder1", "folder2"]

# Function to generate index.html for a folder
def generate_folder_html(folder):
    files = os.listdir(folder)
    html_content = f"<html>\n<head>\n<title>{folder}</title>\n</head>\n<body>\n<h1>{folder}</h1>\n<ul>\n"
    
    for file in files:
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):  # Only include files
            html_content += f'<li><a href="{file}">{file}</a></li>\n'
    
    html_content += "</ul>\n</body>\n</html>"
    
    # Write the index.html for the folder
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html_content)

# Generate root index.html
def generate_root_html(folders):
    html_content = "<html>\n<head>\n<title>Root Directory</title>\n</head>\n<body>\n<h1>Welcome</h1>\n<ul>\n"
    
    for folder in folders:
        if os.path.exists(folder):
            html_content += f'<li><a href="{folder}/index.html">{folder}</a></li>\n'
    
    html_content += "</ul>\n</body>\n</html>"
    
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
