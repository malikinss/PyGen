# Shopping List Program with Unicode-Based Pricing

## Description 📝

This Python program helps Timur calculate the total price of items on his shopping list, where the price of each item is determined by the sum of the Unicode codes of its letters. The items are input as lowercase, separated by commas.
The program groups identical items, calculates their total cost, and displays the result in lexicographic order.

## Purpose 🎯

The purpose of this program is to help Timur, who is unable to use the number keys on his keyboard, calculate the cost of items on his shopping list.
Each item’s price is determined by the sum of the Unicode values of its characters, and the program also accounts for the quantity of each item.

## How It Works 🔍

1. The program reads a comma-separated list of lowercase items.
2. It counts the occurrences of each item.
3. The price of each item is calculated by summing the Unicode values of its characters.
4. The total cost for each group of identical items is calculated.
5. The program outputs the results in lexicographic order, showing the unit price, quantity, and total cost for each group.

## Output 📜

The program outputs each item, its unit price, quantity, and total cost in the following format:

```
<product>:
<unit price> UC x <quantity> = <total cost> UC
```

### Example:

Input:

```
pen,pen,book,pen
```

Output:

```
book:  438 UC x 1 = 438 UC
pen:  323 UC x 3 = 969 UC
```

## Usage 📦

1. Copy the code into a Python file.
2. Run the program.
3. Enter the shopping list items, separated by commas (no spaces).

### Example:

```python
# Input:
pen,pen,book,pen

# Output:
book:  438 UC x 1 = 438 UC
pen:  323 UC x 3 = 969 UC
```

## Conclusion 🚀

The shopping list program allows Timur to easily calculate the cost of items, even when his keyboard is malfunctioning.
The program groups identical items, calculates their total cost, and outputs the results in an organized manner.
