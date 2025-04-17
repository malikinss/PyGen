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

3.

```

```

4.

```

```

5.

```

```

6.

```

```

7.

```

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
