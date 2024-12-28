"""
Library Item Model
===================
Defines a base class for items in the library.
"""

class LibraryItem:
    """
    Represents an item in the library.

    Attributes:
        title (str): Title of the item.
        author (str): Author of the item.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
