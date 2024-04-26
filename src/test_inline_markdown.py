import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images
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

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected_output = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(extract_markdown_images(text), expected_output)

if __name__ == "__main__":
    unittest.main()
