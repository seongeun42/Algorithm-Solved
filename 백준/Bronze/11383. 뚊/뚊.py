N, M = map(int, input().split())
ori = [input() for _ in range(N)]
dou = [input() for _ in range(N)]
ans = "Eyfa"
for i in range(N):
    s = ori[i]
    ns = ""
    for j in range(M):
        ns += s[j] * 2
    if ns != dou[i]:
        ans = "Not Eyfa"
        break
print(ans)