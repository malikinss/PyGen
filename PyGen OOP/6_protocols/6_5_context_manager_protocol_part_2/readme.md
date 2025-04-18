Lesson 6.5: context manager protocol (part 2)

Examples of creating context managers
Single-use, reusable and reentrant context managers
Abstract. The lesson is devoted to the context manager protocol.

https://stepik.org/lesson/933767/step/1?unit=939666

This lesson has good theory explonation, has 12 programing practical tasks and 4 theoretical questions presented on the website.

1. 6_5_1_SuppressAll

```
# SuppressAll Class Exception Silencer (Revised)
The `SuppressAll` class implements a context manager that suppresses all exceptions raised within its `with` block.
It accepts no arguments during instantiation and fulfills the context manager protocol through `__enter__` and `__exit__` methods.
Exceptions occurring in the block are caught and suppressed, allowing execution to proceed uninterrupted.
Intended for scenarios where exceptions can be safely ignored, such as non-critical operations, fallback mechanisms, or testing setups expecting failures.
It streamlines error handling in scripts and serves as a clear example for learning Python’s context manager protocol.
```

2. 6_5_2_Greeter

```
# Greeter Class Polite Context Manager
The `Greeter` class is a context manager that takes a single argument, `name` (a string), during instantiation.
It stores `name` as an attribute and implements the context manager protocol with `__enter__` and `__exit__` methods.
Upon entering a `with` block, it prints `Hello, <name>!`, and upon exiting, it prints `See you there, <name>!`, providing a greeting and farewell around the block’s execution.
Intended for scenarios requiring structured user interaction, such as command-line interfaces, logging user sessions, or scripted dialogues in applications.
It ensures consistent entry/exit messaging, making it useful for user-facing tools or as an educational example of Python’s context manager protocol.
```

3. 6_5_3_Closer

```
# Closer Class Resource Cleanup Manager
The `Closer` class is a context manager that takes an arbitrary object `obj` during instantiation.
It implements the context manager protocol with `__enter__` and `__exit__` methods.
Upon exiting a `with` block, it attempts to call `obj.close()`.
If the object lacks a `close` method, it prints "Unclosed object".
The class ensures proper resource cleanup for objects supporting `close`, such as file handles or sockets.
Intended for managing resources that require explicit closure, such as files, database connections, or network sockets, in a `with` block.
It provides a unified way to ensure cleanup while handling non-closable objects gracefully, suitable for resource-heavy applications, scripting, or educational demonstrations of Python’s context manager protocol.
```

4. 6_5_4_ReadableTextFile

```
# ReadableTextFile Class Line-Stripping File Reader

## Description 📝

The `ReadableTextFile` class is a context manager that opens a text file specified by `filename` for reading in UTF-8 encoding.
It provides access to file lines without trailing newline characters (`\n`) via iteration and closes the file after the `with` block.
The class implements the context manager protocol with `__enter__` and `__exit__` methods and supports iteration with `__iter__` and `__next__` to yield stripped lines.

## Purpose 🎯

Designed for reading text files in a controlled manner, such as processing logs, configuration files, or data inputs where newline characters are unwanted.
The context manager ensures proper file closure, making it suitable for scripting, data parsing, or educational examples of Python’s context manager and iterator protocols.
```

5. 6_5_5_Reloopable

```
# Reloopable Class Re-Iterable File Manager

## Description 📝

The `Reloopable` class is a context manager that accepts a file object open for reading (`file`) during instantiation.
It enables multiple iterations over the file’s contents within a `with` block by resetting the file pointer and closes the file upon exiting the block.
The class implements the context manager protocol with `__enter__` and `__exit__` methods and supports iteration via `__iter__`.

## Purpose 🎯

Intended for scenarios requiring repeated iteration over a file’s contents without reopening, such as parsing logs multiple times, analyzing data in passes, or testing file processing.
The automatic file closure ensures resource cleanup, making it suitable for scripting, data processing, or educational examples of Python’s context manager and iterator protocols.
```

6. 6_5_6_UpperPrint

```
# UpperPrint Class Uppercase Output Transformer

## Description 📝

The `UpperPrint` class is a context manager that takes no arguments during instantiation.
It modifies `sys.stdout.write` within a `with` block to convert all text output to uppercase, restoring the original `write` method upon exit.
The class implements the context manager protocol with `__enter__` and `__exit__` methods, ensuring seamless integration with standard output operations.

## Purpose 🎯

Intended for scenarios requiring temporary modification of console output, such as formatting logs, debugging with emphasized text, or creating stylized command-line interfaces.
It’s also valuable for educational purposes, demonstrating Python’s context manager protocol and manipulation of `sys.stdout`.
```

