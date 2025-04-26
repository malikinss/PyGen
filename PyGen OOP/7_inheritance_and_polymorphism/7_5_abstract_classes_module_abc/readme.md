# Lesson 7.5: Abstract Classes and Module abc 📚

## Description 📝

This lesson covers:

-   Abstract classes in Python
-   The `abc` module for defining abstract base classes
-   The `collections.abc` module for collection-based abstract classes

This lesson includes a detailed theoretical explanation, 8 programming practical tasks, and 16 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand and create abstract classes using the `abc` module  
✅ Use `collections.abc` to implement collection-like interfaces  
✅ Enforce interface contracts with abstract methods  
✅ Apply abstract classes to practical scenarios like DNA sequences and chess pieces

## Concepts & Theory 🔍

### 🔹 Abstract Classes

-   **Purpose**: Define interfaces with methods that subclasses must implement.
-   **How They Work**: Prevent instantiation until all abstract methods are defined.

### 🔹 Module `abc`

-   **Purpose**: Provides tools like `ABC` and `@abstractmethod` for abstract classes.
-   **When Used**: To enforce method implementation in subclasses.

### 🔹 Module `collections.abc`

-   **Purpose**: Offers abstract base classes for collections (e.g., `Sequence`, `Mapping`).
-   **Benefits**: Ensures subclasses conform to collection interfaces with minimal code.

## Practical Task 🧪

### 1️⃣ **Abstract Class Implementations**

The lesson includes 8 practical tasks, each leveraging abstract classes:

1. **`Middle` Hierarchy**: Abstract base for average calculations.

    - Subclasses: `Average`, `Median`, `Harmonic` for rating computations.

2. **`ChessPiece` Hierarchy**: Abstract base for chess pieces.

    - Subclasses: `King`, `Knight` implement `can_move` for move validation.

3. **`Validator` Hierarchy**: Abstract descriptor for validation.

    - Subclasses: `Number` (range check), `String` (length/predicate check).

4. **`is_iterable`/`is_iterator` Functions**: Check iterable/iterator properties.

    - Use type checking for iteration protocol compliance.

5. **`CustomRange` Class**: Subclass of `Sequence`.

    - Handles mixed integer and range inputs for iteration and indexing.

6. **`BitArray` Class**: Subclass of `Sequence`.

    - Manages bit sequences with bitwise operations.

7. **`DNA` Class**: Subclass of `Sequence`.

    - Models DNA strands with complementarity and sequence operations.

8. **`SortedList` Class**: Subclass of `Sequence`.
    - Maintains sorted order with restricted modification methods.

💡 These tasks demonstrate abstract classes for enforcing interfaces and collection behaviors.

## Benefits ✅

-   Abstract classes ensure consistent subclass implementations.
-   `abc` module enforces interface contracts with minimal overhead.
-   `collections.abc` simplifies collection type customization.
-   Robust designs support extensible, type-safe applications.

## Output 📜

After completing this lesson, I now:  
✅ Create abstract classes with `abc` and `collections.abc`  
✅ Implement collection-like interfaces for sequences and validators  
✅ Apply abstract classes to practical use cases like chess and DNA modeling

## Conclusion 🚀

Mastering abstract classes and the `abc` and `collections.abc` modules empowers me to design robust, extensible interfaces.  
From chess move validation to sorted lists, these tools ensure type safety and consistency, enhancing Python applications. 🧑‍💻✨
