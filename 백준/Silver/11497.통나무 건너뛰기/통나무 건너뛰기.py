t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    res = 0
    for i in range(n - 1, 1, -1):
        res = max(res, l[i] - l[i - 2])
    print(res)