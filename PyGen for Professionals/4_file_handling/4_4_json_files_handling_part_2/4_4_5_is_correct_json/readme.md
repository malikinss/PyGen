# JSON Validation Utility 📝

## Description 📝

This script provides a function to verify whether a given string is a valid JSON format.

## Purpose 🎯

The function ensures that a string follows proper JSON syntax, making it useful for validating user input, API responses, or configuration files.

## How It Works 🔍

1. The `is_correct_json()` function takes a string as input.
2. It attempts to parse the string using `json.loads()`.
3. If parsing succeeds, the function returns `True`.
4. If a `json.JSONDecodeError` is raised, it returns `False`.

## Output 📜

### Example Usage:

```python
print(is_correct_json('{"name": "Alice", "age": 25}'))  # True
print(is_correct_json('{name: Alice, age: 25}'))  # False
print(is_correct_json('Invalid JSON'))  # False
```

## Usage 📦

1. Copy the function into your Python script.
2. Call `is_correct_json(your_string)` to validate JSON strings.
3. If the function returns `True`, the string is valid JSON. Otherwise, it's invalid.

## Conclusion 🚀

This simple yet effective function is essential for handling JSON data validation in Python, ensuring data integrity before further processing.
