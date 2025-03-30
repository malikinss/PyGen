# Lesson 4.1: Attributes of Objects and Classes 🏛️

## Description 📝

In this lesson, I will explore:

-   Object-Oriented Programming (OOP) in Python.
-   Understanding the `dir()` function.
-   Differentiating between object attributes and class attributes.
-   Using the `__dict__` attribute.
-   Working with `getattr()`, `setattr()`, `hasattr()`, and `delattr()` functions.

This lesson provides a strong foundation for working with attributes in Python, helping me understand how objects and classes store and manage data.

## Purpose 🎯

By the end of this lesson, I will:
✅ Understand the difference between object and class attributes.  
✅ Learn how to inspect and manipulate attributes dynamically.  
✅ Gain hands-on experience with practical programming tasks.

## How It Works 🔍

### 🔹 Attributes of Objects and Classes

-   **Object attributes**: Attributes that belong to a specific instance of a class.
-   **Class attributes**: Attributes shared among all instances of a class.
-   Example:

```python
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand  # Object attribute

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand)  # Toyota (object attribute)
print(car2.brand)  # Honda (object attribute)
print(car1.wheels)  # 4 (class attribute)
print(car2.wheels)  # 4 (class attribute)
```

### 🔹 The `dir()` Function

The `dir()` function returns a list of all attributes and methods of an object.  
Example:

```python
print(dir(car1))
```

### 🔹 The `__dict__` Attribute

The `__dict__` attribute returns a dictionary representation of an object's attributes.
Example:

```python
print(car1.__dict__)  # {'brand': 'Toyota'}
```

### 🔹 Working with Attribute Functions

Python provides built-in functions for working with attributes:

-   `getattr(obj, "attribute")` → Retrieves an attribute.
-   `setattr(obj, "attribute", value)` → Sets an attribute.
-   `hasattr(obj, "attribute")` → Checks if an attribute exists.
-   `delattr(obj, "attribute")` → Deletes an attribute.

Example:

```python
setattr(car1, "color", "Red")  # Adding a new attribute
print(getattr(car1, "color"))  # Red
print(hasattr(car1, "color"))  # True
delattr(car1, "color")  # Removing the attribute
```

## Practical Tasks 🖥️

This lesson includes **3 programming tasks** related to a **PiggyBank** class:

### 1️⃣ `4_1_1_PiggyBank_1`

**Task:** Create an empty class `PiggyBank` that serves as a foundation for implementing a savings container.

### 2️⃣ `4_1_2_PiggyBank_2`

**Task:** Instantiate multiple objects and dynamically assign attributes.

### 3️⃣ `4_1_3_PiggyBank_3`

**Task:** Define a class with predefined attributes.

## Output 📜

By completing this lesson, I will:
✅ Understand the concept of object and class attributes.  
✅ Learn how to manipulate attributes dynamically using built-in functions.  
✅ Gain practical experience with OOP by solving coding tasks.

## Conclusion 🚀

Attributes are essential in Python's OOP, allowing objects to store and manage data efficiently. Learning how to manipulate attributes dynamically gives me greater flexibility in designing object-oriented applications. By completing this lesson, I will develop a solid foundation for working with attributes in Python. 💡
