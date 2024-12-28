"""
Library Management Application
==============================
Main entry point for the library management system.
"""

from library.controllers.library_controller import LibraryController
from library.views.library_view import LibraryView

def main():
    library = LibraryController()
    view = LibraryView()

    # Adding books
    library.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    library.add_book("1984", "George Orwell", "Dystopian")

    # Viewing books
    items = library.view_items()
    view.display_items(items)

    # Deleting a book
    library.delete_item("1984")
    print("\nAfter Deletion:")
    items = library.view_items()
    view.display_items(items)

if __name__ == "__main__":
    main()
