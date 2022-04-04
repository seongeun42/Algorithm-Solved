def dfs(dep):
    if dep == N:
        print(*arr)
        return
    for i in range(N + 1):
        if not v[i]:
            v[i] = 1
            arr.append(i)
            dfs(dep + 1)
            arr.pop()
            v[i] = 0

N = int(input())
arr = []
v = [1] + [0] * N
dfs(0)