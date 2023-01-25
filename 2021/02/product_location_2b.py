#!python
"""https://adventofcode.com/2021/day/2

"In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

"Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?"

Answer:
1568138742
"""

import argparse
from typing import List, Tuple


def process(lines: List[Tuple[str, str]]) -> int:
    aim = 0
    horizontal = 0
    depth = 0
    for mode, amount_str in lines: 
        amount = int(amount_str)
        if mode == "down":
            aim += amount
        elif mode == "up":
            aim += -amount
        elif mode == "forward":
            horizontal += amount
            depth += amount*aim

    return horizontal*depth


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solves Advent of Code day 2.')
    parser.add_argument(
        'inputPath',
        help='''relative path to input file (in quotes).
Input file is a list of path movements.'''
    )    
    args = parser.parse_args()
    with open(args.inputPath, "r") as f:
        lines = filter(lambda line: line != "", list(f))
        lines = map(lambda line: line.split( " " ), lines)
        result = process(lines)

    print(result)
