import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_quote
)

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



    def test_block_to_block_type(self):
        block = ">This is a quote line\n>This is another quote line\n>This is the last quote line"
        self.assertEqual(block_to_block_type(block), block_type_quote)

if __name__ == "__main__":
    unittest.main()