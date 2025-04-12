# Chapter 5: Magic Methods ✨

## Description 📝

This chapter is dedicated to mastering **magic methods** in Python, enabling me to customize the behavior of objects and make them more intuitive and powerful.  
It consists of **11 comprehensive lessons** with in-depth theoretical explanations, **46 hands-on programming tasks**, and **131 theoretical questions** available on the course platform.

## Purpose 🎯

In this chapter, I will:

-   Learn how to use **magic methods** to control object creation, representation, and behavior.
-   Understand how to implement **custom operators**, **type conversions**, and **attribute access**.
-   Explore **hashing** and its role in creating hashable objects for dictionaries and sets.
-   Practice building flexible and reusable classes with real-world applications.

## Course Modules 📚

### Lesson 5.1: Creation, Initialization, and Clearing of Objects 🛠️

In this lesson, I will explore:

-   Magic methods in Python.
-   The **`__new__()`** and **`__init__()`** magic methods for object creation and initialization.
-   Implementing the **Singleton** design pattern.
-   The **`__del__()`** magic method for object deletion.

By the end of this lesson, I will:

-   ✅ Understand how Python creates and initializes objects using `__new__()` and `__init__()`.
-   ✅ Implement the **Singleton** pattern to ensure a class has only one instance.
-   ✅ Learn how to manage object lifecycle using `__del__()`.
-   ✅ Apply these concepts to optimize code for object creation and clearing.

### Lesson 5.2: String Representation of Objects 📜

In this lesson, I will explore:

-   Functions **`str()`** and **`repr()`** in Python.
-   Magic methods **`__str__()`** and **`__repr__()`** for string representations.
-   Formal (developer-friendly) and informal (user-friendly) object descriptions.
-   Practical implementation across various classes.

By the end of this lesson, I will:

-   ✅ Understand the difference between **`str()`** and **`repr()`** functions.
-   ✅ Implement **`__str__()`** and **`__repr__()`** for custom string representations.
-   ✅ Create formal and informal object descriptions.
-   ✅ Apply these concepts to improve object management in real-world scenarios.

### Lesson 5.3: Comparison of Objects ⚖️

In this lesson, I will explore:

-   Magic methods **`__eq__()`** and **`__ne__()`** for equality and inequality.
-   The **`NotImplemented`** constant for unsupported comparisons.
-   Magic methods **`__lt__()`**, **`__gt__()`**, **`__le__()`**, and **`__ge__()`** for ordering.
-   The **`@total_ordering`** decorator for simplified comparison logic.

By the end of this lesson, I will:

-   ✅ Understand how to implement object comparison using magic methods.
-   ✅ Use **`NotImplemented`** to handle invalid comparison cases.
-   ✅ Apply **`@total_ordering`** to streamline comparison logic.
-   ✅ Compare objects in practical scenarios like vectors, dates, and versions.

### Lesson 5.4: Unary Operators and Functions ➕➖

In this lesson, I will explore:

-   Magic methods **`__pos__()`**, **`__neg__()`**, and **`__invert__()`** for unary operators.
-   Magic methods **`__abs__()`**, **`__round__()`**, and similar functions for extended functionality.
-   Practical implementation of unary operations on objects.

By the end of this lesson, I will:

-   ✅ Understand how to implement unary operators using magic methods.
-   ✅ Use **`__abs__()`** and **`__round__()`** to enhance object behavior.
-   ✅ Apply unary operations in practical scenarios.
-   ✅ Overload operators for custom class behavior.

### Lesson 5.5: Arithmetic Operations 🧮

In this lesson, I will explore:

-   Magic methods **`__add__()`**, **`__sub__()`**, and **`__mul__()`** for basic arithmetic.
-   Magic methods **`__truediv__()`**, **`__floordiv__()`**, and **`__mod__()`** for division and modulo.
-   Reflected arithmetic operations (e.g., handling `scalar * obj`).
-   In-place magic methods like **`__iadd__()`**, **`__isub__()`**, and **`__imul__()`**.

