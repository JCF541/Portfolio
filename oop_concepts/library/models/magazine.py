"""
Magazine Model
==============
Represents a magazine in the library.
"""

from .library_item import LibraryItem
from utils.file_manager import generate_id


class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number, publication_date, item_id=None):
        super().__init__(title, author, item_id or generate_id("MG"))
        self.issue_number = issue_number
        self.publication_date = publication_date

    def __str__(self):
        return f"{super().__str__()} (Issue: {self.issue_number}, Date: {self.publication_date})"
