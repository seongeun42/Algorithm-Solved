import sys
input = sys.stdin.readline
n, m = map(int, input().split())
leng = list(map(int, input().split()))
res, s, e, mid = 1e9, max(leng), sum(leng), 0
while s <= e:
    mid = (s + e) // 2
    cnt, t = 1, 0
    for v in leng:
        if t + v <= mid:
            t += v
        else:
            t = v
            cnt += 1

    if cnt > m:
        s = mid + 1
    else:
        res = min(res, mid)
        e = mid - 1
print(res)