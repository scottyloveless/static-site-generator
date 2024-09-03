class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag or None
        self.value = value or None
        self.children = children or None
        self.props = props or None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_aggregate = ""
        if self.props != None:
            for key, value in self.props.items():
                props_aggregate += f" {key}={value}"
        return props_aggregate

    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props_to_html()}"