By the end of this lesson, I will:

-   ✅ Understand how to implement arithmetic operations using magic methods.
-   ✅ Handle reflected arithmetic for flexible operand ordering.
-   ✅ Use in-place operations for efficient object updates.
-   ✅ Apply arithmetic operations to scenarios like vectors, nutrition, and queues.

### Lesson 5.6: Callable Objects 📞

In this lesson, I will explore:

-   Callable objects in Python.
-   The **`__call__()`** magic method for enabling object invocation.
-   Practical implementation of callable objects and decorators.

By the end of this lesson, I will:

-   ✅ Understand how to make objects callable using **`__call__()`**.
-   ✅ Create callable objects for tasks like arithmetic, formatting, and sorting.
-   ✅ Use callable objects as decorators for function enhancement.
-   ✅ Simplify code and improve functionality with callable objects.

### Lesson 5.7: Type Conversion 🔄

In this lesson, I will explore:

-   Magic method **`__bool__()`** for boolean conversion.
-   Magic methods **`__int__()`**, **`__float__()`**, and **`__complex__()`** for numeric conversions.
-   Practical implementation of type conversion for objects.

By the end of this lesson, I will:

-   ✅ Understand how to implement type conversion using magic methods.
-   ✅ Enable objects to behave like booleans and numbers in various contexts.
-   ✅ Apply type conversion to scenarios like vectors, temperatures, and Roman numerals.

### Lesson 5.8: Working with Object Attributes 🔧

In this lesson, I will explore:

-   Attribute operations in Python.
-   Magic methods **`__getattribute__()`** and **`__getattr__()`** for attribute access.
-   Magic methods **`__setattr__()`** and **`__delattr__()`** for attribute modification and deletion.

By the end of this lesson, I will:

-   ✅ Understand how to control attribute access, modification, and deletion.
-   ✅ Implement custom attribute behavior using magic methods.
-   ✅ Create flexible, secure, and dynamic objects.
-   ✅ Apply these techniques in scenarios like logging, immutability, and access control.

### Lesson 5.9: Object Hashing (Part 1) 🔢

In this lesson, I will explore:

-   Hashing and its role in Python.
-   The built-in **`hash()`** function.
-   Characteristics of a good hash function.
-   Creating custom hash functions and narrowing hash value ranges.

By the end of this lesson, I will:

-   ✅ Understand the concept of hashing and its applications.
-   ✅ Use the **`hash()`** function effectively.
-   ✅ Create custom hash functions with specific properties.
-   ✅ Apply hashing to constrain hash values within a range.

### Lesson 5.10: Object Hashing (Part 2) 🔢

In this lesson, I will explore:

-   Hashability and immutability in Python.
-   The **`__hash__()`** magic method for custom hash values.
-   The hash-equal contract for consistent object behavior.
-   Hashing custom classes for use in sets and dictionaries.

By the end of this lesson, I will:

-   ✅ Understand the relationship between hashability and immutability.
-   ✅ Implement custom hashing using **`__hash__()`**.
-   ✅ Ensure the hash-equal contract for consistent behavior.
-   ✅ Create hashable objects for sets and dictionaries.

### Lesson 5.11: Features of Dictionaries and Sets 📚

In this lesson, I will explore:

-   Features of dictionaries and sets in Python.
-   Performance characteristics and memory consumption.
-   Handling mutable keys and their implications.
-   Pitfalls and downsides of dictionary and set implementations.

By the end of this lesson, I will:

-   ✅ Understand the internal workings of dictionaries and sets.
-   ✅ Recognize factors affecting their performance and memory usage.
-   ✅ Identify risks associated with mutable keys.
-   ✅ Be aware of common pitfalls and implementation limitations.

## Conclusion 🚀

By completing Chapter 5, I will have mastered **magic methods** in Python, enabling me to create intuitive, flexible, and powerful objects.
These skills will enhance my ability to write clean, efficient, and reusable code, preparing me for advanced OOP concepts and real-world Python applications.
