"""
Book Model
==========
Represents a book in the library.
"""

from .library_item import LibraryItem
from utils.file_manager import generate_id

class Book(LibraryItem):
    def __init__(self, title, author, genre, item_id=None):
        super().__init__(title, author, item_id or generate_id("BK"))
        self.genre = genre

    def __str__(self):
        return f"{super().__str__()} (Genre: {self.genre})"

