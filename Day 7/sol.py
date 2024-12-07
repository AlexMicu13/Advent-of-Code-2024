def process_line(res, nrs, concat=False):
    partials = [nrs[0]]
    i = 1

    while i <= len(nrs) and partials:
        curr = partials
        partials = []
        for nr in curr:
            if i == len(nrs):
                if nr == res:
                    return res
            else:
                if nr > res:
                    continue
                partials.append(nr + nrs[i])
                partials.append(nr * nrs[i])
                if concat:
                    partials.append(int(str(nr) + str(nrs[i])))
        i += 1

    return 0

if __name__ == "__main__":
    s1, s2 = 0, 0

    with open("input.txt", 'r') as file:
        for line in file:
            res = int(line.split(':')[0])
            nrs = list(map(int, line.split(' ')[1:]))
            s1 += process_line(res, nrs, False)
            s2 += process_line(res, nrs, True)
    
    print(f"Answer 1: {s1}\nAnswer 2: {s2}")
