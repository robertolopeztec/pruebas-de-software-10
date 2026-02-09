#!/usr/bin/python3
"""
Script that takes a file with a word per line and counts the frequency.
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
    str_values = []

    for v in values:
        try:
            str_values.append(str(v))
        except ValueError as e:
            print(e)

    return str_values

def count_words(str_values: list[str]):
    """
    Given a list of string values, thein iterate over all values within the list,
    check if exists and count.
    """

    count_word_dict = {}
    for str_val in str_values:
        if str_val not in count_word_dict:
            count_word_dict[str_val] = 1
        else:
            count_word_dict[str_val] += 1
    return count_word_dict

def print_and_save(count_word_dict: dict, file_name: str):
    """
    Given a dictionary then print the word and its frequency, and also
    save it in a file.
    """
    with open(f'../results/{file_name}', 'w', encoding='utf8') as f:
        for word, count in count_word_dict.items():
            output_string = f'WORD: {word} | COUNT {count}'
            print(output_string)
            f.write(output_string + '\n')
        f.close()

#----

if __name__ == '__main__':

    start_time = time.perf_counter()

    # Get the first argument when the script is called and
    # get the actual value
    file_path = sys.argv[1]
    file_name_ = file_path.split('/')[-1]

    values_ = read_values_from_file(file_path)
    count_words_ = count_words(values_)
    print_and_save(count_words_, file_name_)

    end_time = time.perf_counter()
    time_elapsed = end_time - start_time
    print('- Time elapsed', time_elapsed, 'seconds')
