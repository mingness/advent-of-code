#!python
"""https://adventofcode.com/2021/day/1

"The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something."

"To do this, count the number of times a depth measurement increases from the previous measurement."
"Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?"
"""

import pandas as pd
import argparse


def process(input_path) -> int:
    df = pd.read_csv(input_path, header=None)
    input_array = df[0].values
    sum_window = input_array[:-2] + input_array[1:-1] + input_array[2:] 
    diffs = sum_window[1:] - sum_window[:-1]
    diffs_inc = [diff for diff in diffs if diff > 0]
    return len(diffs_inc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solves Advent of Code day 1.')
    parser.add_argument(
        'inputPath',
        help='''Relative path to input file. Input file is a list of elevations.'''
    )    
    args = parser.parse_args()
    print(process(args.inputPath))
