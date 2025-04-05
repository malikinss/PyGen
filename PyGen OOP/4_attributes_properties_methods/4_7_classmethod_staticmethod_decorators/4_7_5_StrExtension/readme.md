# StrExtension Class String Toolkit

## Description 📝

The `StrExtension` class provides a collection of static methods for string manipulation, requiring no instantiation arguments.
It includes tools to remove Latin vowels, retain only Latin alphabetic characters, and replace specified characters with a single character, all using regular expressions for efficiency.

## Purpose 🎯

This class is designed for text processing tasks, ideal for educational examples of static methods, text cleaning utilities, or applications needing simple string transformations.

## How It Works 🔍

-   **remove_vowels() Method**: A `@staticmethod` that removes Latin vowels (a, e, i, o, u, y) case-insensitively using a precompiled regex pattern.
-   **leave_alpha() Method**: A `@staticmethod` that strips all non-Latin alphabetic characters, keeping only a-z and A-Z with a precompiled regex.
-   **replace_all() Method**: A `@staticmethod` that replaces all characters from a given set with a specified character, case-sensitively, using regex.
-   **Class Attributes**: Precompiled regex patterns `__VOWELS` and `__ALPHABET` optimize repeated operations.

## Usage 📦

1. Save the class in a Python file, e.g., `str_extension.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from str_extension import StrExtension
print(StrExtension.remove_vowels("Hello World"))
print(StrExtension.leave_alpha("Hello123 World!"))
print(StrExtension.replace_all("abc123", "123", "x"))
```

## Conclusion 🚀

The `StrExtension` class offers a concise and efficient set of string manipulation tools in Python, leveraging static methods and regex for performance.
It’s a practical utility that can be extended with additional text-processing functions or customized regex patterns for broader applications.
