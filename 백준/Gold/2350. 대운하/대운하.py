from collections import deque
import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M, K = map(int, input().split())
    R = list(range(N + 1))
    E = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: -x[2])
    G = [[] for _ in range(N + 1)]
    for i, j, w in E:
        ir = find_root(i, R)
        jr = find_root(j, R)
        if ir != jr:
            R[max(ir, jr)] = min(ir, jr)
            G[i].append((j, w))
            G[j].append((i, w))
    for _ in range(K):
        i, j = map(int, input().split())
        visited = [False] * (N + 1)
        q = deque([(i, 201)])
        visited[i] = True
        while q:
            cn, cw = q.popleft()
            if cn == j:
                print(cw)
                break
            for nn, nw in G[cn]:
                if not visited[nn]:
                    visited[nn] = True
                    q.append((nn, min(cw, nw)))

solve()