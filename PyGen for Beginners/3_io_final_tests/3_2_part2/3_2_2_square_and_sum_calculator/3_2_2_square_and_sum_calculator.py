'''
TODO:
    Write a program that reads two integers a and b and prints the square of
    the sum ((a+b)^2) and the sum of the squares (a^2 + b^2) of these numbers
    in the following format:

    The square of the sum of <a> and <b> is <the square of the sum of a and b>

    The sum of the squares of <a> and <b> is <the sum of the squares of a and b>
'''
num1 = int(input())
num2 = int(input())

square_of_sum = (num1 + num2) ** 2
sum_of_squares = (num1 ** 2) + (num2 ** 2)

print('The square of the sum of', num1, 'and', num2, 'is equal to', square_of_sum)
print('The sum of the squares of', num1, 'and', num2, 'is equal to', sum_of_squares)
