# Lesson 4.6: The `@property` Decorator 🎨

## Description 📝

This lesson is focused on:

-   The **`@property` decorator** in Python
-   How to use the `@property` decorator to define properties that can be accessed like attributes

## Purpose 🎯

By the end of this lesson, I will:
✅ Understand the usage of the `@property` decorator in Python  
✅ Learn how to make **getter** and **setter** methods more Pythonic  
✅ Implement read-only and read-write properties using the decorator  
✅ Enhance code readability and encapsulation in Python classes

## How It Works 🔍

### 🔹 What Is the `@property` Decorator?

The `@property` decorator allows you to define methods that can be accessed like regular attributes.
It is a way to make **getter** and **setter** methods more Pythonic by using them with **attribute-style access**.

### 🔹 Using the `@property` Decorator

With the `@property` decorator, you can define a method to get a value, and optionally another method to set a value.
This avoids the need for explicit getter and setter methods, simplifying your code.

Example of using the `@property` decorator:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive.")
```

### 🔹 Advantages of Using `@property`

✅ **Improved code readability**: Properties provide a clean syntax for working with class attributes  
✅ **Encapsulation**: You can hide implementation details and control access to attributes  
✅ **Dynamic updates**: Properties automatically update when the underlying data changes

---

## Practical Tasks 🖥️

### 1️⃣ **Person Class Name Manager**

📌 `Person` class representing a person with `first_name` and `last_name`
🔹 Implements a **read-write** `fullname` property using the `@property` decorator
🔹 Ensures synchronization between the full name and individual name components

### 2️⃣ **Account Class Security Manager**

📌 `Account` class modeling an Internet user account
🔹 Provides a **read-only** `login` property
🔹 **Read-write** `password` property using hashing to never store the password directly

### 3️⃣ **QuadraticPolynomial Class Math Tool**

📌 `QuadraticPolynomial` class modeling a quadratic equation `ax^2 + bx + c`
🔹 **Read-only** properties for the roots (`x1`, `x2`) and string representation (`view`)
🔹 **Read-write** properties for coefficients that update dynamically

### 4️⃣ **Color Class Hex Manager**

📌 `Color` class representing a color in hexadecimal format
🔹 **Read-write** `hexcode` property, which synchronizes with `r`, `g`, and `b` components

## Output 📜

After completing this lesson, I will:
✅ Be able to use the `@property` decorator to implement getter and setter methods  
✅ Create read-only and read-write properties that offer clean and intuitive code  
✅ Use properties to control access to class attributes while maintaining clean code

## Conclusion 🚀

The `@property` decorator enhances code readability and flexibility by allowing **getter and setter methods** to be used as **attributes**.
It is a powerful tool for **encapsulation** and helps maintain the **integrity of data** while providing a natural interface for interacting with object properties. 🌟
