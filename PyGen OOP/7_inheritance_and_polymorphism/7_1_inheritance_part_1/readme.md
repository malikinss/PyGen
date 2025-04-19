Lesson 7.1: inheritance (part 1)

Introduction to inheritance
Inheritance in Python
Defining and overriding attributes and methods
Implicit inheritance, class object
Multilevel inheritance
Abstract. The lesson is devoted to inheritance in Python.

https://stepik.org/lesson/794707/step/1?unit=797459

This lesson has good theory explonation, has 6 programing practical tasks and 21 theoretical questions presented on the website.

7_1_inheritance_part_1
├───7_1_1_Vehicle
├───7_1_2_Shape
├───7_1_3_Animal
├───7_1_4_User
├───7_1_5_Validator
└───7_1_6_Counter

1. 7_1_1_Vehicle

```
# Vehicle Class Hierarchy

## Description 📝

The provided code defines a hierarchy of empty classes representing vehicles, structured according to the given diagram.
The hierarchy uses inheritance to model relationships between a base `Vehicle` class and its subclasses, categorized by their operating environment (land, water, air) and further specialized into specific vehicle types.

## Purpose 🎯

Intended to establish a foundational class structure for modeling vehicles in applications such as transportation systems, simulations, or inventory management.
The empty classes provide a framework that can be extended with attributes and methods, suitable for object-oriented design or educational examples of inheritance in Python.
```

2. 7_1_2_Shape

```
# Geometric Shape Class Hierarchy

## Description 📝

The provided code defines a hierarchy of empty classes representing geometric shapes, structured according to the given diagram.
The hierarchy uses inheritance to model relationships between a base `Shape` class and its subclasses, categorized by shape type (circle, polygon) and further specialized into specific shapes like quadrilaterals, triangles, and their variants.

## Purpose 🎯

Intended to establish a foundational class structure for modeling geometric shapes in applications such as graphics, CAD systems, or mathematical simulations.
The empty classes provide a framework that can be extended with attributes (e.g., dimensions) and methods (e.g., area calculation), suitable for object-oriented design or educational examples of inheritance in Python.
```

3. 7_1_3_Animal

```
# Animal Class Hierarchy

## Description 📝

The provided code defines a hierarchy of classes representing animals, structured according to the given diagram.
The hierarchy uses inheritance to model relationships between a base `Animal` class and its subclasses (`Fish`, `Bird`, `FlyingBird`).
Each class includes specific empty methods as specified: `Animal` has `sleep` and `eat`, `Fish` has `swim`, `Bird` has `lay_eggs`, and `FlyingBird` has `fly`.

## Purpose 🎯

Intended to establish a foundational class structure for modeling animals in applications such as zoological simulations, educational tools, or behavioral studies.
The empty methods provide a framework for implementing specific behaviors, suitable for object-oriented design or educational examples of inheritance and method specialization in Python.
```

4. 7_1_4_User

```
# User and PremiumUser Class Hierarchy

## Description 📝

The provided code implements two classes: `User` and `PremiumUser`.
The `User` class represents a basic user of an internet resource, initialized with a `name` (string) and featuring a `skip_ads` method that always returns `False`.
The `PremiumUser` class, a subclass of `User`, represents a user with a premium subscription, initialized identically to `User` and overriding `skip_ads` to always return `True`.

## Purpose 🎯

Intended to model users of an internet resource, distinguishing between standard and premium users based on their ability to skip ads.
This structure is suitable for applications like streaming platforms, content websites, or subscription-based services, as well as educational examples of inheritance and method overriding in Python.
```

5. 7_1_5_Validator

```
# Validator and NumberValidator Class Hierarchy

## Description 📝

The provided code implements two classes: `Validator` and `NumberValidator`.
The `Validator` class represents a generic validator that accepts an arbitrary object (`obj`) during initialization and has an `is_valid` method that always returns `None`.
The `NumberValidator` class, a subclass of `Validator`, inherits the same initialization process and overrides `is_valid` to return `True` if the stored object is an `int` or `float`, and `False` otherwise.

## Purpose 🎯

Intended to model a validation framework where values need to be checked for correctness, with extensibility for specific validation rules.
The `Validator` class provides a base for generic validation, while `NumberValidator` specializes in numeric type checking, suitable for data processing, form validation, or educational examples of inheritance and method overriding in Python.
```

6. 7_1_6_Counter

```
# Counter Class Hierarchy

## Description 📝

The provided code implements three classes: `Counter`, `NonDecCounter`, and `LimitedCounter`.
The `Counter` class represents a non-negative counter with a `value` attribute and methods to increment (`inc`) and decrement (`dec`) it.
`NonDecCounter`, a subclass of `Counter`, allows only incrementing, with an empty `dec` method. `LimitedCounter`, another subclass of `Counter`, restricts incrementing to a specified `limit`.
All classes adhere to their respective initialization and behavior requirements.

## Purpose 🎯

Intended to model counters with varying constraints, suitable for applications like score tracking, resource limits, or inventory management.
The hierarchy demonstrates inheritance and method overriding, making it ideal for robust systems or educational examples of object-oriented programming in Python.
```
