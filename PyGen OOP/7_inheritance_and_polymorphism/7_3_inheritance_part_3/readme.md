Lesson 7.3: inheritance (part 3)

The process of creating class instances
Inheritance from immutable data types (int, float, str, tuple)
Abstract: The lesson is devoted to inheritance from built-in immutable data types in Python.

https://stepik.org/lesson/816515/step/1?unit=819845

This lesson has good theory explonation, has 8 programing practical tasks and 13 theoretical questions presented on the website.

1. 7_3_1_UpperPrintString

```
# UpperPrintString Class Implementation

## Description 📝

The provided code implements the `UpperPrintString` class, a subclass of Python's built-in `str` class.
It inherits all behaviors of `str` and overrides the informal string representation to return the string in uppercase.
The initialization process matches that of `str`, accepting the same arguments. When converted to a string (e.g., via `str()` or `print()`), an instance returns its value in uppercase.

## Purpose 🎯

Intended for scenarios where strings need to be displayed in uppercase for informal representation, such as in user interfaces, logging, or formatted outputs, while retaining all standard string functionality.
It’s also suitable for educational examples of inheritance and method overriding in Python.
```

2. 7_3_2_LowerString

```
# LowerString Class Implementation

## Description 📝

The provided code implements the `LowerString` class, a subclass of Python's built-in `str` class.
It automatically converts its initial value to lowercase during instantiation. The class accepts one optional argument, `obj`, which defines the initial string value (defaulting to an empty string).
The resulting instance behaves like a standard string but starts with a lowercase value.

## Purpose 🎯

Intended for scenarios where strings need to be consistently lowercase, such as in case-insensitive data processing, user input normalization, or database key standardization.
It’s also suitable for educational examples of inheritance and custom object creation in Python.
```

3. 7_3_3_FuzzyString

```
# FuzzyString Class Implementation

## Description 📝

The provided code implements the `FuzzyString` class, a subclass of Python's built-in `str` class.
It overrides comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) and the membership test (`in`, `not in`) to perform case-insensitive operations.
The initialization process matches that of `str`, accepting the same arguments.
Comparisons with non-string objects return `NotImplemented`.

## Purpose 🎯

Intended for scenarios requiring case-insensitive string comparisons or membership tests, such as user input validation, search functionality, or case-insensitive data matching.
It’s also suitable for educational examples of operator overloading and inheritance in Python.
```

4.

```

```

5.

```

```

6.

```

```

7.

```

```

8.

```

```
