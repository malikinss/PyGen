# JSON Conversion with Key Filtering

## Description 📝

This Python script converts a dictionary containing words and their phonetic representations into a JSON string while skipping invalid keys.

## Purpose 🎯

The script ensures:

-   Only valid keys (strings) are included in the final JSON output.
-   Invalid keys (such as tuples and frozensets) are ignored.
-   The dictionary is serialized into a JSON string.

## How It Works 🔍

1. **convert_words_to_json() Function**:

    - Uses `json.dumps()` with `skipkeys=True` to exclude non-string keys.
    - Serializes the filtered dictionary into a JSON string.

2. **Example Dictionary**:
    - Contains valid and invalid keys (e.g., frozensets, tuples).
    - The function automatically skips unsupported keys.

## Output 📜

The program prints a valid JSON string, excluding problematic entries:

```json
{
    "travel": "trævl",
    "moonlight": "muːn.laɪt",
    "sunshine": "ˈsʌn.ʃaɪn",
    "adventure": "ədˈventʃər",
    "beautiful": "ˈbjuːtɪfl",
    "bicycle": "baisikl"
}
```

## Usage 📦

1. Save the script as `convert_words.py`.
2. Run the script using:
    ```
    python convert_words.py
    ```
3. The formatted JSON string will be displayed.

## Conclusion 🚀

This script demonstrates how to filter dictionary keys while converting to JSON.
It leverages Python's built-in `json.dumps()` function to handle invalid key types efficiently.
