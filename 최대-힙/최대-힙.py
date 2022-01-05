import heapq
import sys
input = sys.stdin.readline
n = int(input())
hq = []
for _ in range(n):
    v = int(input())
    if not v:
        print(-heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, -v)