print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 01 Day 5")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

from pathlib import Path


def source_to_dest(_almanac, _from, _to):
    print("Mapping from " + _from )
    seed_to_soil = _almanac[_from]
    m =0
    for i in _to:
        for j in seed_to_soil:
            a= j[1]
            b= j[1] + j[2]-1
            if i >= a and i <= b:
                c= i - a
                d= j[0] + c
                _to[m] = d
                print(f'{d} {m} ')
                break
        m+=1     
    print(_to)        
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
seed_pairs= []

k=0
for i in to_be_mapped:
    if k % 2 == 0:
        x= list(range(to_be_mapped[k], to_be_mapped[k]+to_be_mapped[k+1]))
        seed_pairs.extend(x)
    k+=1
print(seed_pairs) 
for i in almanac_keys:
    to_be_mapped = source_to_dest(almanac, i, seed_pairs)

print(min(to_be_mapped))
