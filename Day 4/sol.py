def is_valid(i, j, m, n):
    return 0 <= i < m and 0 <= j < n

def process_grid(file_path):
    directions = [(0, 1), (1, -1), (1, 0), (1, 1)]
    pattern_X = ['M', 'A', 'S']
    pattern_S = ['A', 'M', 'X']
    apps1, apps2 = 0, 0

    with open(file_path, 'r') as file:
        rows = file.read().splitlines()

    m, n = len(rows), len(rows[0])

    for i in range(m):
        for j in range(n):
            cell = rows[i][j]

            if cell in {'X', 'S'}:
                target_pattern = pattern_X if cell == 'X' else pattern_S
                for dr in directions:
                    if all(
                        is_valid(i + dr[0] * step, j + dr[1] * step, m, n) and
                        rows[i + dr[0] * step][j + dr[1] * step] == target_pattern[step - 1]
                        for step in range(1, 4)
                    ):
                        apps1 += 1

            elif cell == 'A':
                diagonals = [
                    [(i - 1, j - 1), (i, j), (i + 1, j + 1)],
                    [(i - 1, j + 1), (i, j), (i + 1, j - 1)]
                ]
                if all(
                    all(is_valid(di[0], di[1], m, n) for di in diag) and
                    ''.join(rows[di[0]][di[1]] for di in diag) in {'MAS', 'SAM'}
                    for diag in diagonals
                ):
                    apps2 += 1

    return apps1, apps2

apps1, apps2 = process_grid("input.txt")
print(apps1, apps2)
