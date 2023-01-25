#!python
"""https://adventofcode.com/2021/day/2

"Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?"
"""

import pandas as pd
import argparse


def process(input_path) -> int:
    df = pd.read_csv(input_path, header=None, delimiter=" ")
    forward_sum = sum(df[df[0]=="forward"][1].values)
    down_sum = sum(df[df[0]=="down"][1].values)
    up_sum = sum(df[df[0]=="up"][1].values)
    return forward_sum*(down_sum-up_sum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solves Advent of Code day 2.')
    parser.add_argument(
        'inputPath',
        help='''relative path to input file (in quotes).
Input file is a list of path movements.'''
    )    
    args = parser.parse_args()
    print(process(args.inputPath))
