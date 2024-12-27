"""
Enhanced Dictionary Use Cases with Error Handling
==================================================
Dictionaries excel at mapping unique keys to values, making them ideal for lookups,
grouping data, and frequency counts. This version includes error handling and robustness.

Use Cases:
1. Word Frequency Counter
2. Grouping Elements by a Condition
3. Merging Dictionaries
"""

def word_frequency_counter(text):
    """
    Counts the frequency of each word in a given text.

    Args:
        text (str): Input text to analyze.
    
    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")
        words = text.split()
        frequency = {}
        for word in words:
            word = word.lower().strip(",.!?")
            frequency[word] = frequency.get(word, 0) + 1
        return frequency
    except Exception as e:
        return {"error": str(e)}

def group_elements_by_parity(numbers):
    """
    Groups numbers into odd and even categories.

    Args:
        numbers (list): List of integers.
    
    Returns:
        dict: A dictionary with keys 'odd' and 'even' mapping to lists of numbers.
    """
    try:
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers.")
        grouped = {'odd': [], 'even': []}
        for num in numbers:
            if num % 2 == 0:
                grouped['even'].append(num)
            else:
                grouped['odd'].append(num)
        return grouped
    except Exception as e:
        return {"error": str(e)}

def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries, summing values for matching keys.

    Args:
        dict1 (dict): First dictionary.
        dict2 (dict): Second dictionary.
    
    Returns:
        dict: A merged dictionary.
    """
    try:
        if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
            raise ValueError("Both inputs must be dictionaries.")
        merged = dict1.copy()
        for key, value in dict2.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid value type for key '{key}': {type(value)}")
            merged[key] = merged.get(key, 0) + value
        return merged
    except Exception as e:
        return {"error": str(e)}

# Testing the functions
if __name__ == "__main__":
    text = "This is a test. This test is only a test."
    print("Word Frequency Counter:", word_frequency_counter(text))

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Grouped by Parity:", group_elements_by_parity(numbers))

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    print("Merged Dictionaries:", merge_dictionaries(dict1, dict2))
