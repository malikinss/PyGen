'''
TODO:
    Red, blue and yellow are called primary colors because they cannot be made
    by mixing other colors.

    When two primary colors are mixed, a secondary color is obtained:
        - if you mix red and blue, you get purple;
        - if you mix red and yellow, you get orange;
        - if you mix blue and yellow, you get green.

    Write a program that reads the names of two primary colors to blend.

    If the user enters anything other than the names "red", "blue",
    or "yellow", then the program should display an error message.

    Otherwise, the program should display the name of the secondary color that
    will be the result.

    The program should display the resulting blend color, or a "color error"
    message if a wrong color was entered.

NOTE:
    If you mix red and red, you get red, and so on.
'''
color_1 = input()
color_2 = input()

red = 'red'
blue = 'blue'
yellow = 'yellow'
orange = 'orange'
green = 'green'
purple = 'purple'

purple_mix_1 = (color_1 == red and color_2 == blue)
purple_mix_2 = (color_1 == blue and color_2 == red)

orange_mix_1 = (color_1 == red and color_2 == yellow)
orange_mix_2 = (color_1 == yellow and color_2 == red)

green_mix_1 = (color_1 == blue and color_2 == yellow)
green_mix_2 = (color_1 == yellow and color_2 == blue)

if purple_mix_1 or purple_mix_2:
    print(purple)
elif orange_mix_1 or orange_mix_2:
    print(orange)
elif green_mix_1 or green_mix_2:
    print(green)
elif (color_1 == color_2 == yellow):
    print(yellow)
elif (color_1 == color_2 == red):
    print(red)
elif (color_1 == color_2 == blue):
    print(blue)
else:
    print('color error')
