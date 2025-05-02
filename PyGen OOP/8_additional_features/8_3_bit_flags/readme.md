Lesson 8.3: bit flags, Flag class

Bit flags
Operators |, &, ^ and ~
Checking for membership
The zero element
Bit flags in Python 3.11
Abstract. The lesson is devoted to bit flags in Python.

https://stepik.org/lesson/958398/step/1?unit=964840

This lesson has good theory explonation, has 2 programing practical tasks and 13 theoretical questions presented on the website.

1. 8_3_1_OrderStatus

```
# OrderStatus Flag Implementation

## Description 📝

The provided code implements the `OrderStatus` class as a Python flag enumeration using `enum.Flag`.
It defines three elements (`ORDER_PLACED`, `PAYMENT_RECEIVED`, `SHIPPING_COMPLETE`) with automatically assigned values via `auto()`.
As a `Flag`, it supports bitwise operations to represent combinations of order states.
Intended for applications tracking online order progress, such as e-commerce systems, order management, or educational examples of Python flag enumerations and bitwise operations.
```

2. 8_3_2_Movie

```
# MovieGenres and Movie Class Implementation

## Description 📝

The provided code implements the `MovieGenres` class as a Python flag enumeration using `enum.Flag` and the `Movie` class to represent a movie with a name and genres.
The `MovieGenres` flag defines five genres (`ACTION`, `COMEDY`, `DRAMA`, `FANTASY`, `HORROR`) with automatically assigned values.
The `Movie` class stores a name and genres, provides a method to check genre membership, and has a string representation of the movie’s name.
Intended for applications involving movie catalogs, recommendation systems, or educational examples of Python flag enumerations, bitwise operations, and object-oriented programming.
```
