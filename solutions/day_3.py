"""
Day 3 solution. both for step 1 and 2
"""

from pathlib import Path


ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

r = 0
for backpack in Path('input_data/input_d3.txt').read_text().split("\n"):
    room1 = set(backpack[:len(backpack)//2])
    room2 = set(backpack[len(backpack)//2:])

    l = str(room1.intersection(room2))[2]

    r += ALPHABETS.index(l) + 1  # 0-indexing

print(f"solution day 3, part 1: {r}")
