Lesson 8.6: dataclasses module

Data classes
Module dataclasses
Decorator @dataclass
Abstract. The lesson is devoted to the dataclasses module.

https://stepik.org/lesson/803002/step/1?unit=806074

This lesson has good theory explonation, has 4 programing practical tasks and 22 theoretical questions presented on the website.

1. 8_6_1_City

```
# City Data Class Implementation

## Description 📝

The provided code implements the `City` class as a Python data class using the `@dataclass` decorator.
It defines a city with three attributes: `name` (string), `population` (integer), and `founded` (integer).
The data class automatically generates an `__init__` method to initialize these attributes, a `__repr__` method for a formal string representation, and an `__eq__` method for equality comparison, meeting all specified requirements.

## Purpose 🎯

Intended for applications requiring structured representation of city data, such as geographic information systems, data analysis, or educational examples of Python data classes, automatic method generation, and comparison operations.
```

2. 8_6_2_MusicAlbum

```
# MusicAlbum Data Class Implementation

## Description 📝

The provided code implements the `MusicAlbum` class as an immutable Python data class using the `@dataclass(frozen=True)` decorator.
It defines a music album with four attributes: `title` (string), `artist` (string), `genre` (string), and `year` (integer).
The data class automatically generates an `__init__` method to initialize these attributes, a `__repr__` method for a formal string representation, and an `__eq__` method for equality comparison based on `title`, `artist`, and `year`.
The `frozen=True` parameter ensures immutability, and `field` settings exclude `genre` and `year` from `__repr__` and `genre` from `__eq__` as required.

## Purpose 🎯

Intended for applications requiring structured, immutable representations of music albums, such as music libraries, catalog systems, or educational examples of Python data classes, immutability, and custom comparison logic.
```

3. 8_6_3_Point

```
# Point Data Class Implementation

## Description 📝

The provided code implements the `Point` class as a Python data class using the `@dataclass` decorator.
It represents a point on a coordinate plane with attributes `x` (float), `y` (float), and `quadrant` (int).
The class accepts `x` and `y` coordinates with default values of `0.0`, computes the `quadrant` automatically, provides methods for symmetry about the x- and y-axes, and supports equality comparisons.
The implementation uses `dataclasses.field` to configure `quadrant` and includes a `__post_init__` method to compute the quadrant based on coordinates.

## Purpose 🎯

Intended for applications involving geometric computations, such as graphics, simulations, or educational examples of Python data classes, coordinate geometry, and custom attribute initialization.
```

4.

```

```
