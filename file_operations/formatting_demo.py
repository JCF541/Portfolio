"""
Working with Structured Data: CSV and JSON
==========================================
Structured data formats like CSV and JSON are commonly used for storing tabular and hierarchical data.

Core Concepts:
- CSV:
  - A comma-separated values file stores tabular data.
  - Python's `csv` module provides functions to read and write CSV files.
- JSON:
  - A lightweight data-interchange format, often used for APIs.
  - Python's `json` module handles serialization (dumping) and deserialization (loading).
"""

import csv
import json

def write_csv(filepath, data):
    """
    Writes tabular data to a CSV file.

    Args:
        filepath (str): Path to the CSV file.
        data (list of lists): Rows of data to write.
    """
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return "CSV file written successfully."

def read_csv(filepath):
    """
    Reads tabular data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.
    
    Returns:
        list: List of rows, where each row is a list of values.
    """
    try:
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return "CSV file not found."

def write_json(filepath, data):
    """
    Writes hierarchical data to a JSON file.

    Args:
        filepath (str): Path to the JSON file.
        data (dict): Data to serialize into JSON.
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    return "JSON file written successfully."

def read_json(filepath):
    """
    Reads hierarchical data from a JSON file.

    Args:
        filepath (str): Path to the JSON file.
    
    Returns:
        dict: Data loaded from the JSON file.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return "JSON file not found."

# Testing the functions
if __name__ == "__main__":
    # CSV file operations
    csv_file = "data.csv"
    csv_data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
    print(write_csv(csv_file, csv_data))
    print("CSV Content:", read_csv(csv_file))

    # JSON file operations
    json_file = "data.json"
    json_data = {"name": "Alice", "age": 25, "city": "New York"}
    print(write_json(json_file, json_data))
    print("JSON Content:", read_json(json_file))
