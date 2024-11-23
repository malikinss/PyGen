'''
TODO:
    Complete the given code so that the list item with the
    Green value is replaced with the Pink value, and the Violet
    item with the Grey value.

    Next, you need to display the resulting list.
'''

# original code
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']


# fixed code
def replace_colors(rainbow):
    """
    Replaces 'Green' with 'Pink' and 'Violet' with 'Grey' in the rainbow list.
    """
    rainbow[3] = 'Pink'  # Replace 'Green' with 'Pink'
    rainbow[-1] = 'Grey'  # Replace 'Violet' with 'Grey'

    return rainbow


# Original list of colors
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# Call the function and print the modified list
print(replace_colors(rainbow))
