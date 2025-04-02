import unittest

from utils import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_new_nodes = \
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)
    
    def test_split_nodes_delimiter_code_5(self):
        node = TextNode("This `is` text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_new_nodes = \
        [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.CODE),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)
        
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = \
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)
    
    def test_extract_markdown_images_one(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_two(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


if __name__ == "__main__":
    unittest.main()