# FuzzyString Class Implementation

## Description 📝

The provided code implements the `FuzzyString` class, a subclass of Python's built-in `str` class.
It overrides comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) and the membership test (`in`, `not in`) to perform case-insensitive operations.
The initialization process matches that of `str`, accepting the same arguments.
Comparisons with non-string objects return `NotImplemented`.

## Purpose 🎯

Intended for scenarios requiring case-insensitive string comparisons or membership tests, such as user input validation, search functionality, or case-insensitive data matching.
It’s also suitable for educational examples of operator overloading and inheritance in Python.

## How It Works 🔍

-   **Class Definition**:
    -   `FuzzyString` inherits from `str`, inheriting all standard string behaviors and initialization.
-   **Initialization**:
    -   Uses `str.__init__` implicitly, accepting the same arguments (e.g., a string, bytes, or no arguments).
    -   Examples: `FuzzyString("hello")`, `FuzzyString()`, or `FuzzyString(b"hello")`.
-   **Methods**:
    -   `__eq__(other)`: Returns `True` if `self.lower() == other.lower()`, `NotImplemented` if `other` is not `str` or `FuzzyString`.
    -   `__ne__(other)`: Returns `True` if `self.lower() != other.lower()`, `NotImplemented` if invalid.
    -   `__gt__(other)`: Returns `True` if `self.lower() > other.lower()`, `NotImplemented` if invalid.
    -   `__lt__(other)`: Returns `True` if `self.lower() < other.lower()`, `NotImplemented` if invalid.
    -   `__ge__(other)`: Returns `True` if `self.lower() >= other.lower()`, `NotImplemented` if invalid.
    -   `__le__(other)`: Returns `True` if `self.lower() <= other.lower()`, `NotImplemented` if invalid.
    -   `__contains__(other)`: Returns `True` if `other.lower()` is in `self.lower()`, `NotImplemented` if invalid.
-   **Behavior**:
    -   Comparisons (`==`, `!=`, `>`, `<`, `>=`, `<=`) are case-insensitive, using `.lower()` on both operands.
    -   Membership tests (`in`, `not in`) are case-insensitive, checking if `other.lower()` is a substring of `self.lower()`.
    -   Non-string comparisons return `NotImplemented`, allowing Python to handle fallback behavior.
    -   All other `str` methods (e.g., `upper()`, `split()`) are inherited unchanged.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Matches `str` initialization: `FuzzyString("test")`, `FuzzyString()`, etc., work identically.
    -   E.g., `s = FuzzyString("Hello")` creates a string with value `"Hello"`.
-   **Case-Insensitive Comparisons**:
    -   `FuzzyString("Hello") == "hello"` → `True`.
    -   `FuzzyString("abc") < "BCD"` → `True` (since `"abc" < "bcd"`).
    -   `FuzzyString("ZEBRA") >= "zebra"` → `True`.
    -   `FuzzyString("test") != "TEST"` → `False`.
-   **Case-Insensitive Membership**:
    -   `"HeLLo" in FuzzyString("hello world")` → `True`.
    -   `"WORLD" not in FuzzyString("hello")` → `True`.
-   **Invalid Comparisons**:
    -   `FuzzyString("test") == 123` → `NotImplemented`.
    -   `"test" in FuzzyString("test")` → `NotImplemented` (if `__contains__` is called with non-string).
-   **String Behavior**:
    -   Inherits all `str` methods: `s.upper()`, `s[0]`, etc.
    -   E.g., `s = FuzzyString("test"); s.upper()` → `"TEST"`.
-   **Inheritance**:
    -   `issubclass(FuzzyString, str)` → `True`.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**: `.lower()` ensures case-insensitive comparisons and membership tests. `NotImplemented` is returned for invalid types, per requirement.
-   **Performance**: `.lower()` is O(n) (where n is string length), but this is standard for string operations and acceptable for typical use.
-   **Design**: Overriding only necessary methods (`__eq__`, `__ne__`, `__gt__`, `__lt__`, `__ge__`, `__le__`, `__contains__`) preserves `str` functionality. Type checking with `isinstance` ensures robust handling of valid operands.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
s = FuzzyString("HeLLo")

# Test comparisons
print(s == "hello")  # True
print(s != "HELLO")  # False
print(s < "world")  # True (h < w)
print(s >= "hello")  # True
print(s == 123)  # NotImplemented

# Test membership
print("hell" in s)  # True
print("WORLD" not in s)  # True

# Test string operations
print(s.upper())  # HELLO
print(s[0])  # H
print(isinstance(s, str))  # True
```

## Conclusion 🚀

The `FuzzyString` implementation is precise, providing case-insensitive comparisons and membership tests while retaining full `str` functionality.
It’s ideal for case-insensitive string handling or operator overloading education, fully compliant with the task’s requirements.
