Lesson 7.6: multiple inheritance

Multiple Inheritance
The Diamond Inheritance Problem
Method Resolution Order (MRO)
Abstract: This lesson is about multiple inheritance in Python.

https://stepik.org/lesson/872533/step/1?unit=876917

This lesson has good theory explonation, has 5 programing practical tasks and 19 theoretical questions presented on the website.

1. 7_6_1_class_hierarchy

```
# Class Hierarchy Implementation

## Description 📝

The provided code implements a class hierarchy based on the given diagram, using empty classes in Python.
The hierarchy is structured as follows:

-   `A` is the base class.
-   `C`, `B`, and `D` directly inherit from `A`.
-   `E` inherits from both `B` and `D` (multiple inheritance).

## Purpose 🎯

Intended to define a class hierarchy for use in scenarios requiring inheritance structures, such as object-oriented design, modeling relationships, or educational examples of single and multiple inheritance in Python.
```

2. 7_6_2_class_hierarchy

```
# Class Hierarchy Implementation

## Description 📝

The provided code implements a class hierarchy based on the given diagram, using empty classes in Python.
The hierarchy is structured as follows:

-   `H` is the base class.
-   `D`, `E`, `F`, and `G` directly inherit from `H`.
-   `B` inherits from `D` and `E` (multiple inheritance).
-   `C` inherits from `F` and `G` (multiple inheritance).
-   `A` inherits from `B` and `C` (multiple inheritance).

## Purpose 🎯

Intended for defining a class hierarchy for use in scenarios requiring complex inheritance structures, such as object-oriented design, modeling relationships, or educational examples of multiple inheritance in Python.
```

3. 7_6_3_get_method_owner

```
# get_method_owner Function Implementation

## Description 📝

The provided code implements the `get_method_owner` function, which takes a class (`cls`) and a method name (`method`) as arguments. It returns the class in the inheritance hierarchy of `cls` that defines the specified `method`.
If the method is not found in `cls` or any of its ancestor classes, the function returns `None`.

## Purpose 🎯

Intended for scenarios requiring introspection of class hierarchies, such as debugging, dynamic method resolution, or framework development.
It’s also suitable for educational examples of Python’s Method Resolution Order (MRO) and attribute lookup.
```

4.

```

```

5.

```

```
