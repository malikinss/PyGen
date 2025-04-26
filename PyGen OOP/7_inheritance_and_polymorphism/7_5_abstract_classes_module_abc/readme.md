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
