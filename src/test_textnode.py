import unittest

from textnode import *
from inline_markdown import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_type(self):
        node = TextNode("This is a test", "italic", None)
        node2 = TextNode("This is a test", "bold")
        self.assertNotEqual(node, node2)
    
    def test_eq_text(self):
        node = TextNode("Some node", "bold", None)
        node2 = TextNode("This is a test", "bold")
        self.assertNotEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a test", "bold", "http://facebook.com")
        node2 = TextNode("This is a test", "bold", "http://facebook.com")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    
    def test_split_nodes(self):
        old_nodes = [TextNode("This is text with a `code block` word", text_type_text), TextNode("This is also text with a `code block` word", text_type_text)]
        self.assertEqual(split_nodes_delimiter(old_nodes, "`", text_type_code), '[TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text)]')


if __name__ == "__main__":
    unittest.main()
