"""
Enhanced Set Use Cases with Error Handling
===========================================
Sets excel at removing duplicates, performing mathematical set operations,
and efficient membership tests. This version includes error handling and robustness.

Use Cases:
1. Removing Duplicates
2. Finding Common Elements
3. Finding Unique Elements
"""

def remove_duplicates(numbers):
    """
    Removes duplicates from a list using a set.

    Args:
        numbers (list): List of numbers.
    
    Returns:
        list: List with duplicates removed.
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list.")
        return list(set(numbers))
    except Exception as e:
        return {"error": str(e)}

def find_common_elements(set1, set2):
    """
    Finds elements common to both sets.

    Args:
        set1 (set): First set.
        set2 (set): Second set.
    
    Returns:
        set: Intersection of the two sets.
    """
    try:
        if not (isinstance(set1, set) and isinstance(set2, set)):
            raise ValueError("Both inputs must be sets.")
        return set1 & set2
    except Exception as e:
        return {"error": str(e)}

def find_unique_elements(set1, set2):
    """
    Finds elements unique to either set (symmetric difference).

    Args:
        set1 (set): First set.
        set2 (set): Second set.
    
    Returns:
        set: Symmetric difference of the two sets.
    """
    try:
        if not (isinstance(set1, set) and isinstance(set2, set)):
            raise ValueError("Both inputs must be sets.")
        return set1 ^ set2
    except Exception as e:
        return {"error": str(e)}

# Testing the functions
if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Remove Duplicates:", remove_duplicates(numbers))

    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Common Elements:", find_common_elements(set1, set2))
    print("Unique Elements:", find_unique_elements(set1, set2))
