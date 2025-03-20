'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches strings that satisfy all of the following
    conditions simultaneously:
        - the string begins with Mr., Mrs., Ms., Dr., or Er.
        - the rest of the string consists of only one or more uppercase Latin
          letters
'''
regex = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'
