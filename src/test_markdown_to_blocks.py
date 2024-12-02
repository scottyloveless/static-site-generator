import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_block_split(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

        self.assertListEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""
            ]
        )

    def test_three_headings(self):
        markdown = """#heading1

        #heading2

        #heading3"""

        self.assertListEqual(
            markdown_to_blocks(markdown),
            [
                "#heading1",
                "#heading2",
                "#heading3"
            ]
        )

    def test_beginning_empty(self):
        markdown = """

        #heading

        Paragraph of text
        """

        self.assertListEqual(
            markdown_to_blocks(markdown),
            [
                "#heading",
                "Paragraph of text"
            ]
        )
    def test_ending_empty(self):
        markdown = """#heading

        Paragraph of text




        """

        self.assertListEqual(
            markdown_to_blocks(markdown),
            [
                "#heading",
                "Paragraph of text"
            ]
        )

    def test_header_block(self):
        markdown = "#heading"

        self.assertEqual(
            block_to_block_type(markdown),
            BlockType.HEADING
        )

    def test_six_headings(self):
        markdown = "######heading6"

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.HEADING
        )

    def test_seven_headings(self):
        markdown = "#######heading7"

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.PARAGRAPH
        )

    def test_ordered_list_correct(self):
        markdown = """1. Ordered List
        2. Test
        3. Does it work?"""

        self.assertEqual(
            block_to_block_type(markdown),
            BlockType.ORDERED_LIST
        )

    def test_ordered_list_starting_negative(self):
        markdown = """-1. Ordered
        2. List
        3. Test"""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.PARAGRAPH
        )

    def test_ordered_list_starting_not_one(self):
        markdown = """2. Ordered
        3. List
        4. Test"""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.PARAGRAPH
        )


    def test_ordered_list_but_not_incrementing_correctly(self):
        markdown = """1. Ordered
        2. List
        4. But
        5. Not
        7. Incrementing"""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.PARAGRAPH
        )

    def test_unordered_correct(self):
        markdown = """* Ordered
        * List
        * Test"""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.UNORDERED_LIST
        )

    def test_unordered_incorrect_no_space_after_asterisk(self):
        markdown = """*Ordered
        *List
        *Test"""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.PARAGRAPH
        )
    def test_unordered_correct_mixed_asterisk_and_dash(self):
        markdown = """* Ordered
        - List
        * But
        - Mixed"""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.UNORDERED_LIST
        )

    def test_quotes_correct(self):
        markdown = """>Quote
        >text
        > correct."""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.QUOTE
        )

    def test_quote_missing_arrow(self):
        markdown = """>Quote
        but
        >missing
        arrows."""

        self.assertEqual(
                block_to_block_type(markdown),
                BlockType.PARAGRAPH
        )
