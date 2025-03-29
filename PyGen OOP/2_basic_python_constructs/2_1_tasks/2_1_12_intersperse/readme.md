# Intersperse Generator Function ⚙️

## Description 📝

The `intersperse()` function is a generator that takes an iterable and a delimiter, then yields each element of the iterable with the delimiter placed between them.
This is useful for creating a sequence where values are separated by a specified delimiter.

## Purpose 🎯

This function is designed to create a generator that allows you to insert a delimiter between each element of an iterable.
It can be particularly useful when formatting output or generating sequences for processing.

## How It Works 🔍

1. The function takes two arguments:
    - `iterable`: The iterable (e.g., list, tuple) whose elements need to be separated by the delimiter.
    - `delimiter`: The value to insert between the elements of the iterable.
2. The function iterates over the elements of the iterable using a generator pattern, yielding the first element and then continuing to yield the delimiter followed by each subsequent element.
3. The iteration continues until all elements are processed, and the generator produces a sequence with the delimiter interspersed between each element.

### Example Inputs & Outputs:

| Input                    | Output                |
| ------------------------ | --------------------- |
| `[1, 2, 3]`, `0`         | `1 0 2 0 3`           |
| `['a', 'b', 'c']`, `'-'` | `'a' '-' 'b' '-' 'c'` |

## Output 📜

The generator produces a sequence where each element of the iterable is followed by the delimiter, except for the last element.

## Usage 📦

1. Call `intersperse()` with an iterable and a delimiter.
2. Iterate over the result to get the interspersed sequence.

## Conclusion 🚀

The `intersperse()` function is a simple but effective way to generate a sequence with a custom delimiter between elements.
It's highly useful for transforming or formatting data.
