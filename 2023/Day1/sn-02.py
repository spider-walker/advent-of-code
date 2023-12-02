from pathlib import Path


print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('Solution 02')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
fixes = { "seven":"7", "two":"2", "one":"1", "nine":"9", "eight":"8", "three":"3", "four":"4", "five":"5", "six":"6" }
cands = set(fixes.keys()) | set(fixes.values())

total = 0
for line in Path("sample02").read_text().splitlines():
   matches = list(filter(lambda k: k in line, cands))
   print(matches)
   first, *_ = sorted(matches, key=line.index)
   *_, last = sorted(matches, key=line.rindex)
   total += int(fixes.get(first, first) + fixes.get(last, last))

print(total)