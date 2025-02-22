# Lesson 5.5: Memory Cleaning Mechanisms 🧹🖥️

## Description 📝

This lesson explains how **memory cleaning mechanisms** work in Python, including **reference counting**, **garbage collection**, and the `gc` module.

## Purpose 🎯

By the end of this lesson, I will:

-   Understand how Python manages memory automatically.
-   Learn about **reference counting** and its role in memory management.
-   Explore Python’s **garbage collector** and the `gc` module for manual control.

## How It Works 🔍

This lesson provides theoretical explanations and **14 questions** available on [Stepik](https://stepik.org/lesson/624149/step/1?unit=619837). Key topics include:

-   **Reference Counting** 🧮
    -   Each object in Python keeps track of how many references point to it.
    -   When the count drops to **zero**, Python automatically deletes the object.
-   **Garbage Collection** 🗑️
    -   Handles memory leaks caused by **cyclic references** (e.g., two objects referring to each other).
    -   Uses **generational garbage collection** to optimize memory cleanup.
-   **`gc` Module** 🔧
    -   Allows **manual control** over garbage collection.
    -   Functions like `gc.collect()` can **force** garbage collection when needed.

## Output 📜

After completing this lesson, I will be able to:  
✅ Explain how **Python cleans up unused memory**.  
✅ Use **reference counting** to track object lifetimes.  
✅ Understand **when and why Python’s garbage collector is needed**.  
✅ Utilize the `gc` module for **manual garbage collection control**.

## Conclusion 🚀

Python’s **memory management system** ensures efficient use of resources by automatically cleaning up unused objects. However, **understanding memory cleaning mechanisms** is essential for writing **efficient and bug-free code**!
