# Flipping a Dictionary 🔄

## Description 📝

This program takes a dictionary with lists as values and inverts it, swapping the keys and values.
In the flipped dictionary, the original values become the keys, and the original keys become the values, grouped into lists.

## Purpose 🎯

✔ Invert a dictionary where each key has a list of values into a new dictionary where each value becomes a key, and the original keys are grouped as values.  
✔ Use `defaultdict(list)` to ensure that each key can have multiple associated values.

## Example Input

```python
original_dict = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
```

## Example Output 📜

```python
{
    1: ['a', 'b'],
    2: ['a', 'c'],
    3: ['b']
}
```

## Output Format

-   The dictionary is reversed so that the values from the original dictionary become keys in the new dictionary.
-   The keys from the original dictionary become values in lists associated with the new keys.

## Usage 📦

To use the program:  
1️⃣ Pass a dictionary where the key is a number or string, and the value is a list of numbers or strings.  
2️⃣ Call the `flip_dict()` function to invert the dictionary.  
3️⃣ The function will return the flipped dictionary, with the values turned into keys and keys turned into lists of values.

### Run the script:

```bash
$ python flip_dict.py
```

## Conclusion 🚀

This program is useful when you need to reverse the structure of a dictionary that has lists as values, allowing you to quickly view the inverse relationships.
The result will maintain the order of keys and values as required.
