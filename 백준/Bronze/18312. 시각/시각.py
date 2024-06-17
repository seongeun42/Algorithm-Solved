N, K = map(int, input().split())
K = str(K)
ans = 0
for h in range(N + 1):
    hh = f'{h:02}'
    for m in range(60):
        mm = f'{m:02}'
        for s in range(60):
            ss = f'{s:02}'
            if K in hh + mm + ss:
                ans += 1
print(ans)