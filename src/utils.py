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

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def build_markdown_link(link, url):
    return f"[{link}]({url})"

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        result.extend(split_node_link(old_node))
    return result
    
def split_node_link(old_node):
    old_node_text = old_node.text
    links = extract_markdown_links(old_node_text)
    result = []
    text = old_node_text
    for link in links:
        link_text = build_markdown_link(link[0], link[1])
        first_index_link = text.find(link_text)
        left_text = text[:first_index_link]
        if left_text != "":
            result.append(TextNode(left_text, TextType.TEXT))
        result.append(TextNode(link[0], TextType.LINK, link[1]))
        text = text[first_index_link + len(link_text):]
    if text != "":
        result.append(TextNode(text, TextType.TEXT))
    return result
    
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def build_image_link(alt_text, url):
    return f"![{alt_text}]({url})"
     
def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        result.extend(split_node_image(old_node))
    return result
    
def split_node_image(old_node):
    old_node_text = old_node.text
    images = extract_markdown_images(old_node_text)
    result = []
    text = old_node_text
    for image in images:
        image_text = build_image_link(image[0], image[1])
        first_index_image = text.find(image_text)
        left_text = text[:first_index_image]
        if left_text != "":
            result.append(TextNode(left_text, TextType.TEXT))
        result.append(TextNode(image[0], TextType.IMAGE, image[1]))
        text = text[first_index_image + len(image_text):]
    if text != "":
        result.append(TextNode(text, TextType.TEXT))
    return result
    