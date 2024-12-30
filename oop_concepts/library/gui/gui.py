"""
Graphical User Interface (GUI)
==============================
Fully functional GUI for the Library Management System using Tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from controllers.library_controller import LibraryController
from models.book import Book
from models.magazine import Magazine
from models.member import Member
from utils.file_manager import save_data, load_data, serialize_library, deserialize_library


class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("900x600")

        # Initialize the controller
        self.controller = LibraryController("GUI Library")

        # Create main sections
        self.create_header()
        self.create_main_content()
        self.create_footer()

        # Dispatch dictionary for tab-specific actions
        self.tab_actions = {
            "Members": {
                "add": self.add_member_form,
                "delete": self.delete_member,
                "update": self.update_member_form,
            },
            "Books": {
                "add": self.add_book_form,
                "delete": self.delete_item,
                "update": self.update_item_form,
            },
            "Magazines": {
                "add": self.add_magazine_form,
                "delete": self.delete_item,
                "update": self.update_item_form,
            },
        }

        # Load initial data
        self.refresh_tabs()

    def create_header(self):
        """Create the header section with title and library management buttons."""
        header_frame = ttk.Frame(self.root, padding=10)
        header_frame.pack(fill=tk.X)

        # Title
        title_label = ttk.Label(
            header_frame, text="Welcome to the Library Management System", font=("Helvetica", 16)
        )
        title_label.pack(side=tk.LEFT, padx=10)

        # Buttons
        ttk.Button(header_frame, text="New Library", command=self.create_new_library).pack(side=tk.RIGHT, padx=5)
        ttk.Button(header_frame, text="Load Library", command=self.load_library).pack(side=tk.RIGHT, padx=5)
        ttk.Button(header_frame, text="Save Library", command=self.save_library).pack(side=tk.RIGHT, padx=5)

    def create_main_content(self):
        """Create the main content section with a table and action buttons."""
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left: Data Table
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.members_tab = ttk.Frame(self.notebook)
        self.books_tab = ttk.Frame(self.notebook)
        self.magazines_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.members_tab, text="Members")
        self.notebook.add(self.books_tab, text="Books")
        self.notebook.add(self.magazines_tab, text="Magazines")

        # Right: Action Buttons
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(side=tk.RIGHT, fill=tk.Y)

        ttk.Button(action_frame, text="ADD", command=lambda: self.handle_action("add")).pack(fill=tk.X, pady=10)
        ttk.Button(action_frame, text="UPDATE", command=lambda: self.handle_action("update")).pack(fill=tk.X, pady=10)
        ttk.Button(action_frame, text="DELETE", command=lambda: self.handle_action("delete")).pack(fill=tk.X, pady=10)

    def create_footer(self):
        """Create the footer section with a helpful message."""
        footer_frame = ttk.Frame(self.root, padding=10)
        footer_frame.pack(fill=tk.X)

        ttk.Label(
            footer_frame,
            text="Switch between Members, Books, and Magazines using the tabs above.",
            font=("Helvetica", 10),
        ).pack()

    def refresh_tabs(self):
        """Refresh the data displayed in all tabs."""
        self.display_data(self.controller.library.list_members(), self.members_tab)
        self.display_data(self.controller.library.list_catalog(), self.books_tab)

    def display_data(self, data, tab):
        """Display data in the given tab."""
        for widget in tab.winfo_children():
            widget.destroy()

        if not data:
            ttk.Label(tab, text="No data available.", font=("Helvetica", 12)).pack(pady=10)
        else:
            for item in data:
                ttk.Label(tab, text=str(item)).pack(anchor="w", padx=10)

    def handle_action(self, action_type):
        """Handle tab-specific actions like add, update, and delete."""
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        action = self.tab_actions.get(current_tab, {}).get(action_type)

        if action:
            action()
        else:
            messagebox.showwarning(
                "Action Not Supported", f"{action_type.capitalize()} is not supported for {current_tab}."
            )

    # Library Management Actions
    def create_new_library(self):
        """Create a new library."""
        self.controller = LibraryController("New Library")
        self.refresh_tabs()
        messagebox.showinfo("New Library", "New library created successfully.")

    def load_library(self):
        """Load a library from a file."""
        data = load_data("library_data.json")
        if data:
            from models.library import Library
            item_classes = {"Book": Book, "Magazine": Magazine}
            self.controller.library = deserialize_library(data, Library, item_classes)
            self.refresh_tabs()
            messagebox.showinfo("Load Library", "Library loaded successfully.")
        else:
            messagebox.showwarning("Load Library", "No saved library data found.")

    def save_library(self):
        """Save the current library to a file."""
        data = serialize_library(self.controller.library)
        save_data("library_data.json", data)
        messagebox.showinfo("Save Library", "Library saved successfully.")

    # Member Actions
    def add_member_form(self):
        """Display a form to add a member."""
        name = self.prompt_for_input("Enter member name:")
        email = self.prompt_for_input("Enter member email:")
        if name and email:
            member = Member(name, email)
            self.controller.add_member(member)
            self.refresh_tabs()
            messagebox.showinfo("Add Member", "Member added successfully.")

    def update_member_form(self):
        """Display a form to update a member."""
        member_id = self.prompt_for_id("member")
        if not member_id:
            return

        updates = {
            "name": self.prompt_for_input("Enter new name (leave blank to keep current):"),
            "email": self.prompt_for_input("Enter new email (leave blank to keep current):"),
        }

        if self.controller.update_member(member_id, **updates):
            self.refresh_tabs()
            messagebox.showinfo("Update Member", "Member updated successfully.")
        else:
            messagebox.showwarning("Update Member", "Member not found.")

    def delete_member(self):
        """Delete a member."""
        member_id = self.prompt_for_id("member")
        if member_id and self.controller.remove_member(member_id):
            self.refresh_tabs()
            messagebox.showinfo("Delete Member", "Member deleted successfully.")
        else:
            messagebox.showwarning("Delete Member", "Member not found.")

    # Item Actions (Books and Magazines)
    def add_book_form(self):
        """Display a form to add a book."""
        title = self.prompt_for_input("Enter book title:")
        author = self.prompt_for_input("Enter book author:")
        genre = self.prompt_for_input("Enter book genre:")
        if title and author and genre:
            self.controller.add_book(title, author, genre)
            self.refresh_tabs()
            messagebox.showinfo("Add Book", "Book added successfully.")

    def add_magazine_form(self):
        """Display a form to add a magazine."""
        title = self.prompt_for_input("Enter magazine title:")
        author = self.prompt_for_input("Enter magazine author:")
        issue = self.prompt_for_input("Enter issue number:")
        date = self.prompt_for_input("Enter publication date:")
        if title and author and issue and date:
            self.controller.add_magazine(title, author, issue, date)
            self.refresh_tabs()
            messagebox.showinfo("Add Magazine", "Magazine added successfully.")

    def update_item_form(self):
        """Display a form to update an item."""
        item_id = self.prompt_for_id("item")
        if not item_id:
            return

        updates = {
            "title": self.prompt_for_input("Enter new title (leave blank to keep current):"),
            "author": self.prompt_for_input("Enter new author (leave blank to keep current):"),
        }

        if self.controller.update_item(item_id, **updates):
            self.refresh_tabs()
            messagebox.showinfo("Update Item", "Item updated successfully.")
        else:
            messagebox.showwarning("Update Item", "Item not found.")

    def delete_item(self):
        """Delete an item (book or magazine)."""
        item_id = self.prompt_for_id("item")
        if item_id and self.controller.delete_item(item_id):
            self.refresh_tabs()
            messagebox.showinfo("Delete Item", "Item deleted successfully.")
        else:
            messagebox.showwarning("Delete Item", "Item not found.")

    # Input Helpers
    def prompt_for_input(self, prompt):
        """Prompt the user for input."""
        return simpledialog.askstring("Input", prompt)

    def prompt_for_id(self, item_type):
        """Prompt the user for an item/member ID."""
        return simpledialog.askstring("ID Input", f"Enter the {item_type} ID:")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
