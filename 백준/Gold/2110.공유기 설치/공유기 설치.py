import sys
input = sys.stdin.readline
n, c = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])
res, s, e = 0, 1, h[-1] - h[0]
while s <= e:
    mid = (s + e) // 2
    cnt, l = 1, 0
    for i in range(1, n):
        if h[i] - h[l] >= mid:
            l = i
            cnt += 1

    if cnt >= c:
        s = mid + 1
        res = mid
    else:
        e = mid - 1
print(res)