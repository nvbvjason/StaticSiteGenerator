import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        split_node_text = old_node.text.split(delimiter)
        for idx, text in enumerate(split_node_text):
            if idx % 2 == 0:
                result.append(TextNode(text, TextType.TEXT))
            if idx % 2 == 1:
                result.append(TextNode(text, text_type))
    return result

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
    