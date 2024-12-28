"""
Member Model
============
Represents a library member who can borrow items from the library.
"""

class Member:
    """
    Represents a library member.

    Attributes:
        member_id (str): A unique ID for the member.
        name (str): The member's name.
        email (str): The member's email address.
        borrowed_items (list): A list of items currently borrowed by the member.
    """
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_items = []

    def borrow_item(self, item):
        """
        Adds an item to the list of borrowed items.

        Args:
            item (LibraryItem): The item to borrow.
        """
        self.borrowed_items.append(item)

    def return_item(self, item_id):
        """
        Removes an item from the borrowed items list by ID.

        Args:
            item_id (str): The unique ID of the item to return.
        """
        self.borrowed_items = [
            item for item in self.borrowed_items if item.item_id != item_id
        ]

    def __str__(self):
        borrowed_titles = [item.title for item in self.borrowed_items]
        return (
            f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, "
            f"Borrowed Items: {borrowed_titles if borrowed_titles else 'None'}"
        )
