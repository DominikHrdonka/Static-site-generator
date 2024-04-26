import unittest

from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

class TestInlineMarkdown(unittest.TestCase):

    def test_split_inline_markdown_code(self):
        
        node = TextNode("This is text with a `code block` word", text_type_text)
        expected_nodes = [TextNode("This is text with a ", "text", None), TextNode("code block", "code", None), TextNode(" word", "text", None)]
        result = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(result, expected_nodes)
    
    def test_split_inline_markdown_bold(self):
        node = TextNode("This is text with a **bold block** word", text_type_text)
        expected_nodes = [TextNode("This is text with a ", "text", None), TextNode("bold block", "bold", None), TextNode(" word", "text", None)]
        result = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(result, expected_nodes)
    
    def test_split_inline_markdown_italic(self):
        node = TextNode("This is text with a *italic block* word", text_type_text)
        expected_nodes = [TextNode("This is text with a ", "text", None), TextNode("italic block", "italic", None), TextNode(" word", "text", None)]
        result = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(result, expected_nodes)


if __name__ == "__main__":
    unittest.main()
