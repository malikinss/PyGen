# CaseHelper Class Style Converter

## Description 📝

The `CaseHelper` class provides static methods for handling strings in Snake Case (e.g., `bee_geek`) and Upper Camel Case (e.g., `BeeGeek`) styles.
It requires no instantiation arguments and includes methods to check string formats and convert between these two naming conventions.

## Purpose 🎯

This class is designed for string style validation and conversion, suitable for coding style enforcement, educational examples of static methods and regex, or applications requiring consistent naming conventions.

## How It Works 🔍

-   **is_snake() Method**: A `@staticmethod` that uses regex to verify if a string matches Snake Case (lowercase words separated by underscores).
-   **is_upper_camel() Method**: A `@staticmethod` that uses regex to check if a string is in Upper Camel Case (capitalized words concatenated).
-   **to_snake() Method**: A `@staticmethod` that inserts underscores before uppercase letters in an Upper Camel Case string and converts it to lowercase.
-   **to_upper_camel() Method**: A `@staticmethod` that splits a Snake Case string by underscores and capitalizes each word, joining them together.

## Usage 📦

1. Save the class in a Python file, e.g., `case_helper.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from case_helper import CaseHelper
print(CaseHelper.is_snake("bee_geek"))
print(CaseHelper.is_upper_camel("BeeGeek"))
print(CaseHelper.to_snake("HelloWorld"))
print(CaseHelper.to_upper_camel("hello_world"))
```

## Conclusion 🚀

The `CaseHelper` class offers a clean and efficient toolkit for managing Snake Case and Upper Camel Case strings in Python.
Its use of static methods and regex ensures flexibility and precision, making it a valuable utility that can be extended with additional case styles or validation rules for broader applications.
