def dfs(cur, idxs):
    visit[cur] = 1
    nxt = num[cur]
    if cur == nxt:
        ans.append(cur)
        return
    if nxt in idxs:
        idxs.append(cur)
        ans.extend(idxs[idxs.index(nxt):])
        return
    if not visit[nxt]:
        dfs(nxt, idxs + [cur])

n = int(input())
num = [0] + [int(input()) for _ in range(n)]
visit = [1] + [0] * n
ans = []
for i in range(1, n + 1):
    if not visit[i]:
        visit[i] = 1
        dfs(num[i], [i])
        
ans.sort()
print(len(ans))
print(*ans, sep="\n")