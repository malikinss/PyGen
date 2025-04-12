# Lesson 5.10: Object Hashing (Part 2) 🔢

## Description 📝

This lesson covers:

-   Hashability and immutability in Python
-   Hashing custom classes
-   Magic method **`__hash__()`** for custom hash values
-   The hash-equal contract for consistent object behavior

This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and 11 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the relationship between hashability and immutability  
✅ Implement custom hashing for classes using **`__hash__()`**  
✅ Ensure the hash-equal contract for consistent object behavior  
✅ Apply hashing to create hashable objects for sets and dictionaries

## Concepts & Theory 🔍

### 🔹 Hashability and Immutability

-   **Purpose**: Hashable objects must be immutable to ensure consistent hash values.
-   **When Used**: In data structures like sets and dictionaries requiring stable keys.

### 🔹 Hashing Custom Classes

-   **Purpose**: Enables custom objects to be used in hash-based collections.
-   **How It Works**: Classes define hashing logic to produce unique identifiers.

### 🔹 **`__hash__()`** Magic Method

-   **Purpose**: Defines custom hash values for objects.
-   **When Used**: Invoked by `hash()` to compute an integer for collections.

### 🔹 Hash-Equal Contract

-   **Purpose**: Ensures consistency between equality and hashing.
-   **Rule**: If `a == b`, then `hash(a) == hash(b)`; unequal objects may have equal hashes.

## Practical Task 🧪

### 1️⃣ **Hashable Custom Classes**

The lesson includes 2 practical tasks, each implementing hashable objects:

1. **`ColoredPoint` Class**: Represents a 2D point with coordinates and color.

    - Read-only properties: `x`, `y`, `color`
    - `__repr__`: `ColoredPoint(x, y, 'color')`
    - Equality: Matches coordinates and color
    - Hash: Based on `(x, y, color)` tuple
    - Returns `NotImplemented` for invalid comparisons.

2. **`Row` Class**: Stores immutable named attributes.
    - `__repr__`: `Row(attr1=value1, ...)`
    - Immutability: Blocks attribute changes/deletions with `AttributeError`
    - Equality: Matches attribute names and values
    - Hash: Based on all attributes.

💡 These tasks demonstrate how to create immutable, hashable objects for reliable use in collections.

## Benefits ✅

-   Immutability ensures stable hash values for reliable hashing.
-   **`__hash__()`** enables custom objects in sets and dictionaries.
-   The hash-equal contract guarantees consistent behavior.
-   Hashable classes enhance data integrity in hash-based structures.

## Output 📜

After completing this lesson, I now:  
✅ Create immutable, hashable classes with **`__hash__()`**  
✅ Uphold the hash-equal contract for consistent equality and hashing  
✅ Apply hashing to practical examples like points and data records

## Conclusion 🚀

Mastering object hashing with **`__hash__()`** and immutability empowers me to build robust, hashable Python objects.  
From colored points to immutable records, these skills enable efficient use in sets, dictionaries, and beyond, ensuring data integrity and performance. 🧑‍💻✨
