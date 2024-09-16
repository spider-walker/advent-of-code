print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution Day 6")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

from pathlib import Path


def solve_b(file_name):
    lines = Path(file_name).read_text().splitlines()
    historys = [x.split(" ") for x in lines]
    total = 0
    for hist in historys:
        hist = hist[::-1]
        current_diffs = [int(x) for x in hist]
        lasts = []

        while True:
            lasts.append(current_diffs[-1])
            diffs = []
            for j in range(1, len(current_diffs)):
                diffs.append(current_diffs[j] - current_diffs[j - 1])
            current_diffs = diffs.copy()
            if len(list(filter(lambda x: x != 0, diffs))) == 0:
                break

        print(sum(lasts)   )     
        total += sum(lasts)

    print(total)





def solve_a(file_name):
    lines = Path(file_name).read_text().splitlines()
    historys = [x.split(" ") for x in lines]
    total = 0
    for hist in historys:
        current_diffs = [int(x) for x in hist]
        lasts = []

        while True:
            lasts.append(current_diffs[-1])
            diffs = []
            for j in range(1, len(current_diffs)):
                diffs.append(current_diffs[j] - current_diffs[j - 1])
            current_diffs = diffs.copy()
            if len(list(filter(lambda x: x != 0, diffs))) == 0:
                break
       
        total += sum(lasts)

    print(total)



# rs = read_lines = solve_a("input")
rs = read_lines = solve_b("sample")
# 2098512764
# 2098530125
