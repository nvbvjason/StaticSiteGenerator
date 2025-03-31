import unittest

from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(leaf_node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()