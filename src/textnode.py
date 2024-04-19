from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(value= text_node.text)
    
    elif text_node.text_type == text_type_bold:
        return LeafNode(tag="b", value = text_node.text)
    
    elif text_node.text_type == text_type_italic:
        return LeafNode(tag="i", value = text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode(tag="code", value = text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode(tag = "a", value= text_node.text, props="href")
    elif text_node.text_type == text_type_image:
        return LeafNode(tag="img", value=None, props={"src": text_node.url, "alt":text_node.text})

    else:
        raise Exception("Not a valid text type")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for oldnode in old_nodes:
        if isinstance(oldnode, TextNode):
            if oldnode.text_type != text_type_text:
                new_nodes.extend(oldnode)
            elif delimiter not in oldnode.text:
                raise Exception("Invalid markdown syntax, delimiter not found")
            else:
                split_text = oldnode.text.split(delimiter)
                return [
                    TextNode(split_text[0], text_type_text),
                    TextNode(split_text[1], )
                ]
            
                new_nodes.extend(split_nodes_delimiter([oldnode], delimiter, text_type))
        return new_nodes
    


