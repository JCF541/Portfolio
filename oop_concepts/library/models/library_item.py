"""
Library Item Model
==================
Base class for all library items.
"""

from utils.id_generator import generate_id


class LibraryItem:
    """
    Represents an item in the library.

    Attributes:
        item_id (str): A unique ID for the library item.
        title (str): Title of the item.
        author (str): Author of the item.
    """

    def __init__(self, title, author):
        self.item_id = generate_id("LI")  # Unique ID with "LI" prefix
        self.title = title
        self.author = author

    def __str__(self):
        return f"ID: {self.item_id}, '{self.title}' by {self.author}"
