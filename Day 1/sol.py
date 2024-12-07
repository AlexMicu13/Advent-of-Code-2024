from collections import Counter

if __name__ == "__main__":
    left = []
    right = []
    right_count = Counter()
    with open('input.txt') as f:
        for line in f:
            e1, e2 = line.split()
            e1, e2 = int(e1), int(e2)
            left.append(e1)
            right.append(e2)
            right_count[e2] += 1

    left.sort()
    right.sort()
    s1 = sum(abs(l - r) for l, r in zip(left, right))
    s2 = sum(x * right_count.get(x, 0) for x in left)
    print(f'Answer 1: {s1}\nAnswer 2: {s2}')
