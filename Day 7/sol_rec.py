def process_line(res, nrs, concat):
    if len(nrs) == 1:
        return res == nrs[0]

    if res <= 0:
        return False

    x = nrs[-1]
    rem = nrs[:-1]
    str_res = str(res)
    len_res = len(str_res)
    str_i = str(x)
    len_i = len(str_i)
    check1 = process_line(res - x, rem, concat)
    check2 = process_line(int(res / x), rem, concat)  if res % x == 0 else False
    check3 = process_line(int(str_res[ : -len_i]), rem, concat) if (concat and (len_i < len_res) and (str_res[-len_i : ] == str_i)) else False
    return check1 or check2 or check3
    
if __name__ == "__main__":
    s1, s2 = 0, 0
    
    with open("input.txt", 'r') as file:
        for line in file:
            res = int(line.split(':')[0])
            nrs = list(map(int, line.split(' ')[1:]))
            s1 += res if process_line(res, nrs, False) else 0
            s2 += res if process_line(res, nrs, True) else 0
    
    print(f"Answer 1: {s1}\nAnswer 2: {s2}")
