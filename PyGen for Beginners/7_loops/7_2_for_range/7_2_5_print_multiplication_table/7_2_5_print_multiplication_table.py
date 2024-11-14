'''
TODO:
    Given a natural number n.
    Write a program that prints the multiplication table for n
    (from 1 to 10 inclusive).
'''


def print_multiplication_table(n: int) -> None:
    """
    Prints the multiplication table for a given natural number n
    (from 1 to 10 inclusive).

    Args:
        n (int): The number for which the multiplication table is generated.

    Returns:
        None
    """
    for i in range(1, 11):
        result = i * n
        print(f"{n} x {i} = {result}")


# Input data
n = int(input("Enter a natural number (n): "))

# Call the function
print_multiplication_table(n)
