"""
Unit Tests for Library Class
============================
Tests the functionality of the Library class, including adding/removing items
and managing members.
"""

import unittest
from models.library import Library
from models.book import Book
from models.magazine import Magazine
from models.member import Member


class TestLibrary(unittest.TestCase):
    """Unit tests for Library class functionality."""

    def setUp(self):
        """Initialize a test library instance before each test."""
        self.library = Library("Test Library")

    def test_add_item(self):
        """Test adding an item to the catalog."""
        book = Book("Test Book", "Author Name", "Fiction")
        self.library.add_item(book)
        self.assertIn(book, self.library.catalog)

    def test_remove_item(self):
        """Test removing an item from the catalog."""
        book = Book("Test Book", "Author Name", "Fiction")
        self.library.add_item(book)
        self.library.remove_item(book.item_id)
        self.assertNotIn(book, self.library.catalog)

    def test_add_member(self):
        """Test registering a new member."""
        member = Member(name="John Doe", email="john@example.com")
        self.library.add_member(member)
        self.assertIn(member, self.library.members)

    def test_find_member(self):
        """Test finding a member by ID."""
        member = Member(name="Jane Doe", email="jane@example.com")
        self.library.add_member(member)
        found_member = self.library.find_member(member.member_id)
        self.assertEqual(member, found_member)


if __name__ == "__main__":
    unittest.main()
