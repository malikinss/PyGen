Lesson 7.3: inheritance (part 3)

The process of creating class instances
Inheritance from immutable data types (int, float, str, tuple)
Abstract: The lesson is devoted to inheritance from built-in immutable data types in Python.

https://stepik.org/lesson/816515/step/1?unit=819845

This lesson has good theory explonation, has 8 programing practical tasks and 13 theoretical questions presented on the website.

7_3_inheritance_part_3
├───7_3_1_UpperPrintString
├───7_3_2_LowerString
├───7_3_3_FuzzyString
├───7_3_4_TitledText
├───7_3_5_SuperInt
├───7_3_6_RoundedInt
├───7_3_7_AdvancedTuple
└───7_3_8_ModularTuple

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

4. 7_3_4_TitledText

```
# TitledText Class Implementation

## Description 📝

The provided code implements the `TitledText` class, a subclass of Python's built-in `str` class.
It represents a string with an associated title, initialized with two arguments: `content` (the text itself) and `text_title` (the title).
The string value of the instance is the `content`, and it includes a `title` method to return the `text_title`.
The implementation ensures the instance behaves as a string while storing and providing access to the title.

## Purpose 🎯

Intended for scenarios where text needs to be associated with metadata, such as titles in documents, articles, or UI elements.
It’s useful for applications like content management systems or text processing, and suitable for educational examples of `str` subclassing and attribute management in Python.
```

5. 7_3_5_SuperInt

```
# SuperInt Class Implementation

## Description 📝

The provided code implements the `SuperInt` class, a subclass of Python's built-in `int` class.
It extends integer functionality with methods for repeating the number, converting to binary, incrementing, decrementing, and iterating over digits as `SuperInt` instances.
The initialization process matches that of `int`, and the class supports iteration over its digits from left to right.

## Purpose 🎯

Intended for applications requiring enhanced integer operations, such as numerical processing, educational tools, or specialized data formats.
The class is also suitable for teaching inheritance, operator overloading, and iterator protocols in Python.
```

6. 7_3_6_RoundedInt

```
# RoundedInt Class Implementation

## Description 📝

The provided code implements the `RoundedInt` class, a subclass of Python's built-in `int` class.
It automatically rounds its numeric value to the nearest even or odd integer during instantiation, based on a boolean `even` parameter.
The class accepts two arguments: `num` (the numeric value) and `even` (True for even rounding, False for odd rounding, defaulting to True).
The resulting instance is an integer with the rounded value, retaining all `int` functionality.

## Purpose 🎯

Intended for scenarios requiring integers to be constrained to specific parity, such as numerical simulations, data normalization, or parity-based algorithms.
It’s also suitable for educational examples of `int` subclassing and custom object creation in Python.
```

7. 7_3_7_AdvancedTuple

```
# AdvancedTuple Class Implementation

## Description 📝

The provided code implements the `AdvancedTuple` class, a subclass of Python's built-in `tuple` class.
It extends tuple functionality to support addition (`+`, `+=`) with any iterable object (e.g., lists, strings, sets), not just `tuple` or `AdvancedTuple` instances.
The initialization process matches that of `tuple`, and all addition operations return a new `AdvancedTuple` instance.

## Purpose 🎯

Intended for scenarios requiring flexible tuple concatenation with various iterable types, such as data aggregation, sequence processing, or functional programming.
It’s also suitable for educational examples of tuple subclassing and operator overloading in Python.
```

8. 7_3_8_ModularTuple

```
# ModularTuple Class Implementation

## Description 📝

The provided code implements the `ModularTuple` class, a subclass of Python's built-in `tuple` class.
It creates a tuple where each element from the input iterable is divided by a specified `size` (integer, default 100), retaining only the remainder (using the modulo operator `%`).
The class accepts two arguments during instantiation: `iterable` (an iterable defining the initial elements, defaulting to an empty tuple) and `size` (the divisor).
The resulting tuple is independent of the original iterable, ensuring immutability and isolation from external changes.

## Purpose 🎯

Intended for scenarios requiring modular arithmetic on sequences, such as cryptographic algorithms, cyclic data structures, or constrained numerical processing.
It’s also suitable for educational examples of tuple subclassing and custom object creation in Python.
```
