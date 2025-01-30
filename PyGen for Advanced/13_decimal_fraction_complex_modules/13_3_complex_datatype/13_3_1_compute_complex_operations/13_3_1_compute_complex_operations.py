'''
TODO:
    Given two complex numbers, write a program that calculates and outputs
    their sum, difference, and product.
'''


def read_complex_number() -> complex:
    """
    Reads a complex number from input.

    Returns:
        complex: User-provided complex number.
    """
    return complex(input("Enter a complex number (e.g., 1+2j): "))


def compute_complex_operations(
    a: complex, b: complex
) -> tuple[complex, complex, complex]:
    """
    Computes the sum, difference, and product of two complex numbers.

    Args:
        a (complex): First complex number.
        b (complex): Second complex number.

    Returns:
        tuple[complex, complex, complex]: Sum, difference, and product.
    """
    return a + b, a - b, a * b


# Read complex numbers from user input
num1 = read_complex_number()
num2 = read_complex_number()

# Perform arithmetic operations
sum_result, diff_result, prod_result = compute_complex_operations(num1, num2)

# Print the results
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {diff_result}")
print(f"{num1} * {num2} = {prod_result}")
