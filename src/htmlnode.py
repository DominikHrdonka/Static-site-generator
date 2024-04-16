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
        if self.props:
            for key, value in self.props.items():
                html_props += f' {key}="{value}"'
        return html_props
        
    
    def __repr__(self) -> str:
        return f"{self}: {self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError("Value property is required!")

    def to_html(self):
        if self.tag == None:
            return f"{self.props_to_html()} {self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("You must provide the tag attribute.")
        elif not self.children:
            raise ValueError("Children attribute must be included.")
        else:
            def concatenate(self):
                string = ""
                for child in self.children:
                    if isinstance(child, ParentNode):
                        concatenate(child)
                    elif isinstance(child, LeafNode):
                        if not child.tag:
                            string += f"{child.value}"
                        else:
                            string += f"<{child.tag}{child.props_to_html()}>{child.value}</{child.tag}>"
                return f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"
            return concatenate(self)
