import unittest
from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node

class TestTextNodeToHTML(unittest.TestCase):
    def test_bold(self):
        node = TextNode("blah blah blah", "bold")
        self.assertEqual(
            text_node_to_html_node(node),
            LeafNode("b", "blah blah blah"),
    )
    def test_italic(self):
        node_italic = TextNode("italic text", "italic")
        self.assertEqual(
                text_node_to_html_node(node_italic),
                LeafNode("i", "italic text"),
        )
    def test_raw_text(self):
        node_raw_text = TextNode("raw text", None)
        self.assertEqual(
                text_node_to_html_node(node_raw_text),
                LeafNode(None, "raw text"),
        )
    def test_code_text(self):
        node_code_text = TextNode("this is some code", "code")
        self.assertEqual(
                text_node_to_html_node(node_code_text),
                LeafNode("code", "this is some code")
        )

    def test_link(self):
        link_text = TextNode("anchor text", "link", "https://google.com")
        self.assertEqual(
                text_node_to_html_node(link_text),
                LeafNode("a", "anchor text", {"href": "https://google.com"})
        )

    def test_image(self):
        image_node = TextNode("alt text", "image", "https://example.com/image.jpg")
        self.assertEqual(
            text_node_to_html_node(image_node),
            LeafNode("img", "", {"src": "https://example.com/image.jpg", "alt": "alt text"})
        )

    def test_invalid_type(self):
        invalid_node = TextNode("some text", "invalid_type")
        with self.assertRaises(ValueError):  # or whatever exception type you're using
            text_node_to_html_node(invalid_node)

    def test_empty_text(self):
        empty_node = TextNode("", "bold")
        self.assertEqual(
            text_node_to_html_node(empty_node),
            LeafNode("b", "")
        )

    def test_empty_link_url(self):
        empty_link_node = TextNode("anchor", "link", "")
        self.assertEqual(
            text_node_to_html_node(empty_link_node),
            LeafNode("a", "anchor", {"href": ""})
        )


if __name__ == "__main__":
    unittest.main()
