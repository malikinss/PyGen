# Replace English Letters with Russian for Maximum 🐝 (bee-coins) Earnings 💰

## Description 📝

This program helps Sam maximize the cost of his comment by replacing specific English letters with visually identical Russian ones.
Since Russian letters have higher Unicode values than their English counterparts, this substitution increases the total cost in bee-coins.

## Purpose 🎯

To compute and compare the cost of the original and modified comments while demonstrating Unicode manipulation and string substitution techniques.

## How It Works 🔍

1. **Input:** User provides a comment string.
2. **Old Cost Calculation:**
    - Each character's cost is calculated as `Unicode value * 3`.
    - The total cost of the original comment is computed.
3. **Replace English with Russian Letters:**
    - The program substitutes specific English letters with their visually similar Russian equivalents:
        - English: `eyopaxcETOPAHXCBM`
        - Russian: `еуорахсЕТОРАНХСВМ`
4. **New Cost Calculation:**
    - The cost of the modified comment is computed using the same formula.
5. **Output:** The program displays both the old and new costs in 🐝.

## Output 📜

### Example:

```bash
Input:
Example text to earn more!

Output:
Old cost: 1734🐝 New cost: 2013🐝
```

### Explanation:

-   Old comment: `Example text to earn more!`
-   Modified comment: `Ехаmрле теxт то еаrn mоrе!`
-   Unicode values of Russian letters increase the total cost.

## Usage 📦

1. Run the program in a Python environment.
2. Enter the comment string when prompted.
3. View the original and modified costs in bee-coins.

### Notes:

-   If the comment doesn't contain any replaceable letters, the old and new costs will be identical.
-   The program ensures all substitutions are visually seamless.

## Conclusion 🚀

This program is a creative way to explore string manipulation, Unicode value computations, and practical coding techniques for optimizing text-based operations.
