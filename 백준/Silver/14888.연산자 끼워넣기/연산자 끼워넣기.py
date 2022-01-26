def dfs(t, i, plus, sub, mult, div):
    if i == n:
        res.append(t)
        return
    if plus:
        dfs(t + a[i], i + 1, plus - 1, sub, mult, div)
    if sub:
        dfs(t - a[i], i + 1, plus, sub - 1, mult, div)
    if mult:
        dfs(t * a[i], i + 1, plus, sub, mult - 1, div)
    if div:
        dfs(int(t / a[i]), i + 1, plus, sub, mult, div - 1)

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
res = []
dfs(a[0], 1, o[0], o[1], o[2], o[3])
print(max(res), min(res), sep='\n')