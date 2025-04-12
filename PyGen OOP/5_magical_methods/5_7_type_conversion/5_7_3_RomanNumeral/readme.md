# RomanNumeral Class Ancient Number System

## Description 📝

The `RomanNumeral` class encapsulates a number in the Roman numeral system, initialized with a string like `IV`.
It provides an informal string representation matching the input, converts to an integer via casting, supports all comparison operations (`==`, `!=`, `>`, `<`, `>=`, `<=`) between instances, and enables addition (`+`) and subtraction (`-`) to produce new `RomanNumeral` instances.
Invalid operations return `NotImplemented`.

## Purpose 🎯

This class is designed for working with Roman numerals, ideal for historical simulations, educational exercises on number systems, or applications needing to manipulate or compare Roman numerals, such as in games, puzzles, or cultural studies.
It bridges ancient notation with modern arithmetic seamlessly.

## How It Works 🔍

-   **Initialization (`__init__`)**: Stores the Roman numeral string (e.g., `IV`) in `self.number` for use in string representation and conversions.
-   **String Representation (`__str__`)**: Returns the Roman numeral string as-is, ensuring the informal output matches the input format.
-   **Integer Conversion (`__int__`)**: Converts the Roman numeral to a decimal integer by iterating through the string, checking for two-character patterns (e.g., `IV`, `CM`) before single characters (e.g., `I`, `V`), and summing their values from a predefined `_NUMS` dictionary (`I: 1`, `IV: 4`, etc.).
-   **Roman Conversion (`_to_roman`)**: A class method that converts a decimal integer back to a Roman numeral string by greedily subtracting the largest possible values from `_NUMS` and appending corresponding symbols, used internally for arithmetic results.
-   **Comparison Operations**:
    -   `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__lt__`, `__le__`: Compare two `RomanNumeral` instances by converting both to integers and applying the respective operator, returning `NotImplemented` for non-`RomanNumeral` operands.
    -   Ensures intuitive ordering (e.g., `V > IV` because `5 > 4`).
-   **Arithmetic Operations**:
    -   `__add__`: Adds two `RomanNumeral` instances by converting to integers, summing, and converting the result back to a Roman numeral.
    -   `__sub__`: Subtracts, assuming the minuend is larger (per guarantee), and converts the difference to a Roman numeral.
    -   Both return `NotImplemented` for invalid types.
-   **Internal Mapping**: Uses `_NUMS` to map Roman symbols and pairs to their decimal values (`M: 1000`, `CM: 900`, etc.), supporting both parsing and generation of numerals.

## Usage 📦

1. **Save the Code**: Store the `RomanNumeral` class in a Python file, e.g., `roman_numeral.py`, for import into projects or submission to a testing system.
2. **Create and Manipulate Numerals**: Instantiate with Roman numeral strings and perform operations:
    ```python
    from roman_numeral import RomanNumeral
    rn1 = RomanNumeral('IV')  # 4
    rn2 = RomanNumeral('VI')  # 6
    print(rn1)           # IV
    print(int(rn1))      # 4
    print(rn1 + rn2)     # X (10)
    print(rn2 - rn1)     # II (2)
    print(rn2 > rn1)     # True
    print(rn1 == RomanNumeral('IV'))  # True
    ```
3. **Apply in Context**: Use in applications like historical date rendering, outline numbering (e.g., book chapters), or puzzles requiring Roman numeral arithmetic and comparison.
4. **Test Edge Cases**: Experiment with inputs like `MCMXCIX` (1999) or `I` (1) to verify conversions and operations, noting that subtraction assumes a positive or zero result.

## Conclusion 🚀

The `RomanNumeral` class delivers a comprehensive and intuitive interface for handling Roman numerals in Python, blending ancient notation with modern functionality.
Its support for integer conversion, comparisons, and arithmetic operations makes it versatile for both practical and academic purposes, enabling users to perform calculations as naturally as with decimal numbers.
The use of a static `_NUMS` dictionary ensures efficient parsing and generation, while the class’s adherence to `NotImplemented` for invalid operations guarantees robustness.
This implementation is ready for immediate use in scenarios requiring Roman numeral manipulation and could be extended with features like validation (e.g., rejecting invalid strings like `IIII`) or negative number support, though the current design fully satisfies the task’s requirements with elegance and precision.
Whether simulating a Roman marketplace or teaching number systems, `RomanNumeral` is a reliable and engaging tool for any Python developer’s collection.
