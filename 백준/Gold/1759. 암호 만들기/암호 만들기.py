def dfs(idx, dep, s, m, j):
    if dep == L:
        if m >= 1 and j >= 2:
            print(s)
        return
    for i in range(idx, C):
        if not visited[i]:
            visited[i] = 1
            if cha[i] in mu:
                dfs(i + 1, dep + 1, s + cha[i], m + 1, j)
            else:
                dfs(i + 1, dep + 1, s + cha[i], m, j + 1)
            visited[i] = 0

L, C = map(int, input().split())
cha = sorted(list(input().split()))
mu = {'a', 'e', 'i', 'o', 'u'}
visited = [0] * C
dfs(0, 0, "", 0, 0)