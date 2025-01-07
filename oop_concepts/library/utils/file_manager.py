import json
import os
from models.member import Member
from utils.id_generator import generate_id  # Import generate_id from id_utils


def save_data(filepath, data):
    """
    Saves data to a file in JSON format.

    Args:
        filepath (str): Path to the file.
        data (dict): Data to save.
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def load_data(filepath):
    """
    Loads data from a JSON file.

    Args:
        filepath (str): Path to the file.

    Returns:
        dict: Loaded data, or an empty structure if the file does not exist.
    """
    if not os.path.exists(filepath):
        return {"catalog": [], "members": []}
    with open(filepath, 'r') as file:
        return json.load(file)


def serialize_library(library):
    """
    Serializes library data into a JSON-compatible format.

    Args:
        library (Library): The library instance.

    Returns:
        dict: Serialized library data.
    """
    return {
        "library_id": library.library_id,
        "name": library.name,
        "catalog": [vars(item) for item in library.catalog],
        "members": [vars(member) for member in library.members],
    }


def deserialize_library(data, library_class, item_classes):
    """
    Deserializes JSON-compatible data into a library instance.

    Args:
        data (dict): Serialized library data.
        library_class (class): The library class.
        item_classes (dict): Mapping of item types to their respective classes.

    Returns:
        Library: Deserialized library instance.
    """
    library_name = data.get("name", "Unnamed Library")
    library_id = data.get("library_id", generate_id("LB"))

    # Initialize library
    library = library_class(library_name)
    library.library_id = library_id

    # Deserialize catalog
    catalog = data.get("catalog", [])
    for item_data in catalog:
        # Dynamically determine the item class based on its attributes
        if "genre" in item_data:
            item_class = item_classes.get("Book")
        elif "issue_number" in item_data:
            item_class = item_classes.get("Magazine")
        else:
            item_class = None

        if item_class:
            item = item_class(**item_data)
            library.add_item(item)
        else:
            print(f"DEBUG: Unknown item type for {item_data}")

    # Deserialize members
    members = data.get("members", [])
    for member_data in members:
        borrowed_items = []
        for borrowed_item_data in member_data.get("borrowed_items", []):
            # Dynamically determine the borrowed item class
            if "genre" in borrowed_item_data:
                borrowed_item_class = item_classes.get("Book")
            elif "issue_number" in borrowed_item_data:
                borrowed_item_class = item_classes.get("Magazine")
            else:
                borrowed_item_class = None

            if borrowed_item_class:
                borrowed_item = borrowed_item_class(**borrowed_item_data)
                borrowed_items.append(borrowed_item)

        member = Member(
            member_id=member_data["member_id"],
            name=member_data["name"],
            email=member_data["email"],
            borrowed_items=borrowed_items,
        )
        library.add_member(member)

    print(f"DEBUG: Deserialized library: {library.name}")
    return library
