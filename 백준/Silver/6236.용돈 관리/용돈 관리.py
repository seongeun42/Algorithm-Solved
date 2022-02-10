import sys
input = sys.stdin.readline
N, M = map(int, input().split())
cost = [int(input()) for _ in range(N)]
s, e = max(cost), sum(cost)
k = 0
while s <= e:
    mid = (s + e) // 2
    bal = mid
    cnt = 1
    for i in range(N):
        if bal < cost[i]:
            bal = mid
            cnt += 1
        bal -= cost[i]

    if cnt > M:
        s = mid + 1
    else:
        e = mid - 1
        k = mid
print(k)