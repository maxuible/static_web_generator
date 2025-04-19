
class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props ==None:
            return ""
        string = ""
        for prop in self.props:
            string += f"{prop}=\"{self.props[prop]}\" "
        string = string.rstrip(" ")
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All LeafNodes must have a value")
        else:
            if self.tag == None:
                return self.value
            else:
                if self.props == None:
                    return f"<{self.tag}>{self.value}</{self.tag}>"
                else:
                    return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNodes must have Tags")
        elif self.children == None:
            raise ValueError("ParentNode must have Children")
        else:
            string = ""
            for child in self.children:
                string += child.to_html()
            if self.props == None:
                return f"<{self.tag}>{string}</{self.tag}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{string}</{self.tag}>"