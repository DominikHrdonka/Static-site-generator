from block_markdown import *
from htmlnode import *

def heading_block_to_html_node(block):
    if block.startswith("# "):
        block_value = block.strip("# ")
        node = HTMLNode("h1", block_value)
    elif block.startswith("## "):
        block_value = block.strip("## ")
        node = HTMLNode("h2", block_value)
    elif block.startswith("### "):
        block_value = block.strip("### ")
        node = HTMLNode("h3", block_value)
    elif block.startswith("#### "):
        block_value = block.strip("#### ")
        node = HTMLNode("h4", block_value)
    elif block.startswith("##### "):
        block_value = block.strip("##### ")
        node = HTMLNode("h5", block_value)
    elif block.startswith("###### "):
        block_value = block.strip("###### ")
        node = HTMLNode("h6", block_value)
    return node

def markdown_to_html_node(markdown_doc):
    html_nodes = []
    block_strings = markdown_to_blocks(markdown_doc)
    for block in block_strings:
        block_type = block_to_block_type(block)
        #Dealing with heading blocks
        if block_type == block_type_heading:
            html_nodes.append(heading_block_to_html_node(block))
            
            