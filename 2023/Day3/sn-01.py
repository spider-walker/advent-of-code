print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution 01 Day 3")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

import re


def search_top(line):
    top = re.search(r"\d+", line)
    return top.span()[0], top.span()[1]


def search_left(line):
    left = re.search(r"\d+", line)
    return left.span()[0], left.span()[1]


def search_width(line):
    width = re.search(r"\d+", line)
    return width.span()[0], width.span()[1]


def search_height(line):
    height = re.search(r"\d+", line)
    return height.span()[0], height.span()[1]


file1 = open("input", "r")
lines = file1.readlines()
line_number = 0
sum = 0
for line in lines:
    x = re.finditer(r"\d+", line)
    for i in x:
        a = i.span()[0] > 0 and i.span()[0] - 1 or i.span()[0]
        b = i.span()[1] > len(line) - 1 and i.span()[1] or i.span()[1] + 1
        lines_to_search = line[a:b]
        numbers = i.group()
        if line_number > 0:
            lines_to_search += lines[line_number - 1][a:b]
        if line_number < len(lines) - 1:
            lines_to_search += lines[line_number + 1][a:b]
        
        lines_to_search = re.sub(r'\d+', '', lines_to_search)
        lines_to_search = re.sub(r'\.', '', lines_to_search)
        
        if lines_to_search.strip() != '':
            print(lines_to_search)
            sum += int(numbers)

    line_number += 1
print(sum)