"""
Sorting Algorithms
==================
This module demonstrates several sorting algorithms implemented as reusable functions.
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

    Time Complexity: O(n^2)
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def selection_sort(numbers):
    """
    Selection Sort Algorithm
    -------------------------
    Divides the list into sorted and unsorted sections. Repeatedly selects the smallest
    element from the unsorted section and moves it to the sorted section.

    Time Complexity: O(n^2)
    """
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

def insertion_sort(numbers):
    """
    Insertion Sort Algorithm
    -------------------------
    Builds the sorted list one element at a time by repeatedly taking an element
    from the unsorted list and inserting it in the correct position.

    Time Complexity: O(n^2)
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def merge_sort(numbers):
    """
    Merge Sort Algorithm
    ---------------------
    Divides the list into halves, recursively sorts each half, and then merges
    the two sorted halves into a single sorted list.

    Time Complexity: O(n log n)
    """
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

def quick_sort(numbers):
    """
    Quick Sort Algorithm
    ---------------------
    Picks a pivot element and partitions the list such that elements less than
    the pivot are on one side and elements greater than the pivot are on the other.
    Recursively applies this partitioning to both sides.

    Time Complexity: O(n log n)
    """
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    less = [x for x in numbers[1:] if x <= pivot]
    greater = [x for x in numbers[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Testing the functions
if __name__ == "__main__":
    sample_data = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", sample_data)
    print("Bubble Sort:", bubble_sort(sample_data[:]))
    print("Selection Sort:", selection_sort(sample_data[:]))
    print("Insertion Sort:", insertion_sort(sample_data[:]))
    print("Merge Sort:", merge_sort(sample_data[:]))
    print("Quick Sort:", quick_sort(sample_data[:]))
