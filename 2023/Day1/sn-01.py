print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('Solution 01')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

file1 = open("input", "r") 
Lines = file1.readlines()
calibration = 0
for line in Lines:
   numbers= ''.join(c for c in line if c.isdigit())
   calibration = calibration + int(numbers[0] + numbers[-1])

print(calibration)