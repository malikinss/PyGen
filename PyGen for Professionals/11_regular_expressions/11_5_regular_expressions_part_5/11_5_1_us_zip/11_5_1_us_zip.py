'''
TODO:
    Complete the code below so that the regex variable contains a regular
    expression that matches U.S. ZIP Codes that satisfy the following
    conditions:
        - the ZIP Code starts with five digits
        - followed by an optional four-digit portion that is separated from
          the first five digits by a hyphen
'''
regex = r'\d{5}(-\d{4})?'
