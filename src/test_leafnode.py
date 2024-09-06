import unittest

from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
#    def test_eq(self):
#        node = HTMLNode("a", "text", None, None)
#        node2 = HTMLNode("a", "text", None, None)
#        self.assertEqual(node, node2)
    def test1(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")

        
    def test2(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), """<a href="https://www.google.com">Click me!</a>""")


if __name__ == "__main__":
    unittest.main()
