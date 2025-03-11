'''
TODO:
    You have access to a file called planets.txt, which contains information
    about various planets.

    The first four lines contain the characteristics of the first planet,
    followed by a blank line, then the characteristics of the second planet,
    and so on:
        Name = Mercury
        Diameter = 4879.4
        Mass = 3.302*10^23
        OrbitalPeriod = 0.241

        Name = Venus
        Diameter = 12103.6
        Mass = 4.869*10^24
        OrbitalPeriod = 0.615

    ...
    Implement a generator function txt_to_dict() that takes no arguments.

    The function should return a generator that produces a sequence of
    dictionaries, each of which contains information about the next planet
    from the planets.txt file, namely its name, diameter, mass,
    and orbital period.

    For example:
        {
            'Name': 'Mercury',
            'Diameter': '4879.4',
            'Mass': '3.302*10^23',
            'OrbitalPeriod': '0.241'
        }
'''
from typing import Generator, Dict, Union


def read_lines(file_path: str) -> Generator[str, None, None]:
    """
    Reads lines from a file, yielding each line.

    Args:
        file_path (str): The path to the file to be read.

    Yields:
        str: Each line from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def parse_mass(value: str) -> float:
    """
    Convert a mass value in scientific notation to a float.

    Args:
        value (str): A mass value in the form of 'a*10^b'.

    Returns:
        float: The mass converted to a float.
    """
    a, b = value.split('*')
    b, c = b.split('^')
    return float(a) * (float(b) ** float(c))


def parse_line(line: str) -> Dict[str, Union[str, float]]:
    """
    Parse a single line into a key-value pair.

    Args:
        line (str): A line containing 'key = value' format.

    Returns:
        dict: A dictionary with one key-value pair.
    """
    key, value = line.split(' = ')
    return {key: value}


def group_planet_data(
    lines: Generator[str, None, None]
) -> Generator[Dict[str, Union[str, float]], None, None]:
    """
    Groups lines into planet data dictionaries.

    Args:
        lines (Generator[str, None, None]): A generator that yields lines from
        the file.

    Yields:
        dict: A dictionary containing the planet's Name, Diameter, Mass,
        and OrbitalPeriod.
    """
    planet_data = {
        'Name': '',
        'Diameter': 0.0,
        'Mass': 0.0,
        'OrbitalPeriod': 0.0
    }

    for line in lines:
        if not line:
            if planet_data['Name']:
                yield planet_data

            # Reset planet data
            planet_data = {
                'Name': '',
                'Diameter': 0.0,
                'Mass': 0.0,
                'OrbitalPeriod': 0.0
            }
            continue

        key_value = parse_line(line)
        planet_data.update(key_value)

    # Yield the last planet data
    if planet_data['Name']:
        yield planet_data


def txt_to_dict() -> Generator[Dict[str, Union[str, float]], None, None]:
    """
    Main generator function to process the planets data and return planet
    dictionaries.

    Yields:
        dict: A dictionary containing the planet's Name, Diameter, Mass,
            and OrbitalPeriod.
    """
    return group_planet_data(read_lines('planets.txt'))
