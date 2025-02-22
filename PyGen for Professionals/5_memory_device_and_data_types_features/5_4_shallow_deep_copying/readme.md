# Lesson 5.4: Shallow and Deep Copying of Objects 📄🔁

## Description 📝

This lesson covers how to create **copies of objects** in Python, including the difference between **shallow and deep copies** and how the `copy` module helps in this process.

## Purpose 🎯

By the end of this lesson, I will:

-   Understand the need for copying objects in Python.
-   Learn about **shallow copies** and **deep copies**.
-   Use the `copy` module effectively to manage object duplication.

## How It Works 🔍

This lesson provides theoretical explanations and **12 questions** available on [Stepik](https://stepik.org/lesson/625739/step/1?unit=621492). Key topics include:

-   **Copying objects in Python**: Why direct assignment (`=`) does not create a real copy.
-   **Shallow copy** (`copy.copy()`)
    -   Copies references of nested objects, meaning changes in mutable sub-objects affect the copy.
-   **Deep copy** (`copy.deepcopy()`)
    -   Recursively copies all nested objects, ensuring full independence from the original.
-   **Practical use cases**: When to use shallow vs. deep copies in real-world scenarios.

## Output 📜

After completing this lesson, I will be able to:  
✅ Explain how object copying works in Python.  
✅ Correctly use `copy.copy()` and `copy.deepcopy()` when needed.  
✅ Avoid unintended side effects when copying mutable objects.

## Conclusion 🚀

Understanding **shallow and deep copies** is crucial when working with mutable objects in Python.
Using the right type of copy prevents unexpected modifications and ensures better memory management.
