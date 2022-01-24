import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))[::-1]
    mp, res = -1e9, 0
    for v in p:
        if v > mp:
            mp = v
        elif v < mp:
            res += mp - v
    print(res)