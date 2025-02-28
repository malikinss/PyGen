# Student ID Generator

## Description 📝

This program defines a function `get_id()` that assigns a unique identification number to a new student enrolling in the BEEGEEK online school.
A student's name must follow specific validation rules, and the function ensures proper error handling for invalid inputs.

## Purpose 🎯

The function helps manage student enrollments by:

-   Checking if the provided name is valid.
-   Assigning an ID based on the current number of students.
-   Raising appropriate exceptions for invalid names.

## How It Works 🔍

1. The function `get_id()` takes two arguments:
    - `names`: A list of current students' names.
    - `name`: The new student's name.
2. It checks if the `name` is a string:
    - If not, it raises a `TypeError` with the message `"Name is not a string"`.
3. It validates the name format using the `is_name_correct()` function:
    - A valid name starts with an uppercase Latin letter followed by lowercase Latin letters.
    - If the name is invalid, a `ValueError` is raised with the message `"Name is not valid"`.
4. If the name is valid, the function returns the new student's identification number, which is `len(names) + 1`.

## Output 📜

-   If the name is valid, the function returns the next available ID.
-   If the input is not a string, an error is raised:
    ```python
    TypeError: Name is not a string
    ```
-   If the name format is invalid, an error is raised:
    ```python
    ValueError: Name is not valid
    ```

## Usage 📦

1. Provide a list of current student names.
2. Pass a new student's name to `get_id()`.
3. The function returns the next available identification number.

Example:

```python
students = ["Timur", "Alice", "Bob"]
new_id = get_id(students, "Charlie")
print(new_id)
```

Output:

```text
4
```

Example with invalid input:

```python
get_id(students, "charlie")
```

Raises:

```text
ValueError: Name is not valid
```

## Conclusion 🚀

The `get_id()` function ensures that student names follow the correct format and assigns a unique ID to new students.
It includes robust error handling, making it a reliable tool for managing student enrollments.
