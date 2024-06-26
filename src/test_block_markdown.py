import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_quote,
    block_type_heading,
    block_type_code,
    block_type_unordered_list,
    block_type_ordered_list
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

    def test_block_to_block_type_heading(self):
        block = "## This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_heading_2(self):
        block = "#### This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_code(self):
        block = "```This is code```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_quote(self):
        block = ">This is a quote line\n>This is another quote line\n>This is the last quote line"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_un_list(self):
        block = "* This is a list line\n* This is another list line"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
    
    def test_block_to_block_type_un_list_2(self):
        block = "* This is a list line\n- This is another list line\n* This is last list line"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_or_list(self):
        block = "1. This is ordered list line\n2. This is another ordered list line\n3. This is last ordered list line"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_block_to_block_type_paragraph(self):
        block = ">This is paragraph line\nThis is also paragraph line"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()