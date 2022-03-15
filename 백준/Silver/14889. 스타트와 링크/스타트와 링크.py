def backtrack(dep, idx):
    global res
    if dep == N//2:
        L = list(set(range(N)) - set(S))
        start, link = 0, 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                start += abil[S[i]][S[j]] + abil[S[j]][S[i]]
                link += abil[L[i]][L[j]] + abil[L[j]][L[i]]
        res = min(res, abs(start - link))
        return

    for k in range(idx, N):
        if not p[k]:
            p[k] = 1
            S[dep] = k
            backtrack(dep + 1, k + 1)
            p[k] = 0

N = int(input())
abil = [[*map(int, input().split())] for _ in range(N)]
p = [0] * N
S = [0] * (N//2)
res = 1e9
backtrack(0, 0)
print(res)