import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_props(self):
        node = ParentNode(
            "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
        )
        self.assertEqual(
                node.to_html(),
                "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
    
    def testing_parent_with_multiple_parents(self):
        node = ParentNode(
            "p",
                [
                    ParentNode(
                        "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode("i", "italic text"),
                            ],
                )
                ],
        )
        self.assertEqual(
                node.to_html(),
                "<p><p><b>Bold text</b><i>italic text</i></p></p>"
        )
    
    def test_repr(self):
        node = ParentNode(
            "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                ],
        )
        self.assertEqual(
                node.__repr__(),
                "ParentNode(p, children: [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None)], None)"
        )
    
    def test_no_children(self):
        node = ParentNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = ParentNode(None, [
                                LeafNode("b", "Bold text"),
                                LeafNode("i", "italic text"),
                            ],
                          )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_values(self):
        node = ParentNode(
                    "p",
                        [ 
                            LeafNode("b", "Bold text"),
                            LeafNode("i", "italic text"),
                        ],
                    )
        self.assertEqual(
                node.tag,
                "p",
        )
        self.assertEqual(
                str(node.children),
                '[LeafNode(b, Bold text, None), LeafNode(i, italic text, None)]',
        )
        self.assertEqual(
            node.value,
            None,
        )






if __name__ == "__main__":
    unittest.main()
