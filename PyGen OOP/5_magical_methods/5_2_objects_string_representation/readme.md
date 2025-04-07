# Lesson 5.2: String Representation of Objects 📜

## Description 📝

This lesson covers:

-   Functions **`str()`** and **`repr()`** in Python
-   Magic methods **`__str__()`** and **`__repr__()`**
-   Formal and informal string representations of objects
-   Practical implementation across various classes

Link to the lesson: [Stepik Lesson 5.2](https://stepik.org/lesson/805770/step/1?unit=808895)

This lesson includes a detailed theoretical explanation, 6 programming practical tasks, and 11 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the difference between **`str()`** and **`repr()`** functions  
✅ Implement **`__str__()`** and **`__repr__()`** magic methods for custom string representations  
✅ Learn to create formal (developer-friendly) and informal (user-friendly) object descriptions  
✅ Apply these concepts to real-world class examples for better object management

## Concepts & Theory 🔍

### 🔹 Functions **`str()`** and **`repr()`**

-   **`str()`**: Returns an informal, human-readable string representation of an object.
-   **`repr()`**: Returns a formal string representation, typically for debugging or recreating the object.

### 🔹 **`__str__()`** Magic Method

-   **Purpose**: Defines the informal string representation of an object, invoked by **`str()`** or **`print()`**.
-   **When Used**: To provide a user-friendly description of the object.

### 🔹 **`__repr__()`** Magic Method

-   **Purpose**: Defines the formal string representation, invoked by **`repr()`** or in debugging contexts.
-   **When Used**: To provide a detailed, unambiguous representation, ideally allowing object recreation.

### 🔹 Formal vs. Informal Representation

-   **Formal**: Aimed at developers, precise and technical (e.g., `ClassName(attr1, attr2)`).
-   **Informal**: Aimed at end-users, readable and concise (e.g., `A class with attr1 and attr2`).

## Practical Task 🧪

### 1️⃣ **String Representation Across Classes**

The lesson includes 6 practical tasks, each implementing string representation for a unique class:

1. **`Book` Class**: Represents a book with title, author, and year.

    - Ascending/descending triangle - `__repr__`: `Book('title', 'author', year)`
    - `__str__`: Readable book description.

2. **`Rectangle` Class**: Represents a rectangle with length and width.

    - `__repr__` & `__str__`: `Rectangle(length, width)`.

3. **`Vector` Class**: Represents a 2D vector with x and y coordinates.

    - `__repr__`: `Vector(x, y)`
    - `__str__`: `A vector on the plane with coordinates (x, y)`.

4. **`IPAddress` Class**: Represents an IP address from string or list input.

    - `__repr__`: Formal IP representation
    - `__str__`: Readable IP format.

5. **`PhoneNumber` Class**: Represents a 10-digit phone number.

    - `__repr__`: `PhoneNumber('dddddddddd')`
    - `__str__`: `(ddd) ddd-dddd`.

6. **`AnyClass` Class**: Dynamically accepts named arguments.
    - `__repr__`: `AnyClass(key1=value1, ...)`
    - `__str__`: `AnyClass: key1=value1, ...`.

💡 These tasks demonstrate how to tailor string representations for different use cases.

## Benefits ✅

-   **`__str__()`** provides user-friendly object descriptions.
-   **`__repr__()`** aids debugging with precise object details.
-   Custom string representations improve code readability and usability.
-   Flexible class designs enhance real-world applicability.

## Output 📜

After completing this lesson, I now:  
✅ Understand and implement **`__str__()`** and **`__repr__()`** for custom object representations  
✅ Differentiate between formal and informal string outputs  
✅ Apply string representation techniques to diverse practical examples

## Conclusion 🚀

Mastering string representation with **`__str__()`** and **`__repr__()`** is key to creating clear, maintainable Python objects.  
These magic methods enhance debugging, improve user interaction, and provide flexibility across applications, from simple data structures to complex systems. 🧑‍💻✨
