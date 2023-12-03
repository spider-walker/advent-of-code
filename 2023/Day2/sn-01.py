print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('Solution 01')
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
    for x in game_string:
       first_key = [a for a, b in x.items()][0]
       if x[first_key]>config[first_key]: 
           return 0
          
    return game_id
   
    
file1 = open("input", "r") 
Lines = file1.readlines()
total = 0
for line in Lines:
   total = total + calculate_cubes(line)

print(total)

