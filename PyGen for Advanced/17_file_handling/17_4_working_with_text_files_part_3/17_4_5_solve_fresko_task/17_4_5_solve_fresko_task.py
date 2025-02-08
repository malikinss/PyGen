'''
TODO:
    One day, Jacques Fresco was asked:
        - "If you're so smart, why aren't you rich?"

    Jacques did not answer such a provocative question, instead he asked the
    questioner a riddle:

        - "There were colorful goats. How much?"
        - "How much of what?"
        - "How many of them make up more than 7% of the total number of goats?"

    A text file is available to you "goats.txt " in the first line of which
    the word COLORS is written, then there is a list of all possible colors
    of goats.

    Then there is a line with the word GOATS, and then directly the
    enumeration of goats of different colors.

    The list of goats includes only the lines from the first list.

    Write a file creation program "answer.txt " and the output of a list of
    goats that satisfy the condition of the riddle from Jacques Fresco.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''
from typing import List, Dict
from collections import Counter


def read_data_from_file(file_name: str) -> List[str]:
    """
    Reads the content of a file and returns it as a list of lines without
    trailing newline characters.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        List[str]: A list of lines from the file, with each line being
                   a string.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def write_data_to_file(file_name: str, data: List[str]) -> None:
    """
    Writes a list of strings to a file, ensuring each string is written on
    a new line.

    Args:
        file_name (str): The name of the file to write to.
        data (List[str]): A list of strings to write to the file.

    Returns:
        None
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        if data:
            file.writelines(f"{line}\n" for line in data)
        else:
            file.write("")


def get_available_colors(data: List[str]) -> List[str]:
    """
    Extracts available goat colors from the input data.

    Args:
        data (List[str]): A list of strings containing color names and goat
                          data.

    Returns:
        List[str]: A list of available goat colors.
    """
    start_idx = data.index("COLOURS") + 1
    end_idx = data.index("GOATS")
    return data[start_idx:end_idx]


def count_goat_colors(goat_list: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of each goat color in the provided list.

    Args:
        goat_list (List[str]): A list of goat colors.

    Returns:
        Dict[str, int]: A dictionary with goat colors as keys and their counts
                        as values.
    """
    return dict(Counter(goat_list))


def calculate_color_percentages(
    color_counts: Dict[str, int], total_goats: int
) -> Dict[str, float]:
    """
    Calculates the percentage of each goat color relative to the total number
    of goats.

    Args:
        color_counts (Dict[str, int]): A dictionary mapping colors to their
                                       counts.
        total_goats (int): The total number of goats.

    Returns:
        Dict[str, float]: A dictionary mapping colors to their percentage of
                          the total.
    """
    return {
        color: (count / total_goats) * 100
        for color, count in color_counts.items()
    }


def filter_colors_by_percentage(
    color_percentages: Dict[str, float], threshold: float
) -> List[str]:
    """
    Filters goat colors that exceed a given percentage threshold.

    Args:
        color_percentages (Dict[str, float]): A dictionary mapping colors to
                                              their percentages.
        threshold (float): The percentage threshold to filter by.

    Returns:
        List[str]: A list of colors exceeding the threshold, sorted
                   alphabetically.
    """
    return sorted([
        color
        for color, percentage in color_percentages.items()
        if percentage > threshold
    ])


def process_goat_data(data: List[str]) -> List[str]:
    """
    Processes the input data to find goat colors that make up more than 7% of
    the total.

    Args:
        data (List[str]): A list of strings containing color names and goat
                          data.

    Returns:
        List[str]: A sorted list of goat colors that make up more than 7% of
                   the total.
    """
    goat_list = data[data.index("GOATS") + 1:]

    color_counts = count_goat_colors(goat_list)
    color_percentages = calculate_color_percentages(
        color_counts, len(goat_list)
    )

    return filter_colors_by_percentage(color_percentages, 7.0)


def solve_fresko_task(input_file: str, output_file: str) -> None:
    """
    Solves the Fresko riddle by processing goat data from an input file and
    writing the result to an output file.

    Args:
        input_file (str): The name of the input file containing goat data.
        output_file (str): The name of the output file where the result will
                           be saved.

    Returns:
        None
    """
    input_data = read_data_from_file(input_file)
    result = process_goat_data(input_data)
    write_data_to_file(output_file, result)


solve_fresko_task("goats.txt", "answer.txt")
