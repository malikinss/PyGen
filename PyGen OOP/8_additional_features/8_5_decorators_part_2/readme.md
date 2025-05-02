Lesson 8.5: Decorators (part 2)

Decorating Classes
Examples of Class Decorating
Abstract: This lesson is about class decorators in Python.

https://stepik.org/lesson/835206/step/1?unit=838840

This lesson has good theory explonation, has 7 programing practical tasks and 8 theoretical questions presented on the website.

1. 8_5_1_track_instances

```
# track_instances Decorator Implementation

## Description 📝

The provided code implements the `track_instances` decorator as a function that decorates a class to track all its instances in a class-level `instances` attribute.
The decorator wraps the class’s `__init__` method to append each new instance to the `instances` list after initialization, preserving the order of creation.
It uses `functools.wraps` to maintain the original `__init__` method’s metadata and supports classes with arbitrary `__init__` arguments.

## Purpose 🎯

Intended for scenarios requiring instance tracking, such as debugging, monitoring object creation, or educational examples of Python class decorators, instance management, and method wrapping.
```

2.

```

```

3.

```

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
