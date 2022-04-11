def backtrack(now, total, start):
    global res
    if res < total:
        return
    if sum(visit) == N:
        if C[now][start]:
            res = min(res, total + C[now][start])
        return
    for next in range(N):
        if not visit[next] and C[now][next]:
            visit[next] = 1
            backtrack(next, total + C[now][next], start)
            visit[next] = 0

N = int(input())
C = [[*map(int, input().split())] for _ in range(N)]
res = 1e9
visit = [0] * N
for i in range(N):
    visit[i] = 1
    backtrack(i, 0, i)
    visit[i] = 0
print(res)