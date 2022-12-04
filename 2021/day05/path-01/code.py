import os

filename = os.path.dirname(__file__) + "\\sample-input"
lines_of_vents = []
with open(filename) as file:
    for line in file:
        xy = line.rstrip().split(' -> ')
        x = list(map(int, xy[0].split(',')))
        y = list(map(int, xy[1].split(',')))
        z = [x, y]
        lines_of_vents.append(z)


def isGreater(q, r):
    inc = 1
    if q > r:
        inc = -1
    return inc


maximum = 0;
data = [];
for lines_of_vent in lines_of_vents:
    if lines_of_vent[0][0] == lines_of_vent[1][0] or lines_of_vent[0][1] == lines_of_vent[1][1]:
        inc_from = isGreater(lines_of_vent[0][0], lines_of_vent[0][1])
        inc_to = isGreater(lines_of_vent[1][0], lines_of_vent[1][1])
        vents_from = list(range(lines_of_vent[0][0], lines_of_vent[0][1] + inc_from, inc_from))
        vents_to = list(range(lines_of_vent[1][0], lines_of_vent[1][1] + inc_to, inc_to))
        data.append(lines_of_vent)
        maximum = max(vents_from + vents_to + [maximum]);

table_of_ts = {}
for dx in data:
    if dx[0][0] == dx[1][0]:
        digits = []
        if f'{dx[0][0]}-y' in table_of_ts.keys():
            digits = table_of_ts[f'{dx[0][0]}-y'];
            digits.append(sorted([dx[0][1], dx[1][1]]))
        else:
            digits.append(sorted([dx[0][1], dx[1][1]]))
        table_of_ts[f'{dx[0][0]}-y'] = digits
    if dx[0][1] == dx[1][1]:
        digits = []
        if f'{dx[0][1]}-x' in table_of_ts.keys():
            digits = table_of_ts[f'{dx[0][1]}-x'];
            digits.append(sorted([dx[0][0], dx[1][0]]))
        else:
            digits.append(sorted([dx[0][0], dx[1][0]]))
        table_of_ts[f'{dx[0][1]}-x'] = digits

print(table_of_ts)
for k in table_of_ts:
    n = [];
    for m in table_of_ts[k]:
        print(m)
