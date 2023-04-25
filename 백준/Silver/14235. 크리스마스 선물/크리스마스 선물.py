import sys, heapq
input = sys.stdin.readline

n = int(input())
gift = []
for _ in range(n):
    s = input().strip()
    if s == "0":
        print(-1 * heapq.heappop(gift) if gift else -1)
    else:
        s = [*map(int, s.split())][1:]
        for v in s:
            heapq.heappush(gift, -v)