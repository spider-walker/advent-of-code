print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 01 Day 3")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

from pathlib import Path

def source_to_dest(_almanac,_from, _to):   
    seed_to_soil = _almanac[_from]
    print(seed_to_soil)
    source=[]
    target=[]
    for i in seed_to_soil:
        _range = i[2]
        source = source +list(range(i[0], i[0] + _range))
        target = target+ list(range(i[1], i[1] + _range))
    print(source)
    print(target)

    seeds = _almanac[_to]
    for i in seeds:
        try:
            index = source.index(i)
            print(target[index],source[index])
        except:
            print(i,i)

almanac = {}
title = ""
next_line_is_title = False
j = 0
for line in Path("sample").read_text().splitlines():
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

source_to_dest(almanac,"seed-to-soil","seeds",)



