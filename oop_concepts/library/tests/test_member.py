import unittest
from models.member import Member
from models.book import Book


class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member(name="John Doe", email="john@example.com")

    def test_borrow_item(self):
        book = Book("Test Book", "Author Name", "Fiction")
        self.member.borrow_item(book)
        self.assertIn(book, self.member.borrowed_items)

    def test_return_item(self):
        book = Book("Test Book", "Author Name", "Fiction")
        self.member.borrow_item(book)
        self.member.return_item(book.item_id)
        self.assertNotIn(book, self.member.borrowed_items)


if __name__ == "__main__":
    unittest.main()