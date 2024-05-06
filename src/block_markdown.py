block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    block_strings = []
    split_blocks = markdown.split("\n\n")
    for block in split_blocks:
        if block == "":
            continue
        block_strings.append(block.strip())
    return block_strings

def block_to_block_type(block):
    block_type = None
    block_lines = block.split("\n")
    quotes = ""
    un_list = ""
    
    # Checking if all lines in a block meet the condition
    for line in block_lines:
        if line.startswith(">"):
            quotes += "y"
        elif line.startswith("* ") or line.startswith("- "):
            un_list += "y"

    if block.startswith ("# ") or block.startswith ("## ") or block.startswith ("### ") or block.startswith ("#### ") or block.startswith ("##### ") or block.startswith ("###### "):
        block_type = block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        block_type = block_type_code

    elif len(quotes) == len(block_lines):
        block_type = block_type_quote
    elif len(un_list) == len(block_lines):
        block_type = block_type_unordered_list
    else:
        block_type = block_type_paragraph
    
    return block_type
