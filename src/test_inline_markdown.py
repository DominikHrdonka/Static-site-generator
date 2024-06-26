import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
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
        self.assertEqual(extract_markdown_images(text), expected_output)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected_output = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_markdown_links(text), expected_output)

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
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
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
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode(" and ", text_type_text),
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
        self.assertEqual(split_nodes_link([node]), expected_output)

    def test_split_nodes_links_complex(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text,
        )
        expected_output = [
            TextNode("This is text with a ", text_type_text),
             TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another")
        ]
        self.assertEqual(split_nodes_link([node]), expected_output)

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
        self.assertEqual(split_nodes_link([node]), expected_output)

    def test_split_nodes_link_empty(self):
        node = TextNode(
                "",
                text_type_text 
            )
        
        expected_output = []
        self.assertEqual(split_nodes_link([node]), expected_output)
    
    def test_split_nodes_links_more_complex(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/second_link) and [third link](https://www.example.com/third_link)",
            text_type_text,
            )
        expected_output = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://www.example.com/second_link"),
            TextNode(" and ", text_type_text),
            TextNode("third link", text_type_link, "https://www.example.com/third_link")
        ]
        self.assertEqual(split_nodes_link([node]), expected_output)


    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        
        expexted_output = [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expexted_output)

    def test_text_to_textnodes_bold(self):
        text = "This is **text** with another **bold** word and yet another **bold word**."
        expexted_output = [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with another ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word and yet another ", text_type_text),
                TextNode("bold word", text_type_bold),
                TextNode(".", text_type_text),
        ]
        self.assertEqual(text_to_textnodes(text), expexted_output)
    
    def test_text_to_textnodes_empty(self):
        text = ""
        expected_output = []
        self.assertEqual(text_to_textnodes(text), expected_output)
    

if __name__ == "__main__":
    unittest.main()
