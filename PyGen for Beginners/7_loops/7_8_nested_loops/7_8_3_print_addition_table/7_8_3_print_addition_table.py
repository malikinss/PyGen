'''
TODO:
    Given a natural number n, (n ≤ 9).

    Write a program that prints an addition table for all numbers
    from 1 to n (inclusive) according to the example.
'''


def print_addition_table(n):
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # For each i, print the addition table with numbers 1 to 9
        for j in range(1, 10):
            a = i + j
            print(f"{i} + {j} = {a}")
        print()  # Print an empty line after each row of the table


# Get input from the user
n = int(input())
# Call the function to print the addition table
print_addition_table(n)
