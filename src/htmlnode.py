class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props = ""
        for key, value in self.props.items():
            html_props += f' {key}="{value}"'
        return html_props
    
    def __repr__(self) -> str:
        return f"{self}: {self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children = None, props=None):
        super().__init__(tag, value, children, props)
        if self.value == None:
            raise ValueError("Value property is required!")

    def to_html(self):
    
        if self.tag == None:
            return f"{self.props_to_html()} {self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            