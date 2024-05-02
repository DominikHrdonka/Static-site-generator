import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image
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
        self.assertEqual(extract_markdown_images(r"!\[(.*?)\]\((.*?)\)", text), expected_output)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected_output = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_markdown_links(r"\[(.*?)\]\((.*?)\)", text), expected_output)

    def test_split_nodes_image_simple(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text,
        )
        expected_output = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        ]
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_nodes_image_complex(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
            )
        expected_output = [
            TextNode("This is text with an ", text_type_text),
            TextNode(" and another ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            
        ]
        self.assertEqual(split_nodes_image([node]), expected_output)
    
    def test_split_nodes_image_more_complex(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and ![third image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
            )
        expected_output = [
            TextNode("This is text with an ", text_type_text),
            TextNode(" and another ", text_type_text),
            TextNode(" and ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode("third image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        self.assertEqual(split_nodes_image([node]), expected_output)
    
    def test_split_nodes_image_no_image(self):
        node = TextNode(
            "This is text with an image",
            text_type_text,
            )
        expected_output = [
            TextNode(
            "This is text with an image",
            text_type_text,
            )
        ]
        self.assertEqual(split_nodes_image([node]), expected_output)
    
    def test_split_nodes_image_empty(self):
        pass

    
    

if __name__ == "__main__":
    unittest.main()
