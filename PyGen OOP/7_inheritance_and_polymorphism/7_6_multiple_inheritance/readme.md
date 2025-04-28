# Lesson 7.6: Multiple Inheritance 🔗

## Description 📝

This lesson covers:

-   Multiple inheritance in Python
-   The diamond inheritance problem
-   Method Resolution Order (MRO)

This lesson includes a detailed theoretical explanation, 5 programming practical tasks, and 19 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand and implement multiple inheritance  
✅ Recognize and resolve the diamond inheritance problem  
✅ Use Method Resolution Order (MRO) to predict attribute lookup  
✅ Apply multiple inheritance to practical class hierarchies

## Concepts & Theory 🔍

### 🔹 Multiple Inheritance

-   **Purpose**: Allows a class to inherit from multiple parent classes.
-   **How It Works**: Combines attributes and methods from all parents, resolved via MRO.

### 🔹 The Diamond Inheritance Problem

-   **Purpose**: Addresses issues when a class inherits from multiple parents sharing a common base.
-   **Solution**: Python’s MRO ensures a consistent, linear order for method resolution.

### 🔹 Method Resolution Order (MRO)

-   **Purpose**: Defines the order in which Python searches for attributes in a class hierarchy.
-   **How It Works**: Uses the C3 linearization algorithm, accessible via `__mro__` or `mro()`.

## Practical Task 🧪

### 1️⃣ **Multiple Inheritance and MRO**

The lesson includes 5 practical tasks, each exploring multiple inheritance:

1. **Class Hierarchy (Task 1)**: Empty class structure.

    - `A` → `C`, `B`, `D` → `E` (inherits `B`, `D`).

2. **Class Hierarchy (Task 2)**: Complex empty class structure.

    - `H` → `D`, `E`, `F`, `G` → `B` (`D`, `E`), `C` (`F`, `G`) → `A` (`B`, `C`).

3. **`get_method_owner` Function**: Finds the class defining a method.

    - Takes `cls` and `method`, returns owning class or `None`.

4. **`FamilyPerson` Hierarchy**: Family roles with shared behavior.

    - `FamilyPerson` (abstract) → `Father`, `Mother`, `Daughter`, `Son`.

5. **`MROHelper` Class**: Static MRO utilities.
    - Methods: `len`, `class_by_index`, `index_by_class` for MRO introspection.

💡 These tasks demonstrate multiple inheritance, MRO, and hierarchy introspection.

## Benefits ✅

-   Multiple inheritance enables flexible, reusable class designs.
-   MRO ensures predictable attribute resolution in complex hierarchies.
-   Understanding the diamond problem prevents inheritance pitfalls.
-   Introspection tools simplify debugging and framework development.

## Output 📜

After completing this lesson, I now:  
✅ Implement multiple inheritance for complex class hierarchies  
✅ Use MRO to resolve method lookup and avoid diamond problem issues  
✅ Apply MRO introspection to practical scenarios like family roles

## Conclusion 🚀

Mastering multiple inheritance and MRO empowers me to design sophisticated class hierarchies in Python.  
From family role modeling to MRO utilities, these tools ensure clarity and flexibility in complex object-oriented systems. 🧑‍💻✨
