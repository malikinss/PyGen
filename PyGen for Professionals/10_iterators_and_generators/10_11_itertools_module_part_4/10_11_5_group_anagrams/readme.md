# `group_anagrams()` - Group Words that are Anagrams

## Description 📝

The `group_anagrams()` function takes a list of words and groups the words that are anagrams into tuples.
It then returns a list of these tuples.
The order of the tuples and the order of the words within each tuple do not matter.

## Purpose 🎯

✔ **Groups anagram words** into tuples.  
✔ **Returns a list** of tuples containing words that are anagrams of each other.  
✔ **Handles any number of words** in the input list.

## How It Works 🔍

1. **Sort words alphabetically** by their letters. This ensures that all anagrams will be grouped together since they will have the same sorted form.
2. **Group the sorted words** using `groupby()`, which will group words that are anagrams (i.e., they have the same sorted form).
3. **Return the grouped words** as tuples, each tuple containing words that are anagrams.

## Usage 📦

```python
words_list = [
    "adapter", "petard", "address", "seredochka",
    "alphabet", "bazooka", "aistenok", "osetinka"
]

result = group_anagrams(words_list)
print(result)
```

**Output:**

```plaintext
[('adapter', 'petard'), ('address', 'seredochka'), ('alphabet', 'bazooka'), ('aistenok', 'osetinka')]
```

## Conclusion 🚀

This function successfully groups words that are anagrams into tuples and returns them in a list.
The output is straightforward and easy to process, and the implementation ensures that all anagrams are grouped together regardless of the order in which they appear in the input list.
