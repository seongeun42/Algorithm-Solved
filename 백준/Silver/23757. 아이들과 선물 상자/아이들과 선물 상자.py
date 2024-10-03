import sys, heapq
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    c = [-v for v in [*map(int, input().split())]]
    w = [*map(int, input().split())]
    heapq.heapify(c)
    for need in w:
        box = abs(heapq.heappop(c))
        if box >= need:
            if box - need > 0:
                heapq.heappush(c, need - box)
        else:
            return 0
    return 1

print(solve())