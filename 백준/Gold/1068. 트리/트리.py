def dfs(node):
    if not G[node] or node >= N:
        return 1
    cnt = 0
    for n in G[node]:
        cnt += dfs(n)
    return cnt

N = int(input())
nodes = [*map(int, input().split())]
roots = []
rmNode = int(input())
G = [[] for _ in range(N)]
for cn, pn in enumerate(nodes):
    if cn == rmNode: continue
    if pn == -1:
        roots.append(cn)
    else:
        G[pn].append(cn)
ans = 0
for n in roots:
    ans += dfs(n)
print(ans)
