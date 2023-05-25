import sys
input = sys.stdin.readline

def find_root(R, n):
    if R[n] != n:
        R[n] = find_root(R, R[n])
    return R[n]

def cal(R, P):
    val = 0
    chk = 0
    for a, b, c in P:
        ar = find_root(R, a)
        br = find_root(R, b)
        if ar != br:
            val += not c
            chk += 1
            if ar < br:
                R[br] = ar
            else:
                R[ar] = br
        if chk == n:
            break
    return val ** 2

n, m = map(int, input().split())
path = [[*map(int, input().split())] for _ in range(m + 1)]
worstR = [i for i in range(n + 1)]
bestR = [i for i in range(n + 1)]
best = cal(bestR, sorted(path, key=lambda x: (-x[2], x[0], x[1])))
worst = cal(worstR, sorted(path, key=lambda x: (x[2], x[0], x[1])))
print(worst - best)