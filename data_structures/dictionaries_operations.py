"""
Enhanced Dictionary Operations with Error Handling
===================================================
Demonstrates dictionary creation, updating, accessing, and removing key-value pairs.
Includes error handling for invalid keys and missing values.
"""

def dictionary_operations():
    """
    Demonstrates various dictionary operations with error handling.
    
    Returns:
        dict: Results of dictionary operations.
    """
    try:
        # Creating a dictionary
        student_grades = {
            "Alice": 85,
            "Bob": 90,
            "Charlie": 78
        }

        # Adding and updating entries
        student_grades["Diana"] = 92
        student_grades["Alice"] = 88

        # Accessing values safely
        bob_grade = student_grades.get("Bob", "Grade not found.")
        missing_grade = student_grades.get("Eve", "Grade not found.")

        # Removing entries with error handling
        removed_grade = student_grades.pop("Charlie", "No such student.")
        
        # Iterating over the dictionary
        for student, grade in student_grades.items():
            print(f"{student}: {grade}")

        return {
            "updated_dictionary": student_grades,
            "bob_grade": bob_grade,
            "missing_grade": missing_grade,
            "removed_grade": removed_grade
        }
    except Exception as e:
        return {"error": str(e)}

# Testing the function
if __name__ == "__main__":
    print("Dictionary Operations:", dictionary_operations())
