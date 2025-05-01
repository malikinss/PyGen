Lesson 8.1: slots, attribute **slots**

Slots
Attribute **slots**
Slots in inheritance
Performance comparison
Abstract. The lesson is devoted to slots and their features.

https://stepik.org/lesson/794701/step/1?unit=797453

This lesson has good theory explonation, has 1 programing practical tasks and 11 theoretical questions presented on the website.

1. 8_1_1_Shape

```
# Shape Class Implementation

## Description 📝

The provided code implements the `Shape` class to represent a geometric shape with a name, color, and area.
The class uses `__slots__` to restrict attributes to `name`, `color`, and `area`, provides an informal string representation, and supports all comparison operations (`==`, `!=`, `>`, `<`, `>=`, `<=`) based on area.
The `@total_ordering` decorator minimizes code by deriving remaining comparison methods from `__eq__` and `__lt__`.

## Purpose 🎯

Intended for geometric applications, such as graphics, simulations, or educational examples of object-oriented programming, comparison protocols, and attribute restriction in Python.
```
