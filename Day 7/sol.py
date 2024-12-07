def process_line(res, nrs, concat):
    partials = [(res, 0)]

    while partials:
        curr = partials
        partials = []
        for nr, i in curr:
            str_i = str(nrs[i])
            len_i = len(str_i)
            if i == len(nrs) - 1:
                if nr == nrs[-1]:
                    return res
            else:
                if nr <= 0:
                    continue
                str_nr = str(nr)
                len_nr = len(str_nr)
                partials.append((nr - nrs[i], i + 1))
                if nr % nrs[i] == 0:
                    partials.append((int(nr / nrs[i]), i + 1))
                if concat and len_i < len_nr and str_nr[-len_i : ] == str_i:
                    partials.append((int(str_nr[ : -len_i]), i + 1))

    return 0

if __name__ == "__main__":
    s1, s2 = 0, 0

    with open("input.txt", 'r') as file:
        for line in file:
            res = int(line.split(':')[0])
            nrs = list(map(int, line.split(' ')[: 0 : -1]))
            s1 += process_line(res, nrs, False)
            s2 += process_line(res, nrs, True)
    
    print(f"Answer 1: {s1}\nAnswer 2: {s2}")
