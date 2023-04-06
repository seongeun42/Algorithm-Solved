def dfs(arr, dep):
    if dep == n:
        ans.append("".join(map(str, arr)))
        return
    for i in range(10):
        if chk[i]: continue
        if (s[dep] == "<" and arr[-1] < i) or (s[dep] == ">" and arr[-1] > i):
            chk[i] = 1
            dfs(arr + [i], dep + 1)
            chk[i] = 0
        elif s[dep] == ">" and arr[-1] <= i:
            break

n = int(input())
s = list(input().split())
chk = [0] * 10
ans = []
for i in range(10):
    chk[i] = 1
    dfs([i], 0)
    chk[i] = 0
ans.sort()
print(ans[-1], ans[0], sep="\n")