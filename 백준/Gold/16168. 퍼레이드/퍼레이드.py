import sys
input = sys.stdin.readline

def find_root(R, n):
    if R[n] != n:
        R[n] = find_root(R, R[n])
    return R[n]

def solve():
    V, E = map(int, input().split())
    R = [i for i in range(V + 1)]
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        ar = find_root(R, a)
        br = find_root(R, b)
        if ar != br:
            R[max(ar, br)] = min(ar, br)
    for i in range(V + 1):
        find_root(R, i)
    if len(set(R)) > 2:
        return "NO"
    cnt = 0
    for i in range(1, V + 1):
        cnt += len(G[i]) % 2
    return "YES" if cnt in {0, 2} else "NO"
    
print(solve())