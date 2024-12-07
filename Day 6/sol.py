def is_in(pos: (int, int), m: int, n: int) -> bool:
    return 0 <= pos[0] < m and 0 <= pos[1] < n


def simulate(map_obs, start_pos, m, n, dirs):
    visited = set()
    pos = start_pos
    direction = 0
    visited.add(pos)

    while True:
        next_pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
        if not is_in(next_pos, m, n):
            break
        if map_obs[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
        else:
            pos = next_pos
            visited.add(pos)

    return visited


def simulate_with_obstacle(map_obs, start_pos, m, n, dirs, obstacle):
    visited = set()
    pos = start_pos
    direction = 0
    if obstacle:
        map_obs[obstacle[0]][obstacle[1]] = '#'

    while True:
        state = (pos, direction)
        if state in visited:
            if obstacle:
                map_obs[obstacle[0]][obstacle[1]] = '.'
            return True
        visited.add(state)

        next_pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
        if not is_in(next_pos, m, n):
            if obstacle:
                map_obs[obstacle[0]][obstacle[1]] = '.'
            break
        if map_obs[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
        else:
            pos = next_pos


if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        map_obs = list(map(list, file.read().splitlines()))

    m, n = len(map_obs), len(map_obs[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start_pos = next((i, j) for i in range(m)
                     for j in range(n) if map_obs[i][j] == '^')

    visited = simulate(map_obs, start_pos, m, n, dirs)

    possible = 0
    for pos in visited:
        if pos != start_pos:
            if simulate_with_obstacle(map_obs, start_pos, m, n, dirs, pos):
                possible += 1

    print(f"Answer 1: {len(visited)}\nAnswer 2: {possible}")