7. 6_5_7_Suppress

```
# Suppress Class Selective Exception Silencer

## Description 📝

The `Suppress` class is a context manager that accepts an arbitrary number of exception types as positional arguments during instantiation.
It suppresses exceptions of the specified types raised within a `with` block, storing the suppressed exception in its `exception` attribute (set to `None` if no exception is suppressed or no exception occurs).
The class implements the context manager protocol with `__enter__` and `__exit__` methods.

## Purpose 🎯

Designed for scenarios requiring targeted exception handling, such as ignoring specific errors in data processing, testing, or user input validation, while preserving others.
The `exception` attribute enables post-block inspection of suppressed errors, making it useful for logging or debugging.
It also serves as an educational tool for Python’s context manager protocol and exception handling.
```

8. 6_5_8_WriteSpy

```
# WriteSpy Class Dual File Writer

## Description 📝

The `WriteSpy` class is a context manager that accepts two file objects (`file1`, `file2`) and a boolean `to_close` (defaulting to `False`) during instantiation.
It enables simultaneous writing to both files within a `with` block, optionally closing them upon exit based on `to_close`.
The class provides methods `write` (writes text to both files), `close` (closes both files), `writable` (checks if both files are writable), and `closed` (checks if both files are closed).
It implements the context manager protocol with `__enter__` and `__exit__` methods.

## Purpose 🎯

Designed for scenarios requiring mirrored writes to multiple files, such as logging to dual destinations, creating redundant backups, or synchronizing outputs.
The ability to control file closure and check file states makes it suitable for resource management in scripting, logging systems, or educational demonstrations of Python’s context manager protocol and file handling.
```

9. 6_5_9_Atomic

```
# Atomic Class Transactional Data Manager

## Description 📝

The `Atomic` class is a context manager that enables atomic operations on a list, set, or dictionary (`data`), with a boolean `deep` parameter (defaulting to `False`).
It ensures that modifications within a `with` block are either fully applied (if no exceptions occur) or discarded (if an exception is raised), restoring the original state.
The `deep` parameter controls whether nested structures are also restored: `False` preserves nested changes, while `True` reverts them.
The class implements the context manager protocol with `__enter__` and `__exit__` methods.

## Purpose 🎯

Designed for scenarios requiring transactional updates to collections, such as configuration management, database-like operations, or undoable edits in applications.
The ability to control nested structure behavior makes it versatile for complex data, suitable for robust scripting, data processing, or educational demonstrations of Python’s context manager protocol and copy mechanics.
```

10. 6_5_10_AdvancedTimer

```
# AdvancedTimer Class Execution Time Tracker

## Description 📝

The `AdvancedTimer` class is a reusable context manager that measures the execution time of code within `with` blocks.
It takes no arguments during instantiation and implements the context manager protocol with `__enter__` and `__exit__` methods.
The class maintains four attributes: `last_run` (time of the most recent block), `runs` (list of all block times), `min` (minimum time across blocks), and `max` (maximum time across blocks).
If no measurements have been made, `last_run`, `min`, and `max` are `None`.

## Purpose 🎯

Intended for performance profiling, benchmarking, or debugging where precise timing of code blocks is needed, such as optimizing algorithms, measuring API response times, or comparing function performance.
The reusable nature and detailed statistics make it suitable for iterative testing or educational demonstrations of Python’s context manager protocol and timing utilities.
```

11. 6_5_11_HtmlTag

```
# HtmlTag Class Structured HTML Generator

## Description 📝

The `HtmlTag` class is a reentrant context manager that generates HTML code with proper indentation and tag nesting.
It accepts a `tag` (HTML tag name) and an optional `inline` boolean (defaulting to `False`) during instantiation.
Within a `with` block, it prints opening and closing tags, and its `print` method outputs content.
The `inline` parameter determines formatting: `True` places tags and content on the same line, while `False` uses separate lines with two-space indentation per nesting level.
The class implements the context manager protocol with `__enter__` and `__exit__` methods.

## Purpose 🎯

Designed for generating structured HTML in scripts, templates, or web development tools, ensuring correct tag nesting and formatting.
Its reentrant nature supports nested tags, making it suitable for dynamic HTML generation, static site builders, or educational examples of Python’s context manager protocol and indentation logic.
```

12.

```

```
