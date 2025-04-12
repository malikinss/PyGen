# Lesson 5.9: Object Hashing (Part 1) 🔢

## Description 📝

This lesson covers:

-   Hashing and its role in Python
-   Applications of hashing in data structures
-   Built-in function **`hash()`**
-   Narrowing the range of hash values
-   Characteristics of a good hash function
-   Creating custom hash functions

This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and 21 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the concept of hashing and its applications  
✅ Use the built-in **`hash()`** function effectively  
✅ Create custom hash functions with specific properties  
✅ Apply hashing techniques to constrain hash values within a range

## Concepts & Theory 🔍

### 🔹 Hashing

-   **Purpose**: Maps data to a fixed-size value (hash) for efficient storage and retrieval.
-   **When Used**: In dictionaries, sets, and other data structures for quick lookups.

### 🔹 Applications of Hashing

-   **Purpose**: Enables fast data access, uniqueness checks, and data integrity verification.
-   **Examples**: Hash tables, caching, checksums, and object identification.

### 🔹 Built-in **`hash()`** Function

-   **Purpose**: Computes a hash value for hashable objects.
-   **When Used**: To generate consistent identifiers for objects in sets or dictionaries.

### 🔹 Narrowing the Range of Hash Values

-   **Purpose**: Restricts hash outputs to a specific range for constrained applications.
-   **How It Works**: Transforms hash values to fit within defined bounds while preserving distribution.

### 🔹 Characteristics of a Good Hash Function

-   **Purpose**: Ensures efficiency and reliability in hashing.
-   **Traits**: Deterministic, uniform distribution, minimal collisions, and fast computation.

### 🔹 Creating Your Own Hash Function

-   **Purpose**: Customizes hashing for specific needs or constraints.
-   **When Used**: When built-in hashing is insufficient or specialized behavior is required.

## Practical Task 🧪

### 1️⃣ **Custom Hashing Functions**

The lesson includes 2 practical tasks, each implementing a unique hashing approach:

1. **`hash_function` Function**: Computes a custom hash for any object.

    - Uses string representation, combining symmetric character pairing and alternating weighted sums.
    - Returns integer modulo `123456791` for consistency.

2. **`limited_hash` Function**: Maps hash values to a specified range `[left, right]`.
    - Accepts optional `hash_function` (defaults to `hash`).
    - Cyclically transforms out-of-range values to fit within bounds.

💡 These tasks demonstrate how to design and constrain hash functions for practical use.

## Benefits ✅

-   Hashing enables efficient data structures like dictionaries and sets.
-   Custom hash functions provide flexibility for specialized needs.
-   Range-bound hashing ensures compatibility with constrained systems.
-   Understanding hashing improves performance in data-intensive applications.

## Output 📜

After completing this lesson, I now:  
✅ Understand hashing and its applications in Python  
✅ Implement custom hash functions with unique algorithms  
✅ Constrain hash values to specific ranges for targeted use cases

## Conclusion 🚀

Mastering object hashing unlocks efficient data handling in Python.  
From crafting custom hash algorithms to fitting values within specific ranges, these skills enhance performance and flexibility, powering everything from hash tables to unique identifiers. 🧑‍💻✨
