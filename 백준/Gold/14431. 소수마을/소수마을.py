import sys, heapq
input = sys.stdin.readline

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 0 or n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def dijkstra(G):
    hq = [(0, 0)]
    dp = [1e9] * len(G)
    dp[0] = 0
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nw, nn in G[cn]:
            w = cw + nw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp[1] if dp[1] != 1e9 else -1

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    town = [(x1, y1), (x2, y2)]
    N = int(input())
    town = town + [[*map(int, input().split())] for _ in range(N)]
    G = [[] for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(i + 1, N + 2):
            dist = int(((town[i][0] - town[j][0]) ** 2 + (town[i][1] - town[j][1]) ** 2) ** 0.5)
            if is_prime(dist):
                G[i].append((dist, j))
                G[j].append((dist, i))
    print(dijkstra(G))
    
solve()