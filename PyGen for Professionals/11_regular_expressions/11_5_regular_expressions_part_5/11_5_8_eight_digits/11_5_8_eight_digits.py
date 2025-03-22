'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches sequences of 8 digits.

    Moreover, the sequence can contain hyphens - as separators, only if they
    divide it into groups of 2 digits.
'''
regex = r'(\d{8})|(\d{2})(-\d{2}){3}'
