"""
Library Model
=============
Represents a library with its own catalog of items and registered members.
"""

from .book import Book
from .magazine import Magazine
from .member import Member

class Library:
    """
    Represents a library system.

    Attributes:
        name (str): The name of the library.
        catalog (list): A collection of library items.
        members (list): A list of registered members.
    """
    def __init__(self, name):
        self.name = name
        self.catalog = []
        self.members = []

    def add_item(self, item):
        """
        Adds an item to the library's catalog.

        Args:
            item (LibraryItem): The item to add.
        """
        self.catalog.append(item)

    def remove_item(self, item_id):
        """
        Removes an item from the catalog by ID.

        Args:
            item_id (str): The unique ID of the item to remove.
        """
        self.catalog = [item for item in self.catalog if item.item_id != item_id]

    def add_member(self, member):
        """
        Registers a new member to the library.

        Args:
            member (Member): The member to register.
        """
        self.members.append(member)

    def find_member(self, member_id):
        """
        Finds a member by their ID.

        Args:
            member_id (str): The ID of the member.

        Returns:
            Member: The member object if found, otherwise None.
        """
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_catalog(self):
        """
        Lists all items in the catalog.

        Returns:
            list: A list of all items in the catalog.
        """
        return [str(item) for item in self.catalog]

    def list_members(self):
        """
        Lists all registered members.

        Returns:
            list: A list of all members.
        """
        return [str(member) for member in self.members]
