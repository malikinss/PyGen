'''
TODO:
    Write a program to calculate and estimate a person's body mass index (BMI).

    BMI shows whether a person weighs more or less than normal for his height.

    A person's BMI is calculated using the formula:
        BMI = mass / height^2
    where mass is measured in kilograms and height in meters.

    A person's weight is considered optimal if his BMI is between 18.5 and 25.

    If the BMI is less than 18.5, then the person is considered
    to be underweight.

    If the BMI value is more than 25, then the person is considered
    to be overweight.

    The program should output:
        "Optimal weight" if the BMI is between 18.5 and 25 (inclusive).
        "Underweight" if BMI is less than 18.5.
        "Overweight" if the BMI value is greater than 25.
'''


def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculates the Body Mass Index (BMI) using the formula:
        BMI = weight / height^2

    Args:
        weight (float): Person's weight in kilograms.
        height (float): Person's height in meters.

    Returns:
        float: The calculated BMI value.
    """
    return weight / height ** 2


def classify_bmi(bmi: float) -> str:
    """
    Classifies the BMI into one of three categories:
    - "Underweight" if BMI is less than 18.5.
    - "Optimal weight" if BMI is between 18.5 and 25 (inclusive).
    - "Overweight" if BMI is greater than 25.

    Args:
        bmi (float): The calculated BMI value.

    Returns:
        str: Classification of the BMI.
    """
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 25:
        return 'Optimal weight'
    else:
        return 'Overweight'


def main() -> None:
    """
    Main function to take input for weight and height, calculate BMI,
    and print the weight classification based on the BMI.
    """
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)

    print(classification)


if __name__ == "__main__":
    main()
