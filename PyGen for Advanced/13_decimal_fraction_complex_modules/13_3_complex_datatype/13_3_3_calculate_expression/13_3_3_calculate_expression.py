'''
TODO:
    Given a natural number n and two complex numbers z1, z2.

    Write a program that calculates and outputs the value of the expression:
        z1^n + z2^n + conj(z1)^n + conj(z2)^(n+1)

NOTE:
    The number conj(z1) is the conjugate of the number z1.
'''


def calculate_expression(n: int, z1: complex, z2: complex) -> complex:
    """
    Calculates the value of the expression:
        z1^n + z2^n + conj(z1)^n + conj(z2)^(n+1)

    Args:
        n (int): Natural number.
        z1 (complex): First complex number.
        z2 (complex): Second complex number.

    Returns:
        complex: Result of the calculation.
    """
    result = pow(z1, n)
    result += pow(z2, n)
    result += pow(z1.conjugate(), n)
    result += pow(z2.conjugate(), n + 1)

    return result


# Read input values
n = int(input())
z1 = complex(input())
z2 = complex(input())

# Calculate result# Calculate result
result = calculate_expression(n, z1, z2)

# Print result
print(result)
