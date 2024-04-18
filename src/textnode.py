from htmlnode import LeafNode
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
    
    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(value= self.text)
        
        elif self.text_type == "bold":
            return LeafNode(tag="b", value = self.text)
        
        elif self.text_type == "italic":
            return LeafNode(tag="i", value = self.text)
        elif self.text_type == "code":
            return LeafNode(tag="code", value = self.text)
        elif self.text_type == "link":
            return LeafNode(tag = "a", value=self.text, props="href")
        elif self.text_type == "image":
            return LeafNode(tag="img", value=None, props={"src": self.url, "alt":self.text})

        else:
            raise Exception("Not a valid text type")
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


