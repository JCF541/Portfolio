"""
Enhanced List Operations with Error Handling and Module Usage
=============================================================
This file demonstrates list operations such as creation, modification, sorting, and slicing.
Includes error handling for invalid operations and the use of the `random` module for generating data.
"""

import random

def list_operations():
    """
    Performs various list operations including appending, removing, sorting, and slicing.
    
    Returns:
        dict: Results of various list operations.
    """
    try:
        # Creating a list with random numbers
        numbers = random.sample(range(1, 101), 10)  # 10 unique random numbers between 1 and 100
        
        # Adding elements
        numbers.append(50)
        numbers.extend([60, 70])
        
        # Removing elements safely
        numbers.remove(20) if 20 in numbers else print("Value 20 not in list.")
        popped = numbers.pop()  # Remove and return the last element
        
        # Sorting and reversing
        numbers.sort()
        numbers.reverse()
        
        # Indexing and slicing
        first_element = numbers[0]
        sublist = numbers[1:3]
        
        return {
            "final_list": numbers,
            "popped_element": popped,
            "first_element": first_element,
            "sublist": sublist
        }
    except Exception as e:
        return {"error": str(e)}

# Testing the function
if __name__ == "__main__":
    print("List Operations:", list_operations())
