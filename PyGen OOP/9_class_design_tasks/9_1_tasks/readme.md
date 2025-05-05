Lesson 9.1: Final Tasks

https://stepik.org/lesson/864077/step/1?unit=923013

This lesson has no theory explonation and theoretical questions but has 13 programing practical tasks

9_1_tasks
├───9_1_1_anything
├───9_1_2_Vector
├───9_1_3_CaesarCipher
├───9_1_4_Progression
├───9_1_5_DomainException
├───9_1_6_HighScoreTable
├───9_1_7_Pagination
├───9_1_8_Testpaper
├───9_1_9_TicTacToe
├───9_1_10_Minesweeper
├───9_1_11_Selfie
├───9_1_12_MultiKeyDict
└───9_1_13_predicate

1. 9_1_1_anything

```
# anything() Function and Anything Class Implementation

## Description 📝

The provided code implements the `anything()` function, which returns an instance of the `Anything` class.
The `Anything` class overrides all comparison magic methods (`__eq__`, `__ne__`, `__gt__`, `__ge__`, `__lt__`, `__le__`) to return `True` for any comparison operation (`==`, `!=`, `>`, `<`, `>=`, `<=`) with any other object.
This ensures that any comparison involving an `Anything` instance always evaluates to `True`.

## Purpose 🎯

Intended for scenarios requiring a universal comparator, such as testing, mocking, or educational examples of Python magic methods, comparison operations, and custom object behavior.
```

2. 9_1_2_Vector

```
# Vector Class Implementation

## Description 📝

The provided code implements the `Vector` class, which represents a vector of arbitrary dimension in a coordinate space.
It supports initialization with any number of coordinates, informal string representation, vector operations (addition, subtraction, dot product, normalization), and equality comparisons.
The class raises a `ValueError` with the message "Vectors must have equal length" when operations are attempted on vectors of different dimensions.
The implementation uses Python’s operator overloading and functional programming techniques for concise operation handling.

## Purpose 🎯

Intended for applications involving vector mathematics, such as physics simulations, computer graphics, or educational examples of Python classes, operator overloading, and mathematical operations.
```

3. 9_1_3_CaesarCipher

```
# CaesarCipher Class Implementation

## Description 📝

The provided code implements the `CaesarCipher` class, which encrypts and decrypts text using the Caesar cipher with a specified shift.
The class supports encryption via the `encode()` method (shifting letters to the right) and decryption via the `decode()` method (shifting letters to the left).
It preserves the case of letters, only processes Latin letters (a-z, A-Z), and leaves non-letter characters unchanged.
The implementation uses a helper method `_code` to handle the core transformation logic for both encryption and decryption.

## Purpose 🎯

Intended for applications requiring simple text encryption/decryption, such as educational exercises, basic security demonstrations, or puzzles involving the Caesar cipher.
```

4. 9_1_4_Progression

```
# ArithmeticProgression and GeometricProgression Class Implementation

## Description 📝

The provided code implements two classes, `ArithmeticProgression` and `GeometricProgression`, for generating terms of infinite arithmetic and geometric progressions, respectively.
Both classes inherit from an abstract base class `Progression`, which defines common iteration logic. `ArithmeticProgression` generates terms by adding a fixed difference, while `GeometricProgression` generates terms by multiplying by a fixed ratio.
Both classes are iterable, infinite, and initialized with a starting term and a step (difference or ratio).

## Purpose 🎯

Intended for applications requiring sequences of numbers, such as mathematical modeling, algorithm testing, or educational examples of Python iterators, abstract base classes, and progression generation.
```

5. 9_1_5_DomainException

```
# DomainException and Domain Class Implementation

## Description 📝

The provided code implements the `DomainException` exception class and the `Domain` class to handle and validate domains.
The `Domain` class supports three creation methods: direct initialization with a domain, `from_url()` for extracting a domain from a URL, and `from_email()` for extracting a domain from an email address.
It validates inputs using regular expressions, raising `DomainException` with the message "Invalid domain, url, or email" for invalid inputs.
The informal string representation of a `Domain` instance is the domain itself.

## Purpose 🎯

Intended for applications requiring domain validation and extraction, such as web scraping, email processing, or educational examples of Python classes, regular expressions, and exception handling.
```

6. 9_1_6_HighScoreTable

```
# HighScoreTable Class Implementation

## Description 📝

The provided code implements the `HighScoreTable` class, which manages a high score table for a game.
The table stores a limited number of top scores, specified at initialization, in descending order.
It supports adding new scores with the `update` method, which only retains scores that rank within the table’s capacity, and resetting all scores with the `reset` method.
The `scores` attribute provides access to the current list of scores.

## Purpose 🎯

Intended for game applications requiring a leaderboard or high score tracking, such as arcade games, or educational examples of Python classes, list management, and sorting.
```

7. 9_1_7_Pagination

```

```

8. 9_1_8_Testpaper

```

```

9. 9_1_9_TicTacToe

```

```

10. 9_1_10_Minesweeper

```


```

11. 9_1_11_Selfie

```

```

12. 9_1_12_MultiKeyDict

```

```

13. 9_1_13_predicate

```

```
