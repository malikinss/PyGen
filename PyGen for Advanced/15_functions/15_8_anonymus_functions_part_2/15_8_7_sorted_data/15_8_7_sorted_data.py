'''
TODO:
    The list data contains population information for some US states.

    Write a program to sort the list data in descending order based on
    the last character in the state name.

    Then print the elements of the list, each on a new line, in the format:
        <state name>: <population>

        Vermont: 626299
        Massachusetts: 7029917
...

NOTE:
    The sorting is lexicographic (alphabetical) in descending order based
    on the last character in the state name.

    However, if two states have the same last character, their relative
    positions in the original list should be preserved.

    Use an anonymous function as the sort criterion.
'''
data = [
    (19542209, 'New York'), (4887871, 'Alabama'),
    (1420491, 'Hawaii'), (626299, 'Vermont'),
    (1805832, 'West Virginia'), (39865590, 'California'),
    (11799448, 'Ohio'), (10711908, 'Georgia'),
    (10077331, 'Michigan'), (10439388, 'Virginia'),
    (7705281, 'Washington'), (7151502, 'Arizona'),
    (7029917, 'Massachusetts'), (6910840, 'Tennessee')
]

# Sort the data in descending order based on the last character
# of the state name.
# If two states have the same last character, their original
# order is preserved.
sorted_data = sorted(data, key=lambda item: item[1][-1], reverse=True)

# Print each state and its population on a new line.
for population, state in sorted_data:
    print(f"{state}: {population}")
