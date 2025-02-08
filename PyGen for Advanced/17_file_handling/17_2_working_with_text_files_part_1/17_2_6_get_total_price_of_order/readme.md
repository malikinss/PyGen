# Calculate Total Order Cost from a File 🛒💰

## Description 📝

This program reads a file named **"prices.txt"**, which contains order information from an **online store**.  
Each line consists of:

-   **Product name**
-   **Quantity (integer)**
-   **Price per unit (integer)**  
    These values are **tab-separated (`\t`)**.

## Purpose 🎯

To **compute and display** the **total cost** of all products in the order.

## How It Works 🔍

1. **File Reading (`get_data_from_file`)**:

    - Opens the file with UTF-8 encoding.
    - Reads all lines, **removing extra spaces/newlines**.

2. **Price Calculation (`get_total_price_of_order`)**:
    - **Splits each line** into a list using `\t` as a separator.
    - Extracts the **quantity** and **price** values.
    - Computes the **total cost** using the formula:  
      \[
      \text{Total Cost} = \sum (\text{quantity} \times \text{price})
      \]

## Example Usage:

**File (`prices.txt`):**

```
Laptop	2	50000
Mouse	3	1500
Keyboard	1	3000
```

**Program Output:**

```python
>>> 106500
```

## Conclusion 🚀

This script efficiently extracts **tab-separated order data**, processes it, and **calculates the total cost**, making it a great **file-handling** and **data processing** example in Python! 🧾📦
