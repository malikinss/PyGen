# Greeter Class Polite Context Manager

## Description 📝

The `Greeter` class is a context manager that takes a single argument, `name` (a string), during instantiation.
It stores `name` as an attribute and implements the context manager protocol with `__enter__` and `__exit__` methods.
Upon entering a `with` block, it prints `Hello, <name>!`, and upon exiting, it prints `See you there, <name>!`, providing a greeting and farewell around the block’s execution.

## Purpose 🎯

Intended for scenarios requiring structured user interaction, such as command-line interfaces, logging user sessions, or scripted dialogues in applications.
It ensures consistent entry/exit messaging, making it useful for user-facing tools or as an educational example of Python’s context manager protocol.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `name` (string) and assigns it to `self.name`, making it accessible as an attribute.
-   **Enter Method (`__enter__`)**:
    -   Prints `Hello, <name>!` using an f-string with `self.name`.
    -   Returns `self`, adhering to the context manager protocol, though the return value is typically unused here.
-   **Exit Method (`__exit__`)**:
    -   Accepts `*args` (for exception details: `exc_type`, `exc_value`, `traceback`) and `**kwargs` for flexibility.
    -   Prints `See you there, <name>!` using `self.name`.
    -   Returns `None` implicitly, allowing any exceptions to propagate, as suppression isn’t required.
-   **Behavior**:
    -   Greets before the `with` block executes.
    -   Farewells after the block, regardless of exceptions.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**: `g = Greeter("Alice")` sets `g.name == "Alice"`.
-   **Greeting**: `with Greeter("Alice"): pass` prints:
    ```
    Hello, Alice!
    See you there, Alice!
    ```
-   **Context Management**: Works in `with` blocks, executing code between messages.
-   **Exceptions**: If an exception occurs, it propagates after printing farewell.
-   **Attribute**: `g.name` is accessible and correct.

## Potential Considerations 🛠️

-   **Correctness**: Prints exact messages with `name`, handles protocol correctly.
-   **Performance**: Minimal overhead with simple print operations.
-   **Design**: Flexible `*args, **kwargs` in `__exit__` ensures compatibility; no exception handling needed per task.

## Usage Example (For Clarity, Not Submission) 📦

```python
with Greeter("Bob"):
    print("Doing stuff")  # Prints:
# Hello, Bob!
# Doing stuff
# See you there, Bob!

g = Greeter("Alice")
print(g.name)  # Alice
```

## Conclusion 🚀

The `Greeter` implementation is precise, fulfilling the context manager role with correct greeting and farewell messages.
It’s ready for user interaction tasks or protocol demonstrations, fully compliant with the specification.
