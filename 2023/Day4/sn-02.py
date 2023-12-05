print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 02 Day 4")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re

file1 = open("sample", "r")
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
    
    prev_wins = 0
    if j  in winnings:
       prev_wins= winnings[j]

    if j not in winnings:
        winnings[j] = original 

    print(f'{j}: ----------------{prev_wins} copies:{original+prev_wins}')
    
    
    
    for i in range(1, len(common)+1):
        index = j + i 
        if index not in winnings:
            winnings[index] = 0
        winnings[index] += original +prev_wins   
        print(f'{index}: ----------------{winnings[index]}')  
    sum += winnings[j] 
print(f'sum={sum}')