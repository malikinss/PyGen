# Expand Multiplications in Text 🔄

## Description 📝

This program expands multiplication patterns found in a given string.
A multiplication pattern is defined as `n(string)`, where:

-   `n` is a non-negative integer.
-   `string` is a sequence of lowercase Latin letters that should be repeated `n` times.

The program recursively expands all such patterns until no multiplications remain.

## Purpose 🎯

The goal is to transform compact notations like `ti2(Be)3(Ge)` into their fully expanded versions (`tiBeBeGeGeGe`).
This can be useful for processing encoded text or generating repetitive patterns.

## How It Works 🔍

1. **Regular Expression Matching**:

    - The program uses the regex pattern `r'(\d+)\((\w+)\)'` to find and extract multiplication patterns.
    - This pattern captures the number (`\d+`) and the enclosed string (`\w+`).

2. **Recursive Expansion**:
    - A helper function `unwrap(match: re.Match) -> str` replaces each pattern with its expanded form by repeating the enclosed string the specified number of times.
    - The `expand_multiplications` function repeatedly applies this replacement until no more multiplication patterns exist in the text.

## Output 📜

### Example Input:

```python
text = "ti2(Be)3(Ge)"
```

### Example Output:

```python
"tiBeBeGeGeGe"
```

### Example Expansion Steps:

1. `"ti2(Be)3(Ge)"` → `"tiBeBe3(Ge)"`
2. `"tiBeBe3(Ge)"` → `"tiBeBeGeGeGe"`

## Usage 📦

1. Run the function with an input string containing multiplication patterns:
    ```python
    result = expand_multiplications("bbb10(2(a))bbb")
    print(result)
    ```
2. The function will output:
    ```python
    "bbbbaaaaaaaaaaaaaaaaaaaabbb"
    ```

## Conclusion 🚀

This program efficiently expands encoded multiplication patterns, ensuring correct order of operations.
It can process nested multiplications and guarantees a fully expanded result within the given constraints.
