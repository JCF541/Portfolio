"""
Book Model
==========
Represents a book in the library.
"""

from .library_item import LibraryItem


class Book(LibraryItem):
    """
    Represents a book in the library, inheriting from LibraryItem.

    Attributes:
        genre (str): Genre of the book.
    """

    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def __str__(self):
        return f"{super().__str__()} (Genre: {self.genre})"
