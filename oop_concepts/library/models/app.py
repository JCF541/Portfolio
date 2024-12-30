"""
App Class
=========
Encapsulates the main application logic for the Library Management System.
"""

from controllers.library_controller import LibraryController
from views.library_view import LibraryView
from views.member_view import MemberView
from .library import Library
from .book import Book
from .magazine import Magazine
from .member import Member


class App:
    def __init__(self):
        self.libraries = []  # List of libraries
        self.current_library = None  # The currently selected library
        self.library_view = LibraryView()
        self.member_view = MemberView()
        self.menu_actions = {
            "1": self.add_library,
            "2": self.select_library,
            "3": self.manage_catalog,
            "4": self.manage_members,
            "5": self.exit_app,
        }

    def add_library(self):
        """Add a new library."""
        name = input("Enter library name: ")
        library = Library(name)
        self.libraries.append(library)
        print(f"Library '{name}' added successfully.")

    def select_library(self):
        """Select an existing library."""
        if not self.libraries:
            print("No libraries available. Add a library first.")
            return
        print("\nAvailable Libraries:")
        for idx, lib in enumerate(self.libraries, start=1):
            print(f"{idx}. {lib.name}")
        choice = input("Select a library by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.libraries):
            self.current_library = self.libraries[int(choice) - 1]
            print(f"Selected library: {self.current_library.name}")
        else:
            print("Invalid choice.")

    def manage_catalog(self):
        """Manage the catalog of the current library."""
        if not self.current_library:
            print("No library selected. Please select a library first.")
            return
        print("\nCatalog Management:")
        options = {
            "1": self.add_book,
            "2": self.add_magazine,
            "3": self.view_catalog,
        }
        print("1. Add Book\n2. Add Magazine\n3. View Catalog")
        choice = input("Choose an option: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

    def add_book(self):
        """Add a book to the catalog."""
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        book = Book(title, author, genre)
        self.current_library.add_item(book)
        print(f"Book '{title}' added successfully.")

    def add_magazine(self):
        """Add a magazine to the catalog."""
        title = input("Enter magazine title: ")
        author = input("Enter magazine author: ")
        issue_number = input("Enter issue number: ")
        publication_date = input("Enter publication date: ")
        magazine = Magazine(title, author, issue_number, publication_date)
        self.current_library.add_item(magazine)
        print(f"Magazine '{title}' added successfully.")

    def view_catalog(self):
        """View the catalog."""
        print("\nCatalog:")
        self.library_view.display_items(self.current_library.list_catalog())

    def manage_members(self):
        """Manage members of the current library."""
        if not self.current_library:
            print("No library selected. Please select a library first.")
            return
        print("\nMember Management:")
        options = {
            "1": self.register_member,
            "2": self.view_members,
        }
        print("1. Register Member\n2. View Members")
        choice = input("Choose an option: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

    def register_member(self):
        """Register a new member."""
        name = input("Enter member name: ")
        email = input("Enter member email: ")
        member = Member(name, email)
        self.current_library.add_member(member)
        print(f"Member '{name}' registered successfully.")

    def view_members(self):
        """View all members."""
        print("\nRegistered Members:")
        self.member_view.display_members(self.current_library.list_members())

    def exit_app(self):
        """Exit the application."""
        print("Exiting application. Goodbye!")
        exit()

    def run(self):
        """Run the application."""
        while True:
            print("\nLibrary Management App:")
            print("1. Add Library")
            print("2. Select Library")
            print("3. Manage Catalog")
            print("4. Manage Members")
            print("5. Exit")
            choice = input("Choose an option: ")
            action = self.menu_actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice.")
