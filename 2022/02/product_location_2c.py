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
from functools import reduce
from itertools import accumulate
import operator
import pandas as pd
from typing import List, Tuple


def process(df: pd.DataFrame) -> int:
    # transform "down" and "up" "amounts" into "delta_slope" by inverting "amount" of "up"
    df["delta_slope"] = 0
    df.loc[df["mode"]=="down", "delta_slope"] = df.loc[df["mode"]=="down", "amount"] 
    df.loc[df["mode"]=="up", "delta_slope"] = -df.loc[df["mode"]=="up", "amount"] 

    # accumulate delta_slope into slope
    df["slope"] = pd.Series(accumulate(df["delta_slope"].values, operator.add))

    # pull out all forward motions, so that they can be paired with slope
    df["forward"] = 0
    df.loc[df["mode"]=="forward", "forward"] = df.loc[df["mode"]=="forward", "amount"] 

    # # calculate final horizontal and depth
    horizontal = reduce(lambda x,y: x+y, df["forward"])
    depth = reduce(lambda x,y: x+y, df["slope"]*df["forward"])

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
        lines = map(lambda line: (line[0], int(line[1])), lines)
        df = pd.DataFrame(data=lines, columns=["mode", "amount"])
        result = process(df)

    print(result)
