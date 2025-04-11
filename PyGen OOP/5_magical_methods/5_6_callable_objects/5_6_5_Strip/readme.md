# Strip Class String Trimmer

## Description 📝

The `Strip` class creates callable instances that remove specified characters from both ends of a string.
It takes a string `chars` during instantiation, defining the characters to strip, and when called with a string, returns the result using Python’s `strip()` method.

## Purpose 🎯

This class is designed for string cleaning, suitable for text preprocessing, educational examples of callable objects, or applications needing custom trimming logic.

## How It Works 🔍

-   **Initialization**: Stores the `chars` string as an instance attribute.
-   **`__call__`()**: Makes instances callable, applying `string.strip(self.chars)` to remove all characters in `chars` from the start and end of the input string.

## Usage 📦

1. Save the class in a Python file, e.g., `strip.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from strip import Strip
stripper = Strip(".,!")
print(stripper("...hello..."))  # "hello"
print(stripper("!!world!!"))    # "world"
print(stripper(".,abc,."))      # "abc"
```

## Conclusion 🚀

The `Strip` class offers a concise and reusable way to trim strings in Python, leveraging the built-in `strip()` method for efficiency.
Its design is simple yet practical, and it can be extended with features like case sensitivity or one-sided stripping (e.g., `lstrip` or `rstrip`) for more specific use cases.
