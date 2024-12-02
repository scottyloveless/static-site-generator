from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = list(map(str.strip, blocks))
    while("" in result):
        result.remove("")
    return result

def block_to_block_type(block):
    type = ""
    lines = block.split("\n")
    lines = list(map(str.lstrip, lines))
    if (block.startswith("#") or block.startswith("##") or block.startswith("###") or block.startswith("####") or block.startswith("#####") or block.startswith("######")) and not block.startswith("#######"):
        type = BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        type = BlockType.CODE
    elif all([line.startswith(">") for line in lines]):
        type = BlockType.QUOTE
    elif all([line.startswith("* ") or line.startswith("- ") for line in lines]):
            type = BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        if all(line[0].isdigit() for line in lines):
            list_of_starting_ints = []
            for line in lines:
                list_of_starting_ints.append(int(line[0]))
            if all(y - x==1 for x,y in zip(list_of_starting_ints,list_of_starting_ints[1:])):
                type = BlockType.ORDERED_LIST
            else:
                type = BlockType.PARAGRAPH
    else:
        type = BlockType.PARAGRAPH
    return type

#def markdown_to_html_node(markdown):
#    parent_node = HTMLNode
#    blocks = markdown_to_blocks(markdown)
#    for block in blocks:
#        block_type = block_to_block_type(block)
#        match block_type:
#            case 
#
#    return parent_node
