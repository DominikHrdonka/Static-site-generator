import unittest

from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):

    def test_block_markdown(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        
        expected_output = [
                    "This is **bolded** paragraph",
                    "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                    "* This is a list\n* with items"
                        ]
        
        self.assertEqual(markdown_to_blocks(markdown), expected_output)
    
    def test_block_markdown_empty(self):
        markdown = ""
        expected_output = []
        self.assertEqual(markdown_to_blocks(markdown), expected_output)
    
    def test_block_markdown_newlines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        expected_output = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected_output)


if __name__ == "__main__":
    unittest.main()