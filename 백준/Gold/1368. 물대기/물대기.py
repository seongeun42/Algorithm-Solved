import sys, heapq
input = sys.stdin.readline

def prim(W, P):
    res = 0
    hq = []
    for i in range(len(W)):
        heapq.heappush(hq, (W[i], i))
    visited = [0] * len(W)
    while hq:
        c, e = heapq.heappop(hq)
        if not visited[e]:
            visited[e] = 1
            res += c
            for i in range(len(W)):
                if i != e and not visited[i]:
                    heapq.heappush(hq, (P[e][i], i))
    return res

def solve():
    N = int(input())
    W = [int(input()) for _ in range(N)]
    P = [[*map(int, input().split())] for _ in range(N)]
    print(prim(W, P))

solve()