def check(s):
    if 'AA' in s or s[-1] == 'A':
        return "NP"
    pcnt = 0
    preA = False
    for c in s:
        if c == 'P':
            if preA:
                pcnt -= 1
                preA = False
            else:
                pcnt += 1
        elif c == 'A':
            if pcnt < 2:
                return "NP"
            preA = True
    return "PPAP" if pcnt == 1 else "NP"

print(check(input()))