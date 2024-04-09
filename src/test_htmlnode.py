import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props(self):
        node = HTMLNode(props={"href":"www.ahoj.cz", "target":"_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.ahoj.cz" target="_blank"')

    def test_props2(self):
        node = HTMLNode(props={"href":"boot.dev", "target":"parent"})
        self.assertEqual(node.props_to_html(), ' href="boot.dev" target="parent"')
    
    def test_props3(self):
        node = HTMLNode(props={"href":"www.gotit.com", "target":"top"})
        self.assertNotEqual(node.props_to_html(), 'href="www.gotit.com" target="_top"')

if __name__ == "__main__":
    unittest.main()