"""
Set Use Cases
=============
Sets excel at removing duplicates, performing mathematical set operations, 
and efficient membership tests.

Use Cases Implemented:
1. Removing Duplicates
2. Finding Common Elements (Intersection)
3. Finding Unique Elements (Symmetric Difference)
"""

def remove_duplicates(numbers):
    """
    Removes duplicates from a list using a set.

    Args:
        numbers (list): List of numbers.
    
    Returns:
        list: List with duplicates removed.
    """
    return list(set(numbers))

def find_common_elements(set1, set2):
    """
    Finds elements common to both sets.

    Args:
        set1 (set): First set.
        set2 (set): Second set.
    
    Returns:
        set: Intersection of the two sets.
    """
    return set1 & set2

def find_unique_elements(set1, set2):
    """
    Finds elements unique to either set (symmetric difference).

    Args:
        set1 (set): First set.
        set2 (set): Second set.
    
    Returns:
        set: Symmetric difference of the two sets.
    """
    return set1 ^ set2

# Testing the functions
if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Remove Duplicates:", remove_duplicates(numbers))

    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Common Elements:", find_common_elements(set1, set2))
    print("Unique Elements:", find_unique_elements(set1, set2))
