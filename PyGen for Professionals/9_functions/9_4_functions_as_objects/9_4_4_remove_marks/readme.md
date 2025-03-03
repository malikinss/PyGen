# Remove Marks Function

## Description 📝

This Python script defines a function `remove_marks(text, marks)`, which removes specified characters from a given string.
The function also tracks the number of times it has been called using a `count` attribute.

## Purpose 🎯

The purpose of this program is to demonstrate:

-   String manipulation by removing unwanted characters.
-   Function attributes in Python (`remove_marks.count`).
-   Tracking function usage with an internal counter.

## How It Works 🔍

1. **Function Definition**: `remove_marks(text, marks)` takes a string (`text`) and a set of characters (`marks`) to be removed.
2. **Attribute Initialization**: The `count` attribute is initialized to track function calls.
3. **Character Removal**: The function iterates over the `marks` set and removes each specified character from `text` using `.replace()`.
4. **Function Call Counter**: The `count` attribute increments each time the function is executed.
5. **Return Value**: The modified string is returned without the specified characters.

## Output 📜

Example usage and outputs:

```python
print(remove_marks("hello, world!", {',', '!'}))
# Output: "hello world"

print(remove_marks("Python is awesome!!!", {'!', 'o'}))
# Output: "Pythn is awesome"

print(remove_marks.count)
# Output: 2
```

## Usage 📦

1. Save the code to a file named `remove_marks_function.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python:

    ```python
    from remove_marks_function import remove_marks

    print(remove_marks("Goodbye, cruel world!", {',', '!'}))
    print(remove_marks("Hello!!!", {'!'}))
    print(remove_marks.count)
    ```

## Conclusion 🚀

This program provides an efficient way to clean text by removing specific characters while keeping track of function calls.
It demonstrates the use of function attributes for tracking and modifying behavior dynamically.
