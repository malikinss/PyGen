# Ignore Command Filter 🛑

## Description 📝

This program defines a function `ignore_command()` that checks whether a given command string contains any restricted substrings.
If the command includes any word from the predefined `ignore` list, the function returns `True`; otherwise, it returns `False`.

## Purpose 🎯

The purpose of this function is to filter out commands that contain potentially sensitive or restricted keywords, preventing their execution.

## How It Works 🔍

1. The function `ignore_command()` accepts a string argument `command`.
2. It defines a list `ignore`, containing restricted words such as `'alias'`, `'configuration'`, `'sql'`, etc.
3. It uses the built-in `any()` function to check if any word from the `ignore` list is present in the command string.
4. If at least one restricted word is found, the function returns `True`, indicating that the command should be ignored. Otherwise, it returns `False`.

## Output 📜

### Example 1

**Input:**

```python
print(ignore_command("show ip interface brief"))
```

**Output:**

```
True
```

### Example 2

**Input:**

```python
print(ignore_command("display version"))
```

**Output:**

```
False
```

## Usage 📦

1. Import the function into your script or use it directly.
2. Pass a command string to `ignore_command()`.
3. The function returns `True` if the command contains restricted words and `False` otherwise.

## Conclusion 🚀

This implementation improves the efficiency of filtering restricted commands by replacing the explicit loop with the `any()` function, making the code more concise and readable.
