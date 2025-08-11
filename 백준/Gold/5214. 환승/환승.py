from collections import deque
import sys
input = sys.stdin.readline

def bfs(hyper, station, N):
    if N == 1:
        return 1
    q = deque([])
    visited_h = [False] * len(hyper)
    visited_s = [0] * (len(station) + 1)
    visited_s[1] = 1
    q.append(1)
    while q:
        cur_s = q.popleft()
        for nxt_h in station[cur_s]:
            if not visited_h[nxt_h]:
                visited_h[nxt_h] = True
                for nxt_s in hyper[nxt_h]:
                    if nxt_s == N:
                        return visited_s[cur_s] + 1
                    if not visited_s[nxt_s]:
                        q.append(nxt_s)
                        visited_s[nxt_s] = visited_s[cur_s] + 1
    return -1

def solve():
    N, K, M = map(int, input().split())
    hyper = []
    station = [[] for _ in range(N + 1)]
    for _ in range(M):
        hyper.append([*map(int, input().split())])
        for v in hyper[-1]:
            station[v].append(len(hyper) - 1)
    print(bfs(hyper, station, N))
    
solve()