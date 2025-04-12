# Ord Class Unicode Accessor

## Description 📝

The `Ord` class serves as an alternative interface to Python’s built-in `ord()` function, designed to return the Unicode code point of a single-character attribute name when accessed.
It requires no arguments during instantiation and dynamically handles attribute requests, providing the Unicode value for valid single-character names or raising an `AttributeError` for invalid ones.

## Purpose 🎯

This class is crafted for scenarios where accessing Unicode code points via attribute syntax is preferred over function calls, offering a novel way to interact with character encodings.
It’s ideal for educational purposes to demonstrate Python’s dynamic attribute handling, or in specialized applications like text processing, character mapping, or creative coding projects where attribute-based access to Unicode values enhances code expressiveness.

## How It Works 🔍

-   **Initialization (`__init__`)**: Defined as an empty method since no arguments or initial state are required, keeping the instance lightweight and ready to process attribute requests dynamically.
-   **Attribute Access (`__getattribute__`)**: Overrides Python’s default attribute retrieval to implement the core functionality:
    -   Takes the attribute name (`name`) as a string.
    -   Checks if `name` is exactly one character long using `len(name) == 1`.
    -   If true, returns the Unicode code point of that character by calling `ord(name)`, mimicking the behavior of `ord()` for single characters.
    -   If false (i.e., the name is empty, multiple characters, or otherwise invalid), raises an `AttributeError` with a descriptive message indicating that the name must be a single character.
-   **Dynamic Behavior**: Since the class defines no attributes upfront, all attribute access is intercepted by `__getattribute__`, ensuring that only single-character names are processed, and no unintended attributes (e.g., internal Python attributes) interfere.

## Usage 📦

1. **Save the Code**: Store the `Ord` class in a Python file, e.g., `ord_class.py`, for use in programs or submission to a testing system.
2. **Create and Test Ord Instances**: Instantiate and access single-character attributes to retrieve Unicode values:
    ```python
    from ord_class import Ord
    o = Ord()
    print(o.a)      # 97 (Unicode for 'a')
    print(o.A)      # 65 (Unicode for 'A')
    print(o.π)      # 960 (Unicode for 'π')
    # print(o.ab)   # Raises AttributeError: 'ab' is not a single character
    ```
3. **Apply in Context**: Use in applications requiring Unicode code points, such as text encoding utilities, character set analysis, or educational tools to explore ASCII/Unicode tables via an attribute-based syntax.
4. **Explore Flexibility**: Test with various single characters, including letters (`o.z`), digits (`o.5`), symbols (`o.$`), or Unicode characters (`o.★`), to confirm consistent behavior across the Unicode spectrum.

## Conclusion 🚀

The `Ord` class offers a creative and efficient alternative to the `ord()` function, transforming Unicode code point access into an attribute-based interface that’s both intuitive and engaging.
By leveraging `__getattribute__`, it ensures precise handling of single-character names while maintaining simplicity with no initialization overhead.
This implementation is perfect for teaching Python’s dynamic capabilities or adding a unique twist to character processing tasks, providing a clear and reliable way to query Unicode values.
While already complete, the class could be extended with features like caching frequent lookups or supporting multi-character escapes for advanced use, but its current form fully satisfies the requirements with elegance and clarity, ready to enrich any project needing character code access with a fresh perspective.
