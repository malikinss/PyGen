'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches strings that satisfy all of the following
    conditions simultaneously:
        - the string begins with one or two digits
        - followed by three or more uppercase Latin letters
        - the string ends with three or fewer dots
'''
regex = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'
