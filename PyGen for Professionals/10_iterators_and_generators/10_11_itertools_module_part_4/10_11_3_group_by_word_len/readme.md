# `group_by_word_len()` - Group Words by Length

## Description 📝

The function `group_by_word_len()` receives a sequence of lowercase Latin words, groups them by their length, and prints them in increasing order of length.
Each group contains words sorted alphabetically.

## Purpose 🎯

✔ **Groups words** based on their length.  
✔ **Sorts words alphabetically** within each group.  
✔ **Prints the groups** in order of increasing length.

## How It Works 🔍

1. **Sort the words by length** to easily group them.
2. **Group the words** by length using `groupby()`.
3. **Sort each group alphabetically**.
4. **Print the grouped words** in the desired format.

## Output 📜

### Example Input

```
apple banana pear peach orange grape
```

### Example Output

```plaintext
4 -> pear
5 -> apple, grape
6 -> banana, peach
7 -> orange
```

## Code Breakdown 🛠

### Step 1: Sort Words by Length

```python
words.sort(key=len)
```

-   The list of words is sorted based on their length, allowing `groupby()` to easily group them by length.

### Step 2: Group Words by Length

```python
grouped = groupby(words, key=len)
```

-   The `groupby()` function groups the words based on their length (`key=len`).

### Step 3: Sort Each Group Alphabetically

```python
for length, group in grouped:
    print_result(length, sorted(group))
```

-   For each group, the words are sorted alphabetically and then printed using the `print_result()` function.

### Step 4: Output the Result

The function `print_result()` formats and prints each group in the desired format: `<length> -> <word>, <word>, ...`.

## Usage 📦

```python
words_data = ["apple", "banana", "pear", "peach", "orange", "grape"]
group_by_word_len(words_data)
```

**Output:**

```plaintext
4 -> pear
5 -> apple, grape
6 -> banana, peach
7 -> orange
```

## Conclusion 🚀

This program effectively groups words by their length, sorts them alphabetically within each group, and prints the result in a clear and organized format.
It is a simple yet efficient solution for grouping and sorting words based on their length.
