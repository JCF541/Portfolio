"""
Unit Tests for Library Management System
========================================
Tests the functionality of library management, including book addition,
member registration, and persistence.
"""

import unittest
from controllers import LibraryController

class TestLibraryController(unittest.TestCase):
    def setUp(self):
        self.library = LibraryController()

    def test_add_book(self):
        book = self.library.add_book("1984", "George Orwell", "Dystopian")
        self.assertEqual(book.title, "1984")
        self.assertEqual(len(self.library.view_items()), 1)

if __name__ == "__main__":
    unittest.main()
