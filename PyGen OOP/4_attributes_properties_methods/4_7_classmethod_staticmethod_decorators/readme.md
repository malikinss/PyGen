# Lesson 4.7: The `@classmethod` and `@staticmethod` Decorators 🏗️

## Description 📝

This lesson is focused on:

-   **Instance Methods**: Methods that operate on an instance of the class
-   **Class Methods**: Methods that operate on the class itself rather than on an instance, created using the `@classmethod` decorator
-   **Static Methods**: Methods that don't depend on either the instance or the class, created using the `@staticmethod` decorator

## Purpose 🎯

By the end of this lesson, I will:
✅ Understand the difference between instance methods, class methods, and static methods  
✅ Learn how to use `@classmethod` and `@staticmethod` decorators in Python  
✅ Implement class and static methods for flexible class design and functionality  
✅ Enhance code structure with more specialized methods

## How It Works 🔍

### 🔹 Instance Methods

Instance methods are the most common type of method. They are defined within the class and typically take `self` as their first argument, which refers to the instance of the class.
These methods operate on instance attributes and allow for dynamic changes to the object's state.

Example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
```

### 🔹 Class Methods (`@classmethod` decorator)

Class methods are bound to the class, not the instance, and are defined using the `@classmethod` decorator. The first argument is typically `cls`, which refers to the class itself. Class methods are used to modify class-level attributes or provide alternate constructors.

Example:

```python
class Circle:
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)
```

### 🔹 Static Methods (`@staticmethod` decorator)

Static methods are independent of both the instance and the class. They do not modify object or class-level attributes and can be called without creating an instance. These methods are defined using the `@staticmethod` decorator and are typically used for utility functions that are related to the class but don't need to interact with the class or its instances.

Example:

```python
class MathOperations:
    @staticmethod
    def square(x):
        return x * x
```

---

## Practical Tasks 🖥️

### 1️⃣ **Circle Class Geometry Builder**

📌 The `Circle` class represents a circle defined by its radius.  
🔹 Includes a class method `from_diameter()` that creates a circle based on a provided diameter, calculating the radius as half the diameter.

### 2️⃣ **Rectangle Class Shape Creator**

📌 The `Rectangle` class represents a rectangle with specified length and width.  
🔹 Includes a class method `square()` that creates a rectangle where both length and width are equal, effectively forming a square.

### 3️⃣ **QuadraticPolynomial Class Polynomial Builder**

📌 The `QuadraticPolynomial` class represents a quadratic equation `ax^2 + bx + c`.  
🔹 Includes two class methods:

-   `from_iterable()` to create an instance from an iterable of coefficients
-   `from_str()` to create one from a space-separated string of coefficients

### 4️⃣ **Pet Class Tracker**

📌 The `Pet` class represents a pet with a given name and tracks all instances.  
🔹 Provides class methods to access the first and last instantiated pets and the total number of pets created.

### 5️⃣ **StrExtension Class String Toolkit**

📌 The `StrExtension` class provides static methods for string manipulation.  
🔹 Includes methods to remove Latin vowels, retain only Latin alphabetic characters, and replace specified characters using regular expressions.

### 6️⃣ **CaseHelper Class Style Converter**

📌 The `CaseHelper` class provides static methods for handling string styles like Snake Case and Upper Camel Case.  
🔹 Includes methods to check string formats and convert between these two naming conventions.

## Output 📜

After completing this lesson, I will:
✅ Understand the usage and advantages of class methods and static methods  
✅ Be able to implement flexible and reusable class methods with `@classmethod`  
✅ Create utility static methods with `@staticmethod` for efficient code  
✅ Use class and static methods to improve class design and functionality

## Conclusion 🚀

The `@classmethod` and `@staticmethod` decorators provide powerful tools for creating flexible, reusable, and efficient methods in Python.
Class methods allow for modifying class-level attributes or creating alternative constructors, while static methods are ideal for utility functions that don't rely on class or instance state. 🌟
