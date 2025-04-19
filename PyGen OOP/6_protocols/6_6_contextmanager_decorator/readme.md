# Lesson 6.6: Decorator @contextmanager 🔧

## Description 📝

This lesson covers:

-   The `@contextmanager` decorator from `contextlib`
-   Handling exceptions when using `@contextmanager`
-   Examples of creating context managers with `@contextmanager`

This lesson includes a detailed theoretical explanation, 4 programming practical tasks, and 15 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to create context managers using `@contextmanager`  
✅ Handle exceptions effectively in context manager functions  
✅ Apply `@contextmanager` to simplify context management in practical scenarios  
✅ Build lightweight context managers for file operations and output control

## Concepts & Theory 🔍

### 🔹 `@contextmanager` Decorator

-   **Purpose**: Simplifies context manager creation using generator functions.
-   **How It Works**: Wraps a generator yielding once, mapping to `__enter__()` and `__exit__()`.

### 🔹 Handling Exceptions with `@contextmanager`

-   **Purpose**: Ensures proper exception handling within context managers.
-   **How It Works**: Exceptions are passed to the generator, which can suppress or handle them using `try`/`except`.

### 🔹 Examples of `@contextmanager`

-   **Purpose**: Demonstrate practical context manager use cases.
-   **Examples**: File operations, output modification, and tagged execution blocks.

## Practical Task 🧪

### 1️⃣ **Context Managers with `@contextmanager`**

The lesson includes 4 practical tasks, each implementing a context manager using `@contextmanager`:

1. **`make_tag` Context Manager**: Prints a tag on entry and exit.

    - Accepts `tag` string, wraps block with tag outputs.

2. **`reversed_print` Context Manager**: Reverses console output text.

    - Modifies `sys.stdout.write` to reverse characters, restores on exit.

3. **`safe_write` Context Manager**: Ensures atomic file writes.

    - Reverts file on exception, reports error, uses temporary file.

4. **`safe_open` Context Manager**: Safely opens files.
    - Yields `(file_object, None)` or `(None, exception)`, closes file.

💡 These tasks showcase lightweight, robust context managers for output and file handling.

## Benefits ✅

-   `@contextmanager` simplifies context manager implementation.
-   Exception handling ensures reliable resource management.
-   Lightweight generator-based context managers reduce boilerplate.
-   Flexible designs support diverse use cases like safe file I/O.

## Output 📜

After completing this lesson, I now:  
✅ Create context managers using `@contextmanager`  
✅ Handle exceptions in generator-based context managers  
✅ Apply `@contextmanager` to practical tasks like file operations

## Conclusion 🚀

Mastering the `@contextmanager` decorator enables me to create efficient, elegant context managers with minimal code.  
From safe file operations to output transformations, these tools streamline resource management, enhancing code reliability and clarity. 🧑‍💻✨
