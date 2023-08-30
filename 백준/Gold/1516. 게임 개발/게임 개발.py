from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    G = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    cost = [0]
    for i in range(N):
        tmp = [*map(int, input().split())]
        cost.append(tmp[0])
        for j in range(1, len(tmp) - 1):
            G[tmp[j]].append(i + 1)
            degree[i + 1] += 1

    q = deque([])
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
            ans[i] = cost[i]

    while q:
        cur = q.popleft()
        for nn in G[cur]:
            degree[nn] -= 1
            if ans[nn] < cost[nn] + ans[cur]:
                ans[nn] = cost[nn] + ans[cur]
            if degree[nn] == 0:
                q.append(nn)

    print(*ans[1:], sep="\n")

solve()