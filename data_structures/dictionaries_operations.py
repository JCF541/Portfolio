def dictionary_operations():
    # Creating a dictionary
    student_grades = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78
    }

    # Adding and updating key-value pairs
    student_grades["Diana"] = 92  # Adds a new key-value pair
    student_grades["Alice"] = 88  # Updates Alice's grade

    # Accessing values
    bob_grade = student_grades.get("Bob")  # Safely retrieves Bob's grade
    missing_grade = student_grades.get("Eve", "Grade not found")  # Default for missing key

    # Removing key-value pairs
    removed_grade = student_grades.pop("Charlie", "No such student")  # Removes Charlie's grade

    # Iterating through a dictionary
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

    return {
        "updated_dictionary": student_grades,
        "bob_grade": bob_grade,
        "missing_grade": missing_grade,
        "removed_grade": removed_grade
    }

# Testing the function
if __name__ == "__main__":
    print("Dictionary Operations:", dictionary_operations())
