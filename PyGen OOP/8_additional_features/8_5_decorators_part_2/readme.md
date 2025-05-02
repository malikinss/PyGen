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

2. 8_5_2_add_attr_to_class

```
# add_attr_to_class Decorator Class Implementation

## Description 📝

The provided code implements the `add_attr_to_class` decorator as a class that adds arbitrary named arguments as attributes to a decorated class.
It uses `setattr` to set the attributes on the class, bypassing the immutability of the class’s `mappingproxy` `__dict__`.
The decorator supports any number of keyword arguments and returns the modified class unchanged in structure, ensuring the attributes are added as specified.

## Purpose 🎯

Intended for scenarios requiring dynamic addition of class attributes, such as metaprogramming, class configuration, or educational examples of Python class decorators, attribute manipulation, and handling `mappingproxy` limitations.

```

3. 8_5_3_jsonattr

```
# jsonattr Decorator Class Implementation

## Description 📝

The provided code implements the `jsonattr` decorator as a class that reads a JSON file and adds its key-value pairs as attributes to a decorated class.
The decorator takes a single argument, `filename`, which specifies the JSON file containing a JSON object.
It uses `json.load` to parse the file and `setattr` to add each key-value pair as a class attribute, bypassing the immutability of the class’s `mappingproxy` `__dict__`.

## Purpose 🎯

Intended for scenarios requiring dynamic class configuration from JSON data, such as configuration management, data-driven programming, or educational examples of Python class decorators, file I/O, JSON parsing, and attribute manipulation.
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
