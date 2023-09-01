from collections import deque
import sys
input = sys.stdin.readline

def topology(q, G, degree):
    ans = list(q)
    while q:
        cur = q.popleft()
        for nn in G[cur]:
            degree[nn] -= 1
            if degree[nn] == 0:
                q.append(nn)
                ans.append(nn)
    if len(ans) == len(G) - 1:
        print(*ans, sep="\n")
    else:
        print(0)

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    q = deque([])
    for _ in range(M):
        task = [*map(int, input().split())]
        for i in range(2, len(task)):
            G[task[i - 1]].append(task[i])
            degree[task[i]] += 1
    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
    topology(q, G, degree)

solve()