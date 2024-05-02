import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_links
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
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
        node = TextNode(
                "",
                text_type_text 
            )
        
        expected_output = []
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_nodes_links_simple(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com)",
            text_type_text,
        )
        expected_output = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com")
        ]
        self.assertEqual(split_nodes_links([node]), expected_output)

    def test_split_nodes_links_complex(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text,
        )
        expected_output = [
            TextNode("This is text with a ", text_type_text),
            TextNode(" and ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode("another", text_type_link, "https://www.example.com/another")
        ]
        self.assertEqual(split_nodes_links([node]), expected_output)

    def test_split_nodes_links_no_link(self):
        node = TextNode(
            "This is text with a link",
            text_type_text,
            )
        expected_output = [
            TextNode(
            "This is text with a link",
            text_type_text,
            )
        ]
        self.assertEqual(split_nodes_links([node]), expected_output)

    def test_split_nodes_link_empty(self):
        node = TextNode(
                "",
                text_type_text 
            )
        
        expected_output = []
        self.assertEqual(split_nodes_links([node]), expected_output)
    
    def test_split_nodes_links_more_complex(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/second_link) and [third link](https://www.example.com/third_link)",
            text_type_text,
            )
        expected_output = [
            TextNode("This is text with a ", text_type_text),
            TextNode(" and another ", text_type_text),
            TextNode(" and ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode("second link", text_type_link, "https://www.example.com/second_link"),
            TextNode("third link", text_type_link, "https://www.example.com/third_link")
        ]
        self.assertEqual(split_nodes_links([node]), expected_output)


    
    

if __name__ == "__main__":
    unittest.main()
