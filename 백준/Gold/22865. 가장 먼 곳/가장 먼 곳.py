import sys, heapq
input = sys.stdin.readline

def dijkstra(hq, arr, G):
    while hq:
        cw, cn = heapq.heappop(hq)
        if arr[cn] < cw:
            continue
        for nw, nn in G[cn]:
            if nw + cw < arr[nn]:
                arr[nn] = nw + cw
                heapq.heappush(hq, (nw + cw, nn))

def solve():
    N = int(input())
    live = set([*map(int, input().split())])
    M = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        D, E, L = map(int, input().split())
        G[D].append((L, E))
        G[E].append((L, D))
    arr = [1e9] * (N + 1)
    hq = []
    for l in live:
        heapq.heappush(hq, (0, l))
        arr[l] = 0
    dijkstra(hq, arr, G)
    ans = [0, 0]
    for i in range(1, N + 1):
        if ans[0] < arr[i]:
            ans = [arr[i], i]
    print(ans[1])

if __name__ == "__main__":
    solve()