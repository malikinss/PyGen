# Lesson 4.5: Properties and the `property()` Function 🧩

## Description 📝

This lesson covers:

-   **Properties in Python**
-   The **`property()` function**
-   The **Property object** and how it improves encapsulation and readability

## Purpose 🎯

By the end of this lesson, I will:
✅ Understand the concept of properties in Python  
✅ Learn how to use the built-in `property()` function  
✅ Be able to create read-only and read-write properties  
✅ Replace manual getters/setters with more Pythonic property syntax

## How It Works 🔍

### 🔹 What Is a Property?

A **property** in Python is a special kind of attribute that allows you to **customize access to private data** using **getter**, **setter**, and **deleter** methods, while still allowing attribute-style access.

Properties provide a clean interface between attribute access and method calls.

### 🔹 Using the `property()` Function

Syntax:

```python
class MyClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            raise ValueError("Must be positive!")

    value = property(get_value, set_value)
```

### 🔹 Advantages of Properties

✅ Allows **controlled access** to attributes  
✅ Avoids breaking the API when changing implementation  
✅ Encourages **cleaner, more readable code**  
✅ Makes encapsulation feel more natural in Python

## Practical Tasks 🖥️

### 1️⃣ **Rectangle Class Geometry Tool**

📌 `Rectangle` class with `length` and `width` as normal attributes  
🔹 Provides **read-only properties** `perimeter` and `area`, which auto-update  
🔹 Demonstrates dynamic calculations using properties

### 2️⃣ **HourClock Class Time Keeper**

📌 `HourClock` class for a 12-hour time model  
🔹 Uses a **read-write property** `hours` with validation (must be int 1–12)  
🔹 Example of using setter logic to control allowed values

### 3️⃣ **Person Class Name Manager**

📌 `Person` class with `first_name` and `last_name`  
🔹 Implements a **read-write** property `fullname`  
🔹 Allows setting a new full name which updates both parts  
🔹 Shows **two-way sync** between attributes and a compound property

## Output 📜

By completing this lesson, I will:
✅ Use `property()` to define custom attribute behavior  
✅ Apply read-only and read-write logic to control how data is accessed or changed  
✅ Improve code readability and maintainability in real-world classes

## Conclusion 🚀

Properties provide a **Pythonic, elegant solution** to attribute management in classes.  
They eliminate the need for explicit `get_`/`set_` methods while still **encapsulating logic**, making classes both **safer and more intuitive to use**.
This lesson’s practical tasks showcase the flexibility and real-world utility of this powerful feature. 🌟
