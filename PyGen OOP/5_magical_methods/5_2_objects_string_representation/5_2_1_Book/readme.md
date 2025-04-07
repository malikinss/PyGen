# Book Class Literature Descriptor

## Description 📝

The `Book` class represents a book with a title, author, and publication year, initialized with these values upon instantiation.
It provides custom string representations: a formal one via `__repr__` for debugging and an informal one via `__str__` for readable output, correcting any prior implementation errors.

## Purpose 🎯

This class is designed for managing book data, suitable for library catalogs, educational examples of string representation, or applications needing structured book information.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `title`, `author`, and `year` attributes.
-   ****str**() Method**: Returns an informal string in the format `<title> (<author>, <year>)`.
-   ****repr**() Method**: Returns a formal string in the format `Book('<title>', '<author>', <year>)`, suitable for recreating the object.

## Usage 📦

1. Save the class in a Python file, e.g., `book.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from book import Book
book = Book("Python 101", "John Doe", 2020)
print(book)
print(repr(book))
```

## Conclusion 🚀

The `Book` class provides a clear and correct implementation of a book object in Python, with distinct formal and informal string representations.
Its straightforward design makes it a reliable tool, easily extensible with additional attributes or methods like ISBN or genre for enhanced functionality.
