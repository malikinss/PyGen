'''
TODO:
    Complete the code below so that the regex variable contains a regular
    expression that matches North American phone numbers that satisfy all of
    the following conditions:
        - the phone number begins with a three-digit area code, which may be
          enclosed in parentheses
        - followed by a space or hyphen, a seven-digit number separated by
          a three-digit prefix and a four-digit line number, separated by
          a hyphen

    A phone number can use any digits with two exceptions: the first digit of
    the area code and the first digit of the prefix cannot be 0 or 1.
'''

area_code = r'(\([2-9]\d{2}\)|[2-9]\d{2})'
separator = r'[- ]?'
number = r'[2-9]\d{2}-\d{4}'

regex = f'{area_code}{separator}{number}'
