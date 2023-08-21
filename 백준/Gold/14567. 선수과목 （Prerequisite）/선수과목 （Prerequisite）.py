from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        degree[B] += 1
    ans = [0] * (N + 1)
    q = deque([])
    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append([i, 1])
            ans[i] = 1
    while q:
        cur, cnt = q.popleft()
        for nn in G[cur]:
            degree[nn] -= 1
            if degree[nn] == 0:
                q.append([nn, cnt + 1])
                ans[nn] = cnt + 1
    print(*ans[1:])

solve()