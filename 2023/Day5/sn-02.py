print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 01 Day 5")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

from pathlib import Path


def source_to_dest(_almanac, _from, _to):
    print(f"Mapping from {_from}")
    seed_to_soil = _almanac[_from]

    for m, i in enumerate(_to):
        for start, a, length in seed_to_soil:
            b = a + length - 1
            if a <= i <= b:
                c = i - a
                _to[m] = start + c
                break

    return _to


almanac = {}
title = ""
next_line_is_title = False

lines = Path("input").read_text().splitlines()

for line in lines:
    if line.strip() == "":
        next_line_is_title = True
        continue
    if next_line_is_title:
        title = line.split(" ")[0]
        almanac[title] = []
        next_line_is_title = False
    else:
        if title not in almanac:
            title, values = line.split(":")
            almanac[title] = [int(x) for x in values.split() if x]
        else:
            almanac[title].append([int(x) for x in line.split() if x])

almanac_keys = list(almanac.keys())
almanac_keys.remove("seeds")
to_be_mapped = almanac["seeds"]

seed_pairs = []
for k in range(0, len(to_be_mapped), 2):
    seed_pairs.extend(range(to_be_mapped[k], to_be_mapped[k] + to_be_mapped[k + 1]))

for i in almanac_keys:
    to_be_mapped = source_to_dest(almanac, i, seed_pairs)

print(min(to_be_mapped))
