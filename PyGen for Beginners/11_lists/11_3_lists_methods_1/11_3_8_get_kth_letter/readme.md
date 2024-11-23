# Extract the kth Letter from Each String 📝

## Description 📝

This Python program takes a natural number `n`, followed by `n` strings, and an integer `k`. It extracts the `k`-th letter from each string (1-based index) and concatenates them into a single string, which is then printed without spaces.

## Purpose 🎯

The program demonstrates how to extract specific characters from multiple strings and concatenate them into a new string. It can be useful for text manipulation tasks.

## How It Works 🔍

1. The function `get_kth_letter()` takes three parameters: `n` (the number of strings), `strings` (the list of strings), and `k` (the index of the letter to extract).
2. The function iterates over the list of strings. For each string, it checks if its length is greater than or equal to `k`. If so, it adds the `k`-th character (1-based index) to the result string.
3. Finally, the concatenated string of `k`-th characters is returned.

## Output 📜

```bash
Example Input:
4
hello
world
python
program
2

Example Output:
eoryr
```

## Usage 📦

1. Save the script as `get_kth_letter.py`.
2. Run the script in a Python environment.
3. Input the number of strings `n`.
4. Input the `n` strings.
5. Input the index `k` of the letter you wish to extract.
6. The program will output the concatenated `k`-th letters from each string.

## Conclusion 🚀

This program efficiently extracts and concatenates specific characters from a set of strings. It is a good example of handling string manipulation tasks in Python.
