'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches strings of length 45 that simultaneously satisfy
    all of the following conditions:
        - the first 40 characters are uppercase or lowercase Latin letters or
          even digits
        - the last 5 characters are odd digits or space characters
'''
regex = r'^[a-zA-Z02468]{40}[13579 ]{5}$'
