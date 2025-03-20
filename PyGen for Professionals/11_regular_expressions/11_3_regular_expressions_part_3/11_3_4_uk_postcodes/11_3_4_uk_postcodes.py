'''
TODO:
    Complete the code below so that the regex variable contains a regular
    expression that matches UK postcodes that satisfy all of the following
    conditions simultaneously:
        - the postcode begins with one or two uppercase Latin letters,
          followed by one digit.
          The digit may be followed by one optional character - a digit or
          uppercase Latin letter
        - followed by one digit and any two uppercase Latin letters except
          C, I, K, M, O, V, separated by a space
'''
regex = r'[A-Z]{1,2}\d[A-Z0-9]? \d[ABDEFGHJLNPQRSTUWXYZ]{2}'
