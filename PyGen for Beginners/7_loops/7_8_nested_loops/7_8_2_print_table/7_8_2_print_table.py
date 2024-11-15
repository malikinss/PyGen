'''
TODO:
    Given a natural number n, (n≤ 9).

    Write a program that prints a table of size n*5, where i-th line
    contains the number i (the numbers are separated by one space).
'''


def print_table(n):
    # Print n rows
    for i in range(1, n + 1):
        # In each row, print the number 'i' five times, separated by space
        for j in range(5):
            print(i, end=' ')

        # Move to the next line after each row
        print()


# Get input from the user
n = int(input())
# Call the function to print the table
print_table(n)
