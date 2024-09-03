import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
#    def test_eq(self):
#        node = HTMLNode("a", "text", None, None)
#        node2 = HTMLNode("a", "text", None, None)
#        self.assertEqual(node, node2)
    def test_print(self):
        node = HTMLNode("a", "text", None, {"href": "https://www.google.com", "target": "_blank"})
        return print(node)




if __name__ == "__main__":
    unittest.main()
