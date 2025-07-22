import sys, heapq
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = float("inf")

def dijkstra(start, G, N):
    dp = [INF] * (N + 1)
    dp[start] = 0
    path = [[] for _ in range(N + 1)]
    hq = [(0, start)]
    while hq:
        c_w, c_n = heapq.heappop(hq)
        if dp[c_n] < c_w:
            continue
        for n_w, n_n in G[c_n]:
            w = c_w + n_w
            if w < dp[n_n]:
                dp[n_n] = w
                path[n_n] = [c_n]
                heapq.heappush(hq, (w, n_n))
            elif w == dp[n_n]:
                path[n_n].append(c_n)
    return path

def find_path(cur, G, target, path, cities, visited):
    if cur == target:
        cities |= set(path)
        return
    for nxt in G[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            path.append(nxt)
            find_path(nxt, G, target, path, cities, visited)
            path.pop()
            visited[nxt] = False

def solve():
    N, M, A, B = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        G[u].append((c, v))
        G[v].append((c, u))
    all_path = dijkstra(A, G, N)
    cities = {A, B}
    visited = [False] * (N + 1)
    visited[B] = True
    find_path(B, all_path, A, [], cities, visited)
    print(len(cities))
    print(*sorted(list(cities)))

solve()