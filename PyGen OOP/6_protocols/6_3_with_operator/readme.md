# Lesson 6.3: With Operator 🔒

## Description 📝

This lesson covers:

-   Resource management in Python
-   The `with` operator for context management
-   Practical implementation of file handling with context managers

This lesson includes a detailed theoretical explanation, 3 programming practical tasks, and 11 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand resource management using the `with` operator  
✅ Implement context managers for safe file handling  
✅ Apply the `with` operator to manage resources in practical scenarios  
✅ Recognize the benefits of automatic resource cleanup

## Concepts & Theory 🔍

### 🔹 Resource Management in Python

-   **Purpose**: Ensures resources (e.g., files, connections) are properly acquired and released.
-   **How It Works**: Context managers automate setup and cleanup, preventing leaks.

### 🔹 `with` Operator

-   **Purpose**: Simplifies resource management by encapsulating setup and teardown.
-   **When Used**: With objects implementing `__enter__()` and `__exit__()` methods, like files, to ensure cleanup even if errors occur.

## Practical Task 🧪

### 1️⃣ **File Handling with `with`**

The lesson includes 3 practical tasks, each implementing resource management with the `with` operator:

1. **`print_file_content` Function**: Displays a text file’s contents.

    - Reads `filename` using UTF-8, prints "File not found" if absent.

2. **`non_closed_files` Function**: Filters open file objects.

    - Returns a list of open files from a given list, preserving order.

3. **`log_for` Function**: Extracts log events for a specific date.
    - Creates `log_for_<date_str>.txt` with matching events from `logfile`, omitting date prefix.

💡 These tasks demonstrate safe file handling and resource management using the `with` operator.

## Benefits ✅

-   The `with` operator ensures resources are closed automatically.
-   Context managers simplify error-prone resource handling.
-   Safe file operations prevent leaks and improve reliability.
-   Clear error handling enhances user experience in file tasks.

## Output 📜

After completing this lesson, I now:  
✅ Use the `with` operator for safe resource management  
✅ Implement file handling with context managers  
✅ Apply resource cleanup to practical file processing tasks

## Conclusion 🚀

Mastering the `with` operator and context managers enables me to manage resources safely and efficiently in Python.  
From reading files to filtering logs, these tools ensure robust, leak-free code, enhancing reliability in file-based applications. 🧑‍💻✨
