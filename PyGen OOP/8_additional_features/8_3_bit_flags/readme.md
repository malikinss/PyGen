# Lesson 8.3: Bit Flags and Flag Class 🎌

## Description 📝

This lesson covers:

-   Bit flags in Python
-   The `Flag` class from the `enum` module
-   Bitwise operators (`|`, `&`, `^`, `~`)
-   Checking membership in flag combinations
-   The zero element in flags
-   Bit flag enhancements in Python 3.11

This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and 13 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand bit flags and their use in representing state combinations  
✅ Create flag enumerations with the `Flag` class  
✅ Use bitwise operators to manipulate flag combinations  
✅ Apply bit flags to practical scenarios like order tracking and movie genres

## Concepts & Theory 🔍

### 🔹 Bit Flags

-   **Purpose**: Represent multiple boolean states compactly using bits.
-   **How They Work**: Each flag is a power of 2, allowing combinations via bitwise operations.

### 🔹 `Flag` Class

-   **Purpose**: Extends `Enum` to support bit flag operations.
-   **Features**: Auto-assigned values and bitwise operator support.

### 🔹 Bitwise Operators (`|`, `&`, `^`, `~`)

-   **Purpose**: Combine or manipulate flag states.
-   **Operators**: Union (`|`), intersection (`&`), symmetric difference (`^`), inversion (`~`).

### 🔹 Checking Membership

-   **Purpose**: Verify if a flag is part of a combination.
-   **How It Works**: Uses `in` operator or bitwise `&` for testing.

### 🔹 The Zero Element

-   **Purpose**: Represents the absence of any flags.
-   **When Used**: Default state or empty combination.

### 🔹 Bit Flags in Python 3.11

-   **Purpose**: Introduce enhancements like improved string representation.
-   **Benefits**: Better usability and debugging for flag enumerations.

## Practical Task 🧪

### 1️⃣ **Flag Enumeration Implementations**

The lesson includes 2 practical tasks, each leveraging bit flags:

1. **`OrderStatus` Flag**: Tracks order progress.

    - Defines `ORDER_PLACED`, `PAYMENT_RECEIVED`, `SHIPPING_COMPLETE` with `auto()`.

2. **`MovieGenres` and `Movie` Classes**: Manages movie genres.
    - `MovieGenres` flags: `ACTION`, `COMEDY`, etc.; `Movie` stores name and genres.

💡 These tasks demonstrate bit flags for compact state management and membership testing.

## Benefits ✅

-   Bit flags efficiently represent multiple states in a single value.
-   `Flag` class simplifies bitwise operations with type safety.
-   Membership testing enables intuitive state queries.
-   Python 3.11 enhancements improve flag usability.

## Output 📜

After completing this lesson, I now:  
✅ Create flag enumerations with `Flag` for state combinations  
✅ Use bitwise operators to manage flag states  
✅ Apply bit flags to practical use cases like order and genre tracking

## Conclusion 🚀

Mastering bit flags and the `Flag` class empowers me to efficiently manage state combinations in Python.  
From order status tracking to movie genre classification, these tools provide compact, type-safe solutions for complex state management. 🧑‍💻✨
