N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
cur, nxt = 0, a[0]
ans = 0
while ans <= N:
    ans += 1
    if nxt == K:
        break
    cur, nxt = nxt, a[nxt]
print(ans if ans <= N else -1)