'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches strings that satisfy all of the following
    conditions:
        - the string begins with two or more digits
        - is followed by zero or more lowercase Latin letters
        - the string ends with zero or more uppercase Latin letters
'''
regex = r'^\d{2,}[a-z]*[A-Z]*$'
