"""
LibraryController
==================
Handles the business logic for the Library Management System.
"""

from models.library import Library
from models.book import Book
from models.magazine import Magazine
from controllers.member_controller import MemberController


class LibraryController:
    """
    Manages library operations including catalog and member management.
    """

    def __init__(self, library_name):
        self.library = Library(library_name)
        self.member_controller = MemberController()

    # Catalog Management
    def add_item(self, item_type, **attributes):
        """Add an item (book or magazine) to the library catalog."""
        item_classes = {"Book": Book, "Magazine": Magazine}
        if item_type not in item_classes:
            return False

        item = item_classes[item_type](**attributes)
        self.library.add_item(item)
        return True

    def delete_item(self, item_id):
        """Delete an item from the catalog by its ID."""
        initial_count = len(self.library.catalog)
        self.library.remove_item(item_id)
        return len(self.library.catalog) < initial_count

    def update_item(self, item_id, **updates):
        """Update attributes of an item in the catalog."""
        item = next((i for i in self.library.catalog if i.item_id == item_id), None)
        if not item:
            return False

        for key, value in updates.items():
            if hasattr(item, key) and value is not None:
                setattr(item, key, value)

        return True

    def list_items(self):
        """List all items in the library catalog."""
        return self.library.list_catalog()

    # Member Management
    def add_member(self, name, email):
        """Create and register a new member."""
        member = self.member_controller.add_member(name, email)
        self.library.add_member(member)
        return member

    def update_member(self, member_id, **updates):
        """Update a member's attributes."""
        return self.member_controller.update_member(member_id, **updates)

    def delete_member(self, member_id):
        """Remove a member by their ID."""
        if self.member_controller.delete_member(member_id):
            self.library.members = [m for m in self.library.members if m.member_id != member_id]
            return True
        return False

    def find_member(self, member_id):
        """Find a member by their ID."""
        return self.member_controller.find_member(member_id)

    def list_members(self):
        """List all registered members."""
        return self.member_controller.list_members()

    # Borrow and Return Operations
    def borrow_item(self, member_id, item_id):
        """Allow a member to borrow an item."""
        member = self.find_member(member_id)
        if not member:
            return "Member not found."

        item = next((i for i in self.library.catalog if i.item_id == item_id), None)
        if not item:
            return "Item not found in the catalog."

        member.borrow_item(item)
        self.library.remove_item(item.item_id)
        return f"'{item.title}' borrowed by {member.name}."

    def return_item(self, member_id, item_id):
        """Allow a member to return an item."""
        member = self.find_member(member_id)
        if not member:
            return "Member not found."

        item = next((i for i in member.borrowed_items if i.item_id == item_id), None)
        if not item:
            return "Item not found in borrowed items."

        self.library.add_item(item)
        member.return_item(item.item_id)
        return f"'{item.title}' returned by {member.name}."
