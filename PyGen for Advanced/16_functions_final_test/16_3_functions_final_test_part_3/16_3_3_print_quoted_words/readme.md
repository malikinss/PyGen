# Printing Quoted Words 🎯

## Description 📝

The `print_quoted_words()` function prints all the words from a given list, each wrapped in double quotes and separated by a space. This is achieved using the `map()` function and the unpacking operator (`*`).

## Purpose 🎯

This function takes a list of words, wraps each word in double quotes, and prints them in a single line separated by spaces.

## How It Works 🔍

1. **`map()`**: This function is used to apply the transformation to each element of the `words` list. The transformation wraps each word in double quotes.
2. **`*` unpacking operator**: The unpacking operator is used to pass each item of the mapped list as a separate argument to `print()`.
3. **`sep=' '`**: The separator ensures that the words are printed with a space between them.

## Example Output:

```python
>>> words = 'the world is mine take a look what you have started'.split()
>>> print_quoted_words(words)
"the" "world" "is" "mine" "take" "a" "look" "what" "you" "have" "started"
```

## Usage 📦

1. The function `print_quoted_words()` takes a list of words as input.
2. The `map()` function wraps each word in double quotes.
3. The `*` operator unpacks the mapped list and passes each word to `print()`.
4. The result is printed in a single line with space-separated quoted words.

## Conclusion 🚀

The solution effectively uses Python’s `map()` and unpacking operator to transform and print a list of words in double quotes on a single line, making the code both clean and concise.
