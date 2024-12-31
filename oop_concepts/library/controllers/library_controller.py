"""
LibraryController
==================
Handles the business logic for the Library Management System.
"""

from models.library import Library
from models.book import Book
from models.magazine import Magazine


class LibraryController:
    """
    Manages library operations including catalog management and member management.
    """

    def __init__(self, library_name):
        self.library = Library(library_name)

    def add_item(self, item_type, **attributes):
        """
        Add an item (book or magazine) to the library catalog.

        Args:
            item_type (str): Type of item ('Book' or 'Magazine').
            attributes (dict): Attributes of the item (e.g., title, author).
        
        Returns:
            bool: True if the item was added successfully, False otherwise.
        """
        item_classes = {"Book": Book, "Magazine": Magazine}
        if item_type not in item_classes:
            return False

        item = item_classes[item_type](**attributes)
        self.library.add_item(item)
        return True

    def delete_item(self, item_id):
        """
        Delete an item from the catalog by its ID.

        Args:
            item_id (str): The unique ID of the item.
        
        Returns:
            bool: True if the item was found and deleted, False otherwise.
        """
        initial_count = len(self.library.catalog)
        self.library.remove_item(item_id)
        return len(self.library.catalog) < initial_count

    def update_item(self, item_id, **updates):
        """
        Update attributes of an item in the catalog.

        Args:
            item_id (str): The ID of the item to update.
            updates (dict): The fields to update with their new values.
        
        Returns:
            bool: True if the item was found and updated, False otherwise.
        """
        item = next((i for i in self.library.catalog if i.item_id == item_id), None)
        if not item:
            return False

        for key, value in updates.items():
            if hasattr(item, key) and value is not None:
                setattr(item, key, value)

        return True

    def list_items(self):
        """
        List all items in the library catalog.

        Returns:
            list: A list of string representations of the items.
        """
        return self.library.list_catalog()

    def borrow_item(self, member_id, item_id):
        """
        Allow a member to borrow an item from the library.

        Args:
            member_id (str): The member's ID.
            item_id (str): The ID of the item to borrow.
        
        Returns:
            str: Message indicating the outcome of the borrow operation.
        """
        member = self.library.find_member(member_id)
        if not member:
            return "Member not found."

        item = next((i for i in self.library.catalog if i.item_id == item_id), None)
        if not item:
            return "Item not found in the catalog."

        member.borrow_item(item)
        self.library.remove_item(item.item_id)
        return f"'{item.title}' borrowed by {member.name}."

    def return_item(self, member_id, item_id):
        """
        Allow a member to return an item to the library.

        Args:
            member_id (str): The member's ID.
            item_id (str): The ID of the item to return.
        
        Returns:
            str: Message indicating the outcome of the return operation.
        """
        member = self.library.find_member(member_id)
        if not member:
            return "Member not found."

        item = next((i for i in member.borrowed_items if i.item_id == item_id), None)
        if not item:
            return "Item not found in borrowed items."

        self.library.add_item(item)
        member.return_item(item.item_id)
        return f"'{item.title}' returned by {member.name}."

    def list_members(self):
        """
        List all registered members.

        Returns:
            list: A list of string representations of the members.
        """
        return self.library.list_members()
