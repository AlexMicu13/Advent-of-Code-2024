if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        data = list(map(list, f.read().splitlines()))

    m = len(data)
    n = len(data[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cost1 = 0
    cost2 = 0

    def is_boundary(x, y, char):
        return not (0 <= x < m and 0 <= y < n) or data[x][y] != char

    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            char = data[i][j]
            stack = [(i, j)]
            visited[i][j] = True
            area = 0
            perimeter = 0
            boundaries = set()
            actual = set()

            while stack:
                curr = stack
                stack = []

                for x, y in curr:
                    area += 1
                    neighbors = [False for _ in range(4)]
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if is_boundary(nx, ny, char):
                            perimeter += 1
                            boundaries.add(((dx, dy), (nx, ny)))
                            actual.add(((dx, dy), (nx, ny)))
                        elif not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))

            for boundary in boundaries:
                if boundary not in actual:
                    continue
                nx, ny = boundary[1]
                d = boundary[0]
                for dx, dy in directions:
                    nnx, nny = nx + dx, ny + dy
                    while (d, (nnx, nny)) in actual:
                        actual.remove((d, (nnx, nny)))
                        nnx += dx
                        nny += dy

            cost1 += area * perimeter
            cost2 += area * len(actual)

    print(f"Answer 1: {cost1}\nAnswer 2: {cost2}")
