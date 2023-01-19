"""
Day 3 solution. both for step 1 and 2
"""

from pathlib import Path


ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_data = Path('input_data/input_d3.txt').read_text().split("\n")

r1 = 0
for backpack in input_data:
    room1 = set(backpack[:len(backpack)//2])
    room2 = set(backpack[len(backpack)//2:])

    l = str(room1.intersection(room2))[2]

    r1 += ALPHABETS.index(l) + 1  # 0-indexing

r2 = 0
for backpack in input_data[::3]:
    backpack2 = set(input_data[input_data.index(backpack) + 1])
    backpack3 = set(input_data[input_data.index(backpack) + 2])

    l = str(set(backpack).intersection(backpack2, backpack3))[2]

    r2 += ALPHABETS.index(l) + 1

print(f"solution day 3, part 1: {r1}")
print(f"solution day 3, part 2: {r2}")
