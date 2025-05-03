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
Intended for scenarios requiring instance tracking, such as debugging, monitoring object creation, or educational examples of Python class decorators, instance management, and method wrapping.
```

2. 8_5_2_add_attr_to_class

```
# add_attr_to_class Decorator Class Implementation

## Description 📝

The provided code implements the `add_attr_to_class` decorator as a class that adds arbitrary named arguments as attributes to a decorated class.
It uses `setattr` to set the attributes on the class, bypassing the immutability of the class’s `mappingproxy` `__dict__`.
The decorator supports any number of keyword arguments and returns the modified class unchanged in structure, ensuring the attributes are added as specified.
Intended for scenarios requiring dynamic addition of class attributes, such as metaprogramming, class configuration, or educational examples of Python class decorators, attribute manipulation, and handling `mappingproxy` limitations.

```

3. 8_5_3_jsonattr

```
# jsonattr Decorator Class Implementation

## Description 📝

The provided code implements the `jsonattr` decorator as a class that reads a JSON file and adds its key-value pairs as attributes to a decorated class.
The decorator takes a single argument, `filename`, which specifies the JSON file containing a JSON object.
It uses `json.load` to parse the file and `setattr` to add each key-value pair as a class attribute, bypassing the immutability of the class’s `mappingproxy` `__dict__`.
Intended for scenarios requiring dynamic class configuration from JSON data, such as configuration management, data-driven programming, or educational examples of Python class decorators, file I/O, JSON parsing, and attribute manipulation.
```

4. 8_5_4_singleton

```
# singleton Decorator Class Implementation

## Description 📝

The provided code implements the `singleton` decorator as a class that transforms a decorated class into a singleton, ensuring only one instance is created.
The decorator stores a single instance in a class-level `_instance` attribute and reuses it for subsequent calls, while allowing the class’s `__init__` to be called each time with new arguments.
It supports arbitrary positional and keyword arguments for `__init__` and uses direct object creation via `object.__new__` to bypass `__init__` during instance creation.
Intended for scenarios requiring a single instance of a class, such as configuration managers, logging systems, or educational examples of Python class decorators, singleton patterns, and instance management.
```

5. 8_5_5_snake_case

```
# snake_case Decorator Class Implementation

## Description 📝

The provided code implements the `snake_case` decorator as a class that renames non-magic methods (and optionally attributes) of a decorated class from Camel Case or lower Camel Case to Snake Case.
The decorator takes a boolean argument `attrs` to determine whether class attributes should also be renamed.
It uses regular expressions in a helper class `CaseHelper` to identify and convert names, ensuring only valid Camel Case names are renamed while preserving leading underscores and skipping magic methods (dunder methods).
Intended for scenarios requiring consistent naming conventions, such as code standardization, API design, or educational examples of Python class decorators, regular expressions, and dynamic attribute manipulation.
```

6. 8_5_6_auto_repr

```
# auto_repr Decorator Class Implementation

## Description 📝

The provided code implements the `auto_repr` decorator as a class that adds a formal string representation (`__repr__`) to a decorated class.
The decorator takes two arguments: `args` (a list of attribute names to display as values) and `kwargs` (a list of attribute names to display as `name=value`).
The resulting `__repr__` method generates a string of the form `<class name>(<attribute>, <attribute>, ...)`, where attributes from `args` appear as values and attributes from `kwargs` appear as `name=value`, in the order specified by the lists.
Intended for scenarios requiring standardized string representations of class instances, such as debugging, logging, or educational examples of Python class decorators, string representation, and dynamic method addition.
```

7. 8_5_7_limiter

```
# limiter Decorator Class Implementation

## Description 📝

The provided code implements the `limiter` decorator as a class that restricts the number of instances a decorated class can create to a specified `limit`.
It uses a `unique` attribute to identify instances and ensures that instances with the same identifier are not duplicated.
If the instance limit is exceeded and the identifier is new, it returns either the first or last created instance based on the `lookup` parameter (`FIRST` or `LAST`).
The decorator supports arbitrary `__init__` arguments and maintains instance state in a dictionary.
Intended for scenarios requiring controlled instance creation, such as resource management, caching, or educational examples of Python class decorators, instance limiting, and identifier-based deduplication.
```
