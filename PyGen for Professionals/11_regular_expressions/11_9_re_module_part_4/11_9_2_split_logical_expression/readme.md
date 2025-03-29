# Logical Expression Splitter 🔢

## Description 📝

This program takes a **logical expression** consisting of variables and logical operators and splits it into its individual components.

## Purpose 🎯

The script helps in **parsing logical expressions** by removing operators (`and`, `or`, `&`, `|`) and extracting only the variables.

## How It Works 🔍

1. **Reads Input**:

    - The program accepts a logical expression containing **variables** separated by logical operators (`and`, `or`, `&`, `|`).

2. **Splits the Expression**:

    - Uses a **regular expression** (`\s*(?:[|&]|and|or)\s*`) to split the string while **removing** the operators and spaces.

3. **Outputs Cleaned Variables**:
    - The extracted variables are printed, separated by a **comma and a space**.

## Output 📜

### Example Input:

```sh
A and B or C & D | E
```

### Example Output:

```sh
A, B, C, D, E
```

## Usage 📦

1. Run the script:
    ```sh
    python logical_splitter.py
    ```
2. Enter a logical expression:
    ```
    X or Y & Z and W | T
    ```
3. The script will output:
    ```
    X, Y, Z, W, T
    ```

## Conclusion 🚀

This tool simplifies **logical expression parsing** by extracting variables and eliminating operators, making it useful for **logical analysis and automation**.
