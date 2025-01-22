# Online Store Sales Summary 📝

## Description 📝

This program processes a list of sales records from an online store and generates a sales summary.
It counts the number of units of each product purchased by each customer and outputs the summary in lexicographic order by customer and product names.

## Purpose 🎯

The purpose of this program is to track the purchases made by customers, including the quantity of each product bought, and output a clear and sorted summary of the sales per customer.

## How It Works 🔍

1. **Input**:
    - The first input is an integer `n`, representing the number of sales records.
    - Each of the following `n` lines contains a sale record in the format:
        ```
        buyer_name product_name quantity
        ```
    - The program stores the sales in a dictionary with the buyer's name as the key and the purchased products and their quantities as nested dictionaries.
2. **Processing**:

    - The program processes each sale record, updating the quantity of the product for the corresponding buyer.
    - If the buyer is new, a new entry is created in the dictionary.
    - If the buyer has already purchased the product, the quantity is updated by adding the purchased amount.

3. **Output**:
    - After processing all sales, the program outputs a sorted list of buyers, followed by a sorted list of products purchased by each buyer and their quantities.

## Output 📜

The output consists of the buyers' names followed by the products they purchased and the quantities in the following format:

```
buyer_name:
product_name quantity
```

Each buyer and their products are listed in lexicographic order.

### Example Input/Output:

**Input**:

```
4
timur banana 2
alice apple 1
timur apple 3
alice banana 5
```

**Output**:

```
alice:
apple 1
banana 5
timur:
apple 3
banana 2
```

### Explanation:

-   For the input data, `timur` bought 2 bananas and 3 apples. `alice` bought 1 apple and 5 bananas.
-   The program outputs the buyers sorted lexicographically: `alice` and then `timur`.
-   The products for each buyer are also sorted lexicographically.

## Usage 📦

1. Copy the code into a Python file (e.g., `sales_summary.py`).
2. Input the number of sales records followed by each sale entry.
3. The program will output the sorted sales summary by buyer and product.

### Example Run:

```python
# Input:
4
timur banana 2
alice apple 1
timur apple 3
alice banana 5

# Output:
alice:
apple 1
banana 5
timur:
apple 3
banana 2
```

## Conclusion 🚀

This program provides an efficient way to summarize online store sales, displaying the number of products purchased by each customer.
It ensures the information is presented clearly, sorted by buyer and product names.
