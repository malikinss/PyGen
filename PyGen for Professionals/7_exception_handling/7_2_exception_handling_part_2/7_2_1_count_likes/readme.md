# Calculate Total Likes with Error Handling 📝

## Description 📝

The program calculates the total sum of the 'Likes' values from a list of dictionaries.
If any dictionary lacks the 'Likes' key, the value is treated as -1. A `try-except` block is added to handle missing keys.

## Purpose 🎯

The goal is to prevent the program from crashing when a dictionary does not contain the 'Likes' key and to ensure the program continues functioning smoothly with a fallback value of -1.

## How It Works 🔍

1. The function iterates over each dictionary in the `blog_posts` list.
2. It attempts to retrieve the 'Likes' value.
3. If the key is missing, the `KeyError` exception is caught, and -1 is added to the total instead of raising an error.

## Output 📜

**Example Input:**

```python
blog_posts = [
    {'Photos': 3, 'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Photos': 8, 'Comments': 1, 'Shares': 1},
    {'Photos': 3, 'Likes': 19, 'Comments': 3}
]
```

**Example Output:**

```python
86
```

## Usage 📦

1. Pass a list of dictionaries representing blog posts to the function `calculate_total_likes()`.
2. The function will sum the 'Likes' values, treating any missing values as -1.

## Conclusion 🚀

The function now safely calculates the sum of 'Likes' values, and if a dictionary is missing the 'Likes' key, it handles the situation by subtracting 1 from the total.
