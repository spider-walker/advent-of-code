import os

filename = os.path.dirname(__file__) + "\\input"

with open(filename) as file:
    x = []
    start = 0
    for line in file:
        text = list(line.rstrip())
        if start == 0:
            x = [0] * len(text)
        i = 0
        for t in text:
            if t == '1':
                x[i] += 1
            i += 1

        start += 1
    gamma_nums = []
    epsilon_nums = []
    for y in x:
        if y > start / 2:
            gamma_nums.append(1)
            epsilon_nums.append(0)
        else:
            gamma_nums.append(0)
            epsilon_nums.append(1)

    gamma = [str(v) for v in gamma_nums]
    epsilon = [str(r) for r in epsilon_nums]
    g = int(''.join(gamma), 2)
    e = int(''.join(epsilon), 2)
    print(g * e)
