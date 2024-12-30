"""
Unit Tests for LibraryController
================================
Tests the functionality of the LibraryController class, ensuring catalog and member
management operations work as expected.
"""

import unittest
from controllers.library_controller import LibraryController
from models.member import Member


class TestLibraryController(unittest.TestCase):
    """Unit tests for LibraryController functionality."""

    def setUp(self):
        """Initialize a test LibraryController instance before each test."""
        self.controller = LibraryController("Test Controller Library")

    def test_add_book(self):
        """Test adding a book to the catalog."""
        self.controller.add_book("Test Book", "Author Name", "Fiction")
        catalog = self.controller.library.catalog
        self.assertTrue(any(item.title == "Test Book" for item in catalog))

    def test_add_magazine(self):
        """Test adding a magazine to the catalog."""
        self.controller.add_magazine("Test Magazine", "Editorial", "Issue 1", "2023-01-01")
        catalog = self.controller.library.catalog
        self.assertTrue(any(item.title == "Test Magazine" for item in catalog))

    def test_add_member(self):
        """Test registering a new member."""
        member = Member(name="John Doe", email="john@example.com")
        self.controller.add_member(member)
        members = self.controller.library.members
        self.assertIn(member, members)


if __name__ == "__main__":
    unittest.main()
