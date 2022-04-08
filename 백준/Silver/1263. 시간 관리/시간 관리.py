N = int(input())
ts = [[*map(int, input().split())] for _ in range(N)]
ts.sort(key=lambda x: (-x[1], -x[0]))
res = ts[0][1] - ts[0][0]
for i in range(1, N):
    if res > ts[i][1]:
        res = ts[i][1] - ts[i][0]
    else:
        res -= ts[i][0]
print(res if res >= 0 else -1)