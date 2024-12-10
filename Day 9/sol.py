if __name__ == "__main__":
    with open("input.txt") as f:
        data = list(map(int, f.read().strip()))
    id = 0
    blocks = []
    blocks_ind = []
    free_blocks = []
    ind = 0

    for i in range(len(data)):
        if id % 2 == 0:
            for _ in range(data[i]):
                blocks.append(id // 2)
            blocks_ind.append((ind, data[i]))
            ind += data[i]
        else:
            for _ in range(data[i]):
                blocks.append(-1)
            free_blocks.append((ind, data[i]))
            ind += data[i]
        id += 1

    start = 0
    end = len(blocks) - 1
    checksum1 = 0
    blocks1 = blocks.copy()

    while start < end:
        if blocks1[start] == -1 and blocks1[end] != -1:
            blocks1[start], blocks1[end] = blocks1[end], blocks1[start]
            checksum1 += blocks1[start] * start
            start += 1
            end -= 1
        elif blocks1[start] != -1:
            checksum1 += blocks1[start] * start
            start += 1
        elif blocks1[end] == -1:
            end -= 1

    while blocks1[start] != -1:
        checksum1 += blocks1[start] * start
        start += 1
    checksum2 = 0
    blocks2 = blocks.copy()

    for ind in range(len(blocks_ind), 0, -1):
        size = blocks_ind[ind - 1][1]
        block_index = blocks_ind[ind - 1][0]
        if blocks2[block_index] == -1:
            continue
        replacement = next(((indFree, sizeFree, where) for where, (indFree,
                           sizeFree) in enumerate(free_blocks) if sizeFree >= size), -1)
        if replacement == -1 or replacement[0] > block_index:
            continue
        free_blocks.pop(replacement[2])
        if replacement[1] > size:
            free_blocks.insert(
                replacement[2], (replacement[0] + size, replacement[1] - size))
        for i in range(size):
            blocks2[replacement[0] + i], blocks2[block_index +
                                                 i] = blocks2[block_index + i], blocks2[replacement[0] + i]

    for i in range(len(blocks2)):
        if blocks2[i] == -1:
            continue
        checksum2 += blocks2[i] * i

    print(f"Answer 1: {checksum1}\nAnswer 2: {checksum2}")
