# Book Sales Income Calculation

## Description 📝

This Python program calculates the total income Timur will earn by selling books to customers.
The program reads the stock of books available for different classes and processes customer requests.
Each customer specifies the class of the book they want and the amount they are willing to pay.
If a book is available, it is sold to the customer.

## Purpose 🎯

The program keeps track of available books by class, handles customer requests, and calculates the total income based on the books sold and the price each customer offers.

## How It Works 🔍

1. **Reading Available Books**: The first input line contains a sequence of numbers representing the available books. Each number corresponds to a class number, and its frequency indicates how many books for that class are in stock.
2. **Processing Customer Requests**: The program then reads the number of customers and their respective requests, which include the class number and the price they are willing to pay for the book.
3. **Selling Books**:
    - The program checks if there is a book available for the requested class.
    - If the book is available, it is sold at the price the customer offers, and the stock of that class is reduced by one.
4. **Output**: The program prints the total income from the books sold.

## Output 📜

The program outputs a single integer, which is the total income Timur earned from selling books.

### Example:

#### Input:

```
2 1 11 9 9 9 5 5 7
7
1 300
1 250
11 400
7 200
9 400
9 300
5 150
```

#### Output:

```
1550
```

## Usage 📦

1. The first line of input should contain a sequence of integers representing the available books in stock.
2. The second line should contain an integer representing the number of customers.
3. For each customer, the next line should contain two integers: the class number and the price offered.

### Example:

```bash
python book_sales.py
```

#### Input Example:

```
2 1 11 9 9 9 5 5 7
7
1 300
1 250
11 400
7 200
9 400
9 300
5 150
```

#### Output Example:

```
1550
```

## Conclusion 🚀

This program efficiently tracks book sales and calculates the total income based on customer requests and available stock.
It is useful for managing sales in businesses with limited stock and variable customer demand.
