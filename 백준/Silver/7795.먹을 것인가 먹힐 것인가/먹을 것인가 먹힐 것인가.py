import bisect
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted([*map(int, input().split())])
    b = sorted([*map(int, input().split())])
    res = 0
    for v in a:
        res += bisect.bisect(b, v - 1)
    print(res)