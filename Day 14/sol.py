import re
from functools import reduce
from operator import mul
from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    number_regex = r"-?\d+"
    m = 103
    n = 101
    half_m = m // 2
    half_n = n // 2
    pos = []
    speeds = []
    safety = []

    with open("input.txt", 'r') as f:
        for line in f:
            nrs = list(map(int, re.findall(number_regex, line)))
            pos.append([nrs[0] % n, nrs[1] % m])
            speeds.append((nrs[2], nrs[3]))

    font_size = 10
    font = ImageFont.truetype("arial.ttf", font_size)
    width = n * font_size
    height = m * font_size

    for iter in range(n * m):
        robots = [[0 for _ in range(n)] for _ in range(m)]
        quads = [0, 0, 0, 0]

        for i in range(len(pos)):
            pos[i][0] = (pos[i][0] + speeds[i][0]) % n
            pos[i][1] = (pos[i][1] + speeds[i][1]) % m
            robots[pos[i][1]][pos[i][0]] = 1

            if pos[i][0] < half_n and pos[i][1] < half_m:
                quads[0] += 1
            elif pos[i][0] > half_n and pos[i][1] < half_m:
                quads[1] += 1
            elif pos[i][0] < half_n and pos[i][1] > half_m:
                quads[2] += 1
            elif pos[i][0] > half_n and pos[i][1] > half_m:
                quads[3] += 1

        safety.append(reduce(mul, quads))

    min_index = safety.index(min(safety))
    print(f"Answer 1: {safety[99]}\nAnswer 2: {min_index + 1}")
