N = int(input())
S = [int(input()) for _ in range(N)]
res = 0
for i in range(N - 2, -1, -1):
    if S[i] >= S[i + 1]:
        res += S[i] - S[i + 1] + 1
        S[i] = S[i + 1] - 1
print(res)