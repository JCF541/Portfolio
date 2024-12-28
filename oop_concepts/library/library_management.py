"""
Library Management System
==========================
Demonstrates Object-Oriented Programming principles such as encapsulation, inheritance,
polymorphism, and special methods.

Core Concepts:
--------------
1. Encapsulation: Attributes and methods are bundled in classes.
2. Inheritance: Sharing functionality between parent and child classes.
3. Polymorphism: Unified interfaces for different data types or classes.
4. Special Methods: Overriding built-in behaviors (e.g., `__init__`, `__str__`, `__add__`).

Use Cases:
---------
- Managing library books and member data.
- Extending functionality with inheritance.
"""

class LibraryItem:
    """
    Represents an item in the library.

    Attributes:
        title (str): Title of the item.
        author (str): Author of the item.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Book(LibraryItem):
    """
    Represents a book in the library, inheriting from LibraryItem.
    """
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def __str__(self):
        return f"{super().__str__()} (Genre: {self.genre})"

class Library:
    """
    Represents a library system.

    Attributes:
        items (list): Collection of library items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Adds a new item to the library."""
        self.items.append(item)

    def view_items(self):
        """Returns a list of all items in the library."""
        return [str(item) for item in self.items]

    def delete_item(self, title):
        """Deletes an item by title."""
        self.items = [item for item in self.items if item.title != title]

# Testing the classes
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_item(Book("To Kill a Mockingbird", "Harper Lee", "Fiction"))
    library.add_item(Book("1984", "George Orwell", "Dystopian"))

    # Viewing books
    print("Library Items:")
    for item in library.view_items():
        print(item)

    # Deleting a book
    library.delete_item("1984")
    print("\nAfter Deletion:")
    for item in library.view_items():
        print(item)
