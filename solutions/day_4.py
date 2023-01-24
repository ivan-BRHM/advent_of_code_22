"""
Day 4 solution. both for part 1 and 2
"""

from pathlib import Path
from re import findall


r = 0
for pair in Path('input_data/input_d4.txt').read_text().split("\n"):
    sections = [int(n) for n in findall(r"[0-9]+", pair)]

    print(sections)

    if sections[0] >= sections[2] and sections[1] <= sections[3] or sections[2] >= sections[0] and sections[3] <= sections[1]:
        r += 1

print(f"Solution day 4, part 1: {r}")
