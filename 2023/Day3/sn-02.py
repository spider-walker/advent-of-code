print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 02 Day 3")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re
from collections import defaultdict



file1 = open("input", "r")
lines = file1.readlines()
total = 0
potential_gears = defaultdict(list)
for i, line in enumerate(lines):
    start_line = max(i - 1, 0)
    end_line = min(i + 2, len(lines))
    for match in re.finditer(r"(\d+)", line):
        start_check = max(0, match.start() - 1)
        end_check = min(len(line), match.end() + 1)
        for l in range(start_line, end_line):
            for c in range(start_check, end_check):
                if lines[l][c] == "*":
                    potential_gears[(l, c)].append(int(match.group()))
for numbers in potential_gears.values():
    if len(numbers) == 2:
        total += numbers[0] * numbers[1]
     
print(total)