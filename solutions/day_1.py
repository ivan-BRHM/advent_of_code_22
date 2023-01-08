"""
day 1 solution. Both for step 1 and 2
"""

from pathlib import Path


def trim_input(data:Path):
    """
    ready the input for further parsing
    """

    raw_input = data.read_text()

    r = []
    for elf in raw_input.split('\n\n'):

        r.append(sum([int(n) for n in elf.split('\n')]))

    return r


trimmed_input = trim_input(Path('input_data/input_d1.txt'))

print(f"Solution day 1, part 1: {max(trimmed_input)}")
print(f"Solution day 1, part 2: {sum(sorted(trimmed_input)[-3:])}")
