def backtrack(pre, visit, last, dep, total):
    global res
    if dep == N - 1:
        if C[pre][last]:
            res = min(res, total + C[pre][last])
        return
    for i in range(N):
        if not visit[i] and C[pre][i] and i != last:
            visit[i] = 1
            backtrack(i, visit, last, dep + 1, total + C[pre][i])
            visit[i] = 0

N = int(input())
C = [[*map(int, input().split())] for _ in range(N)]
res = 1e9
for i in range(N):
    for j in range(N):
        if i == j or not C[j][i]:
            continue
        visit = [0] * N
        visit[i] = 1
        backtrack(i, visit, j, 1, C[j][i])
print(res)