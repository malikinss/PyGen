# Pretty Print List with Frame 🎨

## Description 📝

The `pretty_print()` function prints the contents of a list surrounded by a frame.
It uses customizable characters for the frame sides and the delimiter between elements inside the list.

## Purpose 🎯

This function enhances the presentation of list data by printing it inside a decorative frame.
It helps to make the output more readable and visually appealing.

## How It Works 🔍

-   **Mandatory argument**: The function takes a list (`data`) that will be printed.
-   **Optional arguments**:
    -   `side`: The character used for the frame sides (default is `'-'`).
    -   `delimiter`: The character used to separate elements inside the frame (default is `'|'`).
-   The function constructs the framed list with the specified delimiter and prints the result within a border.

## Example Output:

```text
-------------------------
|1|2|3|4|5|
-------------------------
```

## Usage 📦

1. Provide the list of elements as the first argument.
2. Optionally, specify the frame side character and delimiter.
3. The function will print the list surrounded by a frame.

## Conclusion 🚀

The `pretty_print()` function makes displaying lists more structured and visually attractive.
It’s ideal for cases where the presentation of data is crucial.
