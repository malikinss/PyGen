# Lottery Ticket Generator 🎟️

## Description 📝

This program generates 100 unique 7-digit lottery ticket numbers using the `random` module.
Each ticket number is randomly generated between 1,000,000 and 9,999,999 and ensures that no ticket number starts with zero.
The generated numbers are guaranteed to be unique.

## Purpose 🎯

The program's main purpose is to generate and output 100 unique lottery ticket numbers.
This can be useful in simulations, lotteries, or as a part of larger systems requiring random unique identifiers.

## How It Works 🔍

1. **Input**:
    - No user input is required. The program automatically generates 100 unique ticket numbers.
2. **Processing**:
    - A random 7-digit number is generated using `random.randint()`. The number is constrained to the range of 1,000,000 to 9,999,999 to ensure it is always a 7-digit number.
    - The program ensures that all generated numbers are unique by storing them in a set (sets automatically handle uniqueness).
3. **Output**:
    - The program prints all 100 unique ticket numbers, each on a separate line.

## Output 📜

Each generated lottery ticket number is printed on a separate line, and all ticket numbers are guaranteed to be unique.

### Example:

The output may look something like this:

```
1234567
7654321
8901234
2345678
...
```

## Usage 📦

1. Copy the code into a Python file (e.g., `lottery_ticket_generator.py`).
2. The program will automatically generate 100 unique lottery tickets.
3. The generated ticket numbers will be printed, each on a separate line.

### Example Run:

```python
tickets = generate_lottery_tickets()
print(*tickets, sep='\n')
```

## Conclusion 🚀

This program effectively demonstrates how to generate and output unique 7-digit lottery ticket numbers using Python.
It ensures the uniqueness of the ticket numbers and adheres to the format requirements specified.
