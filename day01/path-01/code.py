import os

filename = os.getcwd() + "\\day01\\input-01"

with open(filename) as file:
    current = k= last= 0
    for line in file:
        current = int(line.rstrip())
        if current > last:
            k += 1

        last = current

    print(k-1)
