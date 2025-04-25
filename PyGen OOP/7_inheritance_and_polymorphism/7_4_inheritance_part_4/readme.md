# Lesson 7.4: Inheritance (Part 4) 🧬

## Description 📝

This lesson covers:

-   Inheritance from the `dict` type
-   Inheritance from the `list` type
-   Using `UserDict` and `UserList` from the `collections` module

This lesson includes a detailed theoretical explanation, 8 programming practical tasks, and 14 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Extend `dict` and `list` types with custom functionality  
✅ Use `UserDict` and `UserList` for safer, flexible subclassing  
✅ Implement specialized dictionaries and lists for practical use cases  
✅ Apply inheritance to enhance collection types

## Concepts & Theory 🔍

### 🔹 Inheritance from `dict` Type

-   **Purpose**: Extends dictionary behavior with custom methods or access patterns.
-   **Challenges**: Direct subclassing requires careful handling of internal state.

### 🔹 Inheritance from `list` Type

-   **Purpose**: Adds specialized functionality to lists, like custom indexing or operations.
-   **Challenges**: Must preserve list semantics while adding new behavior.

### 🔹 `UserDict` and `UserList` from `collections`

-   **Purpose**: Provide wrapper classes for safer, more flexible subclassing of `dict` and `list`.
-   **Benefits**: Simplify customization by managing internal storage and operations.

## Practical Task 🧪

### 1️⃣ **Custom Dictionaries and Lists**

The lesson includes 8 practical tasks, each implementing a specialized `dict` or `list` subclass:

1. **`DefaultList` Class**: Subclass of `UserList`.

    - Returns `default` value for out-of-bounds indices.

2. **`EasyDict` Class**: Subclass of `dict`.

    - Supports attribute-style access (`d.key`) alongside key access.

3. **`TwoWayDict` Class**: Subclass of `UserDict`.

    - Adds reverse `value:key` pairs for bidirectional lookups.

4. **`AdvancedList` Class**: Subclass of `list`.

    - Adds `join`, `map`, and `filter` methods for in-place operations.

5. **`NumberList` Class**: Subclass of `UserList`.

    - Restricts elements to numbers (`int`, `float`), raises `TypeError` otherwise.

6. **`ValueDict` Class**: Subclass of `dict`.

    - Provides `key_of` and `keys_of` for reverse value-to-key lookups.

7. **`BirthdayDict` Class**: Subclass of `UserDict`.

    - Notifies when a birthday matches an existing one.

8. **`MutableString` Class**: Subclass of `UserString`.
    - Supports mutable string operations with indexing and methods.

💡 These tasks demonstrate advanced customization of collection types.

## Benefits ✅

-   `UserDict` and `UserList` simplify safe subclassing.
-   Custom dictionaries and lists enhance functionality for specific needs.
-   Inheritance enables intuitive, specialized data structures.
-   Flexible designs support diverse applications like data validation and bidirectional mappings.

## Output 📜

After completing this lesson, I now:  
✅ Create custom `dict` and `list` subclasses using `UserDict` and `UserList`  
✅ Implement specialized collection behaviors like bidirectional dictionaries  
✅ Apply inheritance to practical scenarios like mutable strings and default lists

## Conclusion 🚀

Mastering inheritance from `dict` and `list` types, along with `UserDict` and `UserList`, empowers me to build tailored collection classes.  
From bidirectional dictionaries to mutable strings, these tools enable robust, intuitive data structures for advanced Python applications. 🧑‍💻✨
