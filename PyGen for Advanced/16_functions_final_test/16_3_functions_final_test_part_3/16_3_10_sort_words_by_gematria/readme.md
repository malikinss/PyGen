# Gematria Sorting 🎯

## Description 📝

The program sorts a list of words based on their gematria values in ascending order. In case two words have the same gematria value, they are sorted alphabetically.

## Purpose 🎯

This function computes the gematria of words, which is the sum of numerical values of each letter in the word. The sorting is done first by gematria value and, in case of ties, by lexicographical order.

## How It Works 🔍

1. **Gematria Calculation**:  
   The `gematria()` function calculates the gematria value of a word by converting each letter to uppercase and finding its numerical value as `ord(letter) - ord('A')`.
2. **Sorting Words**:  
   The `sort_words_by_gematria()` function reads the input words, calculates their gematria, and sorts them using the gematria values as the primary key and the word itself as the secondary key for ties.

3. **Output**:  
   After sorting, the words are printed in ascending order of their gematria, with ties broken alphabetically.

## Example Usage:

```python
>>> n = 3
>>> sort_words_by_gematria(n)
apple
banana
grape
```

## Conclusion 🚀

The `sort_words_by_gematria()` function provides a sorted list of words based on their gematria values, which can be useful for various text analysis or word games. The sorting takes into account both numerical values and lexicographical order for better handling of ties.
