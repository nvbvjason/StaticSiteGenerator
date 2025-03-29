class HtmlNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __repr__(self):
        result = ""
        if self.tag != None:
            result += self.tag
            result += " "
        if self.value != None:
            result += self.value
            result += " "
        if self.children != None:
            result += "children"
            result += '\n'
            for child in self.children:
                result += '\t'
                result += child
                result += '\n'
        if self.props != None:
            result += self.props_to_html()
            result += " "
        return result
            
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f" {key}=\"{value}\"" 
        return result
    
    
    