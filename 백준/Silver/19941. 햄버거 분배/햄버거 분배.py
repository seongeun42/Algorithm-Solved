N, K = map(int, input().split())
S = input()
ans = 0
ate = [0] * N
for i in range(N):
    if S[i] == "H":
        continue
    s = max(0, i - K)
    e = min(N - 1, i + K)
    for j in range(s, e + 1):
        if S[j] == "H" and not ate[j]:
            ate[j] = 1
            ans += 1
            break
print(ans)