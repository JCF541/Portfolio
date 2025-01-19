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
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

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
        main_frame.grid(row=1, column=0, sticky="nsew")

        # Configure grid weight for resizing
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)

        # Left: Data Table
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.members_tab = self.create_tab(self.notebook, "Members", ["member_id", "name", "email"])
        self.books_tab = self.create_tab(self.notebook, "Books", ["ID", "Title", "Author", "Genre"])
        self.magazines_tab = self.create_tab(self.notebook, "Magazines", ["ID", "Title", "Author", "Issue", "Date"])

        # Right: Action Buttons
        action_frame = ttk.Frame(self.root, padding=10)
        action_frame.grid(row=1, column=1, sticky="ns")

        ttk.Button(action_frame, text="ADD", command=lambda: self.handle_action("add")).pack(fill=tk.X, pady=10)
        ttk.Button(action_frame, text="UPDATE", command=lambda: self.handle_action("update")).pack(fill=tk.X, pady=10)
        ttk.Button(action_frame, text="DELETE", command=lambda: self.handle_action("delete")).pack(fill=tk.X, pady=10)

    def create_tab(self, notebook, tab_name, columns):
        """
        Create a tab with a dynamically resizable Treeview table.

        Args:
            notebook (ttk.Notebook): The parent notebook widget.
            tab_name (str): The name of the tab.
            columns (list): The column headers for the Treeview.

        Returns:
            ttk.Frame: The created tab.
        """
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=tab_name)

        # Create Treeview with dynamic columns
        tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")
        tree.pack(fill=tk.BOTH, expand=True)

        # Configure dynamic column sizes
        for col in columns:
            if col == "ID":
                tree.column(col, width=100, anchor="center", stretch=True)
            else:
                tree.column(col, width=150, anchor="w", stretch=True)
            tree.heading(col, text=col)

        setattr(self, f"{tab_name.lower()}_tree", tree)
        return tab

    def create_footer(self):
        """Create the footer section with a helpful message."""
        footer_frame = ttk.Frame(self.root, padding=10)
        footer_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        ttk.Label(
            footer_frame,
            text="Switch between Members, Books, and Magazines using the tabs above.",
            font=("Helvetica", 10),
        ).pack()

    def refresh_tabs(self):
        """Refresh the data displayed in all tabs."""
        self.populate_tree(self.members_tree, self.controller.library.members, ["member_id", "name", "email"])
        self.populate_tree(
            self.books_tree, self.controller.library.list_books(), ["item_id", "title", "author", "genre"]
        )
        self.populate_tree(
            self.magazines_tree,
            self.controller.library.list_magazines(),
            ["item_id", "title", "author", "issue_number", "publication_date"],
        )


    def populate_tree(self, tree, data, fields):
        tree.delete(*tree.get_children())
        for obj in data:
            obj_id = obj.member_id if isinstance(obj, Member) else obj.item_id
            values = [getattr(obj, field, "") for field in fields]

            # Debug print
            print(f"DEBUG: Inserting {obj_id} -> {values}")

            tree.insert("", "end", iid=obj_id, values=values)


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

            # Debug print
            print(f"DEBUG: Library after deserialization: {self.controller.library}")

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
            self.controller.add_member(name, email)  # Pass name and email directly
            self.refresh_tabs()
            messagebox.showinfo("Add Member", "Member added successfully.")

    def update_member_form(self):
        """Display a form to update a member."""
        selected_item = self.get_selected_item(self.members_tree)
        if not selected_item:
            return

        member_id = selected_item["member_id"]
        updates = {
            "name": self.prompt_for_input(f"Enter new name (current: {selected_item['name']}):"),
            "email": self.prompt_for_input(f"Enter new email (current: {selected_item['email']}):"),
        }

        if self.controller.update_member(member_id, **updates):
            self.refresh_tabs()
            messagebox.showinfo("Update Member", "Member updated successfully.")
        else:
            messagebox.showwarning("Update Member", "Member not found.")

    def delete_member(self):
        """Delete a selected member."""
        selected_item = self.get_selected_item(self.members_tree)
        if not selected_item:
            return

        member_id = selected_item.get("member_id")  # Safely retrieve key
        if not member_id:
            messagebox.showwarning("Delete Member", "Member ID not found.")
            return

        if self.controller.delete_member(member_id):
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
        """Display a form to update an item (book or magazine)."""
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        tree = self.books_tree if current_tab == "Books" else self.magazines_tree

        selected_item = self.get_selected_item(tree)
        if not selected_item:
            return

        item_id = selected_item["item_id"]
        updates = {
            "title": self.prompt_for_input(f"Enter new title (current: {selected_item['title']}):"),
            "author": self.prompt_for_input(f"Enter new author (current: {selected_item['author']}):"),
        }

        if current_tab == "Books":
            updates["genre"] = self.prompt_for_input(f"Enter new genre (current: {selected_item['genre']}):")
        elif current_tab == "Magazines":
            updates.update({
                "issue_number": self.prompt_for_input(f"Enter new issue (current: {selected_item['issue_number']}):"),
                "publication_date": self.prompt_for_input(f"Enter new date (current: {selected_item['publication_date']}):"),
            })

        if self.controller.update_item(item_id, **updates):
            self.refresh_tabs()
            messagebox.showinfo(f"Update {current_tab[:-1]}", f"{current_tab[:-1]} updated successfully.")
        else:
            messagebox.showwarning(f"Update {current_tab[:-1]}", f"{current_tab[:-1]} not found.")

    def delete_item(self):
        """Delete a selected item (book or magazine)."""
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        tree = self.books_tree if current_tab == "Books" else self.magazines_tree

        selected_item = self.get_selected_item(tree)
        if not selected_item:
            return

        item_id = selected_item["item_id"]
        if self.controller.delete_item(item_id):
            self.refresh_tabs()
            messagebox.showinfo(f"Delete {current_tab[:-1]}", f"{current_tab[:-1]} deleted successfully.")
        else:
            messagebox.showwarning(f"Delete {current_tab[:-1]}", f"{current_tab[:-1]} not found.")

    # Utility Functions
    def get_selected_item(self, tree):
        """
        Get the selected item from a Treeview.

        Args:
            tree (ttk.Treeview): The Treeview widget.

        Returns:
            dict: A dictionary mapping column names to selected row values.
        """
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "No item selected.")
            return None

        # Get the column headers from the Treeview
        columns = tree["columns"]
        item = tree.item(selected[0], "values")

        selected_item = dict(zip(columns, item))
        print(f"DEBUG: Selected item -> {selected_item}")  # Debugging output
        return selected_item

    def prompt_for_input(self, prompt):
        """Prompt the user for input."""
        return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
