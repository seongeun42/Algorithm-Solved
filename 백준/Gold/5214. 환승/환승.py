from collections import deque
import sys
input = sys.stdin.readline

def bfs(hyper, station, N):
    q = deque([])
    visited = [0] * len(hyper)
    for v in station[1]:
        q.append((v, 1))
        visited[v] = 1
    while q:
        cur_h, cur_s = q.popleft()
        if N in hyper[cur_h]:
            return visited[cur_h] + 1 if cur_s != N else visited[cur_h]
        for nxt_s in hyper[cur_h]:
            for nxt_h in station[nxt_s]:
                if not visited[nxt_h]:
                    q.append((nxt_h, nxt_s))
                    visited[nxt_h] = visited[cur_h] + 1
    return -1

def solve():
    N, K, M = map(int, input().split())
    hyper = []
    station = [[] for _ in range(N + 1)]
    for _ in range(M):
        hyper.append(set([*map(int, input().split())]))
        for v in hyper[-1]:
            station[v].append(len(hyper) - 1)
    print(bfs(hyper, station, N))
    
solve()