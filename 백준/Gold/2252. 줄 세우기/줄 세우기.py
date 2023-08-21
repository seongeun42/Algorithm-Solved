from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        degree[b] += 1
    ans = []
    q = deque([])
    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        ans.append(cur)
        for nn in G[cur]:
            degree[nn] -= 1
            if degree[nn] == 0:
                q.append(nn)
    print(*ans)

solve()