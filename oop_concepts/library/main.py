"""
Library Management Application
==============================
Main entry point for the library management system.
"""

from controllers.library_controller import LibraryController
from views.library_view import LibraryView
from views.member_view import MemberView
from models.member import Member
from utils.file_manager import save_data, load_data, serialize_library, deserialize_library


def main():
    # Filepath for storing library data
    data_file = "library_data.json"

    # Load existing data or initialize a new library
    print("Loading library data...")
    loaded_data = load_data(data_file)
    library_controller = LibraryController(loaded_data.get("name", "City Central Library"))

    # Deserialize data into library structure
    if loaded_data.get("library_id"):
        from models.book import Book
        from models.magazine import Magazine
        from models.library import Library

        item_classes = {"Book": Book, "Magazine": Magazine}
        library_controller.library = deserialize_library(
            loaded_data, Library, item_classes
        )
    else:
        print("No existing data found. Starting with a new library.")

    # Initialize views
    library_view = LibraryView()
    member_view = MemberView()

    # Add books and magazines to the catalog (if not already loaded)
    if not library_controller.library.catalog:
        library_controller.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
        library_controller.add_book("1984", "George Orwell", "Dystopian")
        library_controller.add_magazine("National Geographic", "Editorial Team", "March 2023", "2023-03-01")
        library_controller.add_magazine("Time", "Editorial Team", "April 2023", "2023-04-01")

    # Register members (if not already loaded)
    if not library_controller.library.members:
        member_1 = Member(name="Alice Johnson", email="alice@example.com")
        member_2 = Member(name="Bob Smith", email="bob@example.com")
        library_controller.add_member(member_1)
        library_controller.add_member(member_2)

    # Display library catalog
    print("\nLibrary Catalog:")
    library_view.display_items(library_controller.view_items())

    # Display registered members
    print("\nRegistered Members:")
    member_view.display_members(library_controller.list_members())

    # Simulate borrowing and returning items
    print("\nAlice borrows 'To Kill a Mockingbird':")
    print(library_controller.borrow_item(member_1.member_id, "To Kill a Mockingbird"))
    print("\nUpdated Borrowed Items for Alice:")
    print(member_1)

    print("\nAlice returns 'To Kill a Mockingbird':")
    print(library_controller.return_item(member_1.member_id, "To Kill a Mockingbird"))
    print("\nUpdated Borrowed Items for Alice:")
    print(member_1)

    # Simulate item deletion
    print("\nDeleting '1984' from the catalog:")
    print(library_controller.delete_item("1984"))
    print("\nUpdated Catalog:")
    library_view.display_items(library_controller.view_items())

    # Save library data on exit
    print("\nSaving library data...")
    serialized_data = serialize_library(library_controller.library)
    save_data(data_file, serialized_data)
    print("Library data saved successfully.")


if __name__ == "__main__":
    main()
