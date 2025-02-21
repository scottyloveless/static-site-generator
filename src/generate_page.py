from markdown_blocks import markdown_to_blocks
from markdown_blocks import markdown_to_html_node
from htmlnode import ParentNode

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
    title = extract_title(markdown_contents)
    print(html_string)
    print(title)

    title_replaced = raw_contents.replace("{{ Title }}", title)
    content_replaced = title_replaced.replace("{{ Content }}", html_string)
    print(content_replaced)

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



