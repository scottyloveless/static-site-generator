from generate_page import make_page
from copy_contents import copy_static_to_public

def main():
    copy_static_to_public()
    make_page("content/index.md", "template.html", "static/index.html")
    copy_static_to_public()
main()
