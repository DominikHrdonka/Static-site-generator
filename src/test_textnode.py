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


if __name__ == "__main__":
    unittest.main()
