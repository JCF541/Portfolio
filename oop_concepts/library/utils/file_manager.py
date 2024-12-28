"""
File Manager
============
Handles file-based persistence for the library management system.
"""

import json
import os


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
    library = library_class(data["name"])
    library.library_id = data["library_id"]

    for item_data in data["catalog"]:
        item_type = item_data.pop("__class__", "LibraryItem")
        item_class = item_classes.get(item_type)
        if item_class:
            library.add_item(item_class(**item_data))

    for member_data in data["members"]:
        library.add_member(Member(**member_data))

    return library
