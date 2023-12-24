print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution Day 6")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


import math
from pathlib import Path


def solve_a(lines):
    left_right, directions = lines
    node = "AAA"
    start = directions[node]
    k = 0
    while True:
        k += 1
        dir = left_right.pop(0)
        left_right.append(dir)
        search = 0 if dir == "L" else 1
        node = start[search]
        if node == "ZZZ":
            break
        start = directions[node]
    return k


def solve_b(lines):
    directions= lines[1]
    start_nodes = [x for x in directions.keys() if x.endswith("A")]
    divisors =[]
    for node in start_nodes:
        k = 0
        left_right = lines[0].copy()
        while True:
            k += 1
            dir = left_right.pop(0)
            left_right.append(dir)
            start = directions[node]
            search = 0 if dir == "L" else 1
            node = start[search]
            if node.endswith("Z"):
                divisors.append(k)
                break
            start = directions[node]
    print(divisors)    
    print(math.lcm(*divisors))
    # k = 0

    # while True:
    #     k += 1
    #     dir = left_right.pop(0)
    #     left_right.append(dir)
    #     for i, node in enumerate(start_nodes):
    #         start = directions[node]
    #         search = 0 if dir == "L" else 1
    #         node = start[search]
    #         start_nodes[i] = node

    #     end_nodes = [x for x in start_nodes if not x.endswith("Z")]
    #     if len(end_nodes) == 0:
    #         break
    #     print(k, start_nodes)
    # return k


def read_data(file_name):
    lines = Path(file_name).read_text().splitlines()
    left_right = [*lines[0].strip()]

    directions = {}
    for line in lines[1:]:
        if line.strip() == "":
            continue
        x = line.replace("=", ",").replace(")", "").replace("(", "")
        a, b, c = [x.strip() for x in x.split(",")]
        directions[a] = (b, c)

    return left_right, directions


read_lines = read_data("input")
# k = solve_a(read_lines)
k = solve_b(read_lines)


print(k)
# print(solve_a(read_lines))
# read_lines = read_data("input")
# print(solve_a(read_lines))

# read_lines = read_data("sample")
# print(solve_b(read_lines))
# read_lines = read_data("input")
# print(solve_b(read_lines))
