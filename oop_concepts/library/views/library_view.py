"""
Library View
============
Provides an interface for displaying library operations.
"""

class LibraryView:
    """
    Provides a user interface for library catalog operations.
    """

    @staticmethod
    def display_items(items):
        """
        Displays all items in the library catalog.
        """
        if not items:
            print("The library catalog is empty.")
        else:
            print("Library Catalog:")
            for item in items:
                print(f" - {item}")
