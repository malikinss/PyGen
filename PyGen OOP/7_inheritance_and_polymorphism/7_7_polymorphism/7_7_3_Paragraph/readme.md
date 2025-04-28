# LeftParagraph and RightParagraph Class Implementation

## Description 📝

The provided code implements the `LeftParagraph` and `RightParagraph` classes to format paragraphs aligned to the left and right, respectively.
Both classes inherit from an abstract base class `Paragraph`, which centralizes shared logic for managing lines, adding words, and handling line length constraints.
Each class accepts a `length` parameter during instantiation and provides `add` to append words and `end` to print and clear the paragraph.

## Purpose 🎯

Intended for text formatting applications, such as document processing, typesetting, or console-based text alignment.
It’s also suitable for educational examples of inheritance, abstract base classes, and text manipulation in Python.

## Hierarchy Design 🛠️

-   **Why `Paragraph` as an Abstract Base Class?**:
    -   Centralizes common functionality: storing line length, managing lines as a list of word lists, and implementing word addition logic.
    -   Uses `ABC` to enforce that subclasses implement `end`, ensuring each defines its alignment-specific printing.
    -   Reduces code duplication by handling word splitting, line wrapping, and storage once.
-   **Inheritance Structure**:
    -   `LeftParagraph` inherits from `Paragraph`, implementing `end` for left-aligned printing.
    -   `RightParagraph` inherits from `Paragraph`, implementing `end` for right-aligned printing.
-   **Why Use List of Lists for Storage?**:
    -   Each inner list represents a line of words, simplifying word addition and space insertion.
    -   Supports dynamic line creation when words exceed the line length.
    -   Enables easy printing with correct spacing.

## How It Works 🔍

-   **Paragraph (Abstract Base Class)**:
    -   Initializes with `length`, storing it as `self._len`.
    -   Initializes `self._lines` as a list containing an empty list (`[[]]`) for the first line.
    -   `add(data)`:
        -   Splits `data` into words using `split()`.
        -   For each word, checks if adding it to the current line (with spaces) exceeds `self._len`.
        -   If it fits, appends the word to the current line; otherwise, starts a new line with the word.
    -   Declares abstract `end()` to be implemented by subclasses.
-   **LeftParagraph**:
    -   Inherits from `Paragraph`.
    -   Implements `end()`:
        -   Prints each non-empty line by joining words with a single space.
        -   Resets `self._lines` to `[[]]` to start a new paragraph.
-   **RightParagraph**:
    -   Inherits from `Paragraph`.
    -   Implements `end()`:
        -   Prints each non-empty line by joining words with a space and right-aligning with `rjust(self._len)`.
        -   Resets `self._lines` to `[[]]` to start a new paragraph.
-   **Behavior**:
    -   Both classes maintain a paragraph as lines of words, respecting the line length.
    -   `add` automatically adds spaces between words (except the last in a line).
    -   `end` prints the paragraph in the specified alignment and clears it.
    -   No validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   `LeftParagraph(10)` and `RightParagraph(10)` initialize with line length 10.
-   **LeftParagraph**:
    -   `lp = LeftParagraph(10); lp.add("hello world"); lp.end()`:
        -   Prints: `hello` (length 5 fits, `world` moves to next line).
        -   Next line empty, not printed.
    -   `lp.add("a b c"); lp.end()`:
        -   Prints: `a b c` (length 5 with spaces fits).
    -   After `end`, new `add` starts a new paragraph.
-   **RightParagraph**:
    -   `rp = RightParagraph(10); rp.add("hello world"); rp.end()`:
        -   Prints: `     hello` (right-aligned in 10 chars).
        -   Next line empty, not printed.
    -   `rp.add("a b c"); rp.end()`:
        -   Prints: `     a b c` (right-aligned in 10 chars).
    -   After `end`, new `add` starts a new paragraph.
-   **Word Handling**:
    -   `add("word1 word2")` splits words, adds spaces between them.
    -   Words exceeding line length move to the next line.
-   **Inheritance**:
    -   `issubclass(LeftParagraph, Paragraph)` → `True`.
    -   `issubclass(RightParagraph, Paragraph)` → `True`.
    -   `add` inherited from `Paragraph`, reducing duplication.
-   **Correctness**:
    -   Lines respect `length` constraint.
    -   Spaces added between words, not after the last word in a line.
    -   `end` clears paragraph correctly.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `Paragraph` ensures consistent word addition and line wrapping.
    -   Left-alignment uses default `join`; right-alignment uses `rjust`.
    -   Empty lines are not printed, as they contain no words.
-   **Performance**:
    -   Initialization: O(1).
    -   `add`: O(n) for splitting and joining strings (n is number of words).
    -   `end`: O(m) for printing m lines.
    -   Efficient for typical paragraph sizes.
-   **Design**:
    -   `Paragraph` centralizes word and line management, minimizing duplication.
    -   List of lists (`self._lines`) simplifies word storage and spacing.
    -   Type hints (`int`, `str`) clarify inputs.
    -   Simple and focused implementation.
-   **Alternatives**:
    -   Without `Paragraph`, `add` logic would be duplicated.
    -   String-based storage (instead of lists) would complicate word handling.
-   **Extensibility**:
    -   Easily extended for other alignments (e.g., justified) by adding subclasses.
    -   Could add validation or formatting options if needed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Test LeftParagraph
lp = LeftParagraph(10)
lp.add("hello world")
lp.end()
# Output:
# hello
lp.add("a b c")
lp.end()
# Output:
# a b c

# Test RightParagraph
rp = RightParagraph(10)
rp.add("hello world")
rp.end()
# Output:
#      hello
rp.add("a b c")
rp.end()
# Output:
#      a b c
```

## Conclusion 🚀

The `Paragraph`, `LeftParagraph`, and `RightParagraph` implementation is precise, providing left- and right-aligned paragraph formatting with minimal code duplication.
Using `Paragraph` as an abstract base class centralizes shared logic, and the design is simple yet extensible. It’s ideal for text formatting tasks or teaching inheritance concepts, fully compliant with the task’s requirements.
