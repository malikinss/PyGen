'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches words written twice in a row.

    Words can be separated by one or more spaces.

NOTE:
    A word is a sequence of characters matching \\w surrounded by characters
    matching \\W
'''
regex = r'(\b\w+\b)\s+\b\1\b'
