'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches character sequences of length 6 that
    simultaneously satisfy all of the following conditions:
        - the first character is a lowercase Latin letter
        - the second character is a digit, any letter in any case,
          or an underscore
        - the third character is an uppercase Latin letter
        - the fourth character must match the first character
        - the fifth character must match the second character
        - the sixth character must match the third character
'''
regex = r'([a-z])([\da-zA-Z_])([A-Z])\1\2\3'
