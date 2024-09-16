print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution Day 6")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


from pathlib import Path


def solve_a(lines):
    times = lines["times"]
    distances = lines["distances"]

    number_of_ways = 1
    for time, distance in zip(times, distances):
        for x in range(1, time):
            a = time - x
            if a * x > distance:
                number_of_ways *= (a - x) + 1
                break

    return number_of_ways


def solve_b(lines):
    times = int("".join(str(x) for x in lines["times"]))
    distances = int("".join(str(x) for x in lines["distances"]))

    number_of_ways = 1
    for x in range(1, times):
        a = times - x
        if a * x > distances:
            number_of_ways *= (a - x) + 1
            break

    return number_of_ways


def read_data(file_name):
    lines = Path(file_name).read_text().splitlines()
    times = [int(c) for c in lines[0].split(" ") if c.isdigit()]
    distances = [int(c) for c in lines[1].split(" ") if c.isdigit()]
    return {"times": times, "distances": distances}


read_lines = read_data("sample")
print(solve_a(read_lines))
read_lines = read_data("input")
print(solve_a(read_lines))

read_lines = read_data("sample")
print(solve_b(read_lines))
read_lines = read_data("input")
print(solve_b(read_lines))
