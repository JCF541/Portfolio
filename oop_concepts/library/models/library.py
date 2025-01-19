from utils.id_generator import generate_id
from models.book import Book
from models.magazine import Magazine


class Library:
    """
    Represents a library system.

    Attributes:
        library_id (str): A unique ID for the library.
        name (str): The name of the library.
        catalog (list): A collection of library items.
        members (list): A list of registered members.
    """

    def __init__(self, name):
        self.library_id = generate_id("LB")  # Unique ID with "LB" prefix
        self.name = name
        self.catalog = []
        self.members = []

    def add_item(self, item):
        """Adds an item to the library catalog."""
        self.catalog.append(item)

    def remove_item(self, item_id):
        """Removes an item from the catalog by ID."""
        self.catalog = [item for item in self.catalog if item.item_id != item_id]

    def add_member(self, member):
        """Registers a new member."""
        self.members.append(member)

    def find_member(self, member_id):
        """Finds a member by ID."""
        return next((m for m in self.members if m.member_id == member_id), None)

    def list_catalog(self):
        """Lists all items in the catalog."""
        return [str(item) for item in self.catalog]

    def list_books(self):
        """Lists all books in the catalog."""
        return [item for item in self.catalog if isinstance(item, Book)]

    def list_magazines(self):
        """Lists all magazines in the catalog."""
        return [item for item in self.catalog if isinstance(item, Magazine)]

    def list_members(self):
        """Lists all registered members."""
        return [str(member) for member in self.members]

    def __str__(self):
        return f"Library ID: {self.library_id}, Name: {self.name}, Items: {len(self.catalog)}, Members: {len(self.members)}"
