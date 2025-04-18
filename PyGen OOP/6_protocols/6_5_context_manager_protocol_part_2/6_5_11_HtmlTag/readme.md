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

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Accepts `tag` (string, e.g., "p") and `inline` (boolean).
    -   Stores `tag` as `self.tag` and `inline` as `self.inline`.
    -   Initializes `_tag_indent` as an empty string, later set based on nesting level.
-   **Class Attribute**:
    -   `level`: A class-level integer tracking nesting depth, initialized to `-1` and incremented per context entry.
-   **Enter Method (`__enter__`)**:
    -   Increments `HtmlTag.level` to track nesting.
    -   Sets `self._tag_indent` to `"  " * HtmlTag.level` (two spaces per level).
    -   Prints the opening tag `<tag>` with `self._tag_indent` prefix.
    -   For `inline=True`, suppresses newline (`end=''`); otherwise, adds newline.
    -   Returns `self` for access to the `print` method.
-   **Exit Method (`__exit__`)**:
    -   Accepts `exc_type`, `exc_value`, and `traceback` for protocol compliance.
    -   For `inline=True`, prints `</tag>` without indentation.
    -   For `inline=False`, prints `</tag>` with `self._tag_indent`.
    -   Decrements `HtmlTag.level` to reflect exiting the context.
-   **Print Method (`print`)**:
    -   Takes `text` (string content).
    -   For `inline=True`, prints `text` without indentation or newline (`end=''`).
    -   For `inline=False`, prints `text` with indentation (`self._tag_indent + "  "`) and newline.
-   **Behavior**:
    -   Ensures two-space indentation per nesting level for non-inline formatting.
    -   Supports nested tags via `level` tracking, maintaining correct hierarchy.
    -   Handles inline and block formatting consistently.

## Verification ✅

Implementation satisfies requirements:

-   **Inline Formatting**:
    -   `with HtmlTag("p", inline=True) as t: t.print("Text")` outputs:
    ```
    <p>Text</p>
    ```
-   **Block Formatting**:
    -   `with HtmlTag("p") as t: t.print("Text")` outputs:
    ```
    <p>
      Text
    </p>
    ```
-   **Nesting**:
    -   Nested `with HtmlTag("div"): with HtmlTag("p"): t.print("Text")` outputs:
    ```
    <div>
      <p>
        Text
      </p>
    </div>
    ```
-   **Reentrancy**: Multiple nested or sequential `with` blocks maintain correct indentation and tag closure.
-   **Protocol**: `__enter__` and `__exit__` enable `with` statement usage.

## Potential Considerations 🛠️

-   **Correctness**: Class-level `level` ensures consistent nesting across instances; indentation logic is precise.
-   **Performance**: String operations and printing are O(1) per call, suitable for typical HTML generation.
-   **Design**: `inline` toggle and dynamic indentation via `level` provide flexibility, aligning with arbitrary protocol implementation.

## Usage Example (For Clarity, Not Submission) 📦

```python
with HtmlTag("p") as t:
    t.print("Hello")  # <p>\n  Hello\n</p>
with HtmlTag("div", inline=True) as t:
    t.print("Inline")  # <div>Inline</div>
with HtmlTag("outer"):
    with HtmlTag("inner") as t:
        t.print("Nested")  # <outer>\n  <inner>\n    Nested\n  </inner>\n</outer>
```

## Conclusion 🚀

The `HtmlTag` implementation is robust, generating correctly formatted HTML with proper nesting and indentation.
It’s ideal for HTML generation tasks or protocol education, fully compliant with the task’s requirements.
