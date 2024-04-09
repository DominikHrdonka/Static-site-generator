class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, TextNode_one, TextNode_two):
        if TextNode_one.text == TextNode_two.text and TextNode_one.text_type == TextNode_two.text_type and TextNode_one.url == TextNode_two.url:
            return True
        
    def repr(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


