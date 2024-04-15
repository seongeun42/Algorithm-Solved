import sys
input = sys.stdin.readline

def backtrack(idx, total, min_v, max_v, dep, max_dep):
    if total > R:
        return 0
    if dep == max_dep:
        return 1 if L <= total <= R and max_v - min_v >= X else 0
    cnt = 0
    for i in range(idx, N):
        cnt += backtrack(i + 1, total + A[i], min(min_v, A[i]), max(max_v, A[i]), dep + 1, max_dep)
    return cnt

N, L, R, X = map(int, input().split())
A = sorted([*map(int, input().split())])
print(sum([backtrack(0, 0, 1e7, 0, 0, i) for i in range(2, N + 1)]))