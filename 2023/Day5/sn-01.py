print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 01 Day 5")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

from pathlib import Path


def source_to_dest(_almanac, _from, _to):
    print("Mapping from " + _from )
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
j = 0
for line in Path("input").read_text().splitlines():
    j += 1
    if j == 1:
        tokens = line.split(":")
        title = tokens[0]
        almanac[title] = [int(x) for x in list(filter(None, tokens[1].split(" ")))]
        continue
    if line.strip() == "":
        next_line_is_title = True
        continue
    if next_line_is_title:
        title = line.split(" ")[0]
        almanac[title] = []
    if not next_line_is_title:
        almanac[title].append([int(x) for x in list(filter(None, line.split(" ")))])

    next_line_is_title = False

almanac_keys = list(almanac.keys())
almanac_keys.remove("seeds")
to_be_mapped = almanac["seeds"]
for i in almanac_keys:
    to_be_mapped = source_to_dest(almanac, i, to_be_mapped)

print(min(to_be_mapped))
