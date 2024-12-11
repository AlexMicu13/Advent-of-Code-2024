from collections import defaultdict, Counter


def splitStones(c1: Counter):
    c2 = defaultdict(int)

    for stone, count in c1.items():
        if stone == 0:
            c2[1] += count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            s1, s2 = int(s[:len(s) // 2]), int(s[len(s) // 2:])
            c2[s1] += count
            c2[s2] += count
        else:
            c2[stone * 2024] += count

    return c2


if __name__ == "__main__":
    stones = []
    dp = {}
    dp[0] = 1
    with open("input.txt", 'r') as f:
        stones = Counter(map(int, f.read().strip().split()))

    for _ in range(25):
        stones = splitStones(stones)

    ans1 = sum(stones.values())

    for _ in range(50):
        stones = splitStones(stones)

    ans2 = sum(stones.values())

    print(f"Answer 1: {ans1}\nAnswer 2: {ans2}")
