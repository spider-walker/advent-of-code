import os

filename = os.path.dirname(__file__) + "\\input"
arrayList = []
with open(filename) as file:
    for line in file:
        arrayList.append(line.rstrip())

width = len(arrayList[0].rstrip())
print(f'len {width}')
gamma_nums = arrayList
for r in range(width):
    start = 0
    x = []
    for line in gamma_nums:
        text = list(line.rstrip())
        if start == 0:
            x = [0] * len(text)
        i = 0
        for t in text:
            if t == '1':
                x[i] += 1
            i += 1
        start += 1

    y = x[r]
    if len(gamma_nums) == 1:
        gamma_nums = gamma_nums
    elif y >= start / 2:
        gamma_nums = list(filter(lambda score: score[r] == '1', gamma_nums))
    else:
        gamma_nums = list(filter(lambda score: score[r] == '0', gamma_nums))

co2_nums = arrayList
for r in range(width):
    start = 0
    x = []
    for line in co2_nums:
        text = list(line.rstrip())
        if start == 0:
            x = [0] * len(text)
        i = 0
        for t in text:
            if t == '1':
                x[i] += 1
            i += 1
        start += 1

    y = x[r]
    if len(co2_nums) == 1:
        co2_nums = co2_nums
    elif y < start / 2:
        co2_nums = list(filter(lambda score: score[r] == '1', co2_nums))
    else:
        co2_nums = list(filter(lambda score: score[r] == '0', co2_nums))

print(int(co2_nums[0], 2) * int(gamma_nums[0], 2))
