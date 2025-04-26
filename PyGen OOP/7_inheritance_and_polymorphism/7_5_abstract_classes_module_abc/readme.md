Lesson 7.5: abstract classes, module abc

Abstract classes
Module abc
Module collections.abc

Abstract: The lesson is devoted to abstract classes and modules abc and collections.abc.

https://stepik.org/lesson/872533/step/1?unit=876917

This lesson has good theory explonation, has 8 programing practical tasks and 16 theoretical questions presented on the website.

1. 7_5_1_Middle

```
# Middle and Inheritance Scheme Implementation

## Description 📝

The provided code implements the `Middle` abstract base class and establishes a correct inheritance scheme for the `Average`, `Median`, and `Harmonic` classes.
The `Middle` class serves as a common interface for calculating average ratings (arithmetic mean, median, or harmonic mean) from user and expert votes on a 100-point scale.
It avoids code duplication by centralizing shared functionality, such as vote filtering, while requiring subclasses to implement the specific average calculation via the abstract `get_average` method.

## Purpose 🎯

Intended to unify the interface and shared logic of the `Average`, `Median`, and `Harmonic` classes, which process user and expert ratings for media content.
This hierarchy promotes code reuse, maintainability, and extensibility, making it suitable for applications like rating systems or statistical analysis, as well as educational examples of abstract base classes and inheritance in Python.
```

2. 7_5_2_ChessPiece

```
# ChessPiece, King, and Knight Class Implementation

## Description 📝

The provided code implements the `ChessPiece` abstract base class and its subclasses `King` and `Knight`.
The `ChessPiece` class defines a chess piece with horizontal (`a` to `h`) and vertical (1 to 8) coordinates and an abstract `can_move` method.
The `King` and `Knight` classes inherit from `ChessPiece`, implementing `can_move` to check valid moves for each piece type while maintaining the same initialization and coordinate attributes.

## Purpose 🎯

Intended for chess-related applications, such as game logic, move validation, or chess engines, where pieces need to track positions and verify legal moves.
It’s also suitable for educational examples of abstract base classes, inheritance, and chess move mechanics in Python.
```

3. 7_5_3_Validator

```
# Validator, Number, and String Class Implementation

## Description 📝

The provided code implements the `Validator` abstract base class and its subclasses `Number` and `String`, which are descriptors for validating attribute values.
`Validator` enforces a common interface for attribute access and validation, requiring subclasses to implement the `validate` method.
`Number` validates that values are numbers (`int` or `float`) within a specified range, and `String` validates that values are strings with lengths within specified bounds and optionally passing a predicate function.

## Purpose 🎯

Intended for scenarios requiring robust attribute validation, such as configuration management, form input validation, or data integrity in objects.
It’s also suitable for educational examples of descriptors, abstract base classes, and validation logic in Python.
```

4. 7_5_4_is_iterable

```
# is_iterable and is_iterator Function Implementation

## Description 📝

The provided code implements two functions: `is_iterable` and `is_iterator`.
The `is_iterable` function checks if an object is iterable (i.e., supports iteration, such as lists, strings, or other sequences).
The `is_iterator` function checks if an object is an iterator (i.e., supports the iterator protocol with `__next__` and `__iter__` methods, such as iterator objects returned by `iter()`).

## Purpose 🎯

Intended for scenarios requiring type checking to determine whether an object can be iterated over or is an iterator, such as in data processing, loop handling, or debugging.
It’s also suitable for educational examples of Python’s type system and iteration protocols.
```

5. 7_5_5_CustomRange

```
# CustomRange Class Implementation

## Description 📝

The provided code implements the `CustomRange` class, a subclass of `collections.abc.Sequence`.
It represents a sequence of integers derived from single numbers and ranges (e.g., `"1-4"` for 1, 2, 3, 4).
The class supports iteration, length calculation, reverse iteration, membership testing, and indexing (positive and negative).
It accepts an arbitrary number of positional arguments (integers or range strings) during initialization.

## Purpose 🎯

Intended for scenarios requiring a flexible sequence of integers from mixed inputs (single numbers and ranges), such as data processing, range-based iteration, or custom sequence handling.
It’s also suitable for educational examples of sequence protocols and abstract base classes in Python.
```

6. 7_5_6_BitArray

```
# BitArray Class Implementation

## Description 📝

The provided code implements the `BitArray` class, a subclass of `collections.abc.Sequence`.
It represents a sequence of bits (0s and 1s) initialized from an iterable, supporting iteration, indexing, length calculation, reverse iteration, membership testing, and bitwise operations (`~`, `&`, `|`).
The class ensures independence from the input iterable and handles invalid operands for logical operations by returning `NotImplemented`.

## Purpose 🎯

Intended for scenarios requiring manipulation of bit sequences, such as binary data processing, digital logic, or low-level programming.
It’s also suitable for educational examples of sequence protocols, bitwise operations, and abstract base classes in Python.
```

7.

```

```

8.

```

```
