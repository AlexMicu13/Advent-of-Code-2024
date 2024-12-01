left = []
right = []
with open('input.txt') as f:
	for line in f:
		e1, e2 = line.split()
		left.append(int(e1))
		right.append(int(e2))

s2 = sum(x * right.count(x) for x in left)
left.sort()
right.sort()
s1 = sum(abs(l - r) for l, r in zip(left, right))
print(f'Answer 1: {s1}\nAnswer 2: {s2}')