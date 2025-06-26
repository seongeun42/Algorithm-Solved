import sys, heapq
input = sys.stdin.readline

def solve():
    N, k = map(int, input().split())
    customers = [[*map(int, input().split())] for _ in range(N)]
    counters = [(0, i) for i in range(1, k + 1)]
    heapq.heapify(counters)
    out = []
    for c, w in customers:
        waiting, counter = heapq.heappop(counters)
        heapq.heappush(counters, (waiting + w, counter))
        heapq.heappush(out, (waiting + w, -counter, c))
    ans = 0
    for i in range(1, N + 1):
        o = heapq.heappop(out)
        ans += i * o[-1]
    print(ans)

solve()