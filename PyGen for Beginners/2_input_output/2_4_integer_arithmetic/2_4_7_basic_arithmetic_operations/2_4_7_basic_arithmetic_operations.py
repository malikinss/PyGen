'''
TODO:
    Write a program that takes two numbers a and b as input, calculates
    the sum, difference, and product of these numbers, and outputs text in
    the following format:
        <number a> + <number b> = <sum of numbers a and b>
        <number a> - <number b> = <difference of numbers a and b>
        <number a> * <number b> = <product of numbers a and b>
'''
a = int(input())
b = int(input())

sum_result = a + b
difference_result = a - b
product_result = a * b

print(a, '+', b, '=', sum_result)
print(a, '-', b, '=', difference_result)
print(a, '*', b, '=', product_result)
