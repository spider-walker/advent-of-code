print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 01 Day 3")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

file1 = open("input", "r")
lines = file1.readlines()
line_number = 0
sum = 0
for line in lines:
    parts = re.split(r":|\|", line.strip())
    winning_numbers = list(filter(None,parts[1].split(" ")))
    in_hand = list(filter(None,parts[2].split(" ")))
    common = [x for x in winning_numbers if x in in_hand]
    
    n = 0
    for i in range(0, len(common)):
        if i == 0:
            n += 1
        else:
            n *= 2
    sum += n   

print(sum)