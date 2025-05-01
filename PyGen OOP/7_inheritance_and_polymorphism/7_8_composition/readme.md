Lesson 7.8: composition

Composition
Composition and inheritance
Abstract. The lesson is devoted to composition in class design.

https://stepik.org/lesson/804638/step/1?unit=807762

This lesson has good theory explonation, has 5 programing practical tasks and 7 theoretical questions presented on the website.

7_8_composition
├───7_8_1_Point
├───7_8_2_ShoppingCart
├───7_8_3_Deck
├───7_8_4_Queue
└───7_8_5_Conference

1. 7_8_1_Point

```
# Point and Circle Class Implementation

## Description 📝

The provided code implements the `Point` and `Circle` classes to represent a point and a circle in a 2D plane, respectively.
The `Point` class stores x and y coordinates, while the `Circle` class stores a radius and a center (a `Point` instance).
Both classes provide informal string representations as specified: `(x, y)` for `Point` and `(x, y), r = radius` for `Circle`.

## Purpose 🎯

Intended for geometric applications, such as graphics, simulations, or computational geometry.
It’s also suitable for educational examples of object-oriented programming, class design, and string representation in Python.
```

2. 7_8_2_ShoppingCart

```
# Item and ShoppingCart Class Implementation

## Description 📝

The provided code implements the `Item` and `ShoppingCart` classes to represent a product and a shopping cart, respectively.
The `Item` class stores a product’s name and price, with a string representation of `<name>, <price>$`.
The `ShoppingCart` class manages a list of `Item` instances, supporting adding items, calculating the total cost, removing items by name, and providing a string representation of all items, one per line.

## Purpose 🎯

Intended for e-commerce applications, inventory management, or simulations involving shopping carts.
It’s also suitable for educational examples of object-oriented programming, string representation, and list manipulation in Python.
```

3. 7_8_3_Deck

```
# Card and Deck Class Implementation

## Description 📝

The provided code implements the `Card` and `Deck` classes to represent a playing card and a standard deck of 52 playing cards, respectively.
The `Card` class stores a suit and rank, with a string representation of `<suit><rank>`.
The `Deck` class initializes a full deck ordered by suit and rank, supports shuffling (only when full) and dealing the last card, and provides a string representation of the remaining card count.

## Purpose 🎯

Intended for card game simulations, such as poker or blackjack, or educational examples of object-oriented programming, list manipulation, and exception handling in Python.
```

4. 7_8_4_Queue

```
# Queue Class Implementation

## Description 📝

The provided code implements the `Queue` class to represent a queue of key:value pairs, using a `collections.deque` for efficient operations.
The class supports initialization with a list, dictionary, or no arguments, adding or updating key:value pairs, popping the first pair, and providing formal string representation and length.
It handles key updates by moving existing keys to the end with new values and raises a `KeyError` for popping from an empty queue.

## Purpose 🎯

Intended for applications requiring a queue with key-based updates, such as task scheduling, caching with key priorities, or educational examples of queue operations, deque usage, and Python’s collection protocols.
```

5. 7_8_5_Conference

```
# Lecture and Conference Class Implementation

## Description 📝

The provided code implements the `Lecture` and `Conference` classes to represent a talk and a one-day conference of consecutive talks, respectively.
The `Lecture` class stores a topic, start time, and duration, with times processed using `datetime`.
The `Conference` class manages a list of lectures, ensuring no overlaps, and provides methods to calculate total duration, longest lecture, and longest break, all formatted as `HH:MM`.

## Purpose 🎯

Intended for scheduling applications, such as conference planning, event management, or educational examples of time manipulation, exception handling, and object-oriented programming in Python.
```
