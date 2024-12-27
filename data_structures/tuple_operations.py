"""
Enhanced Tuple Operations with Error Handling
==============================================
Demonstrates tuple operations such as accessing elements, unpacking, and immutability handling.
Includes error handling for invalid operations.
"""

def tuple_operations():
    """
    Demonstrates various tuple operations with error handling.
    
    Returns:
        dict: Results of tuple operations.
    """
    try:
        # Creating a tuple
        person = ("Alice", 25, "Developer")

        # Accessing and unpacking
        name, age, profession = person

        # Using tuples as dictionary keys
        location_mapping = {
            (40.7128, -74.0060): "New York",
            (34.0522, -118.2437): "Los Angeles",
        }
        ny_location = location_mapping.get((40.7128, -74.0060), "Location not found.")

        # Immutability demonstration
        try:
            person[1] = 30  # Attempting to modify
        except TypeError as e:
            immutability_message = str(e)

        return {
            "original_tuple": person,
            "accessed_name": name,
            "ny_location": ny_location,
            "immutability_error": immutability_message
        }
    except Exception as e:
        return {"error": str(e)}

# Testing the function
if __name__ == "__main__":
    print("Tuple Operations:", tuple_operations())
"""
Enhanced Tuple Operations with Error Handling
==============================================
Demonstrates tuple operations such as accessing elements, unpacking, and immutability handling.
Includes error handling for invalid operations.
"""

def tuple_operations():
    """
    Demonstrates various tuple operations with error handling.
    
    Returns:
        dict: Results of tuple operations.
    """
    try:
        # Creating a tuple
        person = ("Alice", 25, "Developer")

        # Accessing and unpacking
        name, age, profession = person

        # Using tuples as dictionary keys
        location_mapping = {
            (40.7128, -74.0060): "New York",
            (34.0522, -118.2437): "Los Angeles",
        }
        ny_location = location_mapping.get((40.7128, -74.0060), "Location not found.")

        # Immutability demonstration
        try:
            person[1] = 30  # Attempting to modify
        except TypeError as e:
            immutability_message = str(e)

        return {
            "original_tuple": person,
            "accessed_name": name,
            "ny_location": ny_location,
            "immutability_error": immutability_message
        }
    except Exception as e:
        return {"error": str(e)}

# Testing the function
if __name__ == "__main__":
    print("Tuple Operations:", tuple_operations())
