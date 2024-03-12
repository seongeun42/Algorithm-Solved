import sys
input = sys.stdin.readline

di = {}

def w(a, b, c):
    res = 0
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        if (20, 20, 20) not in di:
            di[(20, 20, 20)] = w(20, 20, 20)
        return di[(20, 20, 20)]
    
    if a < b < c:
        if (a, b, c - 1) not in di:
            di[(a, b, c - 1)] = w(a, b, c - 1)
        res += di[(a, b, c - 1)]
        if (a, b - 1, c - 1) not in di:
            di[(a, b - 1, c - 1)] = w(a, b - 1, c - 1)
        res += di[(a, b - 1, c - 1)]
        if (a, b - 1, c) not in di:
            di[(a, b - 1, c)] = w(a, b - 1, c)
        res -= di[(a, b - 1, c)]
        return res
    
    if (a - 1, b, c) not in di:
        di[(a - 1, b, c)] = w(a - 1, b, c)
    res += di[(a - 1, b, c)]
    if (a - 1, b - 1, c) not in di:
        di[(a - 1, b - 1, c)] = w(a - 1, b - 1, c)
    res += di[(a - 1, b - 1, c)]
    if (a - 1, b, c - 1) not in di:
        di[(a - 1, b, c - 1)] = w(a - 1, b, c - 1)
    res += di[(a - 1, b, c - 1)]
    if (a - 1, b - 1, c - 1) not in di:
        di[(a - 1, b - 1, c - 1)] = w(a - 1, b - 1, c - 1)
    res -= di[(a - 1, b - 1, c - 1)]
    return res

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    res = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {res}")