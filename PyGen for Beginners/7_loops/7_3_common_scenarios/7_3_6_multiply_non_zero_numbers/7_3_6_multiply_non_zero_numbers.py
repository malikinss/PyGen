'''
TODO:
    Write a program that reads 10 numbers and prints the result
    of multiplication of non-zero numbers.
'''


def multiply_non_zero_numbers():
    """
    Reads 10 numbers from the user and calculates the product
    of non-zero numbers.
    If no non-zero numbers are entered, it prints 0.
    """
    total = 1
    count_non_zero = 0  # This will track the number of non-zero numbers

    for i in range(10):
        number = int(input(f"Enter number {i+1}: "))

        if number != 0:
            total *= number
            count_non_zero += 1

    # If no non-zero numbers were entered, print 0
    if count_non_zero == 0:
        print(0)
    else:
        print(total)


# Call the function
multiply_non_zero_numbers()
