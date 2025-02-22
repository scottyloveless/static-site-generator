from markdown_blocks import markdown_to_blocks
from markdown_blocks import markdown_to_html_node
from copy_contents import copy_static_to_public
import os, shutil

def make_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    markdown_file = open(from_path, 'r')
    markdown_contents = markdown_file.read()
    markdown_file.close()

    html_file = open(template_path)
    raw_contents = html_file.read()
    html_file.close()

    markdown_to_html = markdown_to_html_node(markdown_contents)
    html_string = markdown_to_html.to_html()
    title = extract_title(markdown_contents) or ""
    print(html_string)
    print(title)

    title_replaced = raw_contents.replace("{{ Title }}", title)
    content_replaced = title_replaced.replace("{{ Content }}", html_string)
    print(content_replaced)

    if dest_path.endswith(".md"):
        dest_path = dest_path.rstrip(".md") + ".html"

    with open(dest_path, "w") as file:
        file.write(content_replaced)
        print(f"HTML file {dest_path} created successfully.")



def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            print(block)
            print(block[2:])
            return block[2:]
        else:
            raise Exception("h1 header not found")

def generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="static"):
    if dest_dir_path == "static":
        if os.path.exists("static"):
            shutil.rmtree("static")
            print("static removed")
            os.mkdir("static")
            print("static created")
    #crawl every entry in content/
    dir_list = os.listdir(dir_path_content)


    for item in dir_list:
        new_current_path = os.path.join(dir_path_content, item)
        new_destination_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(new_current_path):
            if item.endswith(".md"):
                make_page(new_current_path, template_path, new_destination_path)
        else:
            if not os.path.exists(new_destination_path):
                os.mkdir(new_destination_path)
            generate_pages_recursive(new_current_path, template_path, new_destination_path)

    #write to static folder so that it gets put in public folder with main.py
    copy_static_to_public()

