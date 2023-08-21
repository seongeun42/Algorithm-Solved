from collections import deque
import sys, heapq
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        degree[B] += 1
    
    ans = []
    hq = []
    for i in range(1, N + 1):
        if degree[i] == 0:
            heapq.heappush(hq, i)
    while hq:
        cur = heapq.heappop(hq)
        ans.append(cur)
        for nn in G[cur]:
            degree[nn] -= 1
            if degree[nn] == 0:
                heapq.heappush(hq, nn)
    print(*ans)

solve()