print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('Solution 02')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')



config = {
    'red' : 12,
    'green': 13,
    'blue': 14
}

def calculate_cubes(cubes_string: str):
    game_id = int(cubes_string.split(":")[0].split(" ")[1])
    game_string = cubes_string.split(":")[1].split(";")
    game_string = [x.strip().split(',') for x in game_string]
    game_string = [item for sublist in game_string for item in sublist]
    game_string = [{
        x.strip().split(' ')[1]: int(x.strip().split(' ')[0])
    } for x in game_string]
    items ={}
    items['green'] = 0
    items['blue'] =0
    items['red'] =0
    for x in game_string:
       first_key = [a for a, b in x.items()][0]
       items[first_key] = max([x[first_key], items[first_key]])

    power = items['blue']*items['green']*items['red']
    
    return power
   

file1 = open("input", "r") 
Lines = file1.readlines()
total = 0
for line in Lines:
   p=  calculate_cubes(line)
   print(p)
   total = total + calculate_cubes(line)

print(total)

