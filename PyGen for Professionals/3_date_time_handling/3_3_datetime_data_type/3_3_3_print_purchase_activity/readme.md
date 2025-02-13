# Purchase Activity Analyzer

## Description 📝

This program analyzes a list of purchase times, checking whether more purchases were made before noon or in the afternoon.
It then outputs whether "Before Noon" or "Afternoon" had more purchases.

## Purpose 🎯

The program is designed to help determine when more purchases are made: before or after noon.
This can be useful for understanding customer behavior and optimizing store operations.

## How It Works 🔍

1. The program receives a list of datetime objects representing the times when purchases were made.
2. It checks each purchase time to see whether it was made before or after noon.
3. The program then compares the count of purchases made before and after noon.
4. Finally, it prints "Before Noon" if more purchases were made before noon, or "Afternoon" if more were made after noon.

## Output 📜

The program outputs one of the following:

-   "Before Noon" if more purchases were made before noon.
-   "Afternoon" if more purchases were made in the afternoon.

### Example Usage:

```plaintext
Input:
A list of datetime objects representing purchase times.

Output:
Before Noon
```

## Usage 📦

1. Call the function `print_purchase_activity(times_of_purchases)` with a list of `datetime` objects representing purchase times.
2. The function will print either "Before Noon" or "Afternoon" based on the analysis.

## Conclusion 🚀

This program efficiently analyzes customer purchase behavior and determines the time of day with the most activity, helping businesses understand their customers' shopping patterns.
