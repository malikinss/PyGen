'''
TODO:
    Given a natural number n, (n≤ 9).

    Write a program that prints an n*3 table consisting of a given number
    (the numbers are separated by a single space).
'''


def print_table(n):
    # Print n rows
    for i in range(n):
        # In each row, print 'n' three times, separated by space
        for j in range(3):
            print(n, end=' ')

        # Move to the next line after each row
        print()


# Get input from the user
n = int(input())
# Call the function to print the table
print_table(n)
