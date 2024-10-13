from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, G, usado):
    q = deque([(s, 1e10)])
    visited = [-1] * len(G)
    visited[s] = 0
    while q:
        cn, v = q.popleft()
        for nn in G[cn]:
            if visited[nn] == -1:
                visited[nn] = min(usado[(cn, nn)], v)
                q.append((nn, visited[nn]))
    return visited

def solve():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    usado = {}
    for _ in range(N - 1):
        p, q, r = map(int, input().split())
        G[p].append(q)
        G[q].append(p)
        usado[(p, q)] = r
        usado[(q, p)] = r
    dist = {}
    for _ in range(Q):
        k, v = map(int, input().split())
        if v not in dist:
            dist[v] = bfs(v, G, usado)
        cnt = 0
        for u in dist[v]:
            if k <= u:
                cnt += 1
        print(cnt)

solve()