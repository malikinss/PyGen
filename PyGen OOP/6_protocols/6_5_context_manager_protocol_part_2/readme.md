# Lesson 6.5: Context Manager Protocol (Part 2) 🔐

## Description 📝

This lesson covers:

-   Examples of creating context managers
-   Single-use, reusable, and reentrant context managers
-   Practical implementation of advanced context management

This lesson includes a detailed theoretical explanation, 12 programming practical tasks, and 4 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Create single-use, reusable, and reentrant context managers  
✅ Implement advanced context managers for diverse use cases  
✅ Understand how to manage resources and state with context managers  
✅ Apply context management to practical scenarios like file handling and HTML generation

## Concepts & Theory 🔍

### 🔹 Examples of Creating Context Managers

-   **Purpose**: Provide structured setup and cleanup for resources or state.
-   **How It Works**: Use `__enter__()` and `__exit__()` to define context behavior.

### 🔹 Single-Use Context Managers

-   **Purpose**: Designed for one-time use, often for simple resources.
-   **Examples**: Temporary file operations or one-off exception suppression.

### 🔹 Reusable Context Managers

-   **Purpose**: Support multiple `with` block uses without reinstantiation.
-   **Examples**: Timers or output formatters that track state across calls.

### 🔹 Reentrant Context Managers

-   **Purpose**: Allow nested `with` blocks for the same instance.
-   **Examples**: HTML tag generators or tree builders with nested structures.

## Practical Task 🧪

### 1️⃣ **Advanced Context Managers**

The lesson includes 12 practical tasks, each implementing a unique context manager:

1. **`SuppressAll` Class**: Suppresses all exceptions in a `with` block.
2. **`Greeter` Class**: Prints greeting/farewell messages with a name.
3. **`Closer` Class**: Calls `close()` on an object, handles non-closable objects.
4. **`ReadableTextFile` Class**: Reads text file lines without newlines, closes file.
5. **`Reloopable` Class**: Enables multiple iterations over a file, closes on exit.
6. **`UpperPrint` Class**: Converts console output to uppercase temporarily.
7. **`Suppress` Class**: Suppresses specified exception types, tracks suppressed errors.
8. **`WriteSpy` Class**: Writes to two files simultaneously, optional closure.
9. **`Atomic` Class**: Ensures atomic updates to collections, supports deep reversion.
10. **`AdvancedTimer` Class**: Tracks execution times with detailed statistics.
11. **`HtmlTag` Class**: Generates indented HTML tags, supports nesting.
12. **`TreeBuilder` Class**: Builds nested list trees with node management.

💡 These tasks demonstrate the versatility of context managers for resource management, output control, and data structuring.

## Benefits ✅

-   Context managers simplify resource setup and cleanup.
-   Reusable and reentrant designs enhance flexibility.
-   Custom context managers handle exceptions and state elegantly.
-   Broad applicability improves code reliability across domains.

## Output 📜

After completing this lesson, I now:  
✅ Create single-use, reusable, and reentrant context managers  
✅ Implement context managers for files, output, and data structures  
✅ Apply advanced context management to practical use cases

## Conclusion 🚀

Mastering the context manager protocol with reusable and reentrant designs empowers me to build robust, efficient Python code.  
From exception suppression to HTML generation and tree building, these tools ensure clean resource handling and structured logic for complex applications. 🧑‍💻✨
