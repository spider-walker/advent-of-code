import os

filename = os.path.dirname(__file__) + "\\input"

with open(filename) as file:
    depth = horizontal = aim = 0
    for line in file:
        text = line.split()
        direction = text[0]
        d = int(text[1])
        if direction == 'forward':
            horizontal += d
            depth += d * aim
        if direction == 'up':
            aim -= d
        if direction == 'down':
            aim += d
        print(f'{aim}')

    print(depth * horizontal)
