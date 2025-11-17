from collections import deque
import sys
input = sys.stdin.readline

def bfs(X, G, visited):
    q = deque([X])
    visited[X] = True
    cnt = 0
    while q:
        cur = q.popleft()
        for nxt in G[cur]:
            if not visited[nxt]:
                cnt += 1
                visited[nxt] = True
                q.append(nxt)
    return cnt

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[B].append(A)
    X = int(input())
    visited = [False] * (N + 1)
    print(bfs(X, G, visited))

solve()