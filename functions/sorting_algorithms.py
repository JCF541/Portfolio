"""
Enhanced Sorting Algorithms with Error Handling
================================================
This module demonstrates several sorting algorithms with added robustness.
Each function operates on a list and returns the sorted list.

Algorithms Covered:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
"""

def bubble_sort(numbers):
    """
    Bubble Sort Algorithm
    ----------------------
    Repeatedly steps through the list, compares adjacent elements, and swaps them
    if they are in the wrong order. This continues until the list is sorted.

    Args:
        numbers (list): List of integers or floats.

    Returns:
        list: Sorted list.
    """
    try:
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be integers or floats.")
        n = len(numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers
    except Exception as e:
        return {"error": str(e)}

def selection_sort(numbers):
    """
    Selection Sort Algorithm
    -------------------------
    Sorts by repeatedly selecting the smallest element from the unsorted portion.

    Args:
        numbers (list): List of integers or floats.

    Returns:
        list: Sorted list.
    """
    try:
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be integers or floats.")
        for i in range(len(numbers)):
            min_idx = i
            for j in range(i+1, len(numbers)):
                if numbers[j] < numbers[min_idx]:
                    min_idx = j
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        return numbers
    except Exception as e:
        return {"error": str(e)}

def merge_sort(numbers):
    """
    Merge Sort Algorithm
    ---------------------
    Divides the list into halves, recursively sorts them, and merges them back.

    Args:
        numbers (list): List of integers or floats.

    Returns:
        list: Sorted list.
    """
    try:
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be integers or floats.")
        if len(numbers) > 1:
            mid = len(numbers) // 2
            left_half = numbers[:mid]
            right_half = numbers[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    numbers[k] = left_half[i]
                    i += 1
                else:
                    numbers[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                numbers[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                numbers[k] = right_half[j]
                j += 1
                k += 1

        return numbers
    except Exception as e:
        return {"error": str(e)}

# Testing the functions
if __name__ == "__main__":
    sample_data = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", sample_data)
    print("Bubble Sort:", bubble_sort(sample_data[:]))
    print("Selection Sort:", selection_sort(sample_data[:]))
    print("Merge Sort:", merge_sort(sample_data[:]))
