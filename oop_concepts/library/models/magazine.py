"""
Magazine Model
==============
Represents a magazine in the library.
"""

from .library_item import LibraryItem


class Magazine(LibraryItem):
    """
    Represents a magazine in the library.

    Attributes:
        issue_number (str): The issue number of the magazine.
        publication_date (str): The publication date of the magazine.
    """

    def __init__(self, title, author, issue_number, publication_date):
        super().__init__(title, author)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def __str__(self):
        return f"{super().__str__()} (Issue: {self.issue_number}, Date: {self.publication_date})"
