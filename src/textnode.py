from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url = ""):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        return self.url == other.url
           
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    