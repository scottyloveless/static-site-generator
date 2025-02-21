import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_header_found_oneline(self):
        markdown = "# Test Yes Header"
        self.assertEqual(
                extract_title(markdown),
                "Test Yes Header",
        )

    def test_header_found(self):
        markdown = "## Test Header"
        with self.assertRaises(Exception) as context:  # Replace ValueError with the specific exception type
            extract_title(markdown)
        self.assertEqual(str(context.exception), "h1 header not found")



if __name__ == "__main__":
    unittest.main()
