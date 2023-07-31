def backtrack(dep, k):
    if dep == k:
        haps.add(sum([S[c] for c in idxs[1:]]))
        return
    for i in range(idxs[-1] + 1, N):
        if i not in idxs:
            idxs.append(i)
            backtrack(dep + 1, k)
            idxs.pop()

N = int(input())
S = [*map(int, input().split())]
haps = set(S)
haps.add(sum(S))
idxs = [-1]
for i in range(2, N):
    backtrack(0, i)
haps = sorted(list(haps))
ans = -1
for i in range(len(haps)):
    if haps[i] != i + 1:
        ans = i + 1
        break
print(ans if ans != -1 else len(haps) + 1)