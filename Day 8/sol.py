from itertools import combinations
from math import gcd


def isValid(pos, m, n):
    return 0 <= pos[0] < m and 0 <= pos[1] < n


if __name__ == "__main__":
    all_antennas = dict()
    uniques1 = set()
    uniques2 = set()
    m, n = 0, 0

    with open("input.txt", 'r') as file:
        str = list(map(list, file.read().splitlines()))
        m, n = len(str), len(str[0])
        for i, line in enumerate(str):
            for j, s in enumerate(line):
                if s != '.':
                    if s not in all_antennas:
                        all_antennas[s] = []
                    all_antennas[s].append((i, j))

    for antennas in all_antennas.values():
        if len(antennas) < 2:
            continue
        combs = list(combinations(antennas, 2))
        for p1, p2 in combs:
            diff_x = p2[0] - p1[0]
            diff_y = p2[1] - p1[1]
            step_gcd = gcd(diff_x, diff_y)
            step_x, step_y = diff_x // step_gcd, diff_y // step_gcd

            a1 = (p1[0] - diff_x, p1[1] - diff_y)
            a2 = (p2[0] + diff_x, p2[1] + diff_y)

            if isValid(a1, m, n):
                uniques1.add(a1)
            if isValid(a2, m, n):
                uniques1.add(a2)

            x, y = p1[0], p1[1]
            while isValid((x, y), m, n):
                uniques2.add((x, y))
                x += step_x
                y += step_y

            x, y = p1[0] - step_x, p1[1] - step_y
            while isValid((x, y), m, n):
                uniques2.add((x, y))
                x -= step_x
                y -= step_y

    print(len(uniques1), len(uniques2))
