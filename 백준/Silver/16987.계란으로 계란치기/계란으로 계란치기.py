def dfs(idx):
    global res
    if idx == N:
        res = max(res, sum([1 for v in egg if v[0] <= 0]))
    else:
        if egg[idx][0] > 0:
            broken = 0
            for i in range(N):
                if i != idx and egg[i][0] > 0:
                    egg[i][0] -= egg[idx][1]
                    egg[idx][0] -= egg[i][1]
                    broken = 1
                    dfs(idx + 1)
                    egg[i][0] += egg[idx][1]
                    egg[idx][0] += egg[i][1]
            if not broken:
                dfs(N)
        else:
            dfs(idx + 1)

N = int(input())
egg = [[*map(int, input().split())] for _ in range(N)]
res = 0
dfs(0)
print(res)