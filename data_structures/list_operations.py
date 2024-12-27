def list_operations():
    # Creation of a list
    numbers = [10, 20, 30, 40]
    
    # Adding elements to the list
    numbers.append(50)  # Adds 50 to the end of the list
    numbers.extend([60, 70])  # Adds multiple elements to the list
    
    # Removing elements from the list
    numbers.remove(20)  # Removes the first occurrence of 20
    popped = numbers.pop()  # Removes and returns the last element
    
    # Sorting the list
    numbers.sort()  # Sorts the list in ascending order
    
    # Reversing the list
    numbers.reverse()  # Reverses the list order
    
    # Indexing and slicing
    first_element = numbers[0]  # Access the first element
    sublist = numbers[1:3]  # Slices the list from index 1 to 2
    
    return {
        "final_list": numbers,
        "popped_element": popped,
        "first_element": first_element,
        "sublist": sublist
    }

# Testing the function
if __name__ == "__main__":
    print("List Operations:", list_operations())
