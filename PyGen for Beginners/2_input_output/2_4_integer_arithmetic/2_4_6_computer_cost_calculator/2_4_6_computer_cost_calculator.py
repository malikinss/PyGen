'''
TODO:
    Write a program that calculates the cost of three computers consisting of
    a monitor, a system unit, a keyboard, and a mouse.

    The program receives four integers (each on a separate line) as input:
        - the cost of the monitor
        - the cost of the system unit
        - the cost of the keyboard
        - the cost of the mouse.

    The program should output one number:
        - the cost of the purchase (three computers).
'''
monitor_cost = int(input("Enter the cost of the monitor: "))
system_unit_cost = int(input("Enter the cost of the system unit: "))
keyboard_cost = int(input("Enter the cost of the keyboard: "))
mouse_cost = int(input("Enter the cost of the mouse: "))

# Calculate the total cost of one computer
cost_of_one_computer = monitor_cost + system_unit_cost + keyboard_cost + mouse_cost

# Calculate the total cost of three computers
total_cost = cost_of_one_computer * 3

print(total_cost)
