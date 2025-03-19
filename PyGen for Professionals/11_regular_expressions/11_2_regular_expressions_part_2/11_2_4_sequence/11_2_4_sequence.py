'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches character sequences of length 5 that
    simultaneously satisfy all of the following conditions:
        - the first character is a lowercase Latin letter
        - the second character is an arbitrary digit
        - the third character is a lowercase Latin letter
        - the fourth character is an uppercase Latin letter
        - the fifth character is an uppercase Latin letter
'''
regex = r'[a-z]\d[a-z][A-Z]{2}'
