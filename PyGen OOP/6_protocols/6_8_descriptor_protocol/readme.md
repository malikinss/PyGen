Lesson 6.8: descriptor protocol

Descriptors
Descriptor protocol
Magic methods **get**(), **set**() and **delete**()
Magic method **set_name**()
Attribute search chain
Abstract. The lesson is devoted to the descriptor protocol.

https://stepik.org/lesson/810856/step/1?unit=816647

This lesson has good theory explonation, has 6 programing practical tasks and 13 theoretical questions presented on the website.

1. 6_8_1_NonKeyword

```
# NonKeyword Class Keyword-Restricting Descriptor

## Description 📝

The `NonKeyword` class is a descriptor that manages an attribute, ensuring its value is not a Python keyword string.
It accepts a `name` argument during instantiation, representing the attribute name.
When accessing the attribute, it returns the stored value or raises `AttributeError` with "Attribute not found" if unset.
When setting the attribute, it checks if the value is a Python keyword string, raising `ValueError` with "Invalid value" if it is, otherwise storing the value.

## Purpose 🎯

Designed for scenarios requiring restricted attribute values, such as configuration objects, domain-specific models, or validation in frameworks, where Python keywords must be avoided to prevent naming conflicts or semantic issues.
It’s also suitable for educational examples demonstrating Python’s descriptor protocol and keyword validation.
```

2. 6_8_2_NonNegativeInteger

```
# NonNegativeInteger Class Restricted Integer Descriptor

## Description 📝

The `NonNegativeInteger` class is a descriptor that ensures an attribute’s value is a non-negative integer.
It accepts two arguments during instantiation: `name` (the attribute name) and `default` (an optional default value, defaulting to `None`).
When accessing the attribute, it returns the stored value or the `default` value if unset; if `default` is `None` and the attribute is unset, it raises `AttributeError` with "Attribute not found".
When setting the attribute, it verifies the value is a non-negative integer, raising `ValueError` with "Invalid value" if not.

## Purpose 🎯

Intended for scenarios requiring strict type and range validation, such as counters, indices, or configuration settings in data models, APIs, or frameworks.
The descriptor enforces data integrity, making it suitable for robust applications or educational examples of Python’s descriptor protocol and value validation.
```

3. 6_8_3_LimitedTakes

```
# LimitedTakes Class Access-Restricted Descriptor

## Description 📝

The `LimitedTakes` class is a descriptor that restricts the number of times an attribute can be accessed, taking a single argument `times` (the access limit) during instantiation.
It must be assigned to an attribute matching the variable name. When accessing the attribute, it returns the stored value if set and within the access limit, raises `AttributeError` with "Attribute not found" if unset, or raises `MaxCallsException` with "The number of times the attribute can be accessed has been exceeded" if the limit is exceeded.
Setting the attribute stores the value without restrictions.

## Purpose 🎯

Intended for scenarios requiring controlled attribute access, such as rate-limiting data retrieval, enforcing usage quotas, or protecting sensitive data in objects.
It’s also suitable for educational examples demonstrating Python’s descriptor protocol and custom exception handling.
```

4. 6_8_4_TypeChecked

```
# TypeChecked Class Type-Restricting Descriptor

## Description 📝

The `TypeChecked` class is a descriptor that ensures an attribute’s value matches one of the specified data types.
It accepts an arbitrary number of type arguments during instantiation and must be assigned to an attribute matching the variable name.
When accessing the attribute, it returns the stored value if set, or raises `AttributeError` with "Attribute not found" if unset.
When setting the attribute, it verifies the value’s type against the specified types, raising `TypeError` with "Invalid value" if it doesn’t match.

## Purpose 🎯

Intended for scenarios requiring strict type validation, such as ensuring data consistency in configuration objects, API models, or domain-specific classes.
It prevents type-related errors, making it suitable for robust applications or educational examples of Python’s descriptor protocol and type checking.
```

5. 6_8_5_RandomNumber

```
# RandomNumber Class Random Integer Descriptor

## Description 📝

The `RandomNumber` class is a descriptor that generates a random integer within a specified range `[start, end]` (inclusive) when an attribute is accessed.
It accepts three arguments during instantiation: `start` (integer), `end` (integer), and `cache` (boolean, defaulting to `False`).
The descriptor must be assigned to an attribute matching the variable name.
If `cache` is `True`, it returns the first generated number on subsequent accesses; otherwise, it generates a new random number each time.
Setting the attribute raises `AttributeError` with "Change is not possible".

## Purpose 🎯

Intended for scenarios requiring controlled random value generation, such as simulations, testing, or game mechanics, where consistent or fresh random numbers are needed.
The read-only nature and caching option make it suitable for applications requiring stable or dynamic randomness, as well as educational examples of Python’s descriptor protocol.
```

6.

```

```
