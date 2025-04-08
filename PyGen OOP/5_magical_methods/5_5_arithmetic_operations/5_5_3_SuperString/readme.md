# SuperString Class Text Manipulator

## Description 📝

The `SuperString` class encapsulates a string, offering an informal representation as the string itself.
It supports concatenation via `+`, repetition via `*` (in both orders), truncation via `/`, and trimming via `<<` (remove end) and `>>` (remove start), all returning new instances.
Invalid operands yield `NotImplemented`.

## Purpose 🎯

This class is tailored for advanced string operations, ideal for text manipulation exercises, operator overloading demos, or creative string processing tasks.

## How It Works 🔍

-   **Initialization**: Stores the input string in `self.string`.
-   ****str**()**: Returns the string value directly.
-   ****add**()**: Concatenates with another `SuperString`.
-   ****mul**() & **rmul**()**: Repeats the string `n` times (integer only), supporting both orders.
-   ****truediv**()**: Takes the first `len // n` characters.
-   ****lshift**()**: Removes the last `n` characters, returning empty if `n >= len`, or full string if `n == 0`.
-   ****rshift**()**: Removes the first `n` characters, returning empty if `n >= len`, or full string if `n == 0`.
-   **Error Handling**: Returns `NotImplemented` for invalid types.

## Usage 📦

1. Save the class in a Python file, e.g., `super_string.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from super_string import SuperString
s1 = SuperString("hello")
s2 = SuperString("world")
print(s1 + s2)      # helloworld
print(s1 * 3)       # hellohellohello
print(2 * s1)       # hellohello
print(s1 / 2)       # he
print(s1 << 2)      # hel
print(s1 >> 2)      # llo
print(s1 << 0)      # hello
print(s1 >> 0)      # hello
```

## Conclusion 🚀

The `SuperString` class delivers a robust and expressive interface for string manipulation in Python, with a full suite of operators for combining, scaling, and slicing strings.
Its explicit handling of edge cases like `n == 0` enhances readability, and it’s easily extensible for additional operations like string reversal or pattern matching.
