import re


def is_close_to_integer(num):
    return abs(round(num) - num) < 0.001


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        strs = f.read().splitlines()

    n = len(strs)
    xb = r"X\+\d+"
    yb = r"Y\+\d+"
    xp = r"X=\d+"
    yp = r"Y=\d+"
    tokens = [0, 0]

    for i in range((n // 4) + 1):
        idx = i * 4
        a = strs[idx]
        ax = int(re.search(xb, a)[0][2:])
        ay = int(re.search(yb, a)[0][2:])
        b = strs[idx + 1]
        bx = int(re.search(xb, b)[0][2:])
        by = int(re.search(yb, b)[0][2:])
        prize = strs[idx + 2]
        x = int(re.search(xp, prize)[0][2:])
        y = int(re.search(yp, prize)[0][2:])
        todo = [(x, y), (10000000000000 + x, 10000000000000 + y)]

        for j in range(2):
            s_a = ay / ax
            y_intercept_a = todo[j][1] - s_a * todo[j][0]
            s_b = by / bx
            y_intercept_b = 0

            x_intercept = (y_intercept_b - y_intercept_a) / (s_a - s_b)
            pb = x_intercept / bx
            pa = (todo[j][0] - x_intercept) / ax
            print(pa, pb)
            if is_close_to_integer(pa) and is_close_to_integer(pb):
                tokens[j] += 3 * round(pa) + round(pb)

    print(f"Answer 1: {tokens[0]}\nAnswer 2: {tokens[1]}")
