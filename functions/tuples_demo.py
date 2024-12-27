"""
Tuple Use Cases
===============
Tuples are immutable and ordered, making them ideal for fixed collections 
of data, especially as keys in dictionaries or as return values from functions.

Use Cases Implemented:
1. Returning Multiple Values
2. Using Tuples as Keys in a Dictionary
3. Immutable Data Handling
"""

def calculate_min_max_avg(numbers):
    """
    Calculates the minimum, maximum, and average of a list of numbers.

    Args:
        numbers (list): List of numbers.
    
    Returns:
        tuple: A tuple containing (min, max, avg).
    """
    total = sum(numbers)
    return min(numbers), max(numbers), total / len(numbers)

def tuple_as_dict_keys():
    """
    Demonstrates using tuples as keys in a dictionary.

    Returns:
        dict: A dictionary mapping coordinates to locations.
    """
    location_mapping = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles",
        (37.7749, -122.4194): "San Francisco"
    }
    return location_mapping

def immutable_data_example():
    """
    Demonstrates immutability of tuples by attempting to modify one.

    Returns:
        str: Error message when attempting modification.
    """
    immutable_tuple = (1, 2, 3)
    try:
        immutable_tuple[1] = 10  # This will raise an error
    except TypeError as e:
        return str(e)

# Testing the functions
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print("Min, Max, Avg:", calculate_min_max_avg(numbers))

    print("Tuple as Dictionary Keys:", tuple_as_dict_keys())

    print("Immutable Data Example:", immutable_data_example())
