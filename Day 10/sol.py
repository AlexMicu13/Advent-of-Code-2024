if __name__ == "__main__":
    paths = []
    starts = []
    uniques = set()
    with open("input.txt", 'r') as f:
        data = list(map(list, f.read().splitlines()))
        for i, d in enumerate(data):
            aux = []
            for j in range(len(d)):
                if d[j] == '9':
                    starts.append(((i, j), (i, j)))
                aux.append(int(d[j]))
            paths.append(aux)

    ways = 0
    rating = 0
    q = starts.copy()

    while q:
        poss, pos = q.pop()
        x, y = pos

        if paths[x][y] == 0:
            if (poss, pos) not in uniques:
                uniques.add((poss, pos))
                ways += 1
            rating += 1
            continue

        if x > 0 and (paths[x][y] - paths[x - 1][y] == 1):
            q.append((poss, (x - 1, y)))
        if x < len(paths) - 1 and (paths[x][y] - paths[x + 1][y] == 1):
            q.append((poss, (x + 1, y)))
        if y > 0 and (paths[x][y] - paths[x][y - 1] == 1):
            q.append((poss, (x, y - 1)))
        if y < len(paths[0]) - 1 and (paths[x][y] - paths[x][y + 1] == 1):
            q.append((poss, (x, y + 1)))

    print(f"Answer 1: {ways}\nAnswer 2: {rating}")
