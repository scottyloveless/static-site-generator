import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_node1_type_different(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", "italics", None)
        node2 = TextNode("This is a text node", "italics", "google.com")
        self.assertNotEqual(node, node2)

    def test_text_is_different(self):
        node = TextNode("This is a text node", "italics", None)
        node2 = TextNode("This is a different text", "italics")
        self.assertNotEqual(node, node2)





if __name__ == "__main__":
    unittest.main()
