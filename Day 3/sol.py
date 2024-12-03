import re

s = 0
pos = 0
todo = True

with open("input.txt", 'r') as file:
	str = file.read()

reg = re.compile(r"mul\(([0-9]){1,3}\,([0-9]){1,3}\)|don\'t\(\)|do\(\)")

while m := reg.search(str, pos):
	pos = m.start() + 1
	if m[0] == "don't()":
		todo = False
		continue
	elif m[0] == "do()":
		todo = True
		continue
	elif todo:
		nrs = list(map(int, re.findall(r'\d+', m[0])))
		s += nrs[0] * nrs[1]

print(s)