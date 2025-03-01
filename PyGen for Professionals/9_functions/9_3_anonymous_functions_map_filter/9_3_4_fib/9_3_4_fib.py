'''
TODO:
        Using anonymous function syntax, implement a recursive function fib()
        that takes one argument:
            n is a natural number

        The function should return the n-th term of the Fibonacci sequence.

NOTE:
        The Fibonacci sequence is a sequence of natural numbers where each
        subsequent number is the sum of the two preceding ones:
            1,1,2,3,5,8,13,21,34,55,89,144,233,...
'''


def fib(n: int) -> int:
    return lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
