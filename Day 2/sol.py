def is_safe(report: list[int]) -> bool:
	decreasing = False
	safed = True
	if report[0] > report[1]:
		decreasing = True
	for i in range(1, len(report)):
		if decreasing and not (1 <= report[i - 1] - report[i] <= 3):
			safed = False
			break
		if not decreasing and not (1 <= report[i] - report[i - 1] <= 3):
			safed = False
			break

	return safed

safe1 = 0
safe2 = 0

with open("input.txt") as f:
	for line in f:
		report = list(map(int, line.strip().split()))
		print(report)
		if is_safe(report):
			safe1 += 1
			safe2 += 1
		else:
			for i in range(len(report)):
				aux = report.copy()
				aux.pop(i)
				if is_safe(aux):
					safe2 += 1
					break

print(f"Answer 1: {safe1}\nAnswer 2: {safe2}")