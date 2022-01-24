import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))[::-1]
    s, mp, res = [], -1e9, 0
    for v in p:
        if v > mp:
            res += sum([mp - k for k in s])
            mp = v
            s = []
        elif v < mp:
            s.append(v)
    print(res + sum([mp - k for k in s]))