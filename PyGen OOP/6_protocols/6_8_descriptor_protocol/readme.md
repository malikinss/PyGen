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
