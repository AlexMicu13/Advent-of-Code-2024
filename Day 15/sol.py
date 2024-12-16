def pushBox1(data, pos, direction):
    i, j = pos
    if data[i][j] == '.':
        return True
    if data[i][j] == '#':
        return False
    if data[i][j] == 'O':
        dest = (i + direction[0], j + direction[1])
        pushed = pushBox1(data, dest, direction)
        if not pushed:
            return pushed
        else:
            data[dest[0]][dest[1]] = data[i][j]
            data[i][j] = '.'
            return True


def pushBox2(data, pos, direction):
    if data[pos[0]][pos[1]] == '.':
        return True
    if data[pos[0]][pos[1]] == '#':
        return False
    if direction[0] == 0:
        dest = (pos[0], pos[1] + direction[1])
        path = [pos, dest]
        while data[dest[0]][dest[1]] == '[' or data[dest[0]][dest[1]] == ']':
            dest = (dest[0], dest[1] + direction[1])
            path.append(dest)
        if data[dest[0]][dest[1]] == '#':
            return False
        for i in range(len(path) - 1, -1, -1):
            data[path[i][0]][path[i][1]] = data[path[i - 1][0]][path[i - 1][1]]
        data[path[0][0]][path[0][1]] = '.'
        return True
    left = (pos[0], pos[1] - 1)
    right = (pos[0], pos[1] + 1)
    other = left if data[pos[0]][pos[1]] == ']' else right
    layer = []
    if other == left:
        layer = [[other, pos]]
    else:
        layer = [[pos, other]]
    rep = []
    while len(layer) > 0:
        new_layer = []
        for l, r in layer:
            dest_l = (l[0] + direction[0], l[1])
            dest_r = (r[0] + direction[0], r[1])
            if data[dest_l[0]][dest_l[1]] == '#' or data[dest_r[0]][dest_r[1]] == '#':
                return False
            rep.append([dest_l, dest_r, l, r])
            if data[dest_l[0]][dest_l[1]] == '[' and data[dest_r[0]][dest_r[1]] == ']':
                new_layer.append([dest_l, dest_r])
            if data[dest_l[0]][dest_l[1]] == '.' and data[dest_r[0]][dest_r[1]] == '.':
                continue
            if data[dest_l[0]][dest_l[1]] == ']':
                other = (dest_l[0], dest_l[1] - 1)
                new_layer.append([other, dest_l])
            if data[dest_r[0]][dest_r[1]] == '[':
                other = (dest_r[0], dest_r[1] + 1)
                new_layer.append([dest_r, other])
        layer = new_layer

    no_backs = set()
    for l, r, l_prev, r_prev in reversed(rep):
        data[l[0]][l[1]] = data[l_prev[0]][l_prev[1]]
        data[r[0]][r[1]] = data[r_prev[0]][r_prev[1]]
        no_backs.add(l_prev)
        no_backs.add(r_prev)
        if l in no_backs:
            no_backs.remove(l)
        if r in no_backs:
            no_backs.remove(r)

    for pos in no_backs:
        data[pos[0]][pos[1]] = '.'

    return True


def simulate(data, moves, start):
    for move in moves:
        direction = directions[move]
        prev = start
        start = (start[0] + direction[0], start[1] + direction[1])
        if data[start[0]][start[1]] == '#':
            start = prev
        elif data[start[0]][start[1]] == 'O':
            box = pushBox1(data, start, direction)
            if not box:
                start = prev
            else:
                data[prev[0]][prev[1]] = '.'
                data[start[0]][start[1]] = '@'
        elif data[start[0]][start[1]] == '[':
            box = pushBox2(data, start, direction)
            if not box:
                start = prev
            else:
                data[prev[0]][prev[1]] = '.'
                data[start[0]][start[1]] = '@'
        elif data[start[0]][start[1]] == ']':
            box = pushBox2(data, start, direction)
            if not box:
                start = prev
            else:
                data[prev[0]][prev[1]] = '.'
                data[start[0]][start[1]] = '@'
        elif data[start[0]][start[1]] == '.':
            data[prev[0]][prev[1]], data[start[0]][start[1]] = \
                data[start[0]][start[1]], data[prev[0]][prev[1]]


if __name__ == '__main__':
    with open("input.txt", 'r') as file:
        data = file.read().splitlines()
        separated = data.index('')
        moves = "".join(data[separated + 1:])
        data = data[:separated]

    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    start = None
    for i, line in enumerate(data):
        if '@' in line:
            start = (i, line.index('@'))
            break

    data = [list(line) for line in data]
    new_data = []
    for line in data:
        new_line = []
        for char in line:
            if char == 'O':
                new_line.append('[')
                new_line.append(']')
            elif char == '@':
                new_line.append('@')
                new_line.append('.')
            else:
                new_line.append(char)
                new_line.append(char)
        new_data.append(new_line)

    simulate(data, moves, start)

    score = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                score += i * 100 + j

    print(f"Answer 1: {score}")

    start = (start[0], start[1] * 2)
    simulate(new_data, moves, start)
    score = 0
    for i in range(len(new_data)):
        for j in range(len(new_data[0])):
            if new_data[i][j] == '[':
                score += i * 100 + j

    print(f"Answer 2: {score}")
