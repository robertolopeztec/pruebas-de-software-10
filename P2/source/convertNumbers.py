#!/usr/bin/python3
"""
This script converts numbers into binary and hexadecimal base.
"""

import sys
import time

#---
# Functions
def read_values_from_file(path: str):
    """
    This function reads the file and returns a list with the found values

    path: the path of the file to be read
    """
    with open(path, 'r', encoding='utf8') as f:
        values = f.read().splitlines()
    f.close()

    # Now, convert the values into float-like
    int_values = []

    for v in values:
        try:
            int_values.append(int(v))
        except ValueError as e:
            print(e)
    return int_values

def convert_into_binary_and_hexa(value: float):
    """
    Takes a float value and converts it into binary or hexadecimal.
    """
    return format(value, 'b'), format(value, 'X')


def iterate_and_convert(values: list[int]):
    """
    Iterate over a list of integers and convert it into binary and hexadecimal values.
    """

    # Generate a 3-items tuple with values and its convertions
    convertions = [
        (value, *convert_into_binary_and_hexa(value))
        for value in values
    ]

    convertions_strings = [
        f"NUMBER: {value} | BINARY: {binary} | HEXADECIMAL: {hexadecimal}"
        for (value, binary, hexadecimal) in convertions
    ]
    return convertions_strings

def print_and_write(convertions_strings: list[str], file_name: str):
    """
    Given a list of strings with a number and its convertions, then
    print each of the lines and write it in a new file.
    """

    # Now iterate over each of the strings, print it and write it
    with open(f'../results/{file_name}', 'w', encoding='utf8') as f:
        for convertion_string in convertions_strings:
            print(convertion_string)
            f.write(convertion_string + '\n')
        f.close()

if __name__ == '__main__':
    start_time = time.perf_counter()
    # Get the first argument when the script is called and
    # get the actual value
    file_path = sys.argv[1]
    file_name_ = file_path.split('/')[-1]

    values_ = read_values_from_file(file_path)
    convertions_strings_ = iterate_and_convert(values_)
    print_and_write(convertions_strings_, file_name_)

    end_time = time.perf_counter()
    time_elapsed = end_time - start_time
    print('- Time elapsed', time_elapsed, 'seconds')
