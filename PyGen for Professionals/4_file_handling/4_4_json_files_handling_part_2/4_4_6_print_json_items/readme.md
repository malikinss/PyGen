# JSON Key-Value Printer 📝

## Description 📝

This program reads a JSON object from input, then prints all its key-value pairs.
If any value is a list, its elements are printed as comma-separated values.
The keys and values are displayed in the original order from the input.

## Purpose 🎯

The goal of this program is to process JSON objects and output each key-value pair in a readable format.
This can be useful for debugging, inspecting JSON objects, or working with APIs.

## How It Works 🔍

1. The program first reads JSON input from the user using the `sys.stdin.read()` method.
2. The input is parsed into a Python dictionary using `json.loads()`.
3. The function `format_if_list()` checks if any value is a list and, if so, formats it by joining the elements with commas.
4. The `print_json_items()` function then prints each key-value pair in the format `key: value`, respecting the order from the JSON input.

## Output 📜

### Example:

Input:

```json
{
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "traveling", "coding"]
}
```

Output:

```
name: Alice
age: 30
hobbies: reading, traveling, coding
```

## Usage 📦

1. Run the program and provide valid JSON as input through standard input.
2. It will output all key-value pairs in the original order.
3. List values will be printed as comma-separated values.

## Conclusion 🚀

This utility allows for easy inspection and display of key-value pairs from a JSON object, with special handling for lists, making it perfect for working with structured data.
