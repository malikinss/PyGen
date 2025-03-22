'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches sequences of 8 digits that satisfy the following
    conditions:
        - the sequence can contain -, ---, or . as separators only if they
          divide it into groups of 2 digits
        - the sequence must contain only one type of separator, if present
'''
regex = r'\d{2}((-|---|\.)?)\d{2}\1\d{2}\1\d{2}'
