# Spell Function

## Description 📝

The `spell()` function processes a list of words and returns a dictionary where:

-   The keys are the first letters of the words (in lowercase).
-   The values are the maximum word lengths for each corresponding letter.

## Purpose 🎯

This function is useful for:

-   Text analysis and processing
-   Grouping words by their starting letters
-   Finding the longest word per letter category

## How It Works 🔍

1. The function takes an arbitrary number of word arguments.
2. It extracts the first letter of each word (ignoring case).
3. It updates the dictionary with the maximum length for words starting with the same letter.
4. If no words are provided, it returns an empty dictionary.

## Output 📜

Example usage and expected outputs:

```python
spell("Apple", "banana", "avocado", "berry", "Cherry", "apricot")
# {'a': 7, 'b': 6, 'c': 6}

spell("cat", "dog", "dolphin", "ant", "cheetah")
# {'c': 7, 'd': 7, 'a': 3}

spell("Hello", "hi", "house", "howdy", "Hero")
# {'h': 6}

spell()
# {}
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Call the `spell()` function in your script or interactive Python shell.

Example:

```python
from spell_checker import spell

print(spell("Mountain", "meadow", "river", "rain", "Road"))
```

## Conclusion 🚀

The `spell()` function efficiently finds the longest word for each starting letter, making it a useful tool for text processing and analysis.
