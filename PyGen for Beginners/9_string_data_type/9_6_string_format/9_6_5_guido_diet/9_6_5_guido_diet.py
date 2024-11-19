'''
TODO:
    Guido, who is sitting at the computer and not leading an active lifestyle,
    has gained "a little" weight.

    There are only 60 days left until summer, but he wants to be in shape.

    So Guido decided to lose weight.

    He numbered all the days until summer from 1 to 60 (inclusive).

    Before starting to lose weight, Guido weighed 100 kg, and his goal was to
    reach a weight of 88 kg (or less).

    He decided to lose the same amount every day.

    Write a program that takes the current day and Guido's current weight
    as input.

    The program should output the phrase:
        - "Everything is going according to plan" (without quotes), if Guido
        manages to maintain the weight loss bar and his weight is lower than
        or equal to what he planned for the current day
        - "Something went wrong" (without quotes), if Guido is not trying very
        hard and his weight is higher than what he planned for the current day

    The program should also output information about the weight loss day
    number, Guido's current weight and the weight goal for the current day
    in the format:
        #<day number> DAY:
            CURRENT WEIGHT = <Guido's current weight> kg,
            WEIGHT GOAL = <weight goal for the current day> kg

NOTE:
    On the 1st day of weight loss, Guido should already have lost weight
    (see test 1).
'''


def check_weight_loss(current_day,
                      current_weight,
                      start_weight=100,
                      target_weight=88,
                      total_days=60):
    """
    This function checks if Guido's current weight is within the target
    for the given day.

    Parameters:
        current_day (int): The current day number (1 to 60).
        current_weight (float): Guido's current weight.
        start_weight (float): Guido's starting weight (default is 100 kg).
        target_weight (float): Guido's target weight (default is 88 kg).
        total_days (int): The total number of days (default is 60).

    Returns:
        str: Message indicating whether everything is going according
        to plan or if something went wrong.
    """
    # Calculate the daily target weight loss
    daily_target = (start_weight - target_weight) / total_days

    # Calculate the weight goal for the current day
    current_target_weight = start_weight - (current_day * daily_target)

    # Check if the weight is according to plan
    if current_weight <= current_target_weight:
        return "Everything is going according to plan", current_target_weight
    else:
        return "Something went wrong", current_target_weight


def main():
    # Input
    current_day = int(input("Enter the current day (1-60): "))
    current_weight = float(input("Enter Guido's current weight: "))

    # Call the function to check weight loss
    message, target_weight = check_weight_loss(current_day, current_weight)

    # Print the message and the result
    print(message)
    print(f"#{current_day} DAY: CURRENT WEIGHT = {current_weight:.2f} kg, WEIGHT GOAL = {target_weight:.2f} kg")


# Call the main function to run the program
main()
