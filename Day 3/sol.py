import re
from functools import reduce
from operator import mul

if __name__ == "__main__":
    s1 = 0
    s2 = 0
    pos = 0
    todo = True

    with open("input.txt", 'r') as file:
        str = file.read()

    reg = re.compile(r"mul\(\d+\,\d+\)|don\'t\(\)|do\(\)")

    while m := reg.search(str, pos):
        pos = m.start() + 1
        if m[0] == "don't()":
            todo = False
            continue
        elif m[0] == "do()":
            todo = True
            continue
        nr = reduce(mul, list(map(int, re.findall(r'\d+', m[0]))))
        s1 += nr
        if todo:
            s2 += nr

    print(f"Answer 1: {s1}\nAnswer 2: {s2}")
