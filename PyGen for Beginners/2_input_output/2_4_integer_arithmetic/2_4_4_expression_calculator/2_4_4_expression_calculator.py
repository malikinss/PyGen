'''
TODO:
    Write a program that, given integer values a and b, calculates the value
    of the following expression:
        3(a+b)^3 + 275b^2 - 127a - 41

NOTE:
    Please note that at this stage of the tutorial we are not yet familiar
    with the exponentiation operator.

    Therefore, we will use the standard definition of a power of a number:
        the number is multiplied by itself the specified number of times.

        For example:
            a^4=a⋅a⋅a⋅a
'''
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Calculate (a + b)^3
a_plus_b = a + b
a_plus_b_cubed = a_plus_b * a_plus_b * a_plus_b

# Calculate the result
result = 3 * a_plus_b_cubed + 275 * (b * b) - 127 * a - 41

# Print the result
print(result)
