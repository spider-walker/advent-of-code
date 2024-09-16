print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 02 Day 4")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

file1 = open("input", "r")
lines = file1.readlines()
line_number = 0
sum = 0
winnings = {}
for j, line in enumerate(lines):
    parts = re.split(r":|\|", line.strip())
    winning_numbers = list(filter(None,parts[1].split(" ")))
    in_hand = list(filter(None,parts[2].split(" ")))
    common = [x for x in winning_numbers if x in in_hand]
    original = len(common)>0 and 1 or 0
    
    if j not in winnings:
        winnings[j] =0
    winnings[j] = winnings[j] + original  
    print(f' {j+1}: {winnings[j]} {original} {len(common)}')  

     

    for i in range(j+1, len(common)+j+1):
        if i not  in winnings:
            winnings[i] =0
        winnings[i] += winnings[j] 
    if len(common)==0:
        winnings[j] += 1    
    sum += winnings[j]   
 

print(f'sum={sum}')