def process_line(res, nrs, i, partial, concat):
    if i == len(nrs):
        return partial == res
    if partial > res:
        return False

    check1 = process_line(res, nrs, i + 1, partial + nrs[i], concat)
    check2 = process_line(res, nrs, i + 1, partial * nrs[i], concat)
    check3 = process_line(res, nrs, i + 1, int(str(partial) + str(nrs[i])), concat) if concat else False
    return check1 or check2 or check3
    
if __name__ == "__main__":
    s1, s2 = 0, 0
    
    with open("input.txt", 'r') as file:
        for line in file:
            res = int(line.split(':')[0])
            nrs = list(map(int, line.split(' ')[1:]))
            s1 += res if process_line(res, nrs, 1, nrs[0], False) else 0
            s2 += res if process_line(res, nrs, 1, nrs[0], True) else 0
    
    print(f"Answer 1: {s1}\nAnswer 2: {s2}")
