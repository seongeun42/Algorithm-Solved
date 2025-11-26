N, M = map(int, input().split())
time = sorted([*map(int, input().split())], reverse=True)
con, i = [0] * M, 0
ans = 0
for t in time:
    if con[i] <= ans:
        con[i] += t
        if ans <= con[i]:
            ans = con[i]
            i = (i + 1) % M
print(ans)