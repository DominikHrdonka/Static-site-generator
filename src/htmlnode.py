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
        for key, value in self.props:
            html_props += f" {key}={value} "
        return html_props
    
    def __repr__(self) -> str:
        return f"{self}: {self.tag}, {self.value}, {self.children}, {self.props}"