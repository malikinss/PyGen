# Revenue Summary 🏆

## Description 📝

This program calculates the total revenue for each product based on given sales data.
The sales data consists of tuples where the first element is the product name, and the second element is the revenue in dollars.
The program aggregates the revenue per product and displays the results in lexicographical order.

## Purpose 🎯

The program performs the following tasks:  
✔ Aggregates revenue for each product.  
✔ Sorts the products alphabetically.  
✔ Displays the total revenue for each product in a structured format.

## Example Input

```python
data = [
    ('Books', 1343), ('Books', 1166), ('Merch', 616),
    ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
    ('Books', 848), ('Courses', 964), ('Tutorials', 832),
    ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
    ('Books', 1218), ('Tutorials', 880), ('Books', 1003),
    ('Merch', 951), ('Books', 920), ('Merch', 729),
    ('Tutorials', 977), ('Books', 656)
]
```

## Example Output 📜

```
Books: $7,969
Courses: $2,991
Merch: $4,082
Tutorials: $3,730
```

(Note: Thousand separators are added for better readability.)

## Output Format

Each product and its total revenue are displayed on a separate line in the following format:

```
<Product>: $<Total Revenue>
```

The products are sorted in alphabetical order.

## Usage 📦

To use the program:  
1️⃣ Ensure the list `data` contains valid product-revenue pairs.  
2️⃣ Run the script to calculate and display total revenue per product.

### Run the script:

```bash
$ python revenue_summary.py
```

## Conclusion 🚀

This program provides a simple yet efficient way to track and summarize revenue data for different products in an educational resource.
The results are formatted for clarity and easy interpretation.
