'''
TODO:
    Write a program that uses exactly three for loops to print the following
    sequence of characters:
        AAA
        AAA
        AAA
        AAA
        AAA
        AAA
        BBBB
        BBBB
        BBBB
        BBBB
        BBBB
        E
        TTTTT
        TTTTT
        TTTTT
        TTTTT
        TTTTT
        TTTTT
        TTTTT
        TTTTT
        TTTTT
        G
'''

# Define the character sequences
row_A = 'AAA'
row_B = 'BBBB'
row_T = 'TTTTT'

# Print row_A six times
for _ in range(6):
    print(row_A)

# Print row_B five times
for _ in range(5):
    print(row_B)

# Print a single 'E'
print('E')

# Print row_T nine times
for _ in range(9):
    print(row_T)

# Print a single 'G'
print('G')
