# Lesson 6.3: Named Tuples (part 1) 🔹

## Description 📝

This lesson focuses on **named tuples**, which are a part of Python's **collections module**.
Named tuples are an **enhanced version of tuples** that provide **named fields** for better readability and maintainability.

## Purpose 🎯

By the end of this lesson, I will:

-   Understand the concept of **named tuples** and how they differ from regular tuples.
-   Learn to use the **collections module** to create and work with named tuples.
-   Be able to apply named tuples to improve the **clarity and structure** of my code.

## How It Works 🔍

Key topics covered in this lesson:

-   **Named Tuples (`namedtuple`)** 🔑

    -   A **tuple subclass** that assigns **names** to the elements of a tuple.
    -   The fields in a named tuple can be accessed by **name** instead of position, making the code more readable.
    -   Named tuples are **immutable** just like regular tuples but offer **field names** for clarity.
    -   Example:
        ```python
        from collections import namedtuple
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(10, 20)
        print(p.x, p.y)  # 10 20
        ```

-   **Benefits** 💡
    -   **Improved readability:** Named fields are easier to understand than index-based access.
    -   **Immutable and lightweight:** Like tuples, named tuples are immutable and take up less memory.
    -   **Access by name or index:** You can access the elements of a named tuple by name (`p.x`) or index (`p[0]`).

## Output 📜

After completing this lesson, I will have:  
✅ A deeper understanding of **named tuples**.  
✅ Knowledge of how to **use the collections module** to create and manipulate named tuples.  
✅ Improved my ability to write **more readable and maintainable code**.

## Conclusion 🚀

Named tuples are a **useful tool** for structuring data in a clear and organized way.
This lesson introduces me to their advantages, and as I progress, I will be able to apply them effectively in my projects.
