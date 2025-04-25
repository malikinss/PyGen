Lesson 7.4: inheritance (part 4)

Inheritance from the dict type
Inheritance from the list type
UserDict and UserList types from the collections module
Abstract. The lesson is devoted to inheritance from the dict and list types.

https://stepik.org/lesson/860444/step/1?unit=864459

This lesson has good theory explonation, has 8 programing practical tasks and 14 theoretical questions presented on the website.

1. 7_4_1_DefaultList

```
# DefaultList Class Implementation

## Description 📝

The provided code implements the `DefaultList` class, a subclass of `collections.UserList`.
It represents a list that returns a specified default value when attempting to access an element at a non-existent index.
The class is initialized with two arguments: `iterable` (defining the initial elements, defaulting to an empty tuple) and `default` (the value returned for out-of-bounds indices, defaulting to `None`).
The list is independent of the input iterable, ensuring that changes to the original iterable do not affect the `DefaultList` instance.

## Purpose 🎯

Intended for scenarios where safe index access is needed, such as data processing, user input handling, or dynamic list manipulation, avoiding `IndexError` exceptions.
It’s also suitable for educational examples of list subclassing and custom indexing behavior in Python.
```

2. 7_4_2_EasyDict

```
# EasyDict Class Implementation

## Description 📝

The provided code implements the `EasyDict` class, a subclass of Python's built-in `dict` class. It allows dictionary values to be accessed and modified both via standard key-based access (`d[key]`) and attribute-style access (`d.key`).
The initialization process matches that of `dict`, accepting the same arguments.
The class supports getting, setting, and deleting values using attribute notation, mirroring dictionary key operations.

## Purpose 🎯

Intended for scenarios where dictionary access needs to be more intuitive or readable, such as configuration objects, data models, or API response handling.
It’s also suitable for educational examples of dictionary subclassing and attribute access customization in Python.
```

3. 7_4_3_TwoWayDict

```
# TwoWayDict Class Implementation

## Description 📝

The provided code implements the `TwoWayDict` class, a subclass of `collections.UserDict`.
It represents a bidirectional dictionary where adding a `key:value` pair automatically adds the reverse `value:key` pair.
The initialization process matches that of `UserDict`, accepting the same arguments.
The class ensures that each key-value pair is mirrored, allowing lookups in both directions.

## Purpose 🎯

Intended for scenarios requiring bidirectional mappings, such as graph edge representations, synonym dictionaries, or two-way lookups in data processing.
It’s also suitable for educational examples of dictionary subclassing and custom item-setting behavior in Python.
```

4. 7_4_4_AdvancedList

```
# AdvancedList Class Implementation

## Description 📝

The provided code implements the `AdvancedList` class, a subclass of Python's built-in `list` class.
It extends list functionality with three methods: `join` (concatenates elements into a string with a separator), `map` (applies a function to each element in-place), and `filter` (removes elements failing a predicate function in-place).
The initialization process matches that of `list`, accepting the same arguments.

## Purpose 🎯

Intended for scenarios requiring enhanced list manipulation, such as data processing, functional programming patterns, or string formatting.
It’s also suitable for educational examples of list subclassing and in-place modifications in Python.
```

5. 7_4_5_NumberList

```
# NumberList Class Implementation

## Description 📝

The provided code implements the `NumberList` class, a subclass of `collections.UserList`.
It represents a list that only contains numbers (`int` or `float`), enforcing this constraint during initialization and modifications (via indexing, addition, `append`, `extend`, and `insert`).
The class accepts an optional `iterable` argument during instantiation, defaulting to an empty tuple.
It raises a `TypeError` with the message "The elements of the NumberList class instance must be numbers" if non-numbers are provided.
The list is independent of the input iterable, and it supports addition (`+`, `+=`) and `extend` with any iterable of numbers.

## Purpose 🎯

Intended for scenarios requiring lists strictly containing numbers, such as numerical computations, statistical analysis, or data validation.
It’s also suitable for educational examples of list subclassing, validation, and operator overloading in Python.
```

6. 7_4_6_ValueDict

```
# ValueDict Class Implementation

## Description 📝

The provided code implements the `ValueDict` class, a subclass of Python's built-in `dict` class.
It extends dictionary functionality with two methods: `key_of` (returns the first key associated with a given value, or `None` if none exists) and `keys_of` (returns an iterable of all keys associated with a given value).
The initialization process matches that of `dict`, accepting the same arguments.

## Purpose 🎯

Intended for scenarios requiring reverse lookups in dictionaries, such as mapping values to keys in data processing, configuration management, or database-like operations.
It’s also suitable for educational examples of dictionary subclassing and iterator usage in Python.
```

7. 7_4_7_BirthdayDict

```
# BirthdayDict Class Implementation

## Description 📝

The provided code implements the `BirthdayDict` class, a subclass of `collections.UserDict`.
It represents a dictionary for storing names (keys) and birthdays (values), with a feature to print a notification when a new or updated key-value pair has a birthday that already exists for another key.
The initialization process matches that of `UserDict`, and the notification message is displayed during addition or modification of key-value pairs.

## Purpose 🎯

Intended for applications managing birthday data, such as calendars, event planners, or social apps, where users should be alerted to shared birthdays.
It’s also suitable for educational examples of dictionary subclassing and custom item-setting behavior in Python.
```

8. 7_4_8_MutableString

```
# MutableString Class Implementation

## Description 📝

The provided code implements the `MutableString` class, a subclass of `collections.UserString`.
It represents a mutable string, allowing in-place modifications via indexing, slicing, and methods for case conversion (`lower`, `upper`) and sorting (`sort`).
The initialization process matches that of `UserString`, and the class supports getting, setting, and deleting characters or substrings using positive or negative indices.

## Purpose 🎯

Intended for scenarios requiring mutable string operations, such as text editing, string manipulation, or dynamic content processing.
It’s also suitable for educational examples of string subclassing, mutability, and indexing in Python.
```
