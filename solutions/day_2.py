"""
day 2 solution. both for step 1 and 2.
"""

from pathlib import Path


# how many points you gain after a given match
points_reward = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

split_input = Path('input_data/input_d2.txt').read_text().split("\n")
r = sum([points_reward[match] for match in split_input])

print(f"Solution day 2, part 1: {r}")
