"""
Library Item Model
==================
Base class for all library items.
"""

from utils.id_generator import generate_id

class LibraryItem:
    def __init__(self, title, author, item_id=None):
        self.item_id = item_id or generate_id("LI")
        self.title = title
        self.author = author

    def __str__(self):
        return f"ID: {self.item_id}, '{self.title}' by {self.author}"
