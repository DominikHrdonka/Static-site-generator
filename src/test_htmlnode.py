import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props(self):
        node = HTMLNode(props={"href":"www.ahoj.cz", "target":"_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.ahoj.cz" target="_blank"')


if __name__ == "__main__":
    unittest.main()