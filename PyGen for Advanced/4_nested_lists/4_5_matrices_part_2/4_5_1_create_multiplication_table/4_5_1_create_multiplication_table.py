'''
TODO:
    The program is fed two natural numbers n and m, the number of rows
    and columns in the matrix, as input.

    Create a matrix mult of size n*m and fill it with a multiplication table
    using the formula mult[i][j] = i * j.
'''


def create_multiplication_table(n: int, m: int) -> None:
    """
    Creates and prints a multiplication table of size n x m.

    Args:
        n (int): Number of rows.
        m (int): Number of columns.
    """
    for i in range(n):
        row_string = ''
        for j in range(m):
            # Create the multiplication value and align
            # it for a clean table format
            row_string += f"{i * j:3}"
        print(row_string)


def main() -> None:
    """
    Main function to read input and create the multiplication table.
    """
    n: int = int(input())  # Number of rows
    m: int = int(input())  # Number of columns

    create_multiplication_table(n, m)


if __name__ == "__main__":
    main()
