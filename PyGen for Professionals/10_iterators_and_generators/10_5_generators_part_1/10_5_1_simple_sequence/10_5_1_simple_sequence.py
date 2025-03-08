'''
TODO:
    Implement a generator function simple_sequence() that takes no arguments.

    The function should return a generator that produces an infinite
    increasing sequence of natural numbers, in which each number occurs
    as many times as it is:
        1,2,2,3,3,3,4,4,4,4,..
'''


def simple_sequence():
    """
    A generator function that produces an infinite sequence where each natural
    number appears as many times as its value.

    Yields:
        int: The next number in the sequence.
    """
    num = 1
    count = 0

    while True:
        yield num
        count += 1
        if count == num:
            num += 1
            count = 0
