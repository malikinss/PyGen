# Lesson 7.3: Inheritance (Part 3) 🧬

## Description 📝

This lesson covers:

-   The process of creating class instances
-   Inheritance from immutable built-in data types (`int`, `float`, `str`, `tuple`)

This lesson includes a detailed theoretical explanation, 8 programming practical tasks, and 13 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to create instances of classes inheriting from immutable types  
✅ Extend built-in immutable types (`int`, `float`, `str`, `tuple`) with custom behavior  
✅ Apply inheritance to enhance functionality of immutable data types  
✅ Implement practical subclasses for specialized string, integer, and tuple operations

## Concepts & Theory 🔍

### 🔹 Process of Creating Class Instances

-   **Purpose**: Defines how objects are initialized and constructed.
-   **How It Works**: Involves `__new__()` for instance creation and `__init__()` for initialization.

### 🔹 Inheritance from Immutable Data Types

-   **Purpose**: Extends immutable types (`int`, `float`, `str`, `tuple`) with custom behavior.
-   **Challenges**: Immutability requires careful handling of instance creation and state.

## Practical Task 🧪

### 1️⃣ **Subclasses of Immutable Types**

The lesson includes 8 practical tasks, each implementing a subclass of an immutable built-in type:

1. **`UpperPrintString` Class**: Subclass of `str`.

    - Returns uppercase for informal string representation.

2. **`LowerString` Class**: Subclass of `str`.

    - Converts initial value to lowercase during instantiation.

3. **`FuzzyString` Class**: Subclass of `str`.

    - Case-insensitive comparisons and membership tests.

4. **`TitledText` Class**: Subclass of `str`.

    - Stores a title, accessible via `title` method.

5. **`SuperInt` Class**: Subclass of `int`.

    - Adds methods for repetition, binary conversion, and digit iteration.

6. **`RoundedInt` Class**: Subclass of `int`.

    - Rounds to nearest even or odd integer based on `even` parameter.

7. **`AdvancedTuple` Class**: Subclass of `tuple`.

    - Supports addition with any iterable, returns `AdvancedTuple`.

8. **`ModularTuple` Class**: Subclass of `tuple`.
    - Elements are remainders after division by `size`.

💡 These tasks demonstrate how to extend immutable types with custom functionality.

## Benefits ✅

-   Inheritance from immutable types preserves their reliability.
-   Custom subclasses add specialized behavior while maintaining type compatibility.
-   Enhanced immutable types support advanced data processing.
-   Understanding instance creation clarifies subclass design.

## Output 📜

After completing this lesson, I now:  
✅ Create subclasses of immutable built-in types  
✅ Extend `str`, `int`, and `tuple` with custom methods and behavior  
✅ Apply inheritance to practical use cases like case-insensitive strings and modular tuples

## Conclusion 🚀

Mastering inheritance from immutable data types empowers me to extend Python’s built-in types with tailored functionality.  
From case-insensitive strings to enhanced integers, these techniques enable robust, specialized data handling for diverse applications. 🧑‍💻✨
