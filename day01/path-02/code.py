import os

filename = os.path.dirname(__file__) + "\\input"

with open(filename) as file:
    current = k = last = 0
    currentSum = []
    for line in file:
        current = int(line.rstrip())
        currentSum.append(current)

        if len(currentSum) > 3:
            current = sum(currentSum[0:3])
            last = sum(currentSum[1:4])
            currentSum.pop(0)

            if current < last:
                k += 1

        last = current

    print(k)
