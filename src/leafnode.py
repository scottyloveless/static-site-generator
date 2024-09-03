from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        elif self.props != None:
            for key, value in self.props.items():
                return f"<{self.tag}{key}={value}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        props_aggregate = ""
        if self.props != None:
            for key, value in self.props.items():
                props_aggregate += f" {key}={value}"
        return props_aggregate

    def __repr__(self):
        if self.props != None:
            return f"""<{self.tag} {list(self.props.keys())[0]}="{list(self.props.values())[0]}">{self.value}</{self.tag}>"""
        else:
            return f"""<{self.tag}>{self.value}</{self.tag}>"""
