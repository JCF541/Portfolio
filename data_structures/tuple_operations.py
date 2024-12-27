def tuple_operations():
    # Creating a tuple
    person = ("Alice", 25, "Developer")

    # Accessing elements
    name = person[0]
    age = person[1]
    profession = person[2]

    # Tuple unpacking
    name, age, profession = person

    # Nested tuples
    nested_tuple = ((1, 2), (3, 4), (5, 6))
    first_pair = nested_tuple[0]
    first, second = first_pair

    # Using tuples as dictionary keys
    location_mapping = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles",
    }
    ny_location = location_mapping.get((40.7128, -74.0060))

    # Immutability demonstration
    try:
        person[1] = 30  # Attempt to modify a tuple (will raise an error)
    except TypeError as e:
        immutability_message = str(e)

    # Tuple concatenation and repetition
    extended_tuple = person + ("Python Developer",)
    repeated_tuple = person * 2

    return {
        "original_tuple": person,
        "accessed_name": name,
        "nested_tuple_first_pair": first_pair,
        "nested_first_element": first,
        "ny_location": ny_location,
        "immutability_error": immutability_message,
        "extended_tuple": extended_tuple,
        "repeated_tuple": repeated_tuple,
    }

# Testing the function
if __name__ == "__main__":
    print("Tuple Operations:", tuple_operations())
