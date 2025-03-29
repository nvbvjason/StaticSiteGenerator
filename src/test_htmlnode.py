import unittest

from htmlnode import HtmlNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        html_node = HtmlNode(props=props)
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(expected, html_node.props_to_html())
        
    def test_repr_empty(self):
        html_node = HtmlNode()
        expected = ""
        self.assertEqual(expected, html_node.__repr__())
        
    def test_repr_only_tag(self):
        html_node = HtmlNode(tag="tag")
        expected = "tag "
        self.assertEqual(expected, html_node.__repr__())
        
    def test_repr_only_value(self):
        html_node = HtmlNode(value="value")
        expected = "value "
        self.assertEqual(expected, html_node.__repr__())
        
    def test_repr_only_children(self):
        children = []
        children.append("first")
        children.append("second")
        children.append("third")
        html_node = HtmlNode(children=children)
        expected = "children"
        expected += "\n\tfirst"
        expected += "\n\tsecond"
        expected += "\n\tthird"
        expected += "\n"
        self.assertEqual(expected, html_node.__repr__())


if __name__ == "__main__":
    unittest.main()