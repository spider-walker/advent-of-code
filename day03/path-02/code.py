import os

filename = os.path.dirname(__file__) + "\\sample-input"

with open(filename) as file:
    arrayLOist = [];
    for line in file:
        arrayLOist.append(line.rstrip())

    x = []
    start = 0
    for line in arrayLOist:
        text = list(line.rstrip())
        if start == 0:
            x = [0] * len(text)
        i = 0
        for t in text:
            if t == '1':
                x[i] += 1
            i += 1

        start += 1
    gamma_nums = arrayLOist
    epsilon_nums = arrayLOist
    m = 0
    for y in x:
        print(f' {y} {start}')
        for g in gamma_nums

        # if y - start / 2 == 0.0:
        #     gamma_nums = list(filter(lambda score: score[m] == '1', gamma_nums))
        #     print(f'=={gamma_nums} {y} {start / 2}')
        # elif y > start / 2:
        #     gamma_nums = list(filter(lambda score: score[m] == '1', gamma_nums))
        #     print(f'>{gamma_nums} {y} {start / 2}')
        # else:
        #     gamma_nums = list(filter(lambda score: score[m] == '0', gamma_nums))
        # m += 1

    print(gamma_nums)
