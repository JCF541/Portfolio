"""
LibraryController
==================
Handles the business logic for the Library Management System.
"""

from models.library import Library


class LibraryController:
    def __init__(self, library_name):
        self.library = Library(library_name)

    def add_book(self, title, author, genre):
        """Add a book to the library."""
        from models.book import Book
        book = Book(title, author, genre)
        self.library.add_item(book)

    def add_magazine(self, title, author, issue, publication_date):
        """Add a magazine to the library."""
        from models.magazine import Magazine
        magazine = Magazine(title, author, issue, publication_date)
        self.library.add_item(magazine)

    def add_member(self, member):
        """Add a new member to the library."""
        self.library.add_member(member)

    def remove_member(self, member_id):
        """Remove a member by their ID."""
        member = self.library.find_member(member_id)
        if member:
            self.library.members.remove(member)
            return True
        return False

    def update_member(self, member_id, **updates):
        """
        Update a member's attributes.

        Args:
            member_id (str): The ID of the member to update.
            updates (dict): The fields to update with new values.
        
        Returns:
            bool: True if the member was updated, False otherwise.
        """
        member = self.library.find_member(member_id)
        if not member:
            return False

        # Update fields
        for key, value in updates.items():
            if hasattr(member, key) and value is not None:
                setattr(member, key, value)

        return True

    def update_item(self, item_id, **updates):
        """
        Update an item's attributes.

        Args:
            item_id (str): The ID of the item to update.
            updates (dict): The fields to update with new values.
        
        Returns:
            bool: True if the item was updated, False otherwise.
        """
        item = next((i for i in self.library.catalog if i.item_id == item_id), None)
        if not item:
            return False

        # Update fields
        for key, value in updates.items():
            if hasattr(item, key) and value is not None:
                setattr(item, key, value)

        return True

    def delete_item(self, item_id):
        """Delete an item from the catalog."""
        self.library.remove_item(item_id)

    def view_items(self):
        """Return the list of catalog items."""
        return self.library.list_catalog()

    def list_members(self):
        """Return the list of registered members."""
        return self.library.list_members()

    def borrow_item(self, member_id, item_title):
        """Borrow an item for a member."""
        member = self.library.find_member(member_id)
        if not member:
            return "Member not found."
        for item in self.library.catalog:
            if item.title == item_title:
                member.borrow_item(item)
                self.library.remove_item(item.item_id)
                return f"'{item_title}' borrowed by {member.name}."
        return f"Item '{item_title}' not found in the catalog."

    def return_item(self, member_id, item_title):
        """Return an item for a member."""
        member = self.library.find_member(member_id)
        if not member:
            return "Member not found."
        for item in member.borrowed_items:
            if item.title == item_title:
                self.library.add_item(item)
                member.return_item(item.item_id)
                return f"'{item_title}' returned by {member.name}."
        return f"Item '{item_title}' not found in {member.name}'s borrowed items."
