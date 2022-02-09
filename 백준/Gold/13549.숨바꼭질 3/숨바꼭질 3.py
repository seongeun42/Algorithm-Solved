import heapq

def bfs():
    q = []
    visit[N] = 1
    heapq.heappush(q, [0, N])
    while q:
        t, l = heapq.heappop(q)
        if l == K:
            return t
        if 0 <= 2 * l < 100001 and not visit[2 * l]:
            visit[2 * l] = 1
            heapq.heappush(q, [t, 2 * l])
        if 0 <= l - 1 < 100001 and not visit[l - 1]:
            visit[l - 1] = 1
            heapq.heappush(q, [t + 1, l - 1])
        if 0 <= l + 1 < 100001 and not visit[l + 1]:
            visit[l + 1] = 1
            heapq.heappush(q, [t + 1, l + 1])


N, K = map(int, input().split())
visit = [0] * 100001
print(bfs())