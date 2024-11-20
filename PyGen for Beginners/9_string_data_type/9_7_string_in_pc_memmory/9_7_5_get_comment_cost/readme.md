# Calculate the Cost of a Comment in 🐝 (bee-coins) 💰

## Description 📝

This program calculates the total cost of a comment based on the Unicode values of its characters.
Each character is valued at `<Unicode value> * 3 🐝`, where 🐝 is a virtual currency called "bee-coins."
The program outputs both the original message and its total cost.

## Purpose 🎯

To automate the process of calculating the payment for comments in bee-coins, ensuring accurate and efficient computations.

## How It Works 🔍

1. **Input:** The user provides a comment string.
2. **Calculate Cost:**
    - Each character in the string is evaluated.
    - The cost of each character is calculated as `Unicode value * 3`.
    - The program sums up the costs of all characters in the string.
3. **Output:**
    - The program displays the original comment.
    - The total cost in 🐝 is presented.

## Output 📜

### Example:

```bash
Input: Hello!
Output:
Message text: 'Hello!' Message cost: 1659🐝
```

### Explanation:

-   Unicode values:
    -   `H`: 72
    -   `e`: 101
    -   `l`: 108
    -   `l`: 108
    -   `o`: 111
    -   `!`: 33
-   Character costs (Unicode value \* 3):
    -   `H`: 216
    -   `e`: 303
    -   `l`: 324
    -   `l`: 324
    -   `o`: 333
    -   `!`: 99
-   Total cost: 216 + 303 + 324 + 324 + 333 + 99 = 1659 🐝.

## Usage 📦

1. Run the program in a Python environment.
2. Enter the comment string when prompted.
3. View the original message and its total cost in bee-coins.

### Notes:

-   Special characters and emojis are included, as their Unicode values contribute to the total.
-   The program handles any string input, including empty strings (resulting in a cost of 0 🐝).

## Conclusion 🚀

This program is a fun and practical way to integrate Unicode calculations into a real-world context, offering insights into character encoding and string manipulations.
