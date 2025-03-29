# Custom String Splitter 🔗

## Description 📝

This program splits a given string based on **periods (.)**, **commas (,)**, and **semicolons (;)**, removing any surrounding spaces.

## Purpose 🎯

The purpose of this script is to extract meaningful values from a string by removing delimiters and unnecessary spaces.

## How It Works 🔍

1. **Reads Input**:

    - The program accepts a string containing words or values separated by `.`, `,`, or `;` with optional spaces around them.

2. **Splits the String**:

    - Uses a regular expression (`\s*[.,;]\s*`) to split the string while trimming surrounding spaces.

3. **Outputs Cleaned Words**:
    - The extracted values are printed, separated by spaces.

## Output 📜

### Example Input:

```sh
apple , banana;  cherry .   mango
```

### Example Output:

```sh
apple banana cherry mango
```

## Usage 📦

1. Run the script and enter a string:
    ```sh
    python string_splitter.py
    ```
2. Enter a string with delimiters:
    ```
    apple, banana ; orange . grape
    ```
3. The script will output:
    ```
    apple banana orange grape
    ```

## Conclusion 🚀

This tool efficiently processes strings by removing unnecessary delimiters and spaces, making data parsing cleaner and more structured.
