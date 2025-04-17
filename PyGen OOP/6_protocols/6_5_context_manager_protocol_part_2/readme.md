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

8.

```

```

9.

```

```

10.

```

```

11.

```

```

12.

```

```
