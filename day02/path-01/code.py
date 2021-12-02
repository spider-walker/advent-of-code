import os

filename = os.path.dirname(__file__) + "\\input"

with open(filename) as file:
    depth = horizontal = 0
    for line in file:
        text = line.split()
        direction = text[0]
        d = int(text[1])
        if direction == 'forward':
            horizontal += d
        if direction == 'up':
            depth -= d
        if direction == 'down':
            depth += d
    print(depth * horizontal)
