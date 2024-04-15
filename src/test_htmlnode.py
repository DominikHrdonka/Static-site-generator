import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html2(self):
        node = LeafNode(tag="p", value="This is a paragraph", props={"target":"_top"})
        self.assertEqual(node.to_html(), '<p target="_top">This is a paragraph</p>')

    def test_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value = None, props={"target":"_top"})

class TestParentNode(unittest.TestCase):
    
    def  test_general(self):
        node = ParentNode(
                    tag="p", children=
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_empty_tag(self):
        node = ParentNode(
                    tag="", children=
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_no_tag(self):
        node = ParentNode(
                    children=
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
        with self.assertRaises(ValueError):
            node.to_html()
        
    
if __name__ == "__main__":
    unittest.main()