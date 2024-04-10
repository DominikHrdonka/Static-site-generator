import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props(self):
        node = HTMLNode(props={"href":"www.ahoj.cz", "target":"_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.ahoj.cz" target="_blank"')

    def test_props2(self):
        node = HTMLNode("div", "Hello", None, props={"href":"boot.dev", "target":"parent"})
        self.assertEqual(node.props_to_html(), ' href="boot.dev" target="parent"')
    
    def test_props3(self):
        node = HTMLNode(props={"href":"www.gotit.com", "target":"top"})
        self.assertNotEqual(node.props_to_html(), 'href="www.gotit.com" target="_top"')

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode(tag="a", value="This is a paragraph", props={"href":"www.boot.dev", "target":"_top"})
        self.assertEqual(node.to_html(), '<a href="www.boot.dev" target="_top">This is a paragraph</a>')



    def test_to_html_tag(self):
        node = LeafNode(tag=None, value="This is a paragraph", props={"href":"www.boot.dev", "target":"_top"})
        self.assertEqual(node.to_html(), ' href="www.boot.dev" target="_top" This is a paragraph')

    
if __name__ == "__main__":
    unittest.main()