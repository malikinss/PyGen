# Lesson 7.1: Inheritance (Part 1) 🧬

## Description 📝

This lesson covers:

-   Introduction to inheritance in Python
-   Defining and overriding attributes and methods
-   Implicit inheritance and the `object` class
-   Multilevel inheritance

This lesson includes a detailed theoretical explanation, 6 programming practical tasks, and 21 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the fundamentals of inheritance in Python  
✅ Define and override methods and attributes in subclasses  
✅ Apply implicit and multilevel inheritance effectively  
✅ Create class hierarchies for practical use cases

## Concepts & Theory 🔍

### 🔹 Introduction to Inheritance

-   **Purpose**: Allows classes to inherit attributes and methods from others.
-   **How It Works**: Subclasses extend or specialize base class behavior.

### 🔹 Inheritance in Python

-   **Purpose**: Enables code reuse and hierarchical organization.
-   **Syntax**: Subclasses are defined with `class SubClass(BaseClass)`.

### 🔹 Defining and Overriding Attributes and Methods

-   **Purpose**: Customizes subclass behavior by redefining inherited members.
-   **When Used**: To specialize or extend functionality in subclasses.

### 🔹 Implicit Inheritance and `object` Class

-   **Purpose**: All classes implicitly inherit from `object` if no base is specified.
-   **Benefits**: Provides default methods like `__init__` and `__str__`.

### 🔹 Multilevel Inheritance

-   **Purpose**: Allows a class to inherit from a subclass, forming a chain.
-   **When Used**: To create deep hierarchies for complex relationships.

## Practical Task 🧪

### 1️⃣ **Class Hierarchies with Inheritance**

The lesson includes 6 practical tasks, each implementing inheritance:

1. **`Vehicle` Class Hierarchy**: Empty classes modeling vehicles.

    - Structured by environment (land, water, air) and vehicle types.

2. **`Shape` Class Hierarchy**: Empty classes for geometric shapes.

    - Organized by shape type (circle, polygon) and subtypes.

3. **`Animal` Class Hierarchy**: Classes with specific methods.

    - `Animal`: `sleep`, `eat`; `Fish`: `swim`; `Bird`: `lay_eggs`; `FlyingBird`: `fly`.

4. **`User` and `PremiumUser` Classes**: Models internet users.

    - `User`: `skip_ads` returns `False`; `PremiumUser`: overrides to `True`.

5. **`Validator` and `NumberValidator` Classes**: Validation framework.

    - `Validator`: `is_valid` returns `None`; `NumberValidator`: checks for `int`/`float`.

6. **`Counter` Class Hierarchy**: Non-negative counters.
    - `Counter`: `inc`, `dec`; `NonDecCounter`: no `dec`; `LimitedCounter`: capped `inc`.

💡 These tasks demonstrate inheritance for modeling real-world hierarchies and behaviors.

## Benefits ✅

-   Inheritance promotes code reuse and modularity.
-   Method overriding enables specialized behavior.
-   Multilevel inheritance supports complex hierarchies.
-   Implicit `object` inheritance ensures consistent base functionality.

## Output 📜

After completing this lesson, I now:  
✅ Create and extend class hierarchies using inheritance  
✅ Override methods and attributes for specialized behavior  
✅ Apply multilevel inheritance to model complex relationships

## Conclusion 🚀

Mastering inheritance in Python empowers me to build modular, extensible class hierarchies.  
From vehicle taxonomies to specialized counters, these tools enable efficient, organized code for diverse applications. 🧑‍💻✨
