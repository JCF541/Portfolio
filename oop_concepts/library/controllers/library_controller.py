"""
Library Controller
===================
Handles library management operations, including item and member management.
"""

from library_management.models.library import Library
from library_management.models.member import Member
from library_management.models.book import Book
from library_management.models.magazine import Magazine


class LibraryController:
    """
    Handles library operations and coordinates between models and views.
    """

    def __init__(self, library_name="Default Library"):
        self.library = Library(library_name)

    def add_book(self, title, author, genre):
        """
        Adds a book to the library's catalog.
        """
        book = Book(title, author, genre)
        self.library.add_item(book)

    def add_magazine(self, title, author, issue_number, publication_date):
        """
        Adds a magazine to the library's catalog.
        """
        magazine = Magazine(title, author, issue_number, publication_date)
        self.library.add_item(magazine)

    def add_member(self, member):
        """
        Registers a new member to the library.
        """
        self.library.add_member(member)

    def borrow_item(self, member_id, item_title):
        """
        Allows a member to borrow an item by its title.
        """
        member = self.library.find_member(member_id)
        if not member:
            raise ValueError(f"No member found with ID: {member_id}")

        for item in self.library.catalog:
            if item.title == item_title:
                member.borrow_item(item)
                self.library.remove_item(item.item_id)
                return f"'{item.title}' has been borrowed by {member.name}."
        raise ValueError(f"No item with title '{item_title}' found in the catalog.")

    def return_item(self, member_id, item_title):
        """
        Allows a member to return an item by its title.
        """
        member = self.library.find_member(member_id)
        if not member:
            raise ValueError(f"No member found with ID: {member_id}")

        for item in member.borrowed_items:
            if item.title == item_title:
                member.return_item(item.item_id)
                self.library.add_item(item)
                return f"'{item.title}' has been returned to the library."
        raise ValueError(f"No borrowed item with title '{item_title}' found for member {member.name}.")

    def view_items(self):
        """
        Returns a list of all catalog items in the library.
        """
        return self.library.list_catalog()

    def list_members(self):
        """
        Returns a list of all registered members.
        """
        return self.library.list_members()

    def delete_item(self, item_title):
        """
        Deletes an item by its title from the library's catalog.
        """
        for item in self.library.catalog:
            if item.title == item_title:
                self.library.remove_item(item.item_id)
                return f"'{item.title}' has been deleted from the catalog."
        raise ValueError(f"No item with title '{item_title}' found in the catalog.")
