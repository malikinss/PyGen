'''
TODO:
    Edit the code below to:
        Displayed the length of the list;
        Displayed the last element of the list;
        Displayed the list in reverse order (remember slices);
        Printed YES if the list contains the numbers 5 and 17,
        and NO otherwise;
        Outputted a list with the first and last elements removed.

NOTE:
    Each output is carried out on a new line.
'''

# original code
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8,
           5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2,
           10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# fixed code
print(len(numbers))  # Display the length of the list
print(numbers[-1])  # Display the last element of the list
print(numbers[::-1])  # Display the list in reverse order

if 5 in numbers and 17 in numbers:  # Check if the list contains 5 and 17
    print('YES')
else:
    print('NO')

# Remove the first and last elements from the list
numbers = numbers[1:-1]
print(numbers)  # Display the modified list
