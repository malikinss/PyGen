# Burger Joint Receipt

## Description 📝

This Python program calculates the total cost of a burger order based on selected ingredients.
The ingredients are categorized into different groups such as bread, meat, sauces, vegetables, and toppings.
The program takes a list of ingredients chosen by the customer, determines their total cost, and outputs a receipt in a formatted style.
The ingredients are displayed in lexicographic order along with their quantities and total price.

## Purpose 🎯

The purpose of this program is to compute the total cost of a custom burger order and print a formatted receipt for the customer.
It organizes ingredients by categories and outputs the receipt with clear and well-aligned information.

## How It Works 🔍

1. **Input**: The program receives a comma-separated list of ingredients.
2. **Price Calculation**: It calculates the total cost based on the prices of each ingredient, which are stored in dictionaries categorized by type (bread, meat, sauces, vegetables, toppings).
3. **Receipt Generation**: The ingredients are sorted lexicographically, and a receipt is generated, showing each ingredient, its quantity, and the total price.
4. **Output**: The receipt is printed to the console with properly formatted lines and a total cost.

## Output 📜

The program prints a receipt that includes:

-   Each ingredient listed with its quantity.
-   A line showing the total cost at the bottom.
-   The ingredients are sorted in lexicographic order.
-   The receipt is aligned and formatted with spaces and dashes.

### Example:

#### Input:

The user inputs the following list of ingredients:

```
булочка с кунжутом,куриный бифштекс,кетчуп,лук,сыр,помидор
```

#### Output:

```
булочка с кунжутом x 1
кетчуп x 1
куриный бифштекс x 1
лук x 1
помидор x 1
сыр x 1
--------------------------
ИТОГ: 120р
```

## Usage 📦

1. The user enters a sequence of ingredients separated by commas.
2. The program will process the input, calculate the total cost, and print the formatted receipt.

### Example:

```bash
Enter ingredients separated by commas: булочка с кунжутом,куриный бифштекс,кетчуп,лук,сыр,помидор
```

#### Example Output:

```
булочка с кунжутом x 1
кетчуп x 1
куриный бифштекс x 1
лук x 1
помидор x 1
сыр x 1
--------------------------
ИТОГ: 120р
```

## Conclusion 🚀

This program is a simple but effective tool for managing burger orders, calculating their total price, and printing an easy-to-read receipt.
It supports adding new ingredients and categories by adjusting the ingredient dictionaries.
