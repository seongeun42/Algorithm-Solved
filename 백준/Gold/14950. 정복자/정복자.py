import sys, heapq
input = sys.stdin.readline

def prim(s):
    ans = 0
    cnt = 0
    hq = G[s]
    heapq.heapify(hq)
    visit[s] = 1
    while hq:
        c, e = heapq.heappop(hq)
        if not visit[e]:
            visit[e] = 1
            ans += c + t * cnt
            cnt += 1
            for nxt in G[e]:
                if not visit[nxt[1]]:
                    heapq.heappush(hq, nxt)
    return ans

N, M, t = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))
visit = [0] * (N + 1)
print(prim(1))