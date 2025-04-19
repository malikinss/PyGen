Lesson 6.6: decorator @contextmanager

Decorator @contextmanager
Handling exceptions when using decorator @contextmanager
Examples of creating context managers using decorator @contextmanager
Abstract. This lesson is devoted to creating context managers using decorator @contextmanager.

https://stepik.org/lesson/934146/step/1?unit=940038

This lesson has good theory explonation, has 4 programing practical tasks and 15 theoretical questions presented on the website.

1. 6_6_1_make_tag

```
# make_tag Context Manager Tag Printer
The `make_tag` context manager, implemented using the `@contextmanager` decorator, accepts a single string argument `tag`.
It prints `tag` when entering a `with` block and again when exiting, wrapping the block’s execution with identical tag outputs.
The context manager yields control to the block, adhering to the context manager protocol.
Designed for scenarios requiring simple bracketing of code execution with markers, such as logging context boundaries, debugging block entry/exit, or formatting output in scripts.
Its lightweight design makes it suitable for quick annotations or educational examples of Python’s context manager protocol using `contextlib`.
```

2. 6_6_2_reversed_print

```
# reversed_print Context Manager Output Reverser
The `reversed_print` context manager, implemented using the `@contextmanager` decorator, takes no arguments.
It modifies `sys.stdout.write` within a `with` block to reverse the order of characters in any text written to standard output, restoring the original `write` method upon exit.
The context manager yields control to the block, adhering to the context manager protocol.
Designed for scenarios requiring temporary transformation of console output, such as creating stylized logs, debugging with reversed text for visual distinction, or experimenting with output formatting in scripts.
Its simplicity makes it suitable for quick modifications or educational examples of Python’s context manager protocol and `sys.stdout` manipulation.
```

3. 6_6_3_safe_write

```
# safe_write Context Manager Transactional File Writer
The `safe_write` context manager, implemented using the `@contextmanager` decorator, accepts a `filename` string and enables safe writing to the specified file.
It yields a file-like object for writing within a `with` block.
If an exception occurs during writing, it absorbs the exception, reverts the file to its original state by discarding changes, and prints a message: `An exception <exception type> was raised while writing to the file`.
The context manager ensures atomic writes using a temporary file, preserving the original file’s state on failure.
Designed for scenarios requiring robust file modifications, such as updating configuration files, logging, or saving data, where partial writes due to errors must be avoided.
Its ability to revert changes and report errors makes it suitable for reliable file operations in scripting, data pipelines, or educational examples of Python’s context manager protocol and atomic file handling.
```

4.

```

```
