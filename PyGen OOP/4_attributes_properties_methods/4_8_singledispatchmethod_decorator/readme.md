# Lesson 4.8: Decorator `@singledispatchmethod` 🎭

## Description 📝

This lesson explores:

-   Method overloading and how Python handles it
-   Alternative ways to initialize or handle data types
-   The `@singledispatchmethod` decorator — a powerful tool for **type-based method dispatching**

## Purpose 🎯

After this lesson, I will:
✅ Understand **method overloading** in Python  
✅ Use `@singledispatchmethod` to implement **polymorphic behavior** without subclassing  
✅ Write flexible code that adapts based on the **input type**  
✅ Avoid manual type-checking with clean, maintainable code

## Concepts & Theory 🔍

### 🔹 Method Overloading in Python

Unlike languages like Java or C++, Python does **not support method overloading** natively. Instead, we use:

-   Default arguments
-   Variable-length arguments (`*args`, `**kwargs`)
-   Type-checking with `isinstance()`  
    ...but these are often **not elegant or scalable**.

### 🔹 `@singledispatchmethod` from `functools`

The `@singledispatchmethod` decorator allows **function overloading by type**, making code:

-   More readable
-   Extensible
-   Cleaner than long `if-elif` chains

#### Example:

```python
from functools import singledispatchmethod

class Demo:
    @singledispatchmethod
    def show(self, arg):
        raise TypeError("Unsupported type")

    @show.register(int)
    def _(self, arg):
        print(f"Integer: {arg}")

    @show.register(str)
    def _(self, arg):
        print(f"String: '{arg}'")
```

## Practical Tasks 🧪

### 1️⃣ **Processor Class Type Handler**

📌 `Processor.process()` converts objects based on type  
🔹 Uses `@singledispatchmethod` to handle:

-   `int` / `float`
-   `str`
-   `list` / `tuple`
    🔹 Raises `TypeError` on unsupported types  
    🛠️ Great example of **polymorphism by input type**

### 2️⃣ **Negator Class Value Inverter**

📌 `Negator.neg()` inverts values by type  
🔹 Handles:

-   Numbers (changes sign)
-   Booleans (flips `True` ↔ `False`)  
    🔹 Raises `TypeError` for other types  
    🧲 Useful in utilities and logic systems

### 3️⃣ **Formatter Class Type Printer**

📌 `Formatter.format()` displays formatted info about values  
🔹 Supported types: `int`, `float`, `list`, `tuple`, `dict`  
🔹 Encloses strings in quotes for clear visual  
🔹 Type-specific `@singledispatchmethod` branches  
🖨️ Ideal for debuggers or CLI tools

### 4️⃣ **BirthInfo Class Age Calculator**

📌 Accepts birth date in multiple formats:

-   `datetime.date`
-   ISO string (`'YYYY-MM-DD'`)
-   List or tuple of integers (`[year, month, day]`)  
    🔹 Stores a `datetime.date` internally  
    🔹 Read-only `age` property calculates current age  
    🔹 Uses `@singledispatchmethod` in initializer  
    📅 Demonstrates powerful **initializer overloading**

## Benefits of `@singledispatchmethod` ✅

-   Enables **cleaner type-based logic**
-   Makes code **easier to extend** for new types
-   Eliminates deep `if-elif` trees or type-checking boilerplate
-   Encourages **OOP and DRY principles**

## Output 📜

By completing this lesson, I now:
✅ Use `@singledispatchmethod` to create method-based type dispatch  
✅ Build more extensible and elegant classes  
✅ Avoid brittle and repetitive type-checking  
✅ Apply real polymorphism without inheritance

## Conclusion 🚀

The `@singledispatchmethod` decorator is a **hidden gem** for writing clean, scalable, and Pythonic code.
Whether you're processing data, formatting output, or supporting multiple input types, this approach helps you write code that is both **beautiful and bulletproof**. 💎
