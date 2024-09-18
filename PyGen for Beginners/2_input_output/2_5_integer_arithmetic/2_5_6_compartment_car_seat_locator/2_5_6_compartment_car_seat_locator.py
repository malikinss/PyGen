'''
TODO:
    A compartment car has 9 compartments with four passenger seats in each.

    Write a program that determines the number of the compartment in which
    a seat with a given number is located (seat numbering is continuous,
    starting with 1).
'''
seat_number = int(input("Enter the seat number: "))

# Calculate the compartment number. Each compartment has 4 seats.
compartment_number = (seat_number - 1) // 4 + 1

print(compartment_number)
