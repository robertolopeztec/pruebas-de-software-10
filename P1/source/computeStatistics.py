"""
Script that reads a file and computes statistics.
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
    float_values = []

    for v in values:
        try:
            float_values.append(float(v))
        except ValueError as e:
            print(e)

    return float_values

def compute_mean(values: list[float]):
    """
    Given a list of float values, compute the mean

    values: A list that contains the values as float
    """
    return sum(values) / len(values)

def compute_median(values: list[float]):
    """
    Given a list of float values, compute the median.
    Meaning the value that splits the values evenly, or is at positioned at the middle
    of the array.

    values: A list that contains the values as float
    """

    # First order the values
    sorted_values = sorted(values)
    len_values = len(values)

    # Find the middle index
    mid = len_values // 2

    if len_values % 2 == 0:
        # If even, average the two middle numbers
        median = (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        # If odd, return the middle number
        median = sorted_values[mid]
    return median

def compute_mode(values: list[float]):
    """
    Given a list of float values, compute the mode.
    Meaning the most frequent value.

    values: A list that contains the values as float
    """

    # Generate a dictionary to keep the values and its frequency
    value_freq = {}

    for v in values:
        if v not in value_freq:
            value_freq[v] = 1
        else:
            value_freq[v] += 1

    # Reverse Sort based on the frequency and get the first value
    mode = sorted(value_freq.items(), key=lambda v: v[1], reverse=True)[0][0]
    return mode

def compute_standard_deviation(values: list[float]):
    """
    Given a list of float values, computes the standard deviation.
    Meaning that it will get the squared root of the sum of squared differences
    between the actual value and the mean, divided by the number of items minus 1.

    """

    # First compute the mean
    mean = compute_mean(values)

    # Then, compute the squared difference of the current value minus the mean
    # for each of the value in values
    sum_squared_diffs = sum((v - mean) ** 2 for v in values)

    # Get the number of values
    n = len(values)

    # Now compute the actual formula
    standard_deviation = ( sum_squared_diffs / (n - 1) ) ** (0.5)
    return standard_deviation

def compute_variance(values: list[float]):
    """
    Given a list of float values, compute the variance.
    In other terms, the variance is the squared standard deviation.
    """

    standard_deviation = compute_standard_deviation(values)
    variance = standard_deviation ** 2
    return variance

#----

if __name__ == '__main__':

    start_time = time.perf_counter()

    # Get the first argument when the script is called and
    # get the actual value
    file_path = sys.argv[1]
    values_ = read_values_from_file(file_path)

    # Compute the statistical values
    mean_ = compute_mean(values_)
    median_ = compute_median(values_)
    mode_ = compute_mode(values_)
    standard_deviation_ = compute_standard_deviation(values_)
    variance_ = compute_variance(values_)

    statistics = [mean_, median_, mode_, standard_deviation_, variance_]
    statistics_name = ['mean', 'median', 'mode', 'std. dev', 'variance']

    for s_name, s in zip(statistics_name, statistics):
        print('-', s_name, ':', s)

    end_time = time.perf_counter()
    time_elapsed = end_time - start_time
    print('- Time elapsed', time_elapsed, 'seconds')
