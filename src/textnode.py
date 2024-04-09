class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = None

    def eq(self, TextNode_one, TextNode_two):
        if TextNode_one.text == TextNode_two.text and TextNode_one.text_type == TextNode_two.text_type and TextNode_one.url == TextNode_two.url:
            return True
        
    def repr(self, TextNode):
        return f"TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url})"