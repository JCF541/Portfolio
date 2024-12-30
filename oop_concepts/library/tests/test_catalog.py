import unittest
from models.library import Library
from models.book import Book
from models.magazine import Magazine


class TestCatalog(unittest.TestCase):
    def setUp(self):
        self.library = Library("Test Library")

    def test_list_catalog(self):
        book = Book("Test Book", "Author Name", "Fiction")
        magazine = Magazine("Test Magazine", "Editorial", "Issue 1", "2023-01-01")
        self.library.add_item(book)
        self.library.add_item(magazine)
        catalog = self.library.list_catalog()
        self.assertIn(str(book), catalog)
        self.assertIn(str(magazine), catalog)


if __name__ == "__main__":
    unittest.main()
