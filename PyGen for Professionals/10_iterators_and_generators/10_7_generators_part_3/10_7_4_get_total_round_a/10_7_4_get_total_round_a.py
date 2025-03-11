'''
TODO:
    You have access to the data.csv file, which contains information about
    investments in various startups. The first column contains the name of
    the company (startup), the second column contains the amount invested
    in dollars, and the third column contains the investment round:
        company,raisedAmt,round
        LifeLock,6850000,b
        LifeLock,6000000,a
        LifeLock,25000000,c
        MyCityFaces,50000,seed
        Flypaper,3000000,a
        ...

    Write a program using generator pipelines that determines the total amount
    invested in round a and outputs the result.

NOTE:
    The separator in the data.csv file is a comma, and quotation marks
    are not used.

    Example output:
        86900000000

    When opening the file, use an explicit UTF-8 encoding.
'''


def get_total_round_a(filename: str) -> int:
    """
    Calculates the total investment amount for round 'a' using generator
    pipelines.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        int: Total investment amount for round 'a'.
    """
    def parse_line(line):
        return line.strip().split(',')

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    headers = parse_line(lines[0])

    data_dicts = (
        dict(
            zip(headers, parse_line(line))
        ) for line in lines if line.strip()  # Skip empty lines
    )

    filtered_entries = (
        entry for entry in data_dicts
        if entry.get("round") == "a"
    )

    valid_entries = (
        int(entry["raisedAmt"]) for entry in filtered_entries
        if entry.get("raisedAmt", "").isdigit()
    )

    return sum(valid_entries)


print(get_total_round_a('data.csv'))
