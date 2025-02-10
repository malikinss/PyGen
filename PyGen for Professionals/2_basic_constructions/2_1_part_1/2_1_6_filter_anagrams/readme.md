# Filter Anagrams

## Description 📝

The `filter_anagrams()` function checks a given list of words and filters out the ones that are anagrams of the provided word.
Anagrams are words that contain the exact same letters in the same frequency.

## Purpose 🎯

The purpose of this function is to identify and return all anagrams of a given word from a list of words.
An anagram is defined as a word formed by rearranging the letters of another word.

## How It Works 🔍

1. The function takes two arguments:
    - `word`: A lowercase word to compare.
    - `words`: A list of lowercase words to check.
2. The function compares each word in the list to the provided `word` by sorting the letters of both.
3. If the sorted version of a word matches the sorted version of `word`, it is considered an anagram and added to the result list.
4. The function returns the list of anagrams in their original order.

## Output 📜

The function returns a list of words that are anagrams of the given word:

-   If there are no anagrams in the list, an empty list is returned.
-   If the word is its own anagram, it will appear in the result.

## Usage 📦

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Call the `filter_anagrams()` function with a word and a list of words.

Example:

```python
filter_anagrams("listen", ["enlist", "google", "inlets", "banana"])
# Output:
# ['enlist', 'inlets']
```

## Conclusion 🚀

The `filter_anagrams()` function is a simple and efficient way to find anagrams of a given word in a list. It utilizes sorting to compare letters and ensure that only valid anagrams are returned, making it useful for word games, puzzles, or text analysis.
