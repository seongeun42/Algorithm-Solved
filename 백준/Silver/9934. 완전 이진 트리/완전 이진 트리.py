def recur(dep, pnode, s, e):
    if dep == K:
        return
    level[dep].append(I[pnode])
    recur(dep + 1, (s + pnode - 1) // 2, s, pnode - 1)
    recur(dep + 1, (pnode + e + 1) // 2, pnode + 1, e)

K = int(input())
I = [*map(int, input().split())]
level = [[] for _ in range(K)]
recur(0, len(I) // 2, 0, len(I) - 1)
for l in level:
    print(*l)