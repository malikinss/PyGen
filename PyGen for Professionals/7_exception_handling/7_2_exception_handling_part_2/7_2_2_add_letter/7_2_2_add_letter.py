'''
TODO:
    You have a program that adds the fifth letter of each word in the food
    list to the list fifth.

    If a word does not have a fifth letter, the _ character is assumed to be
    that letter.

    Add a try-except construct to the code below to ensure that it runs
    without errors.
'''
food = [
    'chocolate', 'chicken', 'corn',
    'sandwich', 'soup', 'potatoes',
    'beef', 'lox', 'lemonade'
]

fifth = []

for x in food:
    try:
        letter_to_add = x[4]
    except IndexError:
        letter_to_add = '_'

    fifth.append(letter_to_add)

print(fifth)
