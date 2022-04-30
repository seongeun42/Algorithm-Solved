def recur(dep, m, s, e):
    if dep == K:
        return
    level[dep].append(I[m])
    recur(dep + 1, (s + m - 1) // 2, s, m - 1)
    recur(dep + 1, (m + e + 1) // 2, m + 1, e)

K = int(input())
I = [*map(int, input().split())]
level = [[] for _ in range(K)]
recur(0, len(I) // 2, 0, len(I) - 1)
for l in level:
    print(*l)