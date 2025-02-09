# Monthly Revenue Calculator

## Description 📝

This Python program calculates the total monthly revenue of a company based on sales data stored in a text file.
Each line in the file represents a payment made by a customer in dollars.

## Purpose 🎯

The program helps businesses quickly determine their total revenue for a given month by reading and summing up all sales records from a file.

## How It Works 🔍

1. **Reading Data**:
    - The program reads a file named `ledger.txt`, which contains sales amounts, one per line.
2. **Processing Data**:
    - It removes the dollar sign (`$`) if present and converts each line into an integer.
3. **Calculating Revenue**:
    - The total sum of all sales amounts is computed.
4. **Displaying Output**:
    - The total revenue is printed in dollar format.

## Output 📜

The program outputs the total revenue in dollars.

Example:
If `ledger.txt` contains:

```
100
200
$150
300
```

The program will output:

```
$750
```

## Usage 📦

1. Save the script as `revenue_calculator.py`.
2. Ensure `ledger.txt` is in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the script's directory.
5. Run the script using:
    ```
    python revenue_calculator.py
    ```
6. The program will display the total revenue.

## Conclusion 🚀

This program simplifies revenue calculations by automatically processing sales data from a file.
It is useful for businesses and financial analysis.
