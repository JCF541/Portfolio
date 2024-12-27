def set_operations():
    # Creating sets
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    # Set operations
    union = set_a | set_b  # Union of sets
    intersection = set_a & set_b  # Intersection of sets
    difference = set_a - set_b  # Difference of sets
    symmetric_difference = set_a ^ set_b  # Symmetric difference
    
    # Adding and removing elements
    set_a.add(7)  # Adds an element to the set
    set_a.discard(1)  # Removes an element if it exists
    set_a.discard(10)  # Does nothing if the element doesn't exist
    set_b.remove(3)  # Removes an element but raises KeyError if it doesn't exist
    
    # Set comprehensions
    squared_set = {x**2 for x in set_a}  # Squares each element in the set

    # Membership tests
    is_present = 5 in set_a
    is_absent = 10 not in set_b

    return {
        "union": union,
        "intersection": intersection,
        "difference": difference,
        "symmetric_difference": symmetric_difference,
        "set_a_after_changes": set_a,
        "set_b_after_changes": set_b,
        "squared_set": squared_set,
        "is_5_present_in_set_a": is_present,
        "is_10_absent_in_set_b": is_absent,
    }

# Testing the function
if __name__ == "__main__":
    print("Set Operations:", set_operations())
